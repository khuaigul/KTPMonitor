from KTP_Monitor.models import Contest_Info
from KTP_Monitor.models import Task_Info
from KTP_Monitor.models import Pupil_Task


def get_statistic_pupil_contest(pupils, links):
    result = {}
    contests = Contest_Info.objects.filter(link__in = links)
    for c in contests:
        result[c.link] = {}
        tasks = list(Task_Info.objects.filter(contest = c))
        cnt_task = len(tasks)
        for p in pupils:
            cnt_acsept = Pupil_Task.objects.filter(task__in = tasks, pupil = p, result = "OK").count()
            result[c.link][p.CF] = (cnt_acsept, cnt_task)

    


    print("pupil_contest statistic done")

    return result




