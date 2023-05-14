from .DB.main_DB_modul import *


def div_stats(division):
    return False


def contest_stats(link):
    all_problem = []
    all_people = []
    result = get_statistic_contest(link)
    people = dict()
    write_stat = dict()
    write_stat["status"] = True
    name = set()
    ch = 0
    for task in result:
        all_problem.append({'name': task.name})
        for pupil in result[task]:
            info = result[task][pupil].split()
            if pupil.CF in name:
                problem = all_people[people[pupil.CF]]['problems']
                problem.append({task.name: info[1]})
                all_people[people[pupil.CF]]['problems'] = problem
            else:
                info_people = dict()
                problem = []
                info_people['name'] = pupil.firstname
                info_people['secondname'] = pupil.secondname
                info_people['surname'] = pupil.secondname
                info_people['nickname'] = pupil.CF
                problem.append({task.name: info[1]})
                info_people['problems'] = problem
                all_people.append(info_people)
                people[pupil.CF] = ch
                ch = ch + 1
                name.add(pupil.CF)
    write_stat["pupils"] = all_people
    write_stat["problems"] = all_problem
    return write_stat


def pupil_stats(nicknane):
    return False


