import mysql.connector


def get_all_contests():
	
	mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="DB_for_tppo123",
	database="KTP_Monitor"
	)


	select_all_contests_query = "SELECT contest_name, contest_id, div_id FROM Contest_Info ORDER BY div_id"


	mycursor = mydb.cursor()
	mycursor.execute(select_all_contests_query)

	result = []

	for row in mycursor:
		result.append((row[0], row[1], row[2]))

	mydb.commit()
	mycursor.close()
	mydb.close()


	print("show contests")

	return result



