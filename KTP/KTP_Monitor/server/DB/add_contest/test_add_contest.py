import sys
sys.path.append('C:/Users/Huawei/Desktop/3_year/tppo_db/')
from  main_DB_modul import *

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

class contest:
	def __init__(self, name, link, div_id, tasks, pupils_tasks):
		self.name = name
		self.link = link
		self.div_id = div_id
		self.tasks = tasks
		self.pupils_tasks = pupils_tasks


tasks = []
t1 = task('A', "Aaa")
t2 = task('B', "Bbb")
t3 = task('C', "Ccc")

tasks.append(t1)
tasks.append(t2)
tasks.append(t3)

pup_task = []
pt1 = pupil_task('CF_Nat', 'A', '5', '+')
pt2 = pupil_task('CF_Nat', 'B', '1', '-')
pt3 = pupil_task('CF_Dan', 'A', '90', '-')

pup_task.append(pt1)
pup_task.append(pt2)
pup_task.append(pt3)


con = contest("Traning", "link_CF", '2', tasks, pup_task)

add_contest(con)