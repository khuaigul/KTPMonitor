from .DB.main_DB_modul import *
from .chek import *


def add_div(name):  # добавление дивизиона
	if name == "":
		return {"status": False}
	add_new_div(name)
	return {"status": True}


def remove_div(div):
	if div == "":
		return {"status": False}
	divs = get_all_divs()
	for item in divs:
		if item.name == div:
			delete_div(item)
			return {"status": True}
	return {"status": False}


def change_people_div(divisions, nickname):
	if divisions == "" or nickname == "":
		return {"status": False}
	divs = get_all_divs()
	dive_id = None
	for item in divs:
		if item.name == divisions:
			dive_id = item
			break
	people_id = None
	pupils = get_all_pupils()
	for item in pupils:
		if nickname == item.CF:
			people_id = item
			break
	change_pupil_div(people_id, dive_id)
	return {"status": True}


def write_div():
	divs = get_all_divs()
	div_write = dict()
	div_name = []
	div_write["status"] = True
	for item in divs:
		div_name.append(item.name)
	div_name.append("не выбрано")
	div_write["divisions"] = div_name
	return div_write

