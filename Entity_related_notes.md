Entities

customer
hotel
room

booking
payment


Attributes


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


