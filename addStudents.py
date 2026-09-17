import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()

# for i in range(5):
#   print("\nEnter student"),i+1)

first_name = input("enter the first name")
last_name = input("enter the last name")
age= input("enter your age")
major= input("enter your major")
country=input("enter your country")
department=input("enter your department")



cursor.execute("""
INSERT INTO student(first_name,last_name,age,major,country,department)
VALUES(?,?,?,?,?,?)
""",(first_name,last_name,age,major,country,department))



connection.commit()
connection.close()

print("student added successfuly")