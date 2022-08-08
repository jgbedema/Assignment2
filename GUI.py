from Classes import *
from Global_Lists import *
from guizero import App, Text, TextBox, Slider, PushButton

# database file connection 
database = sqlite3.connect("Database.db") #connect to the databse provided by Prof
#print ("Opened database successfully")

# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 

default_pw = "default"
bogus_uname = ' ' #make an empty string to run while loop

                                    #functions
#student
def student_login():
    #grab username and pass
    while bogus_uname:
        username = input("\nPlease enter a username: ")

            #store user information to check in db if user exists
        cursor.execute("""SELECT * FROM STUDENT WHERE EMAIL = ? """, [username])
        student_result = cursor.fetchall()
        if (len(student_result) == 0) or (username == bogus_uname):
            print('Username does not exist')
        
        else:
            #grab password and set requirement
            while default_pw:
                password = input("Please enter a password: ")
                if password != default_pw:
                    print("Incorrect password")
                else:
                    print("Successful Login")
                    print("\n")
                    break
                
            break
 
    
        #student details
    for i in student_result:
        print(i)
        stu_fname = i[1]
        stu_lname = i[2]
        stu_id = i[0]
        stu_uname = i[5]


    # print(student_result)

    stu = STUDENT(stu_fname, stu_lname, stu_id)
    print(stu.first)

    # # stu.add_course()
    # # stu.print_sched()
    # # stu.drop_course()
    # # stu.print_sched()

    # stu.List_course()

    choice = ''
    while (choice != "L"):    
        #  ----MENU----
        print("\n----------------------MENU--------------------------------- \nA to Add Courses to Schedule\nB to Remove Courses from Schedule\nC to Print Schedule\nD to View Courses\nE To Search For a Course\nL to Logout\n")
        choice = input("\nPlease select a choice: ")

        if choice == "A":
            stu.List_course() #display list of courses
            stu.add_course() 

        elif choice == "B":
            stu.print_sched()
            stu.drop_course()
            stu.print_sched()

        elif choice == "C":
            stu.print_sched()

        elif choice == "D":
            stu.List_course()

        elif choice == "E":
            stu.Search_course_by_input()

        elif choice.isnumeric():  
            print("Error: Enter a letter from the MENU")

#instructor
def instructor_login():
        #grab username and pass
    while bogus_uname:
            #grab username
        username = input("\nPlease enter a username: ")

            #store user information to check in db if user exists
        cursor.execute("""SELECT * FROM INSTRUCTOR WHERE EMAIL = ? """, [username])
        inst_result = cursor.fetchall()
        if (len(inst_result) == 0) or (username == bogus_uname):
            print('Username does not exist')
        
        else:
            #grab password and set requirement
            while default_pw:
                password = input("Please enter a password: ")
                if password != default_pw:
                    print("Incorrect password")
                else:
                    print("Successful Login")
                    print("\n")
                    break
                
            break
      
      
           #student details
    for i in inst_result:
        print(i)
        instr_fname = i[1]
        instr_lname = i[2]
        instr_id = i[0]
        instr__uname = i[6]


    # print(inst_result)

    instr = INSTRUCTOR(instr_fname, instr_lname, instr_id)
    print(instr.first)

    # instr.add_course()
    # stu.print_sched()
    # stu.drop_course()
    # stu.print_sched()

    # instr.List_course() #print courses

    choice = ''
    while (choice != "L"):    
            #  ----MENU----
        print("\n----------------------MENU--------------------------------- \nA to View Schedule\nB to View Course Roster\nC to List All Courses\nD To Search For a Course\nL to Logout\n")
        
        choice = input("\nPlease select a choice: ")

        if choice == "A":
            instr.print_sched()

        elif choice == "B":
            instr.print_classlist()
            
        elif choice == "C":
            instr.List_course() #print courses
        
        elif choice == "D":
            instr.Search_course_by_input()

        elif choice.isnumeric():  
            print("Error: Enter a letter from the MENU")

#admin
def admin_login():
    #grab username and pass
    while bogus_uname:
        username = input("\nPlease enter a username: ")

            #store user information to check in db if user exists
        cursor.execute("""SELECT * FROM ADMIN WHERE EMAIL = ? """, [username])
        adm_result = cursor.fetchall()
        if (len(adm_result) == 0) or (username == bogus_uname):
            print('Username does not exist')
        
        else:
            #grab password and set requirement
            while default_pw:
                password = input("Please enter a password: ")
                if password != default_pw:
                    print("Incorrect password")
                else:
                    print("Successful Login")
                    print("\n")
                    break
                
            break
        
    

        #student details
    for i in adm_result:
        print(i)
        adm_fname = i[1]
        adm_lname = i[2]
        adm_id = i[0]
        adm_uname = i[5]

    adm = ADMIN(adm_fname, adm_lname, adm_id)
    print(adm.first)

    # adm.add_course()
    # adm.remove_course()

    
    # adm.List_course()

    choice = ''
    while (choice != "L"):    
            #  ----MENU----
        print("----------------------MENU--------------------------------- \nA to Add Course to the System\nB to Remove Course From System\nC to Add an Instructor\nD to Add a Student\nE to Remove a User\nF to List All Courses\nG To Search For a Course\nL to Logout\n")
        
        choice = input("\nPlease select a choice: ")

        if choice == "A":
            adm.List_course() 
            print("\n")
            adm.add_course()
            print("\n")
            adm.List_course() 


        elif choice == "B":
            adm.List_course() 
            adm.remove_course()
            print("\n")
            adm.List_course()
       
        elif choice == "C":
            adm.add_instructor()

        elif choice == "D":
            adm.add_student()   
        
        elif choice == "E":
            adm.remove_user()   

        elif choice == "F":
            adm.List_course()
            print("\n") 
            
        elif choice == "G":
            adm.Search_course_by_input()

        elif choice.isnumeric():  
            print("Error: Enter a letter from the MENU")



# student_login()
# instructor_login()
# admin_login()


#####GUI 


def cb_Login():
        #store user information to check in db if user exists
    cursor.execute("""SELECT * FROM STUDENT WHERE EMAIL = ? """, [username.value])
    student_result = cursor.fetchall()

    cursor.execute("""SELECT * FROM ADMIN WHERE EMAIL = ? """, [username.value])
    admin_result = cursor.fetchall()

    cursor.execute("""SELECT * FROM INSTRUCTOR WHERE EMAIL = ? """, [username.value])
    instr_result = cursor.fetchall()

    for i in student_result or admin_result or instr_result:
        if (len(username.value) == 0) or (password.value == bogus):
            print('Username does not exist')
        
        else:
            if password != default_pw:
                print("Incorrect password")
            else:
                student_login()

app = App(title = "REGISTRATION SYSTEM", layout = "grid")

welcome = Text(app, text = "WELCOME TO THE COURSE REGISTRATION SYSTEM!", grid = [2,2])

login_email = Text(app, text = "Username: ", size=12, font="Times New Roman", color = "black", grid=[0,0])
username = TextBox(app, text = " ", width = 25, grid=[1,0])#, command=change_message)
login_password = Text(app, text = "Password", size=12, font="Times New Roman", color = "black", grid=[0,1])
password = TextBox(app, text = " ", width = 25, grid=[1,1])#, command=change_message)

Login = PushButton(app, command = cb_Login,  text = "Login")




app.display()






# If we skip this, nothing will be saved in the database. 
database.commit() 


# close the connection 
database.close() 