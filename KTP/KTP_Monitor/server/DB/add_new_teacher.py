import mysql.connector
from KTP_Monitor.models import Teacher_Info


# [user.get_id()], ['lastname'], ['firstname'],  ['secondname'], 
#  ['nickname'], ['birthdate'],  ['phone'])
def add_new_teacher(user, lastname, firstname, secondname, CF, phone):
    t = Teacher_Info.objects.create(user=user, lastname=lastname, firstname=firstname, secondname=secondname,
                        			CF=CF, phone=phone)
    t.save()
    
    # if (Teacher_Info.objects.contains(user=user, lastname=lastname, firstname=firstname, secondname=secondname,
    #                     			CF=CF, phone=phone)):
    #     print("Teacher add to DB")
    # else:
    #     print("ERROR Teacher add DB false")
    print("add_new_Teacher")
	




