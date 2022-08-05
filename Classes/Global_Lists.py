from Database import *
from A5 import *

# database file connection 
database = sqlite3.connect("Database.db") #connect to the databse provided by Prof
#print ("Opened database successfully")

# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 

#create a global list for registered classes
bogus = ' '

#Base class
class USER:
    #attributes
    def __init__(self, first, last, ID):
        self.first = first
        self.last = last
        self.ID = ID
        # self.reg_class = [] #list to hold registered courses
        # self.rep_courses = [] #create an empty list to check repeated courses
        # self.reg_id = [] #create an empty list to chold student id for registered course

        
    
    global reg_class, rep_courses, reg_stu_id, reg_prof_name
    reg_class = [] #list to hold registered courses
    # rep_courses = [] #create an empty list to check repeated courses
    reg_stu_id = [] #list to hold student's id's for registered courses
    reg_prof_name = [] #list to hold prof names for registered courses

    def Search_course_by_input(self):
        print("\n|Search For Course By CRN Or Title|")
        print("-----------------------------------")
        
        while bogus:
            choice = input("\nSelect 1 for CRN or 2 for Title: \n")
            if choice == "1":
                crn = input("Enter Course CRN: ")
                if crn.isalpha():
                    print("Incorrect CRN")
                else:
                    print("\nSearching CRN: " + crn)
                    cursor.execute("""SELECT * FROM COURSE WHERE CRN = ?;""", [crn] )
                    query_result = cursor.fetchall()
                
                    for i in query_result:
                        if i in query_result:
                            print("Course Details: \n" + str(i) + "\n")
                        else:
                            print("No Such Course")
                break
            
            elif choice == "2":
                title = input("\nEnter Course Title: \n")
                if title.isnumeric():
                    print("Incorrect Title")
                else:
                    print("\nSearching Title: " + title)
                    cursor.execute("""SELECT * FROM COURSE WHERE TITLE = ?;""", [title] )
                    query_result = cursor.fetchall()

                    for title in query_result:
                        if title in query_result:
                            print("Course Details: \n" + str(title) + "\n")
                        else:
                            print("No Such Course")
                break
            elif not "1" or "2" or choice.isnumeric():
                print("Error: Enter 1 for CRN or 2 for Title")
            
    
    def List_course(self):
        print("\n|COURSES|")
        print("---------")
        cursor.execute("""SELECT * FROM COURSE""")
        course_list = cursor.fetchall()
        # print(course_list)

        print("\t\t\t\t\tCOURSE")
        print("-------------------------------------------------------------------------------------------------")
        for i in course_list:
            print(i)
        print("-------------------------------------------------------------------------------------------------")



user = USER("Joseph", "Gbedema", "10011")
#print("User first name is: ", user.first)
# user.Search_course_by_input()
# user.List_course()


#----Derived Class(es)---#

#Student
class STUDENT(USER):
    def __init__(self, first, last, ID):
        super(STUDENT, self).__init__(first, last, ID) #inherit USER's attributes

    #functions
    def add_course(self): 
        print("\n|ADD COURSE|")
        print("------------")
        crn = input("\nEnter Course CRN: ")
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = ?;""", [crn] )
        course_results = cursor.fetchall()
        while bogus:
            if (len(course_results) == 0) or (crn == bogus):
                print("Error: Course " + crn + " does not exist")
                # crn = input("\nEnter Course CRN: ")
            
            else:
                print("\nCourse Information")
                for i in course_results:
                    print(str(i))
                    # reg_class.append(i) 
                    if i not in reg_class:
                        reg_class.append(i) #save class info in list
                        reg_class.sort() #sort the list for display later
                        reg_stu_id.append(self.ID) #grab the user ID
                        reg_prof_name.append(i[3])
                        reg_prof_name.sort()
                    else:
                        print("You have already registered for this course" )
                print("\nRegistered Courses: ")
                print("CRN \t TITLE")
                for j in reg_class:
                    print(str(j[0]) + "\t " + str(j[1]))
                break
            break

    
    def drop_course(self):
        print("\n|REMOVE COURSE|")
        print("---------------")
        crn = input("\nEnter Course CRN: ")
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = ?;""", [crn] )
        drop_results = cursor.fetchall()
        for i in drop_results:
            if (len(reg_class) == 0) or (crn == bogus):
                print("No Such Course Registered\n")
                
            else:
                # print(drop_results)
                if i in reg_class:
                    # print("Course class ID" + str(reg_stu_id))
                    print("Course reg info" + str(reg_class))
                    # print("Course reg prof info" + str(reg_prof_name))
                    print("Course " + str(i[1]) + " " + str(i[2]) + " has been removed")
                    reg_class.remove(i)
                    reg_prof_name.remove(i[3]) #remove the prof name
                    reg_stu_id.remove(self.ID)#remove the student's id
                    print()
                else:
                    print("No Such Course Registered\n")
        
    # print(reg_class)
    # print(rep_courses)

    def print_sched(self):
        print("\n|REGISTERED COURSES|")
        print("--------------------")
        print("CRN \t TITLE")
        for j in reg_class:
            print(j)

