from KTP_Monitor.models import Contest_Info

def delete_contest(link):
	contest = Contest_Info.objects.get(link = link)
	contest.delete()
    
	print("contest deleted")
