from datetime import datetime
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


def people_add(info):
	if info.POST["name"] == "":
		return {"status": False}
	pupil = New_pupil(info.POST["name"], info.POST["surname"], info.POST["secondname"], info.POST["school"], "10", info.POST["nickname"], info.POST["datebirth"])
	add_new_pupil(pupil)


def people_write_one(info):
	if info == "":
		return {"status": False}
	pupils = get_all_pupils()
	write_people = dict()
	write_people["nickname"] = info
	for [surname, name, patronymic, cf, div_name, pupil_id, div_id] in pupils:
		if info == cf:
			write_people["surname"] = surname
			write_people["name"] = name
			write_people["secondname"] = patronymic
			if div_name == "NULL":
				write_people["div"] = "не выбрано"
			else:
				write_people["div"] = div_name
	return write_people


def people_write_div():
	pupils = get_all_pupils()
	write_people = {}
	name_people = []
	for [surname, name, patronymic, cf, div_name, pupil_id, div_id] in pupils:
		info_people = dict()
		info_people["nickname"] = cf
		info_people["surname"] = surname
		info_people["name"] = name
		info_people["secondname"] = patronymic
		if div_name == "NULL":
			info_people["div"] = "не выбрано"
		else:
			info_people["div"] = div_name
		name_people.append(info_people)
	write_people["students"] = name_people
	return write_people


def people_write_div_onle(info):
	if info == "":
		return {"status": False}
	pupils = get_all_pupils()
	write_people = {}
	name_people = []
	for [surname, name, patronymic, cf, div_name, pupil_id, div_id] in pupils:
		if div_name == info or info == "не выбрано" and div_name == "NULL":
			info_people = dict()
			info_people["nickname"] = cf
			info_people["surname"] = surname
			info_people["name"] = name
			info_people["secondname"] = patronymic
			info_people["div"] = div_name
			name_people.append(info_people)
	write_people["students"] = name_people
	return write_people
