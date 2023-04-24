from .DB.main_DB_modul import *


def add_div(info):  # добавление дивизиона
	if info == "":
		return {"status": False}
	add_new_div(info)
	return {"status": True}


def remove_div(info):
	if info == "":
		return {"status": False}
	divs = get_all_divs()
	for item in divs:
		if item.name == info:
			delete_div(item)
			return {"status": True}
	return {"status": False}


def change_people_div(info):
	if info["divisions"] == "" or info["nickname"] == "":
		return {"status": False}
	divs = get_all_divs()
	dive_id = None
	for item in divs:
		if item.name == info['divisions'] or info['divisions'] == "не выбрано" and item.name == "NULL":
			dive_id = item
			break
	people_id = None
	pupils = get_all_pupils()
	for item in pupils:
		if info['nickname'] == item.CF:
			people_id = item
			break
	change_pupil_div(dive_id, people_id)
	return {"status": True}


def write_div():
	divs = get_all_divs()
	div_write = dict()
	div_name = []
	div_write["status"] = True
	for item in divs:
		if item.name == "NULL":
			continue
		div_name.append(item.name)
	div_name.append("не выбрано")
	div_write["divisions"] = div_name
	return div_write

