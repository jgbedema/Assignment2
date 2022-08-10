from unittest import result
from dbConnection import *
from Classes.User import User
from Classes.Admin import Admin
from Classes.Instructor import Instructor
from Classes.Student import Student

from tkinter import *
from tkinter import messagebox
from tkinter import ttk



def Dummy():
    pass



def logInAsAdmin():
    mainCanvas.delete("all")
    
    cursor.execute(""" SELECT * FROM ADMIN WHERE EMAIL=? """, (userIDEntry.get(),))
    dbRow = cursor.fetchone()
    adminUser = Admin(dbRow[1],dbRow[2],dbRow[0])
    
    def goSearch():
         
        resultTable = ttk.Treeview(root, columns=(0,1,2,3,4,5), show='headings', height=3)
        resultTable.column(0, width=20)
        resultTable.column(1, width=60)
        resultTable.column(2, width=250)
        resultTable.column(3, width=50)
        resultTable.column(4, width=50)
        resultTable.column(5, width=70)
        
        resultTable.heading(0, text=" ")
        resultTable.heading(1, text="CRN")
        resultTable.heading(2, text="Title")
        resultTable.heading(3, text="Day")
        resultTable.heading(4, text="Credits")
        resultTable.heading(5, text="Semester")
        
        results = adminUser.searchCourse(searchEntry.get())
        
       
        
        resultTable.insert("", 'end', iid=None, values=('', results[0], results[1], results[4], results[7], results[5]))
        mainCanvas.create_window(270,320, window=resultTable)
        
        backBttn = Button(root, text="<Back", font=('Helvetica','9'), command=logInAsAdmin, width=8 )
        mainCanvas.create_window(20, 20, window= backBttn)
        
        
        
        
        
    def addCourseToSys():
        CRNEntry= Entry(root,font=('Helvetica','11'), width=20 ) 
        titleEntry= Entry(root,font=('Helvetica','11'), width=20 )
        departmentEntry= Entry(root,font=('Helvetica','11'), width=20 )
        timeEntry= Entry(root,font=('Helvetica','11'), width=20 )
        dayEntry= Entry(root,font=('Helvetica','11'), width=20 )
        semesterEntry= Entry(root,font=('Helvetica','11'), width=20 )
        yearEntry= Entry(root,font=('Helvetica','11'), width=20 )
        creditsEntry= Entry(root,font=('Helvetica','11'), width=20 )
        
        
        def addCToSys():
            if(CRNEntry.get() and titleEntry.get() and departmentEntry.get() and timeEntry.get() and dayEntry.get() and semesterEntry.get() and yearEntry.get() and creditsEntry.get()):
                adminUser.addCourseToSystem(CRNEntry.get(),titleEntry.get(), departmentEntry.get(), timeEntry.get(),dayEntry.get(), semesterEntry.get(), yearEntry.get(), creditsEntry.get())
                messagebox.showinfo("info", "Succesfully added Course to System")
                
            else:
                messagebox.showinfo("info", "Error: At least one field is empty")
                
    
        mainCanvas.delete("all")
        mainCanvas.create_text(300, 45, text="Enter the following info about the course you wish to add to sys:",font=('Helvetica','14','bold'))
        mainCanvas.create_text(300, 65, text="CRN, title, department, time, day, semester, year, credits",font=('Helvetica','11'))
        mainCanvas.create_text(200, 85, text="CRN: ",font=('Helvetica','11'))
        mainCanvas.create_window(340, 85, window=CRNEntry) 
        mainCanvas.create_text(200, 110, text="Title: ",font=('Helvetica','11'))
        mainCanvas.create_window(340, 110, window=titleEntry) 
        mainCanvas.create_text(200, 135, text="Department: ",font=('Helvetica','11'))
        mainCanvas.create_window(340, 135, window=departmentEntry) 
        mainCanvas.create_text(200, 160, text="Time: ",font=('Helvetica','11'))
        mainCanvas.create_window(340, 160, window=timeEntry) 
        mainCanvas.create_text(200, 185, text="Day: ",font=('Helvetica','11'))
        mainCanvas.create_window(340, 185, window=dayEntry) 
        mainCanvas.create_text(200, 210, text="Semester: ",font=('Helvetica','11'))
        mainCanvas.create_window(340, 210, window=semesterEntry) 
        mainCanvas.create_text(200, 235, text="Year: ",font=('Helvetica','11'))
        mainCanvas.create_window(340, 235, window=yearEntry) 
        mainCanvas.create_text(200, 260, text="Credits: ",font=('Helvetica','11'))
        mainCanvas.create_window(340, 260, window=creditsEntry) 
        
        backBttn = Button(root, text="<Back", font=('Helvetica','9'), command=logInAsAdmin, width=7 )
        mainCanvas.create_window(20, 18, window= backBttn)
        addCoursetoSysBttn = Button(root, text="Add Course", font=('Helvetica','11'), command=addCToSys, width=10 )
        mainCanvas.create_window(400, 400, window= addCoursetoSysBttn)
    
    def rmvCourseFromSys():
        def goRmvSearch():
            resultTable = ttk.Treeview(root, columns=(0,1,2,3,4,5), show='headings', height=3)
            resultTable.column(0, width=20)
            resultTable.column(1, width=60)
            resultTable.column(2, width=250)
            resultTable.column(3, width=50)
            resultTable.column(4, width=50)
            resultTable.column(5, width=70)
        
            resultTable.heading(0, text=" ")
            resultTable.heading(1, text="CRN")
            resultTable.heading(2, text="Title")
            resultTable.heading(3, text="Day")
            resultTable.heading(4, text="Credits")
            resultTable.heading(5, text="Semester")
        
            results = adminUser.searchCourse(searchEntry.get())

            def rmvCourse():
                if results:
                    adminUser.removeCourseFromSystem(int(results[0]))
                    messagebox.showinfo("info", "Course removed from System")
                else:
                    messagebox.showinfo("info", "Remove Course Failed: Not currently in Sys")
       
        
            resultTable.insert("", 'end', iid=None, values=('', results[0], results[1], results[4], results[7], results[5]))
            mainCanvas.create_window(270,320, window=resultTable)
        
            backBttn = Button(root, text="<Back", font=('Helvetica','9'), command=logInAsAdmin, width=8 )
            mainCanvas.create_window(20, 20, window= backBttn)
            addBttn = Button(root, text="Remove Course from Sys", font=('Helvetica','9'), command=rmvCourse, width=15 )
            mainCanvas.create_window(400, 400, window= addBttn)
        
        mainCanvas.delete("all")
        mainCanvas.create_text(300, 30, text="Search Course to remove by entering the CRN:",font=('Helvetica','14','bold'))
        mainCanvas.create_text(200, 140, text="CRN: ",font=('Helvetica','11'))
        mainCanvas.create_window(340, 140, window=searchEntry) 
        
        goRmvBttn = Button(root, text="Go", font=('Helvetica','11'), command=goRmvSearch, width=10 )
        mainCanvas.create_window(400, 140, window= goRmvBttn)
        
    def search():
        mainCanvas.delete("all")
        mainCanvas.create_text(300, 30, text="Search Course by entering one of those param (any)",font=('Helvetica','14','bold'))
        mainCanvas.create_text(300, 100, text="CRN or Title: ",font=('Helvetica','11'))
        mainCanvas.create_text(200, 140, text="Param: ",font=('Helvetica','11'))
        mainCanvas.create_window(340, 140, window=searchEntry) 
        goBttn = Button(root, text="Go", font=('Helvetica','11'), command=goSearch, width=20 )
        mainCanvas.create_window(300, 170, window= goBttn)
        
        backBttn = Button(root, text="<Back", font=('Helvetica','9'), command=logInAsAdmin, width=7 )
        mainCanvas.create_window(20, 18, window= backBttn)
        
    mainCanvas.create_text(300, 30, text="Leopard Web accesed by: Admin "+ adminUser.firstName ,font=('Helvetica','14','bold'))
    mainCanvas.create_text(300, 100, text="Please select an item to continue: ",font=('Helvetica','11'))
    


    searchParamBttn = Button(root, text="Search Courses", font=('Helvetica','11'), command=search, width=30 )
    mainCanvas.create_window(300, 200, window= searchParamBttn)
    addCourseBttn = Button(root, text="Add Course to system", font=('Helvetica','11'), command=addCourseToSys, width=30 )
    mainCanvas.create_window(300, 250, window= addCourseBttn)
    removeCourseBttn = Button(root, text="Remove Course from system", font=('Helvetica','11'), command=rmvCourseFromSys, width=30 )
    mainCanvas.create_window(300, 300, window= removeCourseBttn)

