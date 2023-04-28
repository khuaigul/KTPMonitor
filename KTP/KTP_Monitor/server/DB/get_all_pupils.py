import mysql.connector
from KTP_Monitor.models import Pupil_Info

def get_all_pupils(divs = []):

	result = []
	if (len(divs) > 0):
		for d in divs:
			result += list(Pupil_Info.objects.filter(div = d))
	else:
		result += list(Pupil_Info.objects.all().order_by('lastname'))
	
	return result

