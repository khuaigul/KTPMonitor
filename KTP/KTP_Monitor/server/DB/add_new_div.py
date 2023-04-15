from KTP_Monitor.models import Div_Info
import datetime


def add_new_div(name):
	year = datetime.date.today().year
	D = Div_Info.objects.create(name=name, year = int(year))

	# if (Div_Info.objects.contains(name = name)):
	# 	print("Div added to DB")
	# else:
	# 	print("ERROR! Div can't be add DB")
	print("add_div return")
	



# def add_new_div(div):
# 	mydb = mysql.connector.connect(
# 	host="localhost",
# 	user="root",
# 	password="DB_for_tppo123",
# 	database="KTP_Monitor"
# 	)


# 	add_div_query = '''Insert into Div_Info (div_name, div_year) 
#  		VALUES ('''  \
#  		+ '''\''''  + str(div.name) + '''\',''' \
#  		+ div.year \
#  		+ ''');'''
	
# 	print(add_div_query)

# 	mycursor = mydb.cursor()
# 	mycursor.execute(add_div_query)

# 	mydb.commit()
# 	mycursor.close()
# 	mydb.close()

# 	print("div added")