# student = STUDENT("Joe", "Gbe", "10011")
# print("Student first name is: ", student.first)
# student.print_sched()
# student.add_course()
# student.print_sched()
# student.drop_course()
# student.print_sched()

# #test to see what is in the registered course array
# for j in reg_class:
#     print("Stuff inside the registered course list: " + str(j))
# for j in rep_courses:
#     print("Stuff inside the repeated course list: " + str(j))
# for j in class_id:
#     print("IDs inside the registered list: " + str(j))




#Instructor
class INSTRUCTOR(USER):
    def __init__(self, first, last, ID):
        super().__init__(first, last, ID) #inherit USER's attributes

    #functions
    def print_sched(self): 
        print("\n|COURSE TEACHING SCHEDULE|")
        print("--------------------------")
        prof_name = self.first
        prof_last = self.last
            
        cursor.execute("""SELECT * FROM COURSE WHERE INSTRUCTOR = ?;""", [(prof_name + ' ' + prof_last)] )
        print_results = cursor.fetchall()

        print("Course Schedule")
        for i in print_results:
            print(i)


    def print_classlist(self):
        print("\n|COURSE ROSTER|")
        print("---------------")
        
        prof_full_name = (self.first + ' ' + self.last) # make the full name of the instructor
        print(prof_full_name)
        print("student ID in course registered: " + str(reg_stu_id))
        print("Course registered info: " + str(reg_class))
        print("Course reg prof info: " + str(reg_prof_name))
        print(type(reg_class))
        for id in reg_stu_id: #search for student id in reg course id array
            id = int(id)
            print(id)
            # print(type(id))

        cursor.execute("""SELECT * FROM STUDENT WHERE ID = ?;""", [id] ) #query for student info using id from array
        stu_id_results = list(cursor.fetchall())
        for id in stu_id_results: #search for student id from db query
            stu_fname = id[1]
            stu_lname = id[2]

        for course in reg_class: #search for course in reg course array
            if prof_full_name in course:
                # if id in reg_stu_id:
                print(course)
                print("Student: " + stu_fname + " " + stu_lname + " is registered for " + str(course[0]) + " " + str(course[1]))
                print("\n")
                    # print("Student: " + str(id) + " has registered for " + str(course[0]) + " " + str(course[1]))
                # else:
                #     print("No Student Roster")
            # else:
            #     print("No Student Roster")
            #     break

            

# student = STUDENT("Joe", "Gbe", "10011")
# instr = INSTRUCTOR("Henry", "Bess", "20013")
# student.add_course()
# student.add_course()
# instr.print_classlist()
# print("Instrutor first name is: ", instr.first)
# instr.print_sched()

 #Admin
