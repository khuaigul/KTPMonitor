# Тут функции проверяют на валидность данных с бд хз зачем они нужны...
# А вдруг что-то пошло не так ?
# Ну не ток тут будет эти функции это пока (14.04.2023)


def check_name(name):
    if name == "NULL" or name == "":
        return "не введено"
    return name


def check_email(mail):
    if mail == "NULL" or mail == "":
        return "Нету @mail"
    return mail


def check_phone(phone):
    if phone == "NULL" or phone == "":
        return "Не введён телефон"
    return phone


def check_div(div):
    if div == "NULL" or div == "":
        return "Не выбран"
    return div


def check_surname(surname):
    if surname == "NULL" or surname == "":
        return "не введено"
    return surname


def check_secondname(secondname):
    if secondname == "NULL" or secondname == "":
        return "не введено"
    return secondname


def check_school(school):
    if school == "NULL" or school == "":
        return "не введено"
    return school


def check_form(form):
    if form == "NULL" or form == "":
        return "не введено"
    return form


def check_availability_mail(mail):  # проверяет есть ли почта в бд или нет
    info = get_email()  # функция которая получает все почты бд
    for item in info:
        if mail == item:
            return True
    return False


def check_nickname(nickname):
    if nickname == '' or nickname == 'NULL':
        return False
    return True
