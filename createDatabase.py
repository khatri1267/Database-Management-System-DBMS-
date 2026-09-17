import sqlite3w
# craete/connect to database
connection = sqlite3.connect("student.db")

# create cursor
cursor = connection.cursor()

print("Database created succesfully")

connection.close()