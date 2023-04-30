# Тут функции проверяют на валидность данных с бд хз зачем они нужны...
# А вдруг что-то пошло не так ?
# Ну не ток тут будет эти функции это пока (14.04.2023)


def check_name(name):
    if name == None or name == "":
        return "не введено"
    return name


def check_email(mail):
    if mail == None or mail == "":
        return "Нету @mail"
    return mail


def check_phone(phone):
    if phone == None or phone == "":
        return "Не введён телефон"
    return phone


def check_div(div):
    if div == None or div == "":
        return "не выбран"
    return div


def check_surname(surname):
    if surname == None or surname == "":
        return "не введено"
    return surname


def check_secondname(secondname):
    if secondname == None or secondname == "":
        return "не введено"
    return secondname


def check_school(school):
    if school == None or school == "":
        return "не введено"
    return school


def check_form(form):
    if form == None or form == "":
        return "не введено"
    return form


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

