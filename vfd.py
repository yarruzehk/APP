import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="118170919.Naza",
  port="3306",
  database="mydb"
)

print(mydb)