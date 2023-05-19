from KTP_Monitor.models import Contest_Info

def update_contest_time(link, time):
   Contest_Info.objects.filter(link = link).update(last_update = time)
   


	
	




