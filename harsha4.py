# import mysql.connector
# def update_people(name,id):
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="roottoor",
#         database="harsha_ece"
#     )

#     print("connected database successfull")
#     mycursor= mydb.cursor()
#     sql="UPDATE people SET name =%s WHERE id=%s"
#     val=[name,id]
#     mycursor.execute(sql,val)
#     mydb.commit()
#     mycursor.close()
#     print(mycursor.rowcount,"record inserted.")

# id=input("enter the id")
# name=input("enter the name")

# update_people(name,id)