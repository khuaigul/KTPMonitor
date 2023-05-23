from django.test import TestCase
from .server.DB.main_DB_modul import *
from .server.API_CF import *
from .models import *
import datetime


# Create your tests here.
class LogicTestCase(TestCase):
    link = "156"
    letter = "A"
    name_contest = "Поток минимальной стоимости"
    lastname = "Ройтбурд"
    firstname = "Дан"
    secondname = "Дмитриевич"
    CF = "DanRo"
    birthday = "2002-07-23"
    school = "46"
    grade = "11"
    phone = "89119029770"
    e_mail = "qwe@mail.ru"

    def test_B1(selfse):
        result = authorized_request("contest.standings", [("contestId", "566"), ("showUnofficial", "true")])
        selfse.assertEqual('OK', result['status'])
    def test_B2(selfse):
        result = add_new_div("A")
        selfse.assertEqual(True, result)

    def test_B3(selfse):
        Div_Info.objects.get_or_create(name="A", year=datetime.date.today().year)
        result = add_new_div("A")
        selfse.assertEqual(False, result)

    def test_B4(selfse):
        Div_Info.objects.get_or_create(name="A", year="1")
        Div_Info.objects.get_or_create(name="B", year="1")
        result = get_all_divs()
        selfse.assertEqual([Div_Info.objects.get(name="A"), Div_Info.objects.get(name="B")], result)

    def test_B5(selfse):
        result = get_all_divs()
        selfse.assertEqual([], result)

    def test_B6(selfse):
        user = User.objects.create_user("qwe@mail.ru", "qwe@mail.ru", "123")
        result = add_new_pupil(user, selfse.lastname, selfse.firstname, selfse.secondname, selfse.CF,
                               selfse.birthday, selfse.school, selfse.grade, selfse.phone, selfse.e_mail)
        selfse.assertEqual(True, result)

    def test_B7(selfse):
        user = User.objects.create_user("qwe@mail.ru", "qwe@mail.ru", "123")
        Pupil_Info.objects.create(user=user, lastname=selfse.lastname, firstname=selfse.firstname,
                                  secondname=selfse.secondname, CF=selfse.CF, birthday=selfse.birthday,
                                  school=selfse.school, grade=selfse.grade, phone=selfse.phone, e_mail=selfse.e_mail)
        result = add_new_pupil(user, selfse.lastname, selfse.firstname, selfse.secondname, selfse.CF,
                               selfse.birthday, selfse.school, selfse.grade, selfse.phone, selfse.e_mail)
        selfse.assertEqual(False, result)

    def test_B8(selfse):
        user = User.objects.create_user("qwe@mail.ru", "qwe@mail.ru", "123")
        result = add_new_teacher(user, selfse.lastname, selfse.firstname, selfse.secondname, selfse.CF, selfse.phone)
        selfse.assertEqual(True, result)

    def test_B9(selfse):
        user = User.objects.create_user("qwe@mail.ru", "qwe@mail.ru", "123")
        Teacher_Info.objects.create(user=user, lastname=selfse.lastname,
                                    firstname=selfse.firstname, secondname=selfse.secondname,
                                    CF=selfse.CF, phone=selfse.phone)
        result = add_new_teacher(user, selfse.lastname, selfse.firstname, selfse.secondname, selfse.CF, selfse.phone)
        selfse.assertEqual(False, result)

    def test_B10(selfse):
        user = User.objects.create_user("qwe@mail.ru", "qwe@mail.ru", "123")
        Pupil_Info.objects.create(user=user, lastname=selfse.lastname, firstname=selfse.firstname,
                                  secondname=selfse.secondname, CF=selfse.CF, birthday=selfse.birthday,
                                  school=selfse.school, grade=selfse.grade, phone=selfse.phone, e_mail=selfse.e_mail)
        result = get_all_pupils()
        selfse.assertEqual([Pupil_Info.objects.get(user=user)], result)

    def test_B11(selfse):
        result = get_all_pupils()
        selfse.assertEqual([], result)

    def test_B12(selfse):
        Div_Info.objects.get_or_create(name="A", year="1")
        user = User.objects.create_user("qwe@mail.ru", "qwe@mail.ru", "123")
        Pupil_Info.objects.create(user=user, lastname=selfse.lastname, firstname=selfse.firstname,
                                  secondname=selfse.secondname, CF=selfse.CF, birthday=selfse.birthday,
                                  school=selfse.school, grade=selfse.grade, phone=selfse.phone, e_mail=selfse.e_mail)
        pupil = Pupil_Info.objects.get(user=user)
        pupil.div = Div_Info.objects.get(name="A")
        pupil.save()
        result = get_all_pupils([Div_Info.objects.get(name="A")])
        selfse.assertEqual([Pupil_Info.objects.get(user=user)], result)

    def test_B13(selfse):
        Div_Info.objects.get_or_create(name="A", year="1")
        user = User.objects.create_user("qwe@mail.ru", "qwe@mail.ru", "123")
        Pupil_Info.objects.create(user=user, lastname=selfse.lastname, firstname=selfse.firstname,
                                  secondname=selfse.secondname, CF=selfse.CF, birthday=selfse.birthday,
                                  school=selfse.school, grade=selfse.grade, phone=selfse.phone, e_mail=selfse.e_mail)
        result = change_pupil_div(Pupil_Info.objects.get(user=user), Div_Info.objects.get(name="A"))
        selfse.assertEqual(True, result)

    def test_B14(selfse):
        Div_Info.objects.get_or_create(name="A", year="1")
        result = delete_div(Div_Info.objects.get(name="A"))
        selfse.assertEqual(True, result)

    def test_B15(selfse):
        Div_Info.objects.get_or_create(name="A", year="1")
        result = add_contest("Потоки", "156", [Div_Info.objects.get(name="A")])
        selfse.assertEqual(True, result)

    def test_B16(selfse):
        Div_Info.objects.get_or_create(name="A", year="1")
        Contest_Info.objects.create(name="Потоки", link="156")
        result = add_contest("Потоки", "156", [Div_Info.objects.get(name="A")])
        selfse.assertEqual(False, result)

    def test_B17(selfse):
        Div_Info.objects.get_or_create(name="A", year="1")
        Contest_Info.objects.create(name="Потоки", link="156")
        result = add_task(selfse.link, selfse.letter, selfse.name_contest)
        selfse.assertEqual(True, result)

    def test_B18(selfse):
        Div_Info.objects.get_or_create(name="A", year="1")
        Contest_Info.objects.create(name="Потоки", link="156")
        Task_Info.objects.create(contest=Contest_Info.objects.get(link=selfse.link),
                                 letter=selfse.letter, name=selfse.name_contest)
        result = add_task(selfse.link, selfse.letter, selfse.name_contest)
        selfse.assertEqual(False, result)

    def test_B19(selfse):
        Div_Info.objects.get_or_create(name="A", year="1")
        Contest_Info.objects.create(name="Потоки", link="156")
        Task_Info.objects.create(contest=Contest_Info.objects.get(link=selfse.link),
                                 letter=selfse.letter, name=selfse.name_contest)
        user = User.objects.create_user("qwe@mail.ru", "qwe@mail.ru", "123")
        Pupil_Info.objects.create(user=user, lastname=selfse.lastname, firstname=selfse.firstname,
                                  secondname=selfse.secondname, CF=selfse.CF, birthday=selfse.birthday,
                                  school=selfse.school, grade=selfse.grade, phone=selfse.phone,
                                  e_mail=selfse.e_mail)
        result = add_new_send(selfse.link, selfse.letter, selfse.CF, 1, "Ok")
        selfse.assertEqual(True, result)

    def test_B20(selfse):
        user = User.objects.create_user("qwe@mail.ru", "qwe@mail.ru", "123")
        Teacher_Info.objects.create(user=user, lastname=selfse.lastname,
                                    firstname=selfse.firstname, secondname=selfse.secondname,
                                    CF=selfse.CF, phone=selfse.phone)
        teacher = Teacher_Info.objects.get(user=user)
        result = get_all_teachers()
        selfse.assertEqual([teacher], result)

    def test_B21(selfse):
        result = get_all_teachers()
        selfse.assertEqual([], result)

    def test_B22(selfse):
        Div_Info.objects.get_or_create(name="A", year="1")
        user = User.objects.create_user("qwe@mail.ru", "qwe@mail.ru", "123")
        Teacher_Info.objects.create(user=user, lastname=selfse.lastname,
                                    firstname=selfse.firstname, secondname=selfse.secondname,
                                    CF=selfse.CF, phone=selfse.phone)
        teacher = Teacher_Info.objects.get(user=user)
        teacher.div = Div_Info.objects.get(name="A")
        teacher.save()
        result = get_all_teachers([Div_Info.objects.get(name="A")])
        selfse.assertEqual([teacher], result)

    def test_B23(selfse):
        Div_Info.objects.get_or_create(name="A", year="1")
        user = User.objects.create_user("qwe@mail.ru", "qwe@mail.ru", "123")
        Pupil_Info.objects.create(user=user, lastname=selfse.lastname, firstname=selfse.firstname,
                                  secondname=selfse.secondname, CF=selfse.CF, birthday=selfse.birthday,
                                  school=selfse.school, grade=selfse.grade, phone=selfse.phone,
                                  e_mail=selfse.e_mail)
        pupil = Pupil_Info.objects.get(user=user)
        pupil.div = Div_Info.objects.get(name="A")
        pupil.save()
        add_contest("Потоки", selfse.link, [Div_Info.objects.get(name="A")])
        Task_Info.objects.create(contest=Contest_Info.objects.get(link=selfse.link),
                                 letter=selfse.letter, name=selfse.name_contest)
        add_new_send(selfse.link, selfse.letter, selfse.CF, 1, "WA")
        result = get_statistic_contest(selfse.link)
        selfse.assertEqual({list(Task_Info.objects.filter(contest=Contest_Info.objects.get(link="156")))[0]:
                                {pupil: (1, "WA")}}, result)

    def test_B24(selfse):
        Div_Info.objects.get_or_create(name="A", year="1")
        user = User.objects.create_user("qwe@mail.ru", "qwe@mail.ru", "123")
        Pupil_Info.objects.create(user=user, lastname=selfse.lastname, firstname=selfse.firstname,
                                  secondname=selfse.secondname, CF=selfse.CF, birthday=selfse.birthday,
                                  school=selfse.school, grade=selfse.grade, phone=selfse.phone,
                                  e_mail=selfse.e_mail)
        pupil = Pupil_Info.objects.get(user=user)
        pupil.div = Div_Info.objects.get(name="A")
        pupil.save()
        add_contest("Потоки", selfse.link, [Div_Info.objects.get(name="A")])
        Task_Info.objects.create(contest=Contest_Info.objects.get(link=selfse.link),
                                 letter=selfse.letter, name=selfse.name_contest)
        result = get_statistic_contest("156")
        selfse.assertEqual({list(Task_Info.objects.filter(contest=Contest_Info.objects.get(link="156")))[0]:
                                {pupil: (0, None)}}, result)

    def test_B25(selfse):
        Contest_Info.objects.create(name="Потоки", link="156")
        result = get_all_contests()
        selfse.assertEqual([Contest_Info.objects.get(link="156")], result)

    def test_B26(selfse):
        result = get_all_contests()
        selfse.assertEqual([], result)

    def test_B27(selfse):
        Div_Info.objects.get_or_create(name="A", year="1")
        add_contest("Потоки", selfse.link, [Div_Info.objects.get(name="A")])
        result = get_all_contests([Div_Info.objects.get(name="A")])
        selfse.assertEqual([Contest_Info.objects.get(link="156")], result)

    def test_B28(selfse):
        Div_Info.objects.get_or_create(name="A", year="1")
        add_contest("Потоки", selfse.link, [Div_Info.objects.get(name="A")])
        result = delete_contest(selfse.link)
        selfse.assertEqual(True, result)

    def test_B29(selfse):
        Div_Info.objects.get_or_create(name="A", year="1")
        user = User.objects.create_user("qwe@mail.ru", "qwe@mail.ru", "123")
        Pupil_Info.objects.create(user=user, lastname=selfse.lastname, firstname=selfse.firstname,
                                  secondname=selfse.secondname, CF=selfse.CF, birthday=selfse.birthday,
                                  school=selfse.school, grade=selfse.grade, phone=selfse.phone,
                                  e_mail=selfse.e_mail)
        pupil = Pupil_Info.objects.get(user=user)
        pupil.div = Div_Info.objects.get(name="A")
        pupil.save()
        add_contest("Потоки", selfse.link, [Div_Info.objects.get(name="A")])
        Task_Info.objects.create(contest=Contest_Info.objects.get(link=selfse.link),
                                 letter=selfse.letter, name=selfse.name_contest)
        add_new_send(selfse.link, selfse.letter, selfse.CF, 1, "WA")
        result = get_statistic_pupil_contest([Pupil_Info.objects.get(user=user)], [selfse.link])
        selfse.assertEqual({selfse.link: {selfse.CF: (0, 1)}}, result)

