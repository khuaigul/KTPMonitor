import mysql.connector

def delete_div(div_id):
	
	mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="DB_for_tppo123",
	database="KTP_Monitor"
	)

	mycursor = mydb.cursor()

	ch_div_query = '''UPDATE Pupils_Info SET div_id = '''  \
 		+ str(1) \
 		+ ''' WHERE div_id = '''  + str(div_id)  \
 		+ ''';'''

	del_div_query = '''DELETE FROM Div_Info '''  \
		+ ''' WHERE div_id = '''  + str(div_id)  \
		+ ''';'''
 	

	print(ch_div_query)
	print(del_div_query)
	
	mycursor.execute(ch_div_query)
	mycursor.execute(del_div_query)
	

	mydb.commit()
	mycursor.close()
	mydb.close()

	print("div deleted")




