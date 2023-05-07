from KTP_Monitor.models import Teacher_Info

def get_all_teachers(divs = []):

	result = []
	if (len(divs) > 0):
		result += list(Teacher_Info.objects.filter(div__in = divs))
	else:
		result += list(Teacher_Info.objects.all().order_by('lastname'))
	
	return result

