print("-- Python Code by Joseph Gbedema --\n")


#Base class

class USER:
    #attributes
    def __init__(self, first, last, ID):
        self.first = first
        self.last = last
        self.ID = ID

    def PrintAll(self):
       # print(self.first, self.last, self.ID)
        print("User print all function called")


user = USER("Joseph", "Gbedema", "1")
print("User first name is: ", user.first)
user.PrintAll()


#----Derived Class(es)---#

#Student
class STUDENT(USER):
    def __init__(self, first, last, ID):
        super(STUDENT, self).__init__(first, last, ID) #inherit USER's attributes

    #functions
    def search(self):
        print("Student search function called")

    def add_course(self): 
        print("Student add course function called")

    def drop_course(self):
        print("Student drop course function called")

    def print_sched(self):
        print("Student print schedule function called")

student = STUDENT("Joe", "Gbe", "2")
print("Student first name is: ", student.first)
student.print_sched()

#Instructor
class INSTRUCTOR(USER):
    def __init__(self, first, last, ID):
        super().__init__(first, last, ID) #inherit USER's attributes

    #functions
    def print_sched(self): 
        print("Instructor print schedule function called")

    def print_classlist(self):
        print("Instructor print class list function called")
  
    def search_course(self):
        print("Instructor search function called")

instr = INSTRUCTOR("J", "G", "3")
print("Instrutor first name is: ", instr.first)
instr.print_sched()

 #Admin
class ADMIN(USER):
    def __init__(self, first, last, ID):
        super().__init__(first, last, ID) #inherit USER's attributes
        #super(STUDENT).__init__(add_course, drop_course, drop_course) #inherit STUDENT's attributes
        
    #functions
    def add(self): 
        print("Admin add function called")

    def drop(self):
        print("Admin drop function called")

    def remove_course(self):
        print("Admin remove course function called")

    def add_user(self): 
        print("Admin add user function called")

    def remove_user(self):
        print("Admin remove user function called")

    def add_student(self): 
        print("Admin add student  function called")

    def remove_student(self):
        print("Admin remove student function called")
  
    def search_roster(self):
        print("Admin search roster function called")   

    def search_course(self):
        print("Admin search course function called")

    def print_roster(self):
        print("Admin print roster function called")   

    def print_course(self):
        print("Admin print course function called")


admin = ADMIN("Joseph", "G", "2")
print("Admin first name is: ", admin.first)
admin.print_course()




