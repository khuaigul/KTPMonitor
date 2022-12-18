import sys
sys.path.append('C:/Users/Huawei/Desktop/3_year/tppo_db/')
from  main_DB_modul import *

divs = get_all_divs()

for [name, _id] in divs:
		print(name, _id)

