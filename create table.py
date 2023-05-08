import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()

mycursor.execute('create table ineuron.fsds(student_id int , first_name varchar(50) , registration_date int , class varchar(50) , course_name varchar(50))')