def logInAsStudent():
    mainCanvas.delete("all")
    
    cursor.execute(""" SELECT * FROM STUDENT WHERE EMAIL=? """, (userIDEntry.get(),))
    dbRow = cursor.fetchone()
    studentUser = Student(dbRow[1],dbRow[2],dbRow[0])
    
    def goSearch():
        resultTable = ttk.Treeview(root, columns=(0,1,2,3,4,5), show='headings', height=3)
        resultTable.column(0, width=20)
        resultTable.column(1, width=60)
        resultTable.column(2, width=250)
        resultTable.column(3, width=50)
        resultTable.column(4, width=50)
        resultTable.column(5, width=70)
        
        resultTable.heading(0, text=" ")
        resultTable.heading(1, text="CRN")
        resultTable.heading(2, text="Title")
        resultTable.heading(3, text="Day")
        resultTable.heading(4, text="Credits")
        resultTable.heading(5, text="Semester")
        
        results = studentUser.searchCourse(searchEntry.get())
        
        def addFunc():
           
            if results:
                studentUser.schedule.append(results[1])
                messagebox.showinfo("info", "Course Added to schedule")
            else:
                messagebox.showinfo("info", "Add Course Failed")
            print(studentUser.schedule)
        def rmvFunc():
            print(studentUser.schedule)
            print(results[1])
            if (results[1] in studentUser.schedule):
                studentUser.schedule.remove(results[1])
                messagebox.showinfo("info", "Course removed to schedule")
            else:
                messagebox.showinfo("info", "Course is not in schedule")
        
        resultTable.insert("", 'end', iid=None, values=('', results[0], results[1], results[4], results[7], results[5]))
        mainCanvas.create_window(270,300, window=resultTable)
        
        backBttn = Button(root, text="<Back", font=('Helvetica','9'), command=logInAsStudent, width=8 )
        mainCanvas.create_window(20, 20, window= backBttn)
        
        addBttn = Button(root, text="Add to schedule", font=('Helvetica','9'), command=addFunc, width=15 )
        mainCanvas.create_window(400, 400, window= addBttn)
        rmvBttn = Button(root, text="Remove from schedule", font=('Helvetica','9'), command=rmvFunc, width=20 )
        mainCanvas.create_window(400, 450, window= rmvBttn)
        
    
    def search():
        mainCanvas.delete("all")
        mainCanvas.create_text(300, 30, text="Search Course by entering one of those param (any)",font=('Helvetica','14','bold'))
        mainCanvas.create_text(300, 100, text="CRN or Title: ",font=('Helvetica','11'))
        mainCanvas.create_text(200, 140, text="Param: ",font=('Helvetica','11'))
        mainCanvas.create_window(340, 140, window=searchEntry) 
        goBttn = Button(root, text="Go", font=('Helvetica','11'), command=goSearch, width=20 )
        mainCanvas.create_window(300, 200, window= goBttn)
        
    
    def addRemoveCourse():
        mainCanvas.delete("all")
        mainCanvas.create_text(300, 30, text="Add/Remove Course by entering CRN",font=('Helvetica','14','bold'))
        mainCanvas.create_text(200, 100, text="CRN: ",font=('Helvetica','11'))
        mainCanvas.create_window(340, 100, window=searchEntry) 
        goBttn = Button(root, text="Go", font=('Helvetica','11'), command=goSearch, width=20 )
        mainCanvas.create_window(300, 200, window= goBttn)
        
    mainCanvas.create_text(300, 30, text="Leopard Web accesed by: Admin "+ studentUser.firstName ,font=('Helvetica','14','bold'))
    mainCanvas.create_text(300, 100, text="Please select an item to continue: ",font=('Helvetica','11'))
    
    searchBttn = Button(root, text="Search Courses", font=('Helvetica','11'), command=search, width=30 )
    mainCanvas.create_window(300, 200, window= searchBttn)
    addCourseBttn = Button(root, text="Add Course to schedule", font=('Helvetica','11'), command=addRemoveCourse, width=30 )
    mainCanvas.create_window(300, 250, window= addCourseBttn)
    removeCourseBttn = Button(root, text="Remove Course from schedule", font=('Helvetica','11'), command=addRemoveCourse, width=30 )
    mainCanvas.create_window(300, 300, window= removeCourseBttn)

