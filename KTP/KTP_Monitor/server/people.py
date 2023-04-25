from .DB.main_DB_modul import *


def people_write_one(info):
	if info == "":
		return {"status": False}
	pupils = get_all_pupils()
	write_people = dict()
	write_people["status"] = True
	write_people["nickname"] = info
	for [surname, name, patronymic, cf, div_name, pupil_id, div_id] in pupils:
		if info == cf:
			write_people["surname"] = surname
			write_people["name"] = name
			write_people["secondname"] = patronymic
			write_people["div"] = check_div(div_name)
	return write_people


def people_write_all():
	pupils = get_all_pupils()
	write_people = dict()
	write_people["status"] = True
	name_people = []
	for item in pupils:
		info_people = dict()
		info_people["nickname"] = item.CF
		info_people["surname"] = item.lastname
		info_people["name"] = item.name
		info_people["secondname"] = item.secondname
		info_people["div"] = item.div.name
		name_people.append(info_people)
	write_people["pupils"] = name_people
	return write_people


def people_write_div(info):
	if info == "":
		return {"status": False}
	divs = get_all_divs()
	for item in divs:
		if item.name == info or info == 'не выбрано' and item.name == 'NULL':
			pupils = get_all_pupils(item)
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