class ADMIN(USER):
    def __init__(self, first, last, ID):
        super().__init__(first, last, ID) #inherit USER's attributes
        #super(STUDENT).__init__(add_course, drop_course, drop_course) #inherit STUDENT's attributes
        
    #functions
    def add_course(self): 
        print("|ADD A COURSE|")
        print("--------------")
        while bogus:
            crn = input("Enter Course CRN: ")
            if crn.isnumeric():
                title = input("Enter Course Title: ")
                dept = input("Enter Course Dept: ")
                instr = input("Enter Instructor First and Last Name: ")
                time = input("Enter Course Time: ")
                day = input("Enter Course Day: ")
                semester = input("Enter Course Semester: ")
                while bogus:
                    year = input("Enter Course Year: ")
                    credits = input("Enter Course Credits: ")
                    if year.isnumeric() or credits.isnumeric():
                        cursor.execute("""INSERT OR IGNORE INTO COURSE VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);""", (int(crn), title, dept, instr, time, day, semester, year, int(credits)))

                        print("Course " + crn + " " + title + " has been created")  
                        break 
                    else:
                        print("ERROR: YEAR AND CREDITS MUST BE NUMBERS")
            else:
                print("ERROR: CRN MUST BE NUMBERS")
                continue
            break



    def remove_course(self):
        print("|REMOVE A COURSE|")
        print("---------")
        while bogus:
            crn = input("Enter Course CRN: ")
            if crn.isnumeric():
                cursor.execute("""SELECT * FROM COURSE WHERE CRN = ?;""", [crn] )
                rem_course_results = cursor.fetchall()

                for i in rem_course_results:
                    print("Course Information")
                    print("ID: " + str(i))
                    cursor.execute("""DELETE FROM COURSE WHERE CRN = ?;""", [crn] )
                    print("Course " + crn + " " + i[1] + " has been deleted")
            else:
                print("ERROR: CRN MUST BE NUMBERS")
                continue
            break
        


    def add_instructor(self): 
        print ("|ADD AN INSTRUCTOR|")
        print("--------------")
        while bogus:
            id = input("Enter Instructor's ID: ")
            if id.isalpha():
                    print("Incorrect ID")
            else:
                name = input("Enter Instructor's First Name: ")
                last_name = input("Enter Instructor's Last Name: ")
                title = input("Enter Instructor's Title: ")
                while bogus:
                    hire_year = input("Enter Instructor's Hire Year: ")
                    if hire_year.isnumeric():
                        dept = input("Enter Instructor's Dept: ")
                        email = input("Enter Instructor's Email: ")

                        cursor.execute("""INSERT OR IGNORE INTO INSTRUCTOR VALUES('%s', '%s','%s', '%s', '%s', '%s', '%s');""" % (id, name, last_name, title, hire_year, dept, email))

                        print("Instructor " + name + " " + last_name + " has been created\n")

                            #show instructor updates
                        cursor.execute("""SELECT * FROM INSTRUCTOR""")
                        instr_list = cursor.fetchall()
                        # print(course_list)

                        print("\n\t\t\tUPDATED INSTRUCTOR")
                        print("----------------------------------------------------------------------------")
                        for i in instr_list:
                            print(i)
                        print("----------------------------------------------------------------------------\n")
                        break
                    else:
                        print("ERROR: Hire Year Must Be Numbers")
                        continue
                break
                


    def add_student(self): 
        print ("|ADD A STUDENT|")
        print("--------------")
        while bogus:
            id = input("Enter Student's ID: ")
            if id.isalpha():
                    print("Incorrect ID")
            else:
                name = input("Enter Student's First Name: ")
                last_name = input("Enter Student's Last Name: ")
                while bogus:
                    grad_year = input("Enter Student's Grad Year: ")
                    if grad_year.isalpha():
                        print("Incorrect Graduation Year")
                    else:
                        major = input("Enter Student's Major: ")
                        email = input("Enter Student's Email: ")
                
                        cursor.execute("""INSERT OR IGNORE INTO STUDENT VALUES(?, ?, ?, ?, ?, ?);""", (int(id), name, last_name, int(grad_year), major, email))

                        print("Student " + name + " " + last_name + " has been created")

                                        #show student updates
                        cursor.execute("""SELECT * FROM STUDENT""")
                        stu_list = cursor.fetchall()
                        # print(course_list)

                        print("\n\t\tUPDATED STUDENT")
                        print("-----------------------------------------------------------")
                        for i in stu_list:
                            print(i)
                        print("-----------------------------------------------------------\n")
                        break
                    continue
                break

    
    def remove_user(self):
        print ("|REMOVE USER|")
        print("--------------")
        id = input("Enter ID: ")
        if id.isalpha():
                print("Incorrect ID")
        else:
            cursor.execute("""SELECT * FROM ADMIN WHERE ID = ?;""", [id] )
            admin_remove_user = cursor.fetchall()

            cursor.execute("""SELECT * FROM INSTRUCTOR WHERE ID = ?;""", [id] )
            instr_remove_user = cursor.fetchall()

            cursor.execute("""SELECT * FROM STUDENT WHERE ID = ?;""", [id] )
            stud_remove_user = cursor.fetchall()

            for i in admin_remove_user or instr_remove_user or stud_remove_user:
                if i in admin_remove_user or instr_remove_user or stud_remove_user:
                    print("User Information")
                    print("Name: \t\t\t ID:")
                    print("" + str(i[1] + " " + str(i[2])) + "\t\t" + str(i[0]))
                    
                    cursor.execute("""DELETE FROM ADMIN WHERE ID = ?;""", [id] )
                    cursor.execute("""DELETE FROM INSTRUCTOR WHERE ID = ?;""", [id] )
                    cursor.execute("""DELETE FROM STUDENT WHERE ID = ?;""", [id] )

                    print("Name " + i[1] + " " + i[2] + " has been deleted")
                else:
                    print("\nError: Enter an ID")

admin = ADMIN("Joseph", "G", "2")
#print("Admin first name is: ", admin.first)
# admin.remove_course()
# admin.add_instructor()


# If we skip this, nothing will be saved in the database. 
database.commit() 
# database.close()
