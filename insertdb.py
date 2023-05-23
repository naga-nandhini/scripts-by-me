import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="nandynaga"
)

mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ('pradeep' , 'Theni')


mycursor.execute(sql, val)

mydb.commit()

print("records are inserted")
                 
