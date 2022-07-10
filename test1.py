import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="roomchat"
)

mycursor = mydb.cursor()

mycursor.execute(
    "SELECT * FROM `message`")

myresult = mycursor.fetchall()

# print(myresult[0][2])

a = "a\nb"

b = bytes(a, "utf8")

print(b.decode('utf8'))
