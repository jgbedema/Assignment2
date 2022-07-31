import sqlite3
# database file connection 
database = sqlite3.connect("A5.db") #connect to the databse provided by Prof
print ("Opened database successfully")

# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 

#Login (by JG)
#---Registration---#
def register(): #setup account
    id = input("Enter ID: ")
    # a = type(id)
    # print(a)
    name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Enter email: ")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    cursor.execute("INSERT INTO REGISTER values(?, ?, ?, ?, ?, ?)",(id, name, last_name, email, username, password))    
#register()

#---Login--#
def login(): #setup account
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    
    cursor.execute("""SELECT username from REGISTER WHERE USERNAME= ? AND PASSWORD = ? """, (username, password))
    if not cursor.fetchone():  # An empty result evaluates to False.
        print("Login failed")
    else:
        print("Welcome")

        user_type = int(input("Select (1 = Student\t 2 = Instructor\t 3 = Admin): "))
        if(user_type == 1):
            print("Student")
        elif(user_type == 2):
            print("Instructor")
        elif(user_type == 3):
            print("Admin")

login_type = int(input("Select (1 = Register\t 2 = Login): "))
if(login_type == 1):
    register()
elif(login_type == 2):
    login()
 
# SQL command to create LOGIN table in the database 
sql_command = """CREATE TABLE IF NOT EXISTS REGISTER (  
ID TEXT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
SURNAME TEXT NOT NULL,
EMAIL TEXT NOT NULL,
USERNAME TEXT NOT NULL,
PASSWORD TEXT NOT NULL)
;"""

# execute the statement 
cursor.execute(sql_command) 
print ("Table created successfully") 


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