from Database import *
from A5 import *

# database file connection 
database = sqlite3.connect("Database.db") #connect to the databse provided by Prof
print ("Opened database successfully")

# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 

#create a global list for registered classes
bogus = ' '
rep_courses = [] #create an empty list to check repeated courses

#Base class
class USER:
    #attributes
    def __init__(self, first, last, ID):
        self.first = first
        self.last = last
        self.ID = ID
        self.reg_class = [] #list to hold registered courses
        
    
    global reg_class, reg_class_id
    reg_class = [] #list to hold registered courses
    reg_class_id = [] #list to hold student's id's for registered courses

    # def login():
    #     username = input("Please enter a username: ")
    #     cursor.execute("""SELECT * FROM ADMIN WHERE EMAIL = ? """, [username])
    #     admin_result = cursor.fetchall()
    #     cursor.execute("""SELECT * FROM INSTRUCTOR WHERE EMAIL = ? """, [username])
    #     instr_result = cursor.fetchall()
    #     cursor.execute("""SELECT * FROM STUDENT WHERE EMAIL = ? """, [username])
    #     student_result = cursor.fetchall()
        
    #     for username in admin_result or instr_result or student_result:
            
    #         id = username[0]
    #         name = username[1]
    #         surname = username[2]
    #         print(username)   
                

    def Search_course_by_input(self):
        print("\nSearch For Course By CRN Or Title")
        print("---------------------------------")
        crn = input("Enter Course CRN: ")
        title = input("Enter Course Title: ")
        print("CRN: " + crn + "\nTitle: " + title)
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = ?;""", [crn] )
        query_result = cursor.fetchall()

        for i in query_result:
            print("The course information is: " + str(i))
       

    def List_course(self):
        print("\nPrinting Course List")
        print("---------------------------------")
        cursor.execute("""SELECT * FROM COURSE""")
        course_list = cursor.fetchall()
        
        for i in course_list:
            print(i)


user = USER("Joseph", "Gbedema", "1")
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
        print("\nADDING A COURSE")
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
                    print(i)
                    # reg_class.append(i) 
                    if i not in rep_courses:
                        reg_class.append(i)
                        rep_courses.append(i)
                    else:
                        print("You have already registered for this course" )
                print("\nRegistered Courses: ")
                print("CRN \t TITLE")
                for j in reg_class:
                    print(str(j[0]) + "\t " + str(j[1]))
                break
            break

    
    def drop_course(self):
        print("\nREMOVING A COURSE")
        crn = input("\nEnter Course CRN: ")
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = ?;""", [crn] )
        drop_results = cursor.fetchall()
        for i in drop_results:
            if (len(reg_class) == 0) or (crn == bogus):
                print("No Such Course Registered")
                
            else:
                print(drop_results)
                print("Course " + str(i) + " has been removed")
                reg_class.remove(i)
                # reg_class_id.remove(ID)
                print()
     

    def print_sched(self):
        print("\nSCHEDULE")

        print("\nRegistered Courses: ")
        print("CRN \t TITLE")
        for j in reg_class:
            print(j)

student = STUDENT("Joe", "Gbe", "2")
# print("Student first name is: ", student.first)
# student.print_sched()
# student.add_course()
# student.print_sched()
# student.drop_course()
# student.print_sched()

#test to see what is in the registered course array
for j in reg_class:
    print("Stuff inside the registered list: " + str(j))



#Instructor
class INSTRUCTOR(USER):
    def __init__(self, first, last, ID):
        super().__init__(first, last, ID) #inherit USER's attributes

    #functions
    def print_sched(self): 

        for i in reg_class:
            print("\nCourse Information")
            print(i[3])
            crn = i[0]
            prof_name = i[3]
            prof_name_split = prof_name.split(' ', 2)
            first_name = prof_name_split[0]
            second_name = prof_name_split[1]

            cursor.execute("""SELECT * FROM COURSE WHERE INSTRUCTOR = ?;""", [(first_name + ' ' + second_name)] )
            print_results = cursor.fetchall()

            print("Instructor Course Schedule")
            for i in print_results:
                print(i)


    def print_classlist(self):
        print("Instructor Print Class List")



