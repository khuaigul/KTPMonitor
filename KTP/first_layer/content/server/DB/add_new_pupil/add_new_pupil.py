import mysql.connector

def add_new_pupil(pupil):
	
	mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="DB_for_tppo123",
	database="KTP_Monitor"
	)

	mycursor = mydb.cursor()

	add_pupil_query = '''Insert into Pupils_Info (pupil_surname, pupil_name, pupil_patronymic, pupil_school, pupil_grade, pupil_CF, birthday) 
 		VALUES ('''  \
 		+ '''\''''  + str(pupil.surname) + '''\',''' \
 		+ '''\''''  + str(pupil.name) + '''\',''' \
 		+ '''\''''  + str(pupil.patronymic) + '''\',''' \
 		+ '''\''''  + str(pupil.school) + '''\',''' \
 		+ str(pupil.grade) + ''','''\
 		+ '''\''''  + str(pupil.nick_CF) + '''\',''' \
 		+ '''\'''' + str(pupil.birthday) + '''\''''\
 		+ ''');'''

	print(add_pupil_query)
	mycursor.execute(add_pupil_query)

	mydb.commit()
	mycursor.close()
	mydb.close()

	print("pupil added")




