import sqlite3

conn = sqlite3.connect('booking.db')
# I Expect this to return all of the tables names 
# and than used by grid_table_chooser() method
def db_get_tables():
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    cursor.close()

    return tables

# I Expect this to return all of the columns
# and than used by drop down menue to deternime what to show
def db_get_columns(table):
    cursor = conn.cursor()
    # if not isinstance(table, str):
    #     print(table[0])
    #     raise ValueError("Table name must be a string.")

    cursor.execute("SELECT name FROM pragma_table_info(?);",(table[0],)) # table[0] is to convert touple(table) into a string
    columns = cursor.fetchall()
    cursor.close()

    return columns

def db_end():
    conn.close()

# <><><><><><><>
def db_select( table, column, type_condition):

    cursor = conn.cursor()


    #column argument above will soon be an array (command array) to loop through
    #iterating done in componnents.py, hard-coded as first element in array for now  


    cursor.execute("SELECT " + column + " FROM " + table + ";" )

    for i in cursor.fetchall(): #working on display here for search, printing for now

        print(i[0])

    # you wouln't have a one function for any query,
    # because select, edit, insert require different variables
    # why you make your lofi harder???
    #if(choice == 1):
    #if(choice == 2): Edit

        

    #if(choice == 3):

       # cursor.execute("INSERT INTO " + table[0] + " (" + column + ")" + " VALUES " + "(" + type_condition + ")" + ";")

    #if(choice == 4): (Delete)
      

    #clear array here
    conn.commit()
    cursor.close()    


