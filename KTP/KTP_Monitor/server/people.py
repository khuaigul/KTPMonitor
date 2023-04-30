from .DB.main_DB_modul import *
from .chek import *


def people_write_all():
	pupils = get_all_pupils()
	write_people = dict()
	write_people["status"] = True
	name_people = []
	for item in pupils:
		info_people = dict()
		info_people["nickname"] = item.CF
		info_people["surname"] = item.lastname
		info_people["name"] = item.firstname
		info_people["secondname"] = item.secondname
		if item.div == None:
			info_people["div"] = check_div(item.div)
		else:
			info_people["div"] = check_div(item.div.name)
		name_people.append(info_people)
	write_people["pupils"] = name_people
	return write_people


def f():  # не бейте просто пока не предусмотрено, что делать с людими без дива
	pupils = get_all_pupils()
	write_people = dict()
	write_people["status"] = True
	name_people = []
	for item in pupils:
		info_people = dict()
		if item.div == None:
			info_people["nickname"] = item.CF
			info_people["surname"] = item.lastname
			info_people["name"] = item.firstname
			info_people["secondname"] = item.secondname
			name_people.append(info_people)
	write_people["pupils"] = name_people
	return write_people


def people_write_div(info):
	if info == "":
		return {"status": False}
	if info == "не выбран":
		return f()
	divs = get_all_divs()
	flag = True
	for item in divs:
		if item.name == info:
			pupils = get_all_pupils([item])
			flag = False
			break
	if flag:
		return {"status": False}
	write_people = dict()
	write_people["status"] = True
	name_people = []
	for item in pupils:
		info_people = dict()
		info_people["nickname"] = item.CF
		info_people["surname"] = item.lastname
		info_people["name"] = item.firstname
		info_people["secondname"] = item.secondname
		name_people.append(info_people)
	write_people["pupils"] = name_people
	return write_people


def profile_write(nickname):
	if nickname == "":
		return {"status": False}
	write_people = dict()
	write_people["status"] = True
	pupils = get_all_pupils()
	for item in pupils:
		if nickname == item.CF:
			write_people["surname"] = item.lastname
			write_people["name"] = item.firstname
			write_people["secondname"] = item.secondname
			write_people["school"] = item.school
			write_people["email"] = item.e_mail
			write_people["phone"] = item.phone
			write_people["grade"] = item.grade
			if item.div == None:
				write_people["division"] = check_div(item.div)
			else:
				write_people["division"] = check_div(item.div.name)
			write_people["datebitrh"] = item.birthday
			break
	return write_people


def teacher_write_div(info):
	if info == "":
		return {"status": False}
	divs = get_all_divs()
	flag = 1
	teachers = []
	for item in divs:
		if item.name == info or info == 'не выбрано':
			teachers = get_all_teachers(item)
			flag = 0
			break
	if flag:
		return {"status": False}
	write_teachers = dict()
	write_teachers["status"] = True
	all_teachers = []
	for item in teachers:
		info_teachers = dict()
		info_teachers["surname"] = item.lastname
		info_teachers["name"] = item.firstname
		info_teachers["secondname"] = item.secondname
		all_teachers.append(info_teachers)
	write_teachers["teachers"] = all_teachers
	return write_teachers


