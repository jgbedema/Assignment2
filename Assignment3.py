from re import I
import sqlite3
from venv import create

# database file connection 
database = sqlite3.connect("assignment3.db") #connect to the databse provided by Prof
#database = sqlite3.connect("A3.db")
print ("Opened database successfully")


# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 


 #----MENU----
#create functions
def search():
    srch = input("What do you want to search for?")
    # #QUERY FOR ALL
    # print("Entire table")
    # cursor.execute("""SELECT * FROM PROGRAMMER""")
    # query_result = cursor.fetchall()

    # for i in query_result:
    #     print(i)

def insert():
    Table_name = input("Which table do you want to insert to?")
    # uid = "6"
    # fname = input("First name of a famous programmer: ")
    # lname = input("Last name of the same programmer: ")
    # birthyear = input("Birth year of the same programmer: ") 

    # cursor.execute("""INSERT INTO PROGRAMMER VALUES('%s', '%s', '%s', '%s');""" % (uid, fname, lname, birthyear))

def print_all():
    # QUERY FOR ALL
    print("Entire table")
    cursor.execute("""SELECT NAME FROM sqlite_master WHERE type = 'table' """)
    query_result = cursor.fetchall()
    
    for i in query_result:
        print(i)


def create_table():
    print("What is the name of the table you want to create?")

def update():
    print("What would you like to update?")

def remove():
    print("What would you like to remove?")


print("-----MENU----- \nS to search\nI to insert\nP to print all\nC to create table\nU to update\nR to remove\nE to exit\n")

choice = ''
while (choice != "E"):
    choice = input("\nPlease select a choice: ")

    if choice == "S":
        search()

    elif choice == "I":
        insert()

    elif choice == "P":
        print_all()

    elif choice == "U":
        update()

    elif choice == "R":
        remove()


# SQL command to create a table in the database 
    #----create Course table---
sql_command = """CREATE TABLE IF NOT EXISTS COURSE ( 
CRN INTEGER PRIMARY KEY NOT NULL,
TITLE TEXT NOT NULL,
DEPT TEXT NOT NULL,
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
    #---insert course one---
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(100, 'OOP', 'BSCO', '10AM - 11:50 AM', 'M W F', 'SUMMER', 2021, 4);"""
cursor.execute(sql_command) 
    #---insert course 2---
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(200, 'Analog Circuits', 'BSEE', '10AM - 11:50 AM', 'M W F', 'SUMMER', 2021, 4);"""
cursor.execute(sql_command) 
    #---insert course 3---
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(300, 'Modern History', 'HUSS', '3:30PM - 4:50 PM', 'T R', 'SUMMER', 2021, 3);"""
cursor.execute(sql_command) 
    #---insert course 4---
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(400, 'Network Theory 2', 'BSEE', '8AM - 10:50 AM', 'M W F', 'SUMMER', 2021, 4);"""
cursor.execute(sql_command) 
    #---insert course 5---
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(500, 'Calculus', 'MATH', '9AM - 10:20 AM', 'M W', 'SUMMER', 2021, 4);"""
cursor.execute(sql_command) 

# QUERY FOR ALL
print("Entire Courses table")
cursor.execute("""SELECT * FROM COURSE""")
query_result = cursor.fetchall()


# QUERY FOR SOME
        #--query for 4 cred courses---
print("\n4 credits courses:")
cursor.execute("""SELECT * FROM COURSE WHERE CREDITS = 4""")
query_result = cursor.fetchall()

for i in query_result:
	print(i)


        #--query for eng dept courses---
print("\nENG DEPT courses:")
cursor.execute("""SELECT * FROM COURSE WHERE DEPT = 'BSEE' OR 'BSCO' """) #not displaying when I try to select BSEE and BSCO
query_result = cursor.fetchall()

for i in query_result:
	print(i)


        #--query for summer courses---
print("\nSummer semester courses:")
cursor.execute("""SELECT * FROM COURSE WHERE SEMESTER = 'SUMMER'""")
query_result = cursor.fetchall()

for i in query_result:
	print(i)


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
print("\nProfessors who teach courses in their department(s):")
cursor.execute(""" SELECT NAME, SURNAME, COURSE.DEPT, COURSE.TITLE FROM INSTRUCTOR INNER JOIN COURSE ON INSTRUCTOR.DEPT = COURSE.DEPT """)
query_result = cursor.fetchall()

for i in query_result:
	print(i)
    #print("The instructor who teaches %s course is: %s %s ", i, INSTRUCTOR.NAME, INSTRUCTOR.SURNAME)
    
    
# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
database.commit() 
  
# close the connection 
database.close() 