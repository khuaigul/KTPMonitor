import sys
sys.path.append('C:/Users/Huawei/Desktop/3_year/tppo_db/')
from  main_DB_modul import *

contests = get_all_contests()

for [name, contest_id, div_id] in contests:
		print(name, contest_id, div_id)


