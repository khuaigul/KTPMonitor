import mysql.connector
from KTP_Monitor.models import Pupil_Info


# [user.get_id()], ['lastname'], ['firstname'],  ['secondname'], 
#  ['nickname'], ['birthdate'],  
# ['school'], ['grade'],['phone'])
def add_new_pupil(user, lastname, firstname, secondname, CF, birthday, school, grade, phone):
    p = Pupil_Info.objects.create(user=user, lastname=lastname, firstname=firstname, secondname=secondname,
                        			CF=CF, birthday=birthday, school=school, grade=grade, phone=phone)
    
    if (Pupil_Info.objects.contains(user=user, lastname=lastname, firstname=firstname, secondname=secondname,
                        			CF=CF, birthday=birthday, school=school, grade=grade, phone=phone)):
        print("pupil add to DB")
    else:
        print("ERROR pupil add DB false")
    print("add_new_pupil")
	
	# mydb = mysql.connector.connect(
	# host="localhost",
	# user="root",
	# password="DB_for_tppo123",
	# database="KTP_Monitor"
	# )

	# mycursor = mydb.cursor()

	# add_pupil_query = '''Insert into Pupils_Info (pupil_surname, pupil_name, pupil_patronymic, pupil_school, pupil_grade, pupil_CF, birthday) 
 	# 	VALUES ('''  \
 	# 	+ '''\''''  + str(pupil.surname) + '''\',''' \
 	# 	+ '''\''''  + str(pupil.name) + '''\',''' \
 	# 	+ '''\''''  + str(pupil.patronymic) + '''\',''' \
 	# 	+ '''\''''  + str(pupil.school) + '''\',''' \
 	# 	+ str(pupil.grade) + ''','''\
 	# 	+ '''\''''  + str(pupil.nick_CF) + '''\',''' \
 	# 	+ '''\'''' + str(pupil.birthday) + '''\''''\
 	# 	+ ''');'''

	# print(add_pupil_query)
	# mycursor.execute(add_pupil_query)

	# mydb.commit()
	# mycursor.close()
	# mydb.close()

	# print("pupil added")




