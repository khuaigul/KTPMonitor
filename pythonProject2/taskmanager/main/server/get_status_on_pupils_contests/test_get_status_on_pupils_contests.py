import sys
sys.path.append('C:/Users/Huawei/Desktop/3_year/tppo_db/')
from  main_DB_modul import *


pupil_id1 = '1'
pupil_id2 = '2'

pupils = []
pupils.append(pupil_id1)
pupils.append(pupil_id2)


contest_id1 = '1'
contest_id2 = '2'

contests = []
contests.append(contest_id1)
contests.append(contest_id2)


status = get_status_on_pupils_contests(pupils, contests)

for con_id in contests:
	print('%-7s' % con_id,  end=' ')
print()

for pup_id in pupils:
	for con_id in contests:
		print('%-7s' % status[(pup_id, con_id)], end=' ')
	print()


