Entities

customer
hotel
room

booking
payment


Attributes
customer- customer id, name, address, email, payment info, contactinformation
hotel- hotel id, name, city, address, postal code, hotel type(stars), rating, contact information, price range, room types,availability
room- room number, room type, room size, max occupancy, availability, amenities, 
booking- booking id, customer id, hotel id, room number, date from, date to, total price, number of guests
payment- payment id(reference number), booking id, payment method, date, amount, status(pending, confirmed)

Identifiers
(Primary keys)

Relationships
    customer --<payment>-- hotel
    customer --<book>-- room
    hotel --<have>-- room
    

Cardinality
    customer >--<payment>--| hotel
    customer >--<book>--| room
    hotel |--<have>--< room


Weak Entities

booking
payment
room

ID-Dependent Weak Entities

Associative Entities

booking
payment

Subtype Entities


