from KTP_Monitor.models import Contest_Info
from KTP_Monitor.models import Task_Info
from KTP_Monitor.models import Pupil_Info
from KTP_Monitor.models import Pupil_Task
from django.db.models import F


def add_new_send(link, letter, cf, cnt_try, result):
    contest = Contest_Info.objects.get(link = link)
    task = Task_Info.objects.get(contest = contest, letter = letter)
    pupil = Pupil_Info.objects.get(CF = cf)
    
    Pupil_Task.objects.get_or_create(task = task, pupil = pupil)

    r = list(Pupil_Task.objects.filter(task = task, pupil = pupil))
    if (r[0].result != 'OK'):
        Pupil_Task.objects.filter(task = task, pupil = pupil).update(cnt_try = F('cnt_try')+cnt_try, result = result)
        return True
    else:
        return False


	
	




