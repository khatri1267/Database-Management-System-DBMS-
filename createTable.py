
import sqlite3
connection = sqlite3.connect("student.db")
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
           student_id INTEGER PRIMARY KEY ,
           first_name VARCHAR(40) NOT NULL,
           last_name VARCHAR(30) NOT NULL,
           age INT CHECK(age >=18),
           major VARCHAR(20) NOT NULL,
           country VARCHAR(20) NOT NULL,
           department VARCHHAR(30) NOT NULL
    )
    """)
connection.commit()
connection.close()



print("student table created")