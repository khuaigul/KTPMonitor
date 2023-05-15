# Вот этот файл нужен для того, чтобы убрать лишнею информацию из json, который мы получили с cf.
# Кратко что происходит ниже.
# Даём в функцию parsing_json_with_parameter 2 параметра json и параметр
# При чём параметр это то что мы хотим и в таком же виде, как и в json.
# Так как информация, которая нам дали может находиться в списке в списке и глубже.
# Давайте спустимся рекурсивно до того слоя который нам нужен и выведем ответ.
# Вот что эти функции и делают.
# p.s если вы это всё прочитали и вам не помогло то грустно:(


LIST_TYPE = type([])
DICT_TYPE = type({})
STR_TYPE = type("qwe")


def check(info_pars2):  # проверяем массив dict если там 1 элемент то выводим без массива
    if len(info_pars2) == 1:
        return info_pars2[0]
    else:
        return info_pars2


def not_deep(info, params, item):  # если не надо глубоко спускаться, то всё чёткое выводим ответ
    if type(info[item]) == LIST_TYPE:
        info_pars2 = []
        for item2 in info[item]:
            info_pars2.append(item2[params[item]])
        return check(info_pars2)
    else:
        return info[item][params[item]]


def depth_detection(info, params):  # Решим надо ли нам глубже спускаться (типа {a:{b:{c:d}}})
    info_pars = {}
    for item in params:
        if type(params[item]) == LIST_TYPE or type(params[item]) == DICT_TYPE:
            if type(parsing_json(info[item], params[item])) == LIST_TYPE:
                if type(parsing_json(info[item], params[item])[0]) == LIST_TYPE:
                    return parsing_json(info[item], params[item])
                for item2 in parsing_json(info[item], params[item]):
                    info_pars = {**info_pars, **item2}
            else:
                info_pars = {**info_pars , **parsing_json(info[item], params[item])}
        else:
            info_pars[params[item]] = not_deep(info, params, item)
    return info_pars


def parsing_parameter_array(info, params):  # Функция, которая разбивает массив параметров
    new_json1 = []
    for item in params:
        if type(item) == STR_TYPE:
            new_json1.append({item: info[item]})
        else:
            new_json1.append(depth_detection(info, item))
    return new_json1


def parsing_parameter(info, params):  # функция, которая решает что у нас из себя представляет параметр
    if type(params) == LIST_TYPE:
        return parsing_parameter_array(info, params)
    else:
        return depth_detection(info, params)


def parsing_json(info, params):  # функция, которая разбивает массив json на элементы если они есть
    new_json = []
    if type(info) == DICT_TYPE:
        return parsing_parameter(info, params)
    else:
        for item in info:
            new_json.append(parsing_parameter(item, params))
    return new_json


def parsing_json_with_parameter(info, params):  # функция, которую будут import
    return parsing_json(info, params)
