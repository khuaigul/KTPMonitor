import mysql.connector
from KTP_Monitor.models import Div_Info


def get_all_divs():
	return list(Div_Info.objects.all().order_by('name'))



