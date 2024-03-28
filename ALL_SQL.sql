--SQL TABLES

CREATE TABLE Customer (
  cust_id INTEGER PRIMARY KEY,
  f_name TEXT,
  l_name TEXT,
  email TEXT,
  phone INTEGER,
  contact_type TEXT
);

CREATE TABLE PaymentInfo (
  pay_id INTEGER PRIMARY KEY,
  cust_id INTEGER,
  pay_method TEXT,
  pay_date DATE,
  amount INTEGER,
  status TEXT,
  FOREIGN KEY (cust_id) REFERENCES Customer(cust_id)
);

CREATE TABLE Booking (
  booki_id INTEGER PRIMARY KEY,
  prod_id INTEGER,
  pay_id INTEGER,
  date_from DATE,
  date_to DATE,
  totall_price INTEGER,
  num_of_guests INTEGER,
  FOREIGN KEY (prod_id) REFERENCES Product(prod_id),
  FOREIGN KEY (pay_id) REFERENCES PaymentInfo(pay_id)
);

CREATE TABLE Room (
  room_id INTEGER PRIMARY KEY,
  room_num INTEGER,
  room_type TEXT,
  room_size INTEGER,
  max_occup INTEGER,
  availability TEXT,
  description TEXT
);

CREATE TABLE Amenities (
  room_id INTEGER,
  Amen_code INTEGER,
  FOREIGN KEY (room_id) REFERENCES Room(room_id)
);

CREATE TABLE Hotel (
  hotel_id INTEGER PRIMARY KEY,
  legal_entity_id INTEGER,
  hotel_name TEXT,
  country TEXT,
  city TEXT,
  state TEXT,
  ZIP_code INTEGER,
  street_addr TEXT,
  status TEXT,
  currency_code INTEGER,
  room_quantity INTEGER,
  FOREIGN KEY (legal_entity_id) REFERENCES ManagementInfo(legal_entity_id)
);

CREATE TABLE ManagementInfo (
  legal_entity_id INTEGER PRIMARY KEY,
  f_name TEXT,
  l_name TEXT,
  email TEXT,
  phone INTEGER,
  contact_type TEXT
);


CREATE TABLE Product (
  prod_id INTEGER PRIMARY KEY, 
  hotel_id INTEGER,
  room_id INTEGER,
  rate_id INTEGER,
  FOREIGN KEY (hotel_id) REFERENCES Hotel(hotel_id),
  FOREIGN KEY (room_id) REFERENCES Room(room_id),
  FOREIGN KEY (rate_id) REFERENCES RatePlan(rate_id)
);


CREATE TABLE RatePlan (
  rate_id INTEGER,
  room_nights INTEGER,
  RN INTEGER
);




-- SQL INSERT

-- Populate Customer table
INSERT INTO Customer (f_name, l_name, email, phone, contact_type) 
VALUES ('John', 'Doe', 'john@example.com', 1234567890, 'email'),
       ('Jane', 'Smith', 'jane@example.com', 9876543210, 'phone');

-- Populate ManagementInfo table
INSERT INTO ManagementInfo (f_name, l_name, email, phone, contact_type) 
VALUES ('Manager', 'One', 'manager1@example.com', 1234567890, 'email'),
       ('Manager', 'Two', 'manager2@example.com', 9876543210, 'phone');

-- Populate Hotel table
INSERT INTO Hotel (legal_entity_id, hotel_name, country, city, state, ZIP_code, street_addr, status, currency_code, room_quantity) 
VALUES (1, 'Example Hotel', 'USA', 'New York', 'NY', 10001, '123 Main St', 'active', 1, 50),
       (2, 'Test Hotel', 'Canada', 'Toronto', 'ON', 'M5V 2V4', '456 Maple Ave', 'active', 2, 100);

-- Populate Room table
INSERT INTO Room (room_num, room_type, room_size, max_occup, availability, description) 
VALUES (101, 'Standard', 250, 2, 'available', 'Standard room with basic amenities'),
       (201, 'Suite', 500, 4, 'available', 'Luxurious suite with a view');

-- Populate Amenities table
INSERT INTO Amenities (room_id, Amen_code) 
VALUES (1, 101),
       (2, 201);

-- Populate PaymentInfo table
INSERT INTO PaymentInfo (cust_id, pay_method, pay_date, amount, status) 
VALUES (1, 'Credit Card', '2024-02-25', 200, 'paid'),
       (2, 'PayPal', '2024-02-26', 300, 'paid');

-- Populate Product table
INSERT INTO Product (hotel_id, room_id, rate_id) 
VALUES (1, 1, 1),
       (2, 2, 2);

-- Populate RatePlan table
INSERT INTO RatePlan (rate_id, room_nights, RN) 
VALUES (1, 1, 100),
       (2, 2, 200);

-- Populate Booking table
INSERT INTO Booking (prod_id, pay_id, date_from, date_to, totall_price, num_of_guests) 
VALUES (1, 1, '2024-03-01', '2024-03-05', 1000, 2),
       (2, 2, '2024-04-01', '2024-04-10', 2000, 4);

-- SQL DELETE 

DELETE FROM PaymentInfo 
WHERE pay_method = 'PayPal';

DELETE FROM RatePlan
WHERE RN >= 150;

DELETE FROM Customer
WHERE id = 2;


-- SQL UPDATE

UPDATE Customer 
SET f_name = Johan, l_name = Libert
WHERE cust_id = 1;


UPDATE Amenities
SET Amen_code = 777
WHERE room_id = 2;

UPDATE PaymentInfo
SET amount = 350, status = 'unpaid'
WHERE cust_id = 2;



-- SQL QUERY

-- A select query that extracts all fields in a table.
SELECT * FROM Customer;

-- A select query that extracts specific fields in a table.
SELECT f_name, l_name, email FROM Customer;

-- A select query that extracts fields from two or more tables and uses a condition to filter query results.
SELECT b.date_from, b.date_to, p.pay_method, p.status, b.totall_price 
FROM Booking b
JOIN PaymentInfo p ON b.pay_id  = p.pay_id
WHERE b.totall_price > 1500;

-- A select query that extracts fields from two or more tables and uses a pattern search as a filter.
SELECT r.room_id, r.room_type, r.description, a.amen_code
FROM Room r 
JOIN Amenities a ON r.room_id = a.room_id
WHERE r.description like '%Luxuri%' AND a.amen_code = 201;

-- Two select queries that demonstrates the use of group by with aggregate functions
-- Example 1: Total amount of payments per payment method
SELECT pay_method, SUM(amount) AS total_amount
FROM PaymentInfo
GROUP BY pay_method;

-- Example 2: Average number of guests per booking
SELECT AVG(num_of_guests) AS avg_guests
FROM Booking;

-- A select query that demonstrates the use of group by with having
clause and sorts the data in a descending format.
SELECT booki_id, date_from, date_to
FROM Booking
GROUP BY booki_id
HAVING totall_price >= 2
ORDER BY totall_price DESC;

-- A select query that utilizes a subquery
SELECT f_name, l_name, email
FROM Customer
WHERE cust_id IN (
    SELECT cust_id
    FROM Booking
    JOIN Product ON Booking.prod_id = Product.prod_id
    JOIN Hotel ON Product.hotel_id = Hotel.hotel_id
    WHERE hotel_name = 'Example Hotel'
);

-- h. Other queries discussed in the class

SELECT pay_method FROM PaymentInfo
MINUS
SELECT pay_method FROM PaymentInfo;



