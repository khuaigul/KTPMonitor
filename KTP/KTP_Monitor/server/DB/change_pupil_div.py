# import mysql.connector
from KTP_Monitor.models import Pupil_Info

def change_pupil_div(user, div):
	Pupil_Info.objects.filter(user=user).update(div=div)
    
	return True