import mysql.connector

mydb = mysql.connector.connect(
    host="db4free.net",
    user="lenafam96",
    password="CK@l?KcZ6WUJVcv?",
    database="lenafam96"
)

mycursor = mydb.cursor()

mycursor.execute(
    "SELECT * FROM `message`")

myresult = mycursor.fetchall()

print(myresult[0][2])
