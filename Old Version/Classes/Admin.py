from Classes.User import User
import sqlite3
import sys
# setting path
sys.path.append('../LeopardWeb')
from dbConnection import *

class Admin(User):
    # constructor
    def __init__(self, firstName, lastName, ID):
        super().__init__(firstName,lastName, ID)

    def addCourseToSystem(self, CRN, title, department, time, day, semester, year, credits):
        cursor.execute("""INSERT OR IGNORE INTO COURSE (CRN, TITLE, DEPARTMENT, TIME, DAY, SEMESTER, YEAR, CREDITS ) VALUES (?,?,?,?,?,?,?,?) """, (CRN, title, department, time, day, semester, year, credits))

    def removeCourseFromSystem(self, CRNin):
        cursor.execute("""DELETE FROM COURSE WHERE CRN = ? """, (CRNin,))

    def addUser(self, firstName, lastName, ID, userType):
        print(f"You have add a new {userType} to the system\n")

    def removeUser(self, userID):
        print(
            f"You have removed the user with UserID: {userID} from the system\n")

    def addStudentToCourse(self, studentID, courseName):
        print(f"You have added a new student to the course: {courseName}.\n")

    def removeStudentFromCourse(self, studentID, courseName):
        print(f"You have removed a student from the course: {courseName}\n")

    def searchCourse(self, courseInfo):
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = ? OR TITLE= ?  """, (courseInfo, courseInfo))

        query_result = cursor.fetchone()
        return query_result 

