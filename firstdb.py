import mysql.connector
conn = mysql.connector.connect(host='localhost',password='root',user='root')
if conn.is_connected():
    print("Coonnection is establised with  python")                           
                               
                               
                               
