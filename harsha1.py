import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",
    database="harsha_ece"
)
print("connected database successfully")