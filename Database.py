from re import I
import sqlite3
from venv import create

# database file connection 
database = sqlite3.connect("Database.db") #connect to the databse provided by Prof
print ("Opened database successfully")

# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 

# SQL command to create a table in the database 
    #----create Course table---
sql_command = """CREATE TABLE IF NOT EXISTS COURSE ( 
CRN INTEGER PRIMARY KEY NOT NULL,
TITLE TEXT NOT NULL,
DEPT TEXT NOT NULL,
INSTRUCTOR TEXT NOT NULL,
TIME TEXT NOT NULL,
DAY TEXT NOT NULL,
SEMESTER TEXT NOT NULL,
YEAR TEXT NOT NULL,
CREDITS INTEGER NOT NULL)
;"""

# execute the statement 
cursor.execute(sql_command) 
print ("Table created successfully") 

# SQL command to insert the data in the table, must be done one at a time 

# QUERY FOR ALL
#print("Entire Courses table")
cursor.execute("""SELECT * FROM COURSE""")
query_result = cursor.fetchall()


# QUERY FOR SOME
        #--query for 4 cred courses---
#print("\n4 credits courses:")
cursor.execute("""SELECT * FROM COURSE WHERE CREDITS = 4""")
query_result = cursor.fetchall()

# for i in query_result:
# 	print(i)


        #--query for eng dept courses---
#print("\nENG DEPT courses:")
cursor.execute("""SELECT * FROM COURSE WHERE DEPT = 'BSEE' OR 'BSCO' """) #not displaying when I try to select BSEE and BSCO
query_result = cursor.fetchall()

# for i in query_result:
# 	print(i)


        #--query for summer courses---
#print("\nSummer semester courses:")
cursor.execute("""SELECT * FROM COURSE WHERE SEMESTER = 'SUMMER'""")
query_result = cursor.fetchall()

# for i in query_result:
# 	print(i)


    #---insert STUDENT 11---
sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(0038, 'Joseph', 'Gbedema', 2022, 'BSCO', 'gbedemaj@wit.edu');"""
cursor.execute(sql_command) 
    #---insert STUDENT 12---
sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(0047, 'John', 'Doe', 2090, 'BSEE', 'doej@wit.edu');"""
cursor.execute(sql_command) 

    #---remove an instr (Dan Bern)---
sql_command = """DELETE FROM INSTRUCTOR WHERE ID = 20006 """ 
cursor.execute(sql_command) 

    #---update an admin's title (Vera Rubin)---
sql_command = """UPDATE ADMIN SET TITLE = 'Vice President' WHERE TITLE = 'Registrar' """ 
cursor.execute(sql_command) 


        #--query for course dept to match instr dept ---
#print("\nProfessors who teach courses in their department(s):")
cursor.execute(""" SELECT NAME, SURNAME, COURSE.DEPT, COURSE.TITLE FROM INSTRUCTOR INNER JOIN COURSE ON INSTRUCTOR.DEPT = COURSE.DEPT """)
query_result = cursor.fetchall()

# for i in query_result:
# 	print(i)
#     #print("The instructor who teaches %s course is: %s %s ", i, INSTRUCTOR.NAME, INSTRUCTOR.SURNAME)


  #--- Insert STUDENTS--#
sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10011, 'Joseph', 'Gbedema', 2022, 'BSCO', 'gbedemaj');"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10012, 'Abdul', 'Ibrahim', 2022, 'BSCO', 'ibrahimi');"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10013, 'Abdeil', 'Danastor', 2022, 'BSCO', 'danastora');"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10014, 'Jonathan', 'Kerr', 2005, 'BSARCH', 'kerrj');"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10015, 'Ahmed', 'Demin', 1903, 'BMED', 'demina');"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10016, 'Jack', 'Frost', 1900, 'BSARCH', 'frostj');"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10017, 'Sarah', 'Pearl', 1956, 'BSCO', 'sarahp');"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10018, 'Mary', 'Magdon', 1987, 'BSARCH', 'magdonm');"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10019, 'Elizabeth', 'Earl', 2050, 'BSCO', 'earle');"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10020, 'James', 'Cranford', 1967, 'BMED', 'cranfordj');"""
cursor.execute(sql_command) 