# instr = INSTRUCTOR("Henry", "Bess", "3")
# print("Instrutor first name is: ", instr.first)
# instr.print_sched()

 #Admin
class ADMIN(USER):
    def __init__(self, first, last, ID):
        super().__init__(first, last, ID) #inherit USER's attributes
        #super(STUDENT).__init__(add_course, drop_course, drop_course) #inherit STUDENT's attributes
        
    #functions
    def add_course(self): 
        crn = input("Enter Course CRN: ")
        title = input("Enter Course Title: ")
        dept = input("Enter Course Dept: ")
        instr = input("Enter Instructor First and Last Name: ")
        time = input("Enter Course Time: ")
        day = input("Enter Course Day: ")
        semester = input("Enter Course Semester: ")
        year = input("Enter Course Year: ")
        credits = input("Enter Course Credits: ")

        cursor.execute("""INSERT OR IGNORE INTO COURSE VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);""", (int(crn), title, dept, instr, time, day, semester, year, int(credits)))

        print("Course " + crn + " " + title + " has been created")

    def remove_course(self):
        crn = input("Enter Course CRN: ")
       # title = input("Enter Course Title: ")

        cursor.execute("""SELECT * FROM COURSE WHERE CRN = ?;""", [crn] )
        rem_course_results = cursor.fetchall()

        for i in rem_course_results:
            print("Course Information")
            print("ID: " + str(i))
            cursor.execute("""DELETE FROM COURSE WHERE CRN = ?;""", [crn] )
            print("Course " + crn + " " + i[1] + " has been deleted")

    def add_instructor(self): 
        print ("ADDING AN INSTRUCTOR")
        id = input("Enter Instructor's ID: ")
        name = input("Enter Instructor's First Name: ")
        last_name = input("Enter Instructor's Last Name: ")
        title = input("Enter Instructor's Title: ")
        hire_year = input("Enter Instructor's Hire Year: ")
        dept = input("Enter Instructor's Dept: ")
        email = input("Enter Instructor's Email: ")

        cursor.execute("""INSERT OR IGNORE INTO INSTRUCTOR VALUES('%s', '%s','%s', '%s', '%s', '%s', '%s');""" % (id, name, last_name, title, hire_year, dept, email))

        print("Instructor " + name + " " + last_name + " has been created")

    def add_student(self): 
        print ("ADDING A STUDENT")
        id = input("Enter Student's ID: ")
        name = input("Enter Student's First Name: ")
        last_name = input("Enter Student's Last Name: ")
        grad_year = input("Enter Student's Grad Year: ")
        major = input("Enter Student's Major: ")
        email = input("Enter Student's Email: ")
 
        cursor.execute("""INSERT OR IGNORE INTO STUDENT VALUES('%s', '%s','%s', '%s', '%s', '%s');""" % (int(id), name, last_name, int(grad_year), major, email))

        print("Student " + name + " " + last_name + " has been created")
    
    def remove_user(self):
        print ("REMOVING A USER")
        id = input("Enter ID: ")

        cursor.execute("""SELECT * FROM ADMIN WHERE ID = ?;""", [id] )
        admin_remove_user = cursor.fetchall()

        cursor.execute("""SELECT * FROM INSTRUCTOR WHERE ID = ?;""", [id] )
        instr_remove_user = cursor.fetchall()

        cursor.execute("""SELECT * FROM STUDENT WHERE ID = ?;""", [id] )
        stud_remove_user = cursor.fetchall()

        for i in admin_remove_user or instr_remove_user or stud_remove_user:
            print("User Information")
            print("ID: " + str(i[0]))
            cursor.execute("""DELETE FROM ADMIN WHERE ID = ?;""", [id] )
            cursor.execute("""DELETE FROM INSTRUCTOR WHERE ID = ?;""", [id] )
            cursor.execute("""DELETE FROM STUDENT WHERE ID = ?;""", [id] )

            print("Name " + i[1] + " " + i[2] + " has been deleted")

admin = ADMIN("Joseph", "G", "2")
#print("Admin first name is: ", admin.first)
# admin.remove_course()


# If we skip this, nothing will be saved in the database. 
database.commit() 
# database.close()