def logInAsInstructor():
    mainCanvas.delete("all")
    
    cursor.execute(""" SELECT * FROM INSTRUCTOR WHERE EMAIL=? """, (userIDEntry.get(),))
    dbRow = cursor.fetchone()
    instructorUser = Instructor(dbRow[1],dbRow[2],dbRow[0])
    
    def goSearch():
         
        resultTable = ttk.Treeview(root, columns=(0,1,2,3,4,5), show='headings', height=3)
        resultTable.column(0, width=20)
        resultTable.column(1, width=60)
        resultTable.column(2, width=250)
        resultTable.column(3, width=50)
        resultTable.column(4, width=50)
        resultTable.column(5, width=70)
        
        resultTable.heading(0, text=" ")
        resultTable.heading(1, text="CRN")
        resultTable.heading(2, text="Title")
        resultTable.heading(3, text="Day")
        resultTable.heading(4, text="Credits")
        resultTable.heading(5, text="Semester")
        
        results = instructorUser.searchCourse(searchEntry.get())
        
       
        
        resultTable.insert("", 'end', iid=None, values=('', results[0], results[1], results[4], results[7], results[5]))
        mainCanvas.create_window(270,320, window=resultTable)
        
        backBttn = Button(root, text="<Back", font=('Helvetica','9'), command=logInAsInstructor, width=8 )
        mainCanvas.create_window(20, 20, window= backBttn)
        
        
    
    def search():
        mainCanvas.delete("all")
        mainCanvas.create_text(300, 30, text="Search Course by entering one of those param (any)",font=('Helvetica','14','bold'))
        mainCanvas.create_text(300, 100, text="CRN or Title: ",font=('Helvetica','11'))
        mainCanvas.create_text(200, 140, text="Param: ",font=('Helvetica','11'))
        mainCanvas.create_window(340, 140, window=searchEntry) 
        goBttn = Button(root, text="Go", font=('Helvetica','11'), command=goSearch, width=20 )
        mainCanvas.create_window(300, 170, window= goBttn)
        
    
    
   
        
    mainCanvas.create_text(300, 30, text="Leopard Web accesed by: Prof. "+ instructorUser.firstName ,font=('Helvetica','14','bold'))
    mainCanvas.create_text(300, 100, text="Please select an item to continue: ",font=('Helvetica','11'))
    
    searchBttn = Button(root, text="Search Courses", font=('Helvetica','11'), command=search, width=30 )
    mainCanvas.create_window(300, 200, window= searchBttn)
    printRosterBttn = Button(root, text="Print Course Roster", font=('Helvetica','11'), command=Dummy, width=30 )
    mainCanvas.create_window(300, 250, window= printRosterBttn)


