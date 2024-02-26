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

