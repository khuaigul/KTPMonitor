import mysql.connector

def change_pupil_div(p_div):
	
	mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="DB_for_tppo123",
	database="KTP_Monitor"
	)

	mycursor = mydb.cursor()

# 	UPDATE Customers
# SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
# WHERE CustomerID = 1;

	ch_pupil_div_query = '''UPDATE Pupils_Info SET div_id = '''  \
 		+ str(p_div.div_id) \
 		+ ''' WHERE pupil_id = '''  + str(p_div.pupil_id)  \
 		+ ''';'''

	print(ch_pupil_div_query)
	mycursor.execute(ch_pupil_div_query)

	mydb.commit()
	mycursor.close()
	mydb.close()

	print("pupil div changed")




