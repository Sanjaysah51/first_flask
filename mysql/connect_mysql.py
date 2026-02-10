import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="studentdb"
)

if conn.is_connected():
    print("Connected to MySQL")

cursor = conn.cursor()

insert = "INSERT INTO student_detail VALUES (4, 'Sanjay sah', 26);"
update="UPDATE student_detail SET name = 'suraj' WHERE id = 2;"

cursor.execute(insert)
cursor.execute(update)

show="select * from student_detail;"

cursor.execute(show)

# fetch all records
result = cursor.fetchall()

# display data
for row in result:
    print(row)

# close connection
cursor.close()

conn.close()