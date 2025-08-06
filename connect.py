# import mysql.connector
# def insert_data(id,name,email):
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="roottoor",
#         database="harsha_ece"
#     )

#     print("connected database successfull")
#     mycursor= mydb.cursor()
#     sql="INSERT INTO people(id,name,email)values(%s,%s,%s)"
#     val=[id,name,email]
#     mycursor.execute(sql,val)
#     mydb.commit()
#     mycursor.close()
#     print(mycursor.rowcount,"record inserted.")

# id=input("enter the id")
# name=input("enter the name")
# email=input("enter the email")
# insert_data(id,name,email)