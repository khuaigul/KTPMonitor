import mysql.connector


def get_all_divs():

	print("im here")
	mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="DB_for_tppo123",
	database="KTP_Monitor"
	)


	select_all_pupils_query = "SELECT div_name, div_id FROM Div_Info ORDER BY div_name"


	mycursor = mydb.cursor()
	mycursor.execute(select_all_pupils_query)

	result = []

	for row in mycursor:
		result.append((row[0], row[1]))

	mydb.commit()
	mycursor.close()
	mydb.close()


	for [f, s] in result:
		print(f, s)

	print("show divs")

	return result



