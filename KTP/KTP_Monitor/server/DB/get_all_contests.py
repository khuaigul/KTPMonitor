from KTP_Monitor.models import Contest_Info
from KTP_Monitor.models import Contest_Div


def get_all_contests(divs = []):

	result = []
	if (len(divs) > 0):
		result = list(Contest_Info.objects.filter(divs__in = divs).distinct())
	else:
		result += list(Contest_Info.objects.all().order_by('name'))
	
	return result
