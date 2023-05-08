import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()

mycursor.execute("select * from ineuron.fsds")

for i in mycursor:
    print(i)

mycursor.execute('select student_id , first_name , class from ineuron.fsds')

for i in mycursor:
        print(i)

mycursor.execute('select * from ineuron.fsds where student_id > 1236')

for i in mycursor:
    print(i)


mycursor.execute("select * from ineuron.fsds where first_name = 'shilpi' and class = 'sql'")

for i in mycursor:
    print(i)

mycursor.execute("update ineuron.fsds set first_name = 'amit' where student_id = 12312")

mydb.commit()

mycursor.execute("update ineuron.fsds set class = 'mysql'")

mydb.commit()

mycursor.execute("delete from ineuron.fsds where first_name = 'amit'")

mydb.commit()

mycursor.execute("select max(student_id) from ineuron.fsds")

for i in mycursor:
    print(i)

mycursor.execute("select count(*) from ineuron.fsds")

for i in mycursor:
    print(i)

    mycursor.execute("update ineuron.fsds set class = 'mongodb' where student_id between 12312 and 12314")

    mydb.commit() 

    mycursor.execute("select count(*) ,class from ineuron.fsds group by class")

    for i in mycursor:
        print(i)

    #mycursor.execute("drop table ineuron.fsds")
    #mydb.commit()

    mycursor.execute("drop database ineuron")
    

