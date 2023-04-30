import mysql.connector
from KTP_Monitor.models import Teacher_Info


# [user.get_id()], ['lastname'], ['firstname'],  ['secondname'], 
#  ['nickname'], ['birthdate'],  ['phone'])
def add_new_teacher(user, lastname, firstname, secondname, CF, phone):
    Teacher_Info.objects.create(user=user, lastname=lastname, firstname=firstname, secondname=secondname,
                        			CF=CF, phone=phone)

    print("add_new_Teacher")
	




