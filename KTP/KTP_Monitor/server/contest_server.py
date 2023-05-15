# Тут будут функции которые отвечают за работу бд с Contest.


from .parsing import parsing_json_with_parameter
from .API_CF import authorized_request
from .chek import *
from .DB.main_DB_modul import *
import time
from django.db import IntegrityError
from django.db import transaction
from db_mutex import DBMutexError, DBMutexTimeoutError
from db_mutex.db_mutex import db_mutex

def write_contest_list(info):  # вывод конкретного Contest
    if info == "":
        return {"status": False}
    divs = get_all_divs()
    for item in divs:
        if item.name == info:
            print("tyttyttyttyttyttyttyttyt")
            contests = get_all_contests([item])
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            write_contests = dict()
            write_contests["status"] = True
            name_contests = []
            for item2 in contests:
                info_contests = dict()
                info_contests["name"] = item2.name
                info_contests["link"] = item2.link
                name_contests.append(info_contests)
            write_contests["contests"] = name_contests
            print(write_contests)
            return write_contests
    return {"status": False}


def add_problem(id_contest):
    request = [("contestId", str(id_contest)), ("from", str(1)), ("count", str(1))]
    request_for_cf = authorized_request("contest.standings", request)  # делаем запрос на кф
    if request_for_cf is None:  # что-то пошло не так и запрос не удалось сделать
        return False
    request = {'result': {'problems': ['name', 'index']}}
    info = parsing_json_with_parameter(request_for_cf, request)
    for item in info:
        name = item[0]['name']
        index = item[1]['index']
        print(index, name)
        add_task(id_contest, index, name)
    return True


def get_name_contest(lint):
    request = [("contestId", str(lint)), ("from", str(1)), ("count", str(1))]
    request_for_cf = authorized_request("contest.standings", request)  # делаем запрос на кф
    if request_for_cf is None:  # что-то пошло не так и запрос не удалось сделать
        return False
    request = {'result': {'contest': ['name']}}
    name = parsing_json_with_parameter(request_for_cf, request)
    return name['name']


def add_contestt(link, divison):
#    while(True):
    try:
        with db_mutex('lock_id'):
            if link == "" or divison == "":
                return {"status": False}
            divs = get_all_divs()
            name = get_name_contest(link)
            if type(name) == type(False):
                return {"status": False}
            print(name)
            print(link)
            for item in divs:
                if item.name == divison:
                    if not add_contest(name, link, [item]):
                        print("add contest")
                        return {"status": True}

                    print("add task!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
                    while True:
                        if add_problem(link):
                            return {"status": True}
            pass
            return {"status": False}
#            break
    except DBMutexError:
        print('Could not obtain lock')
    except DBMutexTimeoutError:
        print('Task completed but the lock timed out')
    except Exception as e:
        print(0)


def remove_contest(id_contest):  # удаление конкретного Contest
    if id_contest == "":
        return {"status": False}
    delete_contest(id_contest)
    return {"status": True}


