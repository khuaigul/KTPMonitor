import mysql.connector


def get_all_pupils():
	
	mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="DB_for_tppo123",
	database="KTP_Monitor"
	)


	select_all_pupils_query = "SELECT Pupils_Info.pupil_surname, Pupils_Info.pupil_name, Pupils_Info.pupil_patronymic, " \
	"Pupils_Info.pupil_CF, Div_Info.div_name, "  \
+ "Pupils_Info.pupil_id, Pupils_Info.div_id " \
+ "FROM Pupils_Info JOIN Div_Info ON Pupils_Info.div_id = Div_Info.div_id " \
+ "ORDER BY pupil_surname"

	print(select_all_pupils_query)						

	mycursor = mydb.cursor()
	mycursor.execute(select_all_pupils_query)

	result = []

	for row in mycursor:
		result.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

	mydb.commit()
	mycursor.close()
	mydb.close()


	# for [f, s] in result:
	# 	print(f, s)

	print("show pupils")

	return result