sql_command = """DELETE FROM STUDENT WHERE ID = 38;"""
cursor.execute(sql_command) 

  #--- Insert INSTRUCTORS--#
sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20006, 'Ryan', 'Beto', 'Full Prof.', '2005', 'BSARCH', 'betor');"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20007, 'Anthony', 'Smart', 'Assistant  Prof.', '2006', 'BSEE', 'smarta');"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20008, 'Jordan', 'David', 'Full Prof.', '2007', 'HUSS', 'davidj');"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20009, 'Jackson', 'Cartes', 'Assistant  Prof.', '2008', 'HUSS', 'cartesj');"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20010, 'Benjamin', 'Najj', 'Full Prof.', '2009', 'BSCO', 'najjb');"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20011, 'Katherine', 'Kelsey', 'Assistant  Prof.', '2010', 'BMED', 'kelseyk');"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20012, 'Lily', 'Apple', 'Full Prof.', '2011', 'BMED', 'applel');"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20013, 'Henry', 'Bess', 'Assistant  Prof.', '2012', 'BCOS', 'bessh');"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20014, 'Skyler', 'Fast', 'Full Prof.', '2013', 'BSCO', 'fasts');"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20015, 'Paige', 'Test', 'Assistant  Prof.', '2014', 'BSARCH', 'testp');"""
cursor.execute(sql_command) 

  #--- Insert COURSES--#
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(100, 'OOP', 'BSCO', 'Alan Turing', '10AM - 11:50 AM', 'M W F', 'SUMMER', 2021, 4);"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(200, 'Analog Circuits', 'BSEE', 'Anthony Smart', '10AM - 11:50 AM', 'M W F', 'SUMMER', 2021, 4);"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(300, 'Modern History', 'HUSS', 'Jackson Cartes', '3:30PM - 4:50 PM', 'T R', 'SUMMER', 2021, 3);"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(400, 'Network Theory 2', 'BSEE', 'Anthony Smart', '8AM - 10:50 AM', 'M W F', 'SUMMER', 2021, 4);"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(500, 'Calculus', 'MATH', 'Henry Bess', '9AM - 10:20 AM', 'M W', 'SUMMER', 2021, 4);"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(600, 'Calculus II', 'MATH', 'Henry Bess', '10:30 AM - 11:50 AM', 'M W', 'SUMMER', 2021, 4);"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(700, 'Diff E', 'MATH', 'Henry Bess', '3:00 PM - 4:50 PM', 'T R', 'FALL', 2020, 4);"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(800, 'Discrete Math', 'MATH', 'Henry Bess', '11AM - 12:20 PM', 'M W F', 'SPRING', 2023, 4);"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(900, 'Digital Logic', 'BSCO', 'Skyler Fast', '9AM - 10:20 AM', 'W F', 'FALL', 2021, 4);"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(1000, 'Computer Arch', 'BSCO', 'Skyler Fast', '9AM - 10:20 AM', 'M W', 'SUMMER', 2019, 4);"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(1100, 'Sociolgy', 'HUSS', 'Henry Bess', '9AM - 10:20 AM', 'T R F', 'SUMMER', 2018, 3);"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(1200, 'Hardware Security LAB', 'BSCO', 'Skyler Fast', '2 PM - 5 PM', 'M W', 'SUMMER', 2018, 4);"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(1300, 'Motors & Controls LAB ', 'BSEE', 'Henry Bess', '2 PM - 5 PM', 'T R', 'SPRING', 2023, 4);"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(1400, 'MEDICALS', 'BMED', 'Henry Bess', '11 AM - 12:20 PM', 'T R F', 'SUMMER', 2021, 4);"""
cursor.execute(sql_command) 
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(1500, 'Solid State', 'BSEE', 'Jordan David', '9AM - 10:20 AM', 'M W', 'SUMMER', 2019, 4);"""
cursor.execute(sql_command) 


cursor.execute(sql_command) 
sql_command = """DELETE FROM STUDENT WHERE ID = 47;"""
cursor.execute(sql_command) 
    
# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
database.commit() 
  
# close the connection 
database.close() 