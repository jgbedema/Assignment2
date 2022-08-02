from Classes import *
from Database import *
from A5 import *
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
   # cursor.execute("INSERT INTO REGISTER values(?, ?, ?, ?, ?, ?)",(id, name, last_name, email, username, password))    
#register()

#---Login--#
def login(): #setup account
    
   # cursor.execute("""SELECT username from REGISTER WHERE USERNAME= ? AND PASSWORD = ? """, (username, password))
    cursor.execute("""SELECT EMAIL from ADMIN WHERE EMAIL= ? """, [username])
    cursor.execute("""SELECT EMAIL from INSTRUCTOR WHERE EMAIL= ? """, [username])
    cursor.execute("""SELECT EMAIL from STUDENT WHERE EMAIL= ? """, [username])
    
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

#globals
username = input("Enter a username: ")
password = input("Enter a password: ")

