import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb.is_connected())

cur = mydb.cursor()
a = cur.execute("show databases")

for i in cur :
    print(i)
