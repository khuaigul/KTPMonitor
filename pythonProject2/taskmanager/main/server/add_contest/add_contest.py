import mysql.connector

def add_contest(contest):
	
	mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="DB_for_tppo123",
	database="KTP_Monitor"
	)

	mycursor = mydb.cursor()

	add_contest_query = '''Insert into Contest_Info (contest_name, task_nmb, link_CF, div_id) 
		VALUES ('''  \
		+ '''\''''  + str(contest.name) + '''\', ''' \
		+ '''\''''  + str(len(contest.tasks)) + '''\',''' \
		+ '''\''''  + str(contest.link) + '''\', ''' \
		+ '''\''''  + str(contest.div_id) + '''\'''' \
		+ ''');'''

	print(add_contest_query)
	mycursor.execute(add_contest_query)


	mycursor.execute('SELECT LAST_INSERT_ID()')
	for row in mycursor:
		for cur in row:
			contest_id = cur

	print(contest_id)


	for task in contest.tasks:
		add_task_query = '''Insert into Task_Info (letter, task_name, contest_id) 
			VALUES ('''  \
			+ '''\''''  + str(task.letter) + '''\', ''' \
			+ '''\''''  + str(task.name) + '''\', ''' \
			+ '''\''''  + str(contest_id) + '''\'''' \
			+ ''');'''
		print(add_task_query)
		mycursor.execute(add_task_query)


	print("HERE!!!!")
	print(" ")
	for p_t in contest.pupils_tasks:
		q = "SELECT pupil_id FROM Pupils_Info WHERE pupil_CF = '" + p_t.pupil_CF + "'"

		mycursor.execute(q)

		pup_id = -1

		for row in mycursor:
				pup_id = row[0]

		if (pup_id == -1):
			continue;

		q = "SELECT task_id FROM Task_Info WHERE letter = '" + p_t.task_letter + "' AND contest_id = " + str(contest_id)
		print(q)

		mycursor.execute(q)
		for row in mycursor:
			task_id = row[0]

		q = '''INSERT INTO Pupil_Task (pupil_id, task_id, cnt_send, result) ''' \
		+ ''' VALUES ( \' ''' \
		+ str(pup_id) + '''\', ''' \
		+ '''\'''' + str(task_id) + '''\', ''' \
		+ str(p_t.cnt_try) + ''', ''' \
		+ '''\'''' + str(p_t.result) + '''\'''' \
		+ ''');'''

		print(q)

		mycursor.execute(q)


	mydb.commit()
	mycursor.close()
	mydb.close()

	print("contest added")
	print("tasks added")
	print("pupils and tasks added")
	
	




