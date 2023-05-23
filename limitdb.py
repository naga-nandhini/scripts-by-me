import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='root',database='nandynaga')
mycursor=conn.cursor()
sql = "SELECT * FROM customers LIMIT 5 OFFSET 2"
mycursor.execute(sql)
response = mycursor.fetchall()
conn.commit()
for row in response:
    print(row , end = "\n")
