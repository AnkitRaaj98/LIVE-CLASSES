import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)


cur = mydb.cursor()

#cur.execute('create database ankit')

cur.execute('use ankit')

#cur.execute('create table ineuron (name varchar(40) , roll_no int , mail_id varchar(50)) ')

cur.execute("insert into ineuron values ('ankit' , 91234 , 'ankit@gmail.com')")


mydb.commit()
