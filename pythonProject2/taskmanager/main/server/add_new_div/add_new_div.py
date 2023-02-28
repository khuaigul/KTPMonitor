import mysql.connector


def add_new_div(div):
	mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="DB_for_tppo123",
	database="KTP_Monitor"
	)


	add_div_query = '''Insert into Div_Info (div_name, div_year) 
 		VALUES ('''  \
 		+ '''\''''  + str(div.name) + '''\',''' \
 		+ div.year \
 		+ ''');'''
	
	print(add_div_query)

	mycursor = mydb.cursor()
	mycursor.execute(add_div_query)

	mydb.commit()
	mycursor.close()
	mydb.close()

	print("div added")



