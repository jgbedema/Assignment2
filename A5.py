import sqlite3
# database file connection 
database = sqlite3.connect("A5.db") #connect to the databse provided by Prof
print ("Opened database successfully")

# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 

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
sql_command = """INSERT OR IGNORE INTO COURSE VALUES(600, 'Calculus II', 'MATH', '2PM - 3:20 PM', 'TR', 'FALL', 2022, 4);"""
cursor.execute(sql_command) 

sql_command = """INSERT OR IGNORE INTO COURSE VALUES(700, 'APC', 'MATH', '2PM - 3:20 PM', 'TR', 'FALL', 2022, 4);"""
cursor.execute(sql_command) 

sql_command = """INSERT OR IGNORE INTO COURSE VALUES(800, 'Matlab', 'MATH', '2PM - 3:20 PM', 'TR', 'FALL', 2022, 4);"""
cursor.execute(sql_command) 

sql_command = """INSERT OR IGNORE INTO COURSE VALUES(900, 'Calculus II', 'MATH', '2PM - 3:20 PM', 'TR', 'FALL', 2022, 4);"""
cursor.execute(sql_command) 

sql_command = """INSERT OR IGNORE INTO COURSE VALUES(1000, 'Calculus II', 'MATH', '2PM - 3:20 PM', 'TR', 'FALL', 2022, 4);"""
cursor.execute(sql_command) 

sql_command = """INSERT OR IGNORE INTO COURSE VALUES(1100, 'Calculus II', 'MATH', '2PM - 3:20 PM', 'TR', 'FALL', 2022, 4);"""
cursor.execute(sql_command) 

sql_command = """INSERT OR IGNORE INTO COURSE VALUES(1200, 'Calculus II', 'MATH', '2PM - 3:20 PM', 'TR', 'FALL', 2022, 4);"""
cursor.execute(sql_command) 

sql_command = """INSERT OR IGNORE INTO COURSE VALUES(1300, 'Calculus II', 'MATH', '2PM - 3:20 PM', 'TR', 'FALL', 2022, 4);"""
cursor.execute(sql_command) 

sql_command = """INSERT OR IGNORE INTO COURSE VALUES(1400, 'Calculus II', 'MATH', '2PM - 3:20 PM', 'TR', 'FALL', 2022, 4);"""
cursor.execute(sql_command) 

sql_command = """INSERT OR IGNORE INTO COURSE VALUES(1500, 'Calculus II', 'MATH', '2PM - 3:20 PM', 'TR', 'FALL', 2022, 4);"""
cursor.execute(sql_command) 

sql_command = """DELETE FROM STUDENT WHERE ID = 47;"""
cursor.execute(sql_command) 


# print("-----MENU----- \nS to search\nI to insert\nP to print all\nC to create table\nU to update\nR to remove\nE to exit\n")

# choice = ''
# while (choice != "E"):
#     choice = input("\nPlease select a choice: ")

#     if choice == "S":
#         search()

#     elif choice == "I":
#         insert()

#     elif choice == "P":
#         print_all()

#     elif choice == "U":
#         update()

#     elif choice == "R":
#         remove()


# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
database.commit() 
  
# close the connection 
database.close() 