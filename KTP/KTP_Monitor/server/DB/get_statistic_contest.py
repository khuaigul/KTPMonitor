from KTP_Monitor.models import Contest_Info
from KTP_Monitor.models import Task_Info
from KTP_Monitor.models import Pupil_Info

from KTP_Monitor.models import Pupil_Task


def get_statistic_contest(link):
    contest = Contest_Info.objects.get(link = link)
    tasks = list(Task_Info.objects.filter(contest = contest))
    pupils = list(Pupil_Info.objects.filter(div__in = list(contest.divs.all())))

    result = {}
    for t in tasks:
        result[t] = {} 
        for p in pupils:
            result[t][p] = (0, 'None')
            item, r = Pupil_Task.objects.get_or_create(task = t, pupil = p)
            result[t][p] = (item.cnt_try, item.result)

    print("contest statistic done")
    return result


# def get_statistic_contest(link):
#     contest = Contest_Info.objects.get(link = link)
#     tasks = list(Task_Info.objects.filter(contest = contest))

#     result = {}

#     for t in tasks:
#         result[t] = {}
#         # print("add key " + t.letter)
#         q = Pupil_Task.objects.filter(task = t)
        
#         for item in q:
#             result[item.task][item.pupil] = (item.cnt_try, item.result)


#     print("contest statistic done")

#     return result





