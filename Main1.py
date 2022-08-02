from Classes import *



# database file connection 
database = sqlite3.connect("Database.db") #connect to the databse provided by Prof
print ("Opened database successfully")

# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 

default_pw = "default"
bogus_uname = ' '


#functions

#student
def student_login():
    user_type = 1
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



    choice = ''
    while (choice != "E"):    
        #  ----MENU----
        print("\n----------------------MENU--------------------------------- \nA to Add Courses to Schedule\nR to Remove Courses from Schedule\nP to Print Schedule\nE to exit\n")
        choice = input("\nPlease select a choice: ")

        if choice == "A":
            stu.add_course()

        elif choice == "R":
            stu.drop_course()

        elif choice == "P":
            stu.print_sched()
        elif choice.isnumeric():  
            print("Error: Enter a letter from the MENU")

#instructor
def instructor_login():
    user_type = 2
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


    choice = ''
    while (choice != "E"):    
            #  ----MENU----
        print("\n----------------------MENU--------------------------------- \nS to View Schedule\nC to Search Course Roster\nE to exit\n")
        
        choice = input("\nPlease select a choice: ")

        if choice == "S":
            instr.print_sched()
        elif choice == "C":
            instr.print_classlist()
        elif int(choice):  
            print("Error: Enter a letter from the MENU")
        elif choice.isnumeric():  
            print("Error: Enter a letter from the MENU")

#admin
def admin_login():
    user_type = 3
    #grab username and pass
    while bogus_uname:
        username = input("\nPlease enter a username: ")

            #store user information to check in db if user exists
        cursor.execute("""SELECT * FROM STUDENT WHERE EMAIL = ? """, [username])
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

    


    choice = ''
    while (choice != "E"):    
            #  ----MENU----
        print("----------------------MENU--------------------------------- \nA to Add Course to the System\nR to Remove Course From System\nI to Add an Instructor\nS to Add a Student\nU to Remove a User\nE to exit\n")
        
        choice = input("\nPlease select a choice: ")

        if choice == "A":
            adm.add_course()

        elif choice == "R":
            adm.remove_course()
       
        elif choice == "I":
            adm.add_instructor()

        elif choice == "S":
            adm.add_student()   
        
        elif choice == "U":
            adm.remove_user()   
        elif int(choice):  
            print("Error: Enter a letter from the MENU")
        elif choice.isnumeric():  
            print("Error: Enter a letter from the MENU")


# print("Welcome!")
# user_type = input("\nEnter 1 for STUDENT LOGIN\nEnter 2 for INSTRUCTOR LOGIN\nEnter 3 for ADMIN LOGIN\nEnter 4 to Log Out\n")


# if (user_type == 1):
#     student_login()
# elif(user_type == 2):
#     instructor_login(user_type)
# elif (user_type == 3):
#     admin_login(user_type)
# elif (user_type == 4):
#     pass


student_login()
# instructor_login()
# admin_login()



# #grab password and set requirement
# password = input("Please enter a password: ")
# if password != default_pw:
#     print("Incorrect password")
# else:
#     print("Successful Login")
#     print("\n")
#     #call student function
#     # student_login()
#     # instructor_login()
#     # admin_login()








# user = USER(name, surname, id)
# admin = ADMIN()
# instr = INSTRUCTOR(name, surname, id)
# stu = STUDENT(name, surname, id)


# If we skip this, nothing will be saved in the database. 
database.commit() 