def logout():
    
    return mainCanvas


#sign in function to sign in as user "functiions" above    
def signIn():
    cursor.execute("SELECT * FROM ADMIN_LOGINS where username=? AND password=?",(userIDEntry.get(), passwordEntry.get()))
    logAdmin=cursor.fetchone()
    cursor.execute("SELECT * FROM INSTRUCTOR_LOGINS where username=? AND password=?",(userIDEntry.get(), passwordEntry.get()))
    logInstructor=cursor.fetchone()
    cursor.execute("SELECT * FROM STUDENT_LOGINS where username=? AND password=?",(userIDEntry.get(), passwordEntry.get()))
    logStudent=cursor.fetchone()
    
    if logAdmin:
        logInAsAdmin()
    elif logStudent:
        logInAsStudent()
    elif logInstructor:
        logInAsInstructor()
    else:
        messagebox.showinfo("info", "Login Failed.")
        



def main():
    createLogins()
    global root
    root=Tk()
    root.title('Leopard Web')
    root.geometry('600x500')
    root['padx']=20
    
  
    global mainCanvas
    mainCanvas = Canvas(root, width=400, height=400) #create canvas
    mainCanvas.pack(fill="both", expand=True)

    mainCanvas.create_text(300, 30, text="Welcome to Leopard Web",font=('Helvetica','14','bold'))
    mainCanvas.create_text(300, 100, text="Please enter your Username and password. ",font=('Helvetica','11'))
    
    global userIDEntry, passwordEntry, searchEntry
    userIDEntry= Entry(root,font=('Helvetica','11'), width=20 ) 
    passwordEntry= Entry(root,show="*",font=('Helvetica','11'), width=20 ) 
    searchEntry= Entry(root,font=('Helvetica','11'), width=20 ) 
    
    mainCanvas.create_text(200, 140, text="Username: ",font=('Helvetica','11'))
    mainCanvas.create_window(340, 140, window=userIDEntry) 
    mainCanvas.create_text(200, 170, text="Password: ",font=('Helvetica','11'))
    mainCanvas.create_window(340, 170, window=passwordEntry) 

    global signInBttn
    signInBttn = Button(root, text="Sign In", font=('Helvetica','11'), command=signIn, width=20 )
    mainCanvas.create_window(300, 260, window= signInBttn)
    
    root.mainloop()

    #close the connection 
    database.commit() 
    database.close()


if __name__ == '__main__':
    main()