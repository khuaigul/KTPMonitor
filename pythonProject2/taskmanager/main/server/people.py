# import json
#
# def people_add(info):
# 	pupil = New_pupil(info["name"], info["surname"], info["patronymic"], info["school"], "10", info["cf"], info["date"])
# 	add_new_pupil(pupil)
#
# def people_write():
# 	pupils = get_all_pupils()
# 	write_people = {}
# 	name_people = []
# 	for [surname, name, patronymic, cf, div_name, pupil_id, div_id] in pupils:
# 		info_people = {}
# 		info_people["surname"] = surname
# 		info_people["name" ] = name
# 		info_people["secondname" ] = patronymic
# 		info_people["div" ] = div_name
# 		name_people.append(info_people)
# 	write_people["students"] = name_people
# 	return json.dumps(write_people, sort_keys=True, ensure_ascii=False, separators=(",", ": "))
#
# def people_write_onli_name():
# 	pupils = get_all_pupils()
# 	write_people = {}
# 	name_people = []
# 	for [surname, name, patronymic, cf, div_name, pupil_id, div_id] in pupils:
# 		info_people = {}
# 		info_people["surname"] = surname
# 		info_people["name" ] = name
# 		info_people["secondname" ] = patronymic
# 		name_people.append(info_people)
# 	write_people["students"] = name_people
# 	return json.dumps(write_people, sort_keys=True, ensure_ascii=False, separators=(",", ": "))
