from .DB.main_DB_modul import *


def div_stats(division):
    divs = get_all_divs()
    for div in divs:
        if div.name == division:
            result = dict()
            result['status'] = True
            pupils = []
            contest = []
            contests = get_all_contests(div)
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
            people_cf = []
            for c in all_people:
                people_name[c.CF] = c.name
                people_surname[c.CF] = c.secondname
                people_secondname[c.CF] = c.surname

            for c in contests:
                name_contest[c.link] = c.name
                all_contest.append(c.link)
            contest = []
            pupils = []
            for contest_link in r:
                for pupil_nick in r[contest_link]:
                    info = r[contest_link][pupil_nick]
                    count_contest[contest_link] = info[1]
                    if people in pupil_nick:
                        people[pupil_nick].append({contest_link: info[0]})
                    else:
                        people_cf.append(pupil_nick)
                        people[pupil_nick] = []
                        people[pupil_nick].append({contest_link: info[0]})

            for item in people_cf:
                info = dict()
                info['name'] = people_name[item]
                info['surname'] = people_surname[item]
                info['secondname'] = people_secondname[item]
                info['nickname'] = item
                info['results'] = people[item]
                pupils.append(info)

            for item in all_contest:
                info = dict()
                info['name'] = name_contest[item]
                info['id'] = item
                info['count'] = count_contest[item]
                contest.append(info)

            result['contest'] = contest
            result['pupils'] = pupils
            qwe = dict()
            qwe['stat'] = [pupils]
            return qwe

    return {"status": False}


def contest_stats(link):
    all_problem = []
    all_people = []
    result = get_statistic_contest([link])
    people = dict()
    write_stat = dict()
    write_stat["status"] = True
    name = set()
    ch = 0
    for task in result:
        all_problem.append({'name': task.name})
        for pupil in result[task]:
            info = result[task][pupil]
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


def pupil_statssss(nickname):
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
    result = dict()
    info = dict()
    all_contest = []
    all_pupils = []
    set_pupils = set()
    name_pupils = dict()

    for item in pupils:
        set_pupils.add(item)
        name_pupils[item] =[]

    for item in contest:
        result_c = get_statistic_contest(item)

        for task in result_c:
            if result_c[task].CF in set_pupils:
                info['contest'] = all_contest

    info['contest'] = all_contest
    info['pupils'] = all_pupils
    result['stat'] = [info]
    return result

