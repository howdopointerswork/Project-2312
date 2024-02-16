todo:

legend: 

    I will use this syntax to represent tasks "- [ ]"
    when a task is done I will show it this way "- [x]"
    this means a branch a person responsible for the branch "==name=="


==business==
- [x] System Selection
    - [x] make a document with systems that are used by business,
        leave links to their sites, no need for any details, just 
        give as options, we can change our "theme" later(give as 2-3 options)

{pls ask me(Alex) if you need help with all this}
- [ ] Requirement Gathering

    - [ ] make a use-case diagram for a system
        a nice tutorial if you are lost https://www.youtube.com/watch?v=4emxjxonNRI

    - [ ] make a short report on data "requirements", to make it you should do the following

        - [ ] Document Use Cases:
            document the various use cases and scenarios in which the system will be used,

        - [ ] Gather Requirements: {I would help you with that}
            copy them for existing documentation for the system
            if there is no ware to take it from
            just make a list of what "system does" and "system provides"

            example: we have a online bookstore system, so our 
                'system will let users to browse avaliable books' <-- this is one of the requirements
                'system will provide ability to add new books'
                ...
        
    - [ ] Entity-Relationship Diagram

        - [ ] Identify Entities and Attributes
            look though the requirements you wrote down 
            to Identify the `Entities` (objects or consepts) 
            and than see what this Entities `Attributes` (properties) they have

            example: we have an e-commerce system, so our
                Entities would can be: "Customers", "Products", "Orders" ...
                and this Entities will have Attributes like:
                "Customers" will have "name", "birth" ...
                "Orders" will  have "dates" ...

        - [ ] Define Relationships
            determine relationships between different `Entities`
            meaning you need to describe how entities connect or interact with each other

            example: let's say we have e-commerce again
                customer may "have" an order, the "have" here is a relationship

        {I will add aditional stuff to your report, so this is what I want from you}

==dbms==
- [ ] Conceptual Design-Based 
- [ ] Logical Design
- [ ] Physical Design 
- [ ] Data management
- [ ] Queries
{ I will not wright instactions for myself lol 😌}

==programming==
- [ ] deside on how it is going to work
    meaning, when user will open your app what he will see and 
    what each button will do, you can make a sketch if you want

the UI will consust of the following parts 
adding, editing, deleting, and searching.
I suguest you to approach a project this way
- [ ] do base  
    do the basic gui where you would have 4 options
    so far you would need to figure out how to make "screen transition"
    I want you to make a simple demmo where there would be 4 buttons (on the main page) and 
    when ever you press on the one of the button you screen whould switch (to the buttons page)
    to their respective screen and there leave a button so that user may go back (to the main page)
- [ ] make a simple imput fiels

after Physical Design will be made you will be able to do
- [ ] adding 
    see what table we would have and make an imput fiels
    that will co respond with the values that SQL insert query will need  
    so take a sql query and use variables as input to them
- [ ] editing
- [ ] deleting
    when implementing a SQL delete query don't forget about WHERE
    and the fact that you should take user input to in which cases to delete data
    other wise you will delere all of our data
- [ ] searching
    this is going to be simple SQL SELECT * FROM table WHERE query
- [ ] do the design ( Caesar is a sucker for looks, but if you don't want to do it, it's fine )
    do this if will have time


