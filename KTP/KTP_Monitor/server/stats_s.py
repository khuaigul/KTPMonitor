from .DB.main_DB_modul import *


def div_stats(division):
    divs = get_all_divs()
    for div in divs:
        if div.name == division:
            result = dict()
            pupils = []
            contest = []
            contests = get_all_contests([div])
            for c in contests:
                contest.append(c.link)
            all_people = get_all_pupils([div])
            for c in all_people:
                pupils.append(c)
            r = get_statistic_pupil_contest(pupils, contest)

            name_contest = dict()
            all_contest = []
            count_contest = dict()
            people = dict()
            people_name = dict()
            people_surname = dict()
            people_secondname = dict()
            people_task = dict()
            people_cf = []
            for c in all_people:
                people_name[c.CF] = c.firstname
                people_surname[c.CF] = c.secondname
                people_secondname[c.CF] = c.lastname

            for c in contests:
                name_contest[c.link] = c.name
                all_contest.append(c.link)
            contest = []
            pupils = []
            for contest_link in r:
                for pupil_nick in r[contest_link]:
                    info = r[contest_link][pupil_nick]
                    count_contest[contest_link] = info[1]
                    if pupil_nick in people:
                        people_task[pupil_nick] += int(info[0])
                        people[pupil_nick].append({'id': contest_link, 'solved': info[0]})
                    else:
                        people_cf.append(pupil_nick)
                        people_task[pupil_nick] = int(info[0])
                        people[pupil_nick] = []
                        people[pupil_nick].append({'solved': info[0], 'id': contest_link})

            for item in people_cf:
                info = dict()
                info['name'] = people_name[item]
                info['surname'] = people_secondname[item]
                info['secondname'] = people_surname[item]
                info['nickname'] = item
                info['results'] = people[item]
                info['summ_task'] = people_task[item]
                pupils.append(info)

            for item in all_contest:
                info = dict()
                info['name'] = name_contest[item]
                info['id'] = item
                info['count'] = count_contest[item]
                contest.append(info)

            result['contest'] = contest
            result['pupils'] = sorted(pupils, key=lambda x: x['summ_task'], reverse=True)
            qwe = dict()
            qwe['stat'] = result
            return qwe
    return {"status": False}


def contest_stats(link):
    all_problem = []
    all_people = []
    people = dict()
    write_stat = dict()
    write_stat["status"] = True
    name = set()
    ch = 0
    result = get_statistic_contest(link)
    for task in result:
        all_problem.append({'name': task.letter})
        for pupil in result[task]:
            info = result[task][pupil]
            if pupil.CF in name:
                problem = all_people[people[pupil.CF]]['problems']
                if info[1] == "OK":
                    if info[0] == 1:
                        problem.append({'name': task.letter, "status": "+"})
                        all_people[people[pupil.CF]]['summ_task'] += 1
                    else:
                        problem.append({'name': task.letter, "status": "+"+str(info[0]-1)})
                        all_people[people[pupil.CF]]['summ_task'] += 1
                else:
                    if info[0] == 0:
                        problem.append({'name': task.letter, "status": ""})
                    else:
                        problem.append({'name': task.letter, "status": "-"+str(info[0])})
                all_people[people[pupil.CF]]['problems'] = problem
            else:
                info_people = dict()
                problem = []
                info_people['name'] = pupil.firstname
                info_people['secondname'] = pupil.secondname
                info_people['surname'] = pupil.lastname
                info_people['nickname'] = pupil.CF
                info_people['summ_task'] = 0
                if info[1] == "OK":
                    if info[0] == 1:
                        info_people['summ_task'] += 1
                        problem.append({'name': task.letter, "status": "+"})
                    else:
                        info_people['summ_task'] += 1
                        problem.append({'name': task.letter, "status": "+"+str(int(info[0])-1)})
                else:
                    if info[0] == 0:
                        problem.append({'name': task.letter, "status": ""})
                    else:
                        problem.append({'name': task.letter, "status": "-"+str(info[0])})
                info_people['problems'] = problem
                all_people.append(info_people)
                people[pupil.CF] = ch
                ch = ch + 1
                name.add(pupil.CF)
    write_stat["pupils"] = sorted(all_people, key=lambda x: x['summ_task'], reverse=True)
    write_stat["problems"] = all_problem
    return write_stat


def pupil_stats(nickname):
    result = dict()
    pupils = get_all_pupils()
    id_people = None
    for item in pupils:
        if item.CF == nickname:
            id_people = item
            break
    divs = get_all_divs()
    div = None
    for it in divs:
        if id_people.div.name == it.name:
            div = it
            break

    contest = get_all_contests([div])
    contest_info = []
    for it in contest:
        info = dict()
        info['name'] = it.name
        r = get_statistic_pupil_contest([id_people], [it.link])
        info['solved'] = r[it.link][id_people.CF][0]
        info['count'] = r[it.link][id_people.CF][1]

        contest_info.append(info)
    result['stats'] = contest_info
    return result


def full_Stats(pupils, contest):
    all_contest = []
    set_pupils_2 = []
    all_pupils = []
    set_pupils = set()
    set_contest = set()
    name_pupils = dict()
    name_contest = dict()
    pupils_info_all = get_all_pupils()
    contest_info_all = get_all_contests()

    for item in pupils:
        set_pupils.add(item)

    for item in contest:
        set_contest.add(item)
    ch = 0
    for item in contest_info_all:
        if item.link in set_contest:
            info_contest = dict()
            info_contest['name'] = item.name
            info_contest['id'] = item.link
            info_contest['count'] = 0
            all_contest.append(info_contest)
            name_contest[item.link] = ch
            ch = ch + 1
    ch = 0
    for item in pupils_info_all:
        if item.CF in set_pupils:
            info_human = dict()
            set_pupils_2.append(item)
            info_human['name'] = item.firstname
            info_human['secondname'] = item.secondname
            info_human['surname'] = item.lastname
            info_human['nickname'] = item.CF
            info_human['results'] = []
            info_human['summ_task'] = 0
            all_pupils.append(info_human)
            name_pupils[item.CF] = ch
            ch = ch + 1
    r = get_statistic_pupil_contest(set_pupils_2, contest)
    for contest_link in r:
        for pupil_nick in r[contest_link]:
            info = dict()
            info['id'] = contest_link
            info['solved'] = r[contest_link][pupil_nick][0]
            all_pupils[name_pupils[pupil_nick]]['summ_task'] += r[contest_link][pupil_nick][0]
            all_pupils[name_pupils[pupil_nick]]['results'].append(info)
            all_contest[name_contest[contest_link]]['count'] = r[contest_link][pupil_nick][1]

    result = dict()
    info = dict()
    info['contest'] = all_contest
    info['pupils'] = sorted(all_pupils, key=lambda x: x['summ_task'], reverse=True)
    result['stat'] = info
    return result

