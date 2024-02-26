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




