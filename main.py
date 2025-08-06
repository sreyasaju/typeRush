import mysql.connector as sqlconnector

mycon = sqlconnector.connect(host="localhost", user="root", passwd="", database="test")
if mycon.is_connected():
    print("Sucessfully connected to MySQL database")
cursor = mycon.cursor()