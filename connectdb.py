import mysql.connector
conn = mysql.connector.connect(host='localhost',password='root',user='root',database='nandynaga')
mycursor = conn.cursor()
if conn.is_connected():
    print("database is connected now")
