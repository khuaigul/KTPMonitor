from datetime import datetime
# from main_DB_modul import *
from .DB.add_contest.add_contest import add_contest
from .DB.add_new_div.add_new_div import add_new_div
from .DB.add_new_pupil.add_new_pupil import add_new_pupil
from .DB.change_pupil_div.change_pupil_div import change_pupil_div
from .DB.delete_div.delete_div import delete_div
from .DB.get_all_contests.get_all_contests import get_all_contests
from .DB.get_all_divs.get_all_divs import get_all_divs
from .DB.get_all_pupils.get_all_pupils import get_all_pupils

class New_div:
	def __init__(self, name, year):
		self.name = name
		self.year = year

class New_pupil:
	def __init__(self, surname, name, patronymic, school, grade, nick_CF, birthday):
		self.surname = surname
		self.name = name
		self.patronymic = patronymic

		self.school = school
		self.grade = grade
		self.nick_CF = nick_CF
		self.birthday = birthday

class pupil_div:
	def __init__(self, pupil_id, div_id):
		self.pupil_id = pupil_id
		self.div_id = div_id

class contest:
	def __init__(self, name, link, div_id, tasks, pupils_tasks):
		self.name = name
		self.link = link
		self.div_id = div_id
		self.tasks = tasks
		self.pupils_tasks = pupils_tasks

class task:
	def __init__(self, letter, name):
		self.letter = letter
		self.name = name

class pupil_task:
	def __init__(self, pupil_CF, task_letter, cnt_try, result):
		self.pupil_CF = pupil_CF
		self.task_letter = task_letter
		self.cnt_try = cnt_try
		self.result = result


def add_div(info):  # добавление дивизиона
	if info == "":
		return {"status": False}
	current_date = str(datetime.today())
	try:
		div = New_div(info, "2023")
		add_new_div(div)
		return {"status": True}
	except:
		return {"status": False}


def remove_div(info):
	if info == "":
		return {"status": False}
	try:
		divs = get_all_divs()
		id_remove = None
		for [name, _id] in divs:
			if name == info:
				id_remove = _id
		if id_remove is None:
			return {"status": False}
		delete_div(id_remove)
		return {"status": True}
	except:
		return {"status": False}


def change_people_div(info):
	if info["div"] == "" or info["nickname"] == "":
		return {"status": False}
	divs = get_all_divs()
	dive_id = None
	for [name, _id] in divs:
		if name == info['div'] or info['div'] == "не выбрано" and name == "NULL":
			dive_id = _id

	people_id = None
	pupils = get_all_pupils()
	for [surname, name, patronymic, cf, div_name, pupil_id, div_id] in pupils:
		if info['nickname'] == cf:
			people_id = pupil_id
	ch = pupil_div(people_id, dive_id)
	change_pupil_div(ch)
	return {"status": True}


def write_div():
	try:
		divs = get_all_divs()
		div_write = dict()
		div_name = []
		div_write["status"] = True
		for [name, _id] in divs:
			if name == "NULL":
				continue
			div_name.append(name)
		div_name.append("не выбрано")
		div_write["divisions"] = div_name
		return div_write
	except:
		return {"status": False}
