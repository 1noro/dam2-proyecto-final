import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="DCHAN"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM BOARD")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)