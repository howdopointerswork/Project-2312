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

def db_search(table, columns_to_search, condition_columns, operators, conditions):

    cursor = conn.cursor()

    select_columns = ""
    search_results = []

    




    if(len(columns_to_search) > 0 and conditions != ""):


        if not(columns_to_search[0].get() == "*"):


            for i in range(len(columns_to_search)):

                if(i > 0):

                    select_columns += ", "

                select_columns += columns_to_search[i].get()
        else:

            select_columns = "*"
        
        

        if(conditions[0].get() != ""):

                
            select_conditions = " WHERE "

            for i in range(len(conditions)):

                if(i > 0):

                    select_conditions += " AND " 

                select_conditions += condition_columns[i].get() + operators[i].get() + conditions[i].get()
  
            cursor.execute("SELECT " + select_columns + " FROM " + table[0] + select_conditions + ";")
            for result in cursor.fetchall():
                for i in range(len(result)):
                    search_results.append(result[i])


                #print(select_conditions)

            
        else:

            cursor.execute("SELECT " + select_columns + " FROM " + table[0] + ";")
            for result in cursor.fetchall():
                for i in range(len(result)):
                    search_results.append(result[i])

                #print(select_conditions)

    #need column name for displaying results    
    

    conn.commit()
    cursor.close()  

    return search_results  
    


def db_edit(table, columns_to_edit, values, condition_columns, operators, conditions):
    
    #handle for all *
    cursor = conn.cursor()
    non_empty = True


    for val in values:
        if(val.get() == ""):
            non_empty = False


    query = ""
    if(len(columns_to_edit) > 0 and non_empty == True):
        for i in range(len(columns_to_edit)):

            if(i > 0):

                query += ", "

            query += columns_to_edit[i].get() + "=" + values[i].get() 




        query += " WHERE "

        for i in range(len(conditions)):

            if(i > 0):

                query += " AND "

            query += condition_columns[i].get() + operators[i].get() + conditions[i].get()

 

        query += ";"        
        cursor.execute("UPDATE " + table[0] + " SET " + query)        
        conn.commit()
        cursor.close()         



def db_add(columns_to_add, values, table):

    cursor = conn.cursor()


    if(len(columns_to_add) > 0):
  
        cols = ""
        vals = ""



        for i in range(len(columns_to_add)):
            if(i > 0):

                cols += ", "
                vals += ", "

          
            cols += columns_to_add[i].get()
            vals += values[i].get()



        if(vals != ""):
            cursor.execute("INSERT INTO " + table[0] + "(" + cols + ") VALUES ( " + vals + ");")

            conn.commit()
            cursor.close()   
    

def db_delete(columns_to_delete, conditions, operators, table):
    #handle for all *
    cursor = conn.cursor()
    non_empty = True

    for condition in conditions:
        if(condition.get() == ""):
            non_empty = False

    if(non_empty):
        for i in range(len(conditions)):
        
             

            cursor.execute("DELETE FROM " + table[0] + " WHERE " + columns_to_delete[i].get() + operators[i].get() + conditions[i].get() + ";")
    
        conn.commit()
        cursor.close()      





 




