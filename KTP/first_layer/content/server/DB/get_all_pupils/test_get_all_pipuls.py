import sys
sys.path.append('C:/Users/Huawei/Desktop/3_year/tppo_db/')
from  main_DB_modul import *


pupils = get_all_pupils()

for [surname, name, patronymic, cf, div_name, pupil_id, div_id] in pupils:
		print(surname, name, patronymic, cf, div_name, pupil_id, div_id)

