# from 'C:\\Users\\Huawei\\Desktop\\3_year\\tppo_db\\main_DB_modul' import *
import sys
sys.path.append('C:/Users/Huawei/Desktop/3_year/tppo_db/')
from  main_DB_modul import *


class New_div:
	def __init__(self, name, year):
		self.name = name
		self.year = year

div2 = New_div("test_div2", "2020")
div3 = New_div("test_div3", "2020")
div4 = New_div("test_div4", "2020")

add_new_div(div2)
add_new_div(div3)
add_new_div(div4)

	