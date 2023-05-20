
from .parsing import parsing_json_with_parameter
from .API_CF import authorized_request
# from .DB.main_DB_modul import *


STR_TYPE = type("qwe")
info = {}


def check_nickname(nickname):
    if nickname == '' or nickname == None:
        return False
    return True


def check_human(handle, id_contest):  # проверка на наличие человека в Contest
    if handle == "" or id_contest == "":
        return False
    return True


def check_verdict(handle, id_contest, problem):  # проверка на ранний вердикт в Contest
    if handle == "" or id_contest == "" or problem == "":
        return False
    return True


def give_json(id_contest):  # получение json надо сь которым дальше будем работать
    request = [("contestId", str(id_contest))]
    request_for_cf = authorized_request("contest.status", request)  # делаем запрос на кф
    if request_for_cf is None:  # что-то пошло не так и запрос не удалось сделать
        return True
    request = {'result': [{'author': {'members': 'handle'}}, {'problem': 'index'},
                          {'problem': 'name'}, 'verdict', 'creationTimeSeconds']}
    global info
    info = parsing_json_with_parameter(request_for_cf, request)
    return False


def up_contest(id_contest, last_submit):  # обновление данных в Contest для бд
    if give_json(id_contest):
        return False
    global info
    last = last_submit
    i = 1
    for item in info:  # ищем посылку, которая была последней раньше
        if last < item[4]['creationTimeSeconds'] and check_human(item[0]['handle'], id_contest):
            last = item[4]['creationTimeSeconds']
        if item[4]['creationTimeSeconds'] == last_submit:
            break
        i = i + 1
    while i != 1:  # добавляем разницу между прошлой последней посылкой и текущей
        i = i - 1
        item = info[i-1]
        verdict = item[3]['verdict']
        handle = item[0]['handle']
        problem = item[1]['index']
        name = item[2]['name']
        if check_human(handle, id_contest) and check_verdict(handle, id_contest, problem):
            print(verdict, " ", handle, " ", problem, " ", name)
        # тут ещё надо написать обновление ласт посылки
    return True


def add_new_human_in_contest(id_contest, human, last_submit):  # добавление данных человека в конкретный Contest
    if give_json(id_contest):
        return False
    global info
    last = last_submit
    i = 1
    for item in info:  # ищем посылку, которая была последней раньше
        if last < item[4]['creationTimeSeconds'] and check_human(item[0]['handle'], id_contest):
            last = item[4]['creationTimeSeconds']
        i = i + 1
    while i != 1:  # добавляем разницу между прошлой последней посылкой и текущей
        i = i - 1
        item = info[i - 1]
        verdict = item[3]['verdict']
        handle = item[0]['handle']
        problem = item[1]['index']
        name = item[2]['name']
        if name == human and check_verdict(handle, id_contest, problem):
            print(name, verdict)

    return True


def add_new_human(human):  # добавление данных человека во все Contest
    if human == "" or STR_TYPE != type(human):
        return False
    id_contest = 1
    last = 1
    if add_new_human_in_contest(id_contest, human, last):
        return True
    return False


up_contest(104363, 0)
