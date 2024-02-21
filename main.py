import sqlite3

conn = sqlite3.connect('test.db')

c = conn.cursor()

# test_name = ("if you see me this means python code works",)
# c.execute("INSERT INTO people (first_name) VALUES (?);", test_name )

c.execute("SELECT * FROM people;") # apperently having ; is not a requirement
rows = c.fetchall()

conn.commit()

for row in rows:
    print(row)


conn.close()
