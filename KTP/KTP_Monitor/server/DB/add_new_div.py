from KTP_Monitor.models import Div_Info
import datetime

def add_new_div(name):
	year = datetime.date.today().year
	r = Div_Info.objects.get_or_create(name=name, year = year)
	
	print("add_div return")
	return r[1]
	
