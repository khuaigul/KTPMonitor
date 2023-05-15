from .DB.main_DB_modul import *


def all_people_and_div():
    result = dict()
    info = []
    divs = get_all_divs()
    for it in divs:
        item = dict()
        item['name'] = it.name
        people = []

        pupils = get_all_pupils([it])
        for it2 in pupils:
            human = dict()
            human['nickname'] = it2.CF
            human['surname'] = it2.lastname
            human['name'] = it2.firstname
            human['secondname'] = it2.secondname
            people.append(human)
        item['pupils'] = people
        info.append(item)
    result['divisions'] = info
    return result


def all_people_and_div_and_contest():
    result = dict()
    info = []
    divs = get_all_divs()
    for it in divs:
        item = dict()
        item['name'] = it.name
        people = []

        pupils = get_all_pupils(it)
        for it2 in pupils:
            human = dict()
            human['nickname'] = it2.CF
            human['surname'] = it2.lastname
            human['name'] = it2.firstname
            human['secondname'] = it2.secondname
            people.append(human)
        item['pupils'] = people
        info.append(item)
    result['divisions'] = info
    return result


def all_contest_and_div():
    result = dict()
    info = []
    divs = get_all_divs()
    for it in divs:
        item = dict()
        item['name'] = it.name
        contest = []

        conests = get_all_contests([it])


    result['divisions'] = info
    return result