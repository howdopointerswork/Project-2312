import sqlite3

conn = sqlite3.connect('booking.db')
def db_get_tables():
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    cursor.close()

    return tables

def db_get_columns(table):
    cursor = conn.cursor()
    # if not isinstance(table, str):
    #     print(table[0])
    #     raise ValueError("Table name must be a string.")

    cursor.execute("SELECT name FROM pragma_table_info(?);",(table[0],))
    columns = cursor.fetchall()
    cursor.close()

    return columns

def db_end():
    conn.close()
