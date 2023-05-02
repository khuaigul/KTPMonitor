from KTP_Monitor.models import Contest_Info
from KTP_Monitor.models import Task_Info
from KTP_Monitor.models import Pupil_Task


def get_statistic_contest(link):
    contest = Contest_Info.objects.get(link = link)
    tasks = list(Task_Info.objects.filter(contest = contest))

    result = {}

    for t in tasks:
        result[t.letter] = {}
        print("add key " + t.letter)
        q = Pupil_Task.objects.filter(task = t)
        
        for item in q:
            result[item.task.letter][item.pupil.CF] = (item.cnt_try, item.result)

    
    # for p in result:
    #     print(p, sep=' ')
    #     for t in result[p]:
    #         print(result[p][t], sep= ' ')
    #     print()

    print("contest statistic done")

    return result




