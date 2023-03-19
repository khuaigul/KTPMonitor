import mysql.connector


def get_status_on_pupils_contests(pupils, contests):
	
	mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="DB_for_tppo123",
	database="KTP_Monitor"
	)

	mycursor = mydb.cursor()

	d = {}

	for pup_id in pupils:
		for con_id in contests:
			pup_div_q = "SELECT div_id FROM Pupils_Info WHERE pupil_id = " + str(pup_id)
			print(pup_div_q)
			mycursor.execute(pup_div_q)

			for row in mycursor:
				for cur in row:
					pup_div = cur

			con_div_q = "SELECT div_id FROM Contest_Info WHERE contest_id = " + str(con_id)
			print(con_div_q)
			mycursor.execute(con_div_q)

			for row in mycursor:
				for cur in row:
					con_div = cur

			if (pup_div != con_div):
				d[(pup_id, con_id)] = '-'
				continue;

			cnt_acc_q = ''' SELECT count(*) FROM Task_Info ti CROSS JOIN Pupil_Task pt ON ti.task_id = pt.task_id '''\
			+ ''' WHERE ti.contest_id = ''' + str(con_id) \
			+ ''' AND pt.pupil_id = ''' + str(pup_id) \
			+ ''' AND pt.result = '+'; '''

			print(cnt_acc_q)

			mycursor.execute(cnt_acc_q)

			for row in mycursor:
				for cur in row:
					cnt_acc = cur

			cnt_task_q = "SELECT task_nmb FROM Contest_Info WHERE contest_id = " + str(con_id)
			mycursor.execute(cnt_task_q)

			for row in mycursor:
				for cur in row:
					cnt_task = cur

			res = str(cnt_acc) + '/' + str(cnt_task)

			d[(pup_id, con_id)] = res




	mydb.commit()
	mycursor.close()
	mydb.close()


	print("status done")

	return d



