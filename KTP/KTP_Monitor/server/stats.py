from .DB.main_DB_modul import *


def div_stats(division):
    return False


def contest_stats(link):
    all_problem = []
    all_problem2 = dict()
    contests = get_all_contests()
    for info in contests:
        if link == info.link:
            problem = dict()
            problem['name'] = info.name
            all_problem2[info.index] = info.name
            all_problem.append(problem)
    result = get_statistic_contest(link)
    write_stat = dict()
    write_stat["status"] = True
    all_people = {}
    name = set()
    for task_letter in result:
        for pupil_nick in result[task_letter]:
            info = result[task_letter][pupil_nick].split()
            if pupil_nick in name:
                problem = all_people[pupil_nick]
                problem.append({all_problem2[task_letter]: info[1]})
                all_people[pupil_nick] = problem
            else:
                problem = []
                problem.append({all_problem2[task_letter]: info[1]})
                all_people[pupil_nick] = problem
                name.add(pupil_nick)
    pupils = []
    people = get_all_pupils()
    for pupil_nick in people:
        if pupil_nick.CF in name:
            info = dict()
            info["name"] = pupil_nick.firstname
            info["secondname"] = pupil_nick.secondname
            info["surname"] = pupil_nick.lastname
            info["nickname"] = pupil_nick.CF
            info["problems"] = all_people[pupil_nick.CF]
            pupils.append(info)
    write_stat["pupils"] = pupils
    write_stat["problems"] = all_problem
    return write_stat


def pupil_stats(nicknane):
    return False


