from KTP_Monitor.models import Contest_Info
from KTP_Monitor.models import Task_Info

def add_task(link, letter, name):
    contest = Contest_Info.objects.get(link = link)
    Task_Info.objects.get_or_create(contest = contest, letter = letter, name = name)
    
    print("task added")

	
	




