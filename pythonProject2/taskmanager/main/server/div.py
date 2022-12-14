from datetime import datetime
import json

# def add_div(info):
# 	current_date = date.today()
# 	div = New_div(info['name'], current_date)
# 	add_new_div(div)
#
# def remove_div(info):
# 	divs = get_all_divs()
# 	id_dalete = None
# 	for [name, _id] in divs:
# 		if name == info['div']:
# 			id_dalete = _id
# 	delete_div(id_dalete)
#
# def change_people_div(info):
# 	divs = get_all_divs()
# 	dive_id = None
# 	for [name, _id] in divs:
# 		if name == info['div']:
# 			dive_id = _id
#
# 	people_id = None
# 	pupils = get_all_pupils()
# 	for [surname, name, patronymic, cf, div_name, pupil_id, div_id] in pupils:
# 		print(surname, name, patronymic, cf, div_name, pupil_id, div_id)
# 		if info['name'] == name && info['surname'] == surname && info['patronymic'] == patronymic :
# 			people_id = pupil_id
#
# 	ch = pupil_div(people_id, dive_id)
# 	change_pupil_div(ch)
#
# def write_div():
# 	divs = get_all_divs()
# 	write_div = {}
# 	div_name = []
# 	for [name, _id] in divs:
# 		div_name.append(name)
# 	write_div["divisions"] = div_name
# 	return json.dumps(write_div, sort_keys=True, ensure_ascii=False, separators=(",", ": "))
