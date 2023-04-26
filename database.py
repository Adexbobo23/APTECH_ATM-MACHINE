import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="aptech"
)

mycursor = mydb.cursor()

sql = "INSERT INTO staff (full_name, email, phone) VALUES (%s, %s, %s)"
val = ("Olanrewaju Adeshewa", "adeshewa@gmail.com", "08145237890")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted")