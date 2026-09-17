import sqlite3
connection = sqlite3.connect("student.db")
cursor = connection.cursor()


cursor.execute("""
SELECT * FROM student
    """)
data = cursor.fetchall()

for row in data:
    print(row)
connection.commit()
connection.close()



print("student fetched created")