from .DB.main_DB_modul import *


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
		info_people["div"] = item.div.name
		name_people.append(info_people)
	write_people["pupils"] = name_people
	return write_people


def people_write_div(info):
	if info == "":
		return {"status": False, "problem": "name clear"}
	divs = get_all_divs()
	for item in divs:
		if item.name == info:
			pupils = get_all_pupils([item])
			write_people = dict()
			write_people["status"] = True
			name_people = []
			for item2 in pupils:
				info_people = dict()
				info_people["nickname"] = item2.CF
				info_people["surname"] = item2.lastname
				info_people["name"] = item2.firstname
				info_people["secondname"] = item2.secondname
				name_people.append(info_people)
			write_people["pupils"] = name_people
			return write_people
	return {"status": False, "problem": "dont take name div in bd"}


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
			write_people["division"] = item.div.name
			write_people["datebirth"] = item.birthday
			break
	return write_people


def teacher_write_div(info):
	if info == "":
		return {"status": False}
	divs = get_all_divs()
	for item in divs:
		if item.name == info:
			teachers = get_all_teachers([item])
			write_teachers = dict()
			write_teachers["status"] = True
			all_teachers = []
			for item2 in teachers:
				info_teachers = dict()
				info_teachers["surname"] = item2.lastname
				info_teachers["name"] = item2.firstname
				info_teachers["secondname"] = item2.secondname
				all_teachers.append(info_teachers)
			write_teachers["teachers"] = all_teachers
			return write_teachers
	return {"status": False}



