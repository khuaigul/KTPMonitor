import mysql.connector
from KTP_Monitor.models import Pupil_Info
from KTP_Monitor.models import Teacher_Info



def get_profile_info(user, role):
	if (role): #??????????????
		return (Pupil_Info.objects.get(user = user))
	else:
		return Teacher_Info.objects.get(user = user)



