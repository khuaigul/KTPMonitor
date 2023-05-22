from django.test import TestCase
from .server.DB.main_DB_modul import *
from .models import *

# Create your tests here.
class LogicTestCase(TestCase):
    def test_B2(selfse):
        result = add_new_div("A")
        selfse.assertEqual(True, result)

    def test_B3(selfse):
        add_new_div("A")
        result = add_new_div("A")
        selfse.assertEqual(False, result)

    def test_B4(selfse):
        add_new_div("A")
        add_new_div("B")
        add_new_div("C")
        info_div = get_all_divs()
        result = []
        for item in info_div:
            result.append(item.name)
        selfse.assertEqual(["A", "B", "C"], result)

    def test_B5(selfse):
        result = get_all_divs()
        selfse.assertEqual([], result)

    def test_B6(selfse):
        user = User.objects.create_user("qwe@mail.ru", "qwe@mail.ru", "123")
        lastname = "Ройтбурд"
        firstname = "Дан"
        secondname = "Дмитриевич"
        CF = "DanRo"
        birthday = "2002-07-23"
        school = "46"
        grade = "11"
        phone = "89119029770"
        e_mail = "qwe@mail.ru"
        result = add_new_pupil(user, lastname, firstname, secondname, CF, birthday, school, grade, phone, e_mail)
        selfse.assertEqual(True, result)

    def test_B7(selfse):
        user = User.objects.create_user("qwe@mail.ru", "qwe@mail.ru", "123")
        lastname = "Ройтбурд"
        firstname = "Дан"
        secondname = "Дмитриевич"
        CF = "DanRo"
        birthday = "2002-07-23"
        school = "46"
        grade = "11"
        phone = "89119029770"
        e_mail = "qwe@mail.ru"
        add_new_pupil(user, lastname, firstname, secondname, CF, birthday, school, grade, phone, e_mail)
        result = add_new_pupil(user, lastname, firstname, secondname, CF, birthday, school, grade, phone, e_mail)
        selfse.assertEqual(False, result)

    def test_B8(selfse):
        user = User.objects.create_user("qwe@mail.ru", "qwe@mail.ru", "123")
        lastname = "Ройтбурд"
        firstname = "Дан"
        secondname = "Дмитриевич"
        CF = "DanRo"
        phone = "89119029770"
        result = add_new_teacher(user, lastname, firstname, secondname, CF, phone)
        selfse.assertEqual(True, result)

    def test_B9(selfse):
        user = User.objects.create_user("qwe@mail.ru", "qwe@mail.ru", "123")
        lastname = "Ройтбурд"
        firstname = "Дан"
        secondname = "Дмитриевич"
        CF = "DanRo"
        phone = "89119029770"
        add_new_teacher(user, lastname, firstname, secondname, CF, phone)
        result = add_new_teacher(user, lastname, firstname, secondname, CF, phone)
        selfse.assertEqual(False, result)

    def test_B10(selfse):
        user = User.objects.create_user("qwe@mail.ru", "qwe@mail.ru", "123")
        lastname = "Ройтбурд"
        firstname = "Дан"
        secondname = "Дмитриевич"
        CF = "DanRo"
        birthday = "2002-07-23"
        school = "46"
        grade = "11"
        phone = "89119029770"
        e_mail = "qwe@mail.ru"
        add_new_pupil(user, lastname, firstname, secondname, CF, birthday, school, grade, phone, e_mail)
        info_pupils = get_all_pupils()
        result = []
        for item in info_pupils:
            result.append(item.CF)
        selfse.assertEqual(["DanRo"], result)

    def test_B11(selfse):
        result = get_all_pupils()
        selfse.assertEqual([], result)

    def test_B12(selfse):
        add_new_div("A")
        info_div = get_all_divs()
        info_div = info_div[0]
        user = User.objects.create_user("qwe@mail.ru", "qwe@mail.ru", "123")
        lastname = "Ройтбурд"
        firstname = "Дан"
        secondname = "Дмитриевич"
        CF = "DanRo"
        birthday = "2002-07-23"
        school = "46"
        grade = "11"
        phone = "89119029770"
        e_mail = "qwe@mail.ru"
        add_new_pupil(user, lastname, firstname, secondname, CF, birthday, school, grade, phone, e_mail)
        info_pupils = get_all_pupils()
        info_pupils = info_pupils[0]
        change_pupil_div(info_pupils, info_div)
        info_pupils = get_all_pupils([info_div])
        result = []
        for item in info_pupils:
            result.append(item.CF)
        selfse.assertEqual(["DanRo"], result)

    def test_B12(selfse):
        add_new_div("A")
        info_div = get_all_divs()
        info_div = info_div[0]
        user = User.objects.create_user("qwe@mail.ru", "qwe@mail.ru", "123")
        lastname = "Ройтбурд"
        firstname = "Дан"
        secondname = "Дмитриевич"
        CF = "DanRo"
        birthday = "2002-07-23"
        school = "46"
        grade = "11"
        phone = "89119029770"
        e_mail = "qwe@mail.ru"
        add_new_pupil(user, lastname, firstname, secondname, CF, birthday, school, grade, phone, e_mail)
        info_pupils = get_all_pupils()
        info_pupils = info_pupils[0]
        result = change_pupil_div(info_pupils, info_div)
        selfse.assertEqual(True, result)

