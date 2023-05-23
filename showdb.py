import mysql.connector
conn = mysql.connector.connect(host='localhost',password='root',user='root')
mycursor = conn.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
