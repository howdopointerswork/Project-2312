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
-- Example: Retrieve all customers who booked a room in 'Example Hotel'
SELECT f_name, l_name, email
FROM Customer
WHERE cust_id IN (
    SELECT cust_id
    FROM Booking
    JOIN Product ON Booking.prod_id = Product.prod_id
    JOIN Hotel ON Product.hotel_id = Hotel.hotel_id
    WHERE hotel_name = 'Example Hotel'
);

