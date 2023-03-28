import sys
sys.path.append('C:/Users/Huawei/Desktop/3_year/tppo_db/')
from  main_DB_modul import *

class pupil_div:
	def __init__(self, pupil_id, div_id):
		self.pupil_id = pupil_id
		self.div_id = div_id

ch = pupil_div("1", "2")
change_pupil_div(ch)