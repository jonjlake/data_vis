# Adapting from https://www.w3schools.com/python/python_mysql_select.asp

import mysql.connector

mydb = mysql.connector.connect(
		host="localhost",
		user="user",
		password="password",
		database="database"
		)

table_name = "table_name"

mycursor = mydb.cursor()
columns = ['id','value']
read_statement = "SELECT " + ",".join(columns) + " FROM " + table_name
mycursor.execute(read_statement)

# returns a list of tuples
myresult = mycursor.fetchall()

for x in myresult:
	print(x)

print(myresult)
