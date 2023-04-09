import mysql.connector

def create_all_tables():

	create_Div_Info =  """
	CREATE TABLE IF NOT EXISTS Div_Info(
	  div_id INT AUTO_INCREMENT PRIMARY KEY,
	  div_name VARCHAR(200) NOT NULL,
	  div_year YEAR NOT NULL 
	) 

	"""

	create_Pupils_Info =  """
	CREATE TABLE IF NOT EXISTS Pupils_Info(
	  	pupil_id INT AUTO_INCREMENT PRIMARY KEY,
	  	
	  	pupil_surname VARCHAR(200) NOT NULL,
	  	pupil_name VARCHAR(200) NOT NULL,
	  	pupil_patronymic VARCHAR(200) NOT NULL,
	  	
	  	pupil_school VARCHAR(100) NOT NULL,
	  	pupil_grade INT NOT NULL,    
		pupil_CF VARCHAR(100) NOT NULL,
		
		birthday DATE NOT NULL,
		div_id INT DEFAULT 1,

		FOREIGN KEY (div_id)  REFERENCES Div_Info(div_id),
	  	CHECK (pupil_grade >= 5 AND pupil_grade <= 11)
	)
	"""

	create_Contest_Info =  """
	CREATE TABLE IF NOT EXISTS Contest_Info(
	  contest_id INT AUTO_INCREMENT PRIMARY KEY,
	  contest_name VARCHAR(200) NOT NULL,
	  task_nmb INT,
	  link_CF VARCHAR(200) NOT NULL,
	  div_id INT NOT NULL,
	  FOREIGN KEY (div_id)  REFERENCES Div_Info(div_id)
	)
	"""

	create_Task_Info =  """
	CREATE TABLE IF NOT EXISTS Task_Info(
	  task_id INT AUTO_INCREMENT PRIMARY KEY,
	  letter CHAR(1) NOT NULL,
	  task_name VARCHAR(200) NOT NULL,
	  contest_id INT NOT NULL,
	  FOREIGN KEY (contest_id)  REFERENCES Contest_Info(contest_id)
	)
	"""

	create_Pupil_Task =  """
	CREATE TABLE IF NOT EXISTS Pupil_Task(
	  pupil_id INT NOT NULL,
	  task_id INT NOT NULL,
	  cnt_send INT,    
	  result VARCHAR(100),
	  PRIMARY KEY(pupil_id, task_id),
	  FOREIGN KEY (pupil_id)  REFERENCES Pupils_Info(pupil_id),
	  FOREIGN KEY (task_id)  REFERENCES Task_Info(task_id)
	)
	"""

	create_Pupil_Contest =  """
	CREATE TABLE IF NOT EXISTS Pupil_Contest(
	  pupil_id INT NOT NULL,
	  contest_id INT NOT NULL,
	  cnt_accept INT,    
	  PRIMARY KEY(pupil_id, contest_id),
	  FOREIGN KEY (pupil_id)  REFERENCES Pupils_Info(pupil_id),
	  FOREIGN KEY (contest_id)  REFERENCES Contest_Info(contest_id)
	)
	"""


	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  password="DB_for_tppo123",
	  database="KTP_Monitor"
	)
	print(mydb)
	
	mycursor = mydb.cursor()

	mycursor.execute("DROP TABLE IF EXISTS Pupil_Div;")
	mycursor.execute("DROP TABLE IF EXISTS Pupil_Contest;")
	mycursor.execute("DROP TABLE IF EXISTS Div_Contest;")
	mycursor.execute("DROP TABLE IF EXISTS Pupil_Task;")
	mycursor.execute("DROP TABLE IF EXISTS Task_Info;")
	mycursor.execute("DROP TABLE IF EXISTS Contest_Info;")
	mycursor.execute("DROP TABLE IF EXISTS Pupils_Info;")
	mycursor.execute("DROP TABLE IF EXISTS Div_Info;")

	mycursor.execute(create_Div_Info)
	mycursor.execute("Insert into Div_Info (div_name, div_year) VALUES ('NULL', 2000)")
	
	mycursor.execute(create_Pupils_Info)
	
	mycursor.execute(create_Contest_Info)
	mycursor.execute(create_Task_Info)

	mycursor.execute(create_Pupil_Task)
	# mycursor.execute(create_Div_Contest)
	mycursor.execute(create_Pupil_Contest)
	# mycursor.execute(create_Pupil_Div)

	mydb.commit()
	mycursor.close()
	mydb.close()

	print("tables created!")



# create_all_tables()
