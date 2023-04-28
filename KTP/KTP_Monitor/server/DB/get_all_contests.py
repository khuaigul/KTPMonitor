from KTP_Monitor.models import Contest_Info

def get_all_contests(divs = []):

	result = []
	if (len(divs) > 0):
		for d in divs:
			result += list(Contest_Info.objects.filter(div = d))
	else:
		result += list(Contest_Info.objects.all().order_by('name'))
	
	return result
