import sys
sys.path.append('C:/Users/Huawei/Desktop/3_year/tppo_db/')
from  main_DB_modul import *

class New_pupil:
	def __init__(self, surname, name, patronymic, school, grade, nick_CF, birthday):
		self.surname = surname
		self.name = name
		self.patronymic = patronymic

		self.school = school
		self.grade = grade
		self.nick_CF = nick_CF
		self.birthday = birthday
		
		

pupil1 = New_pupil("test_Sob", "test_Nat", "test_Nik", "school 666", "10", "CF_Nat", "2001-05-15")
pupil2 = New_pupil("test_R", "test_Dan", "test_ooo", "school 666", "10", "CF_Dan", "2001-05-15")

add_new_pupil(pupil1)
add_new_pupil(pupil2)

print("test add pipul positive")