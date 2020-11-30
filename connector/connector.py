# Adapting from https://www.w3schools.com/python/python_mysql_select.asp
# pip install mysql-connector-python
# pip install matplotlib?

import mysql.connector
import matplotlib.pyplot as plt

##
# read_database reads from a mysql database.
# The host, username, password, database, and
# table are specified in the function.
#
# @return A list of tuples representing each row
##
def read_database():
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

	myresult = mycursor.fetchall()

	return myresult

##
# convert_db_to_plot takes mysql data and converts it to
# a better data representation for plotting.
#
# @param db_data A list of tuples representing row data
# @return A two-value tuple. First value is a list of x values, second is for y.
##
def convert_db_to_plot(db_data):
	index = []
	value = []

	for x in db_data:
		index.append(x[0])
		value.append(x[1])

	return (index, value)

##
# plot_data saves data as a .jpg graph.
#
# @param data 2-tuple: (x-list, y-list)
##
def plot_data(data):
	fig, ax = plt.subplots()

	plt.plot(data[0], data[1])	
	plt.ylabel('some numbers')

	fig.savefig('plot.jpg')

##
# Start of script
##
db_data = read_database()
plt_data = convert_db_to_plot(db_data)

print(plt_data)
plot_data(plt_data)

