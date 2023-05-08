import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()

mycursor.execute("""insert into ineuron.fsds values( 1236 , 'shilpi' , 2023-11-11 , 'sql' , 'fsds'),
( 1235 , 'ankit' , 2023-11-11 , 'sql' , 'fsds'),
( 1238 , 'amit' , 2023-11-11 , 'sql' , 'fsds'),
( 1239 , 'ayushman' , 2023-11-11 , 'sql' , 'fsds'),
( 12310 , 'vishal' , 2023-11-11 , 'sql' , 'fsds'),
( 12311, 'sanu' , 2023-11-11 , 'sql' , 'fsds'),
( 12312, 'sonu' , 2023-11-11 , 'sql' , 'fsds'),
( 12314, 'palak' , 2023-11-11 , 'sql' , 'fsds')""")


mydb.commit()

mycursor.execute('select * from ineuron.fsds')

for i in mycursor:
    print(i)