from .parsing import parsing_json_with_parameter
from .API_CF import authorized_request
from .DB.main_DB_modul import *


STR_TYPE = type("qwe")
info = {}
pupils = set()


def check_human(handle):  # проверка на наличие человека в Contest
    global pupils
    if handle == "":
        return False
    if handle in pupils:
        return True
    return False


def give_json(id_contest):  # получение json надо сь которым дальше будем работать
    request = [("contestId", str(id_contest))]
    request_for_cf = authorized_request("contest.status", request)  # делаем запрос на кф
    if request_for_cf is None:  # что-то пошло не так и запрос не удалось сделать
        return True
    request = {'result': [{'author': {'members': 'handle'}}, {'problem': 'index'},
                          'verdict', 'creationTimeSeconds']}
    global info
    info = parsing_json_with_parameter(request_for_cf, request)
    return False


def up_contest(id_contest, last_submit):  # обновление данных в Contest для бд
    if give_json(id_contest):
        return False
    global info
    if last_submit == "":
        last_submit = 0
    last = int(last_submit)
    i = 1
    for item in info:  # ищем посылку, которая была последней раньше
        if int(item[3]['creationTimeSeconds']) == int(last_submit):
            break
        if last < int(item[3]['creationTimeSeconds']):
            last = int(item[3]['creationTimeSeconds'])
        i = i + 1
    while i != 1:  # добавляем разницу между прошлой последней посылкой и текущей
        i = i - 1
        item = info[i-1]
        verdict = item[2]['verdict']
        handle = item[0]['handle']
        problem = item[1]['index']
        if type(handle) == type([]):
            for handle_1 in handle:
                if check_human(handle_1):
                    print(handle)
                    print(verdict)
                    add_new_send(id_contest, problem, handle_1, 1, verdict)
        else:
            if check_human(handle):
                print(handle)
                print(verdict)
                add_new_send(id_contest, problem, handle, 1, verdict)
    print(int(info[0][3]['creationTimeSeconds']))
    update_contest_time(id_contest, int(info[0][3]['creationTimeSeconds']))
    return True


# def add_new_human_in_contest(id_contest, human, last_submit):  # добавление данных человека в конкретный Contest
#     if give_json(id_contest):
#         return False
#     global info
#     last = last_submit
#     i = 1
#     for item in info:  # ищем посылку, которая была последней раньше
#         if last < item[4]['creationTimeSeconds'] and check_human(item[0]['handle'], id_contest):
#             last = item[4]['creationTimeSeconds']
#         i = i + 1
#     while i != 1:  # добавляем разницу между прошлой последней посылкой и текущей
#         i = i - 1
#         item = info[i - 1]
#         verdict = item[3]['verdict']
#         handle = item[0]['handle']
#         problem = item[1]['index']
#         name = item[2]['name']
#         if name == human and check_verdict(handle, id_contest, problem):
#             print(name, verdict)
#
#     return True


# def add_new_human(human):  # добавление данных человека во все Contest
#     if human == "" or STR_TYPE != type(human):
#         return False
#     id_contest = 1
#     last = 1
#     if add_new_human_in_contest(id_contest, human, last):
#         return True
#     return False

def launch_all():
    print('Hello')
    pupils_ = get_all_pupils()
    for item in pupils_:
        pupils.add(item.CF)
    contest = get_all_contests()
    for item in contest:
        cnt = 0
        print(item.link)
        while cnt < 100 and (not up_contest(item.link, item.last_update)):
            cnt = cnt + 1
    return

