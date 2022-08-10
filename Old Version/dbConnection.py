from secrets import choice
import sqlite3
from traceback import print_tb

# database file connection 
database = sqlite3.connect("assignment5.db") 
  
# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 

def searchStudentByName(studentName):
    cursor.execute("""SELECT * FROM STUDENT WHERE STUDENT.NAME='%s';""" % (studentName))
    query_result = cursor.fetchall()
    for i in query_result:
	    print(i)

def add2NewStudentToDB():
	#SQL command to add students to database
	sql_command="""INSERT OR IGNORE INTO STUDENT VALUES(10011, 'Abdul', 
	'Ibrahim','2023', 'BSCO','ibrahima1');"""
	cursor.execute(sql_command) 

	sql_command="""INSERT OR IGNORE INTO STUDENT VALUES(10012, 'Abdiel', 
	'Danastor','2022', 'BSCO','danastora');"""
	cursor.execute(sql_command) 

def remove1InstrutorInTable():
	#SQL command to remove 1 instructor ID=20005
	sql_command="""DELETE FROM INSTRUCTOR WHERE ID=20005;"""
	cursor.execute(sql_command)

def updateAdminVeraTitle():
	#SQL command to update 1 administrator
	sql_command="""UPDATE ADMIN SET TITLE='Vice-President' WHERE ID=30002;"""
	cursor.execute(sql_command)


def createTableOf5CoursesInDB():  
	#SQL command to create a table of courses in the database 
	sql_command = """CREATE TABLE IF NOT EXISTS COURSE (  
	CRN INTEGER PRIMARY KEY NOT NULL,
	TITLE TEXT NOT NULL,
	DEPARTMENT TEXT NOT NULL,
	TIME TEXT NOT NULL,
	DAY TEXT NOT NULL,
	SEMESTER TEXT NOT NULL,
	YEAR INTEGER NOT NULL,
	CREDITS INTEGER NOT NULL)
	;"""
  
	# execute the statement 
	cursor.execute(sql_command) 
  
	# SQL command to insert the data in the COURSE table, must be done one at a time 
	sql_command = """INSERT OR IGNORE INTO COURSE VALUES(3225, 'APPLIED PROGRAMMING CONCEPTS', 
	'BSEE','8:00 am - 9:50 am', 'TR', 'SUMMER', 2022, 4 );"""
	cursor.execute(sql_command) 

	sql_command = """INSERT OR IGNORE INTO COURSE VALUES(3550, 'COMPUTER NETWORKS FOR ENGINEERS', 
	'BSCO','8:00 am - 9:20 am', 'WF', 'SUMMER', 2022, 4 );"""
	cursor.execute(sql_command) 

	sql_command = """INSERT OR IGNORE INTO COURSE VALUES(3200, 'SIGNALS AND SYSTEM', 
	'BSEE','10:00 am - 11:50 am', 'TR', 'SUMMER', 2022, 4 );"""
	cursor.execute(sql_command)  
               
	sql_command = """INSERT OR IGNORE INTO COURSE VALUES(4552, 'INDUSTRIAL ORGANIZATION PSYCHOLOGY', 
	'HUSS','5:00 pm - 6:50 pm', 'MW', 'SPRING', 2022, 4 );"""
	cursor.execute(sql_command) 

	sql_command = """INSERT OR IGNORE INTO COURSE VALUES(3150, 'OBJECT ORIENTED PROGRAMMING', 
	'BSCO','11:00 am - 12:20 pm', 'TR', 'FALL', 2021, 4);"""
	cursor.execute(sql_command) 

	sql_command = """INSERT OR IGNORE INTO COURSE VALUES(2200, 'ENGLISH II', 
	'ENGL','8:00 am - 09:50 am', 'TR', 'FALL', 2022, 4);"""
	cursor.execute(sql_command) 

def InsertIntoTable(tableName):
    pass

def printEntireTable(tableName):
    print(f"Printing {tableName} table")
    cursor.execute("""SELECT * FROM UPPER(%s)""" % (tableName))
    query_result = cursor.fetchall()
  
    for i in query_result:
	    print(i)
    


def courseInstructorMatch():
	#Querry to look for match for each course
	sql_command="""SELECT COURSE.TITLE, INSTRUCTOR.NAME
	FROM COURSE, INSTRUCTOR
	WHERE INSTRUCTOR.DEPT = COURSE.DEPARTMENT """
	cursor.execute(sql_command)
	query_result = cursor.fetchall()

	for i in query_result:
		print(i)


def createLogins():
    cursor.execute("""CREATE TABLE IF NOT EXISTS ADMIN_LOGINS(USERNAME TEXT, PASSWORD TEXT DEFAULT "pass123", TYPE INTERGER DEFAULT 1)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS INSTRUCTOR_LOGINS(USERNAME TEXT, PASSWORD TEXT DEFAULT "pass1234", TYPE INTERGER DEFAULT 2)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS STUDENT_LOGINS(USERNAME TEXT, PASSWORD TEXT DEFAULT "pass1235", TYPE INTERGER DEFAULT 3)""")
    cursor.execute("""INSERT OR IGNORE INTO ADMIN_LOGINS (USERNAME) SELECT EMAIL FROM ADMIN""")
    cursor.execute("""INSERT OR IGNORE INTO INSTRUCTOR_LOGINS (USERNAME) SELECT EMAIL FROM INSTRUCTOR""")
    cursor.execute("""INSERT OR IGNORE INTO STUDENT_LOGINS (USERNAME) SELECT EMAIL FROM STUDENT""")



           

# To save the changes in the files. 

database.commit()  
#close the connection 
#database.close()