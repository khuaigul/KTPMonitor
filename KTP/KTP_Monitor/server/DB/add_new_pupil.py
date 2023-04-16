import mysql.connector
from KTP_Monitor.models import Pupil_Info
# [user.get_id()], ['lastname'], ['firstname'],  ['secondname'], 
#  ['nickname'], ['birthdate'],  
# ['school'], ['grade'],['phone'])
def add_new_pupil(user, lastname, firstname, secondname, CF, birthday, school, grade, phone):
    p = Pupil_Info.objects.create(user=user, lastname=lastname, firstname=firstname, secondname=secondname,
                        			CF=CF, birthday=birthday, school=school, grade=grade, phone=phone)
    p.save()
    # if (Pupil_Info.objects.contains(user=user, lastname=lastname, firstname=firstname, secondname=secondname,
    #                     			CF=CF, birthday=birthday, school=school, grade=grade, phone=phone)):
    #     print("pupil add to DB")
    # else:
    #     print("ERROR pupil add DB false")
    # print("add_new_pupil")

