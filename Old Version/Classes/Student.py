from Classes.User import User
import sqlite3
import sys
# setting path
sys.path.append('../LeopardWeb')
from dbConnection import *

class Student(User):
    # constructor
    def __init__(self, firstName, lastName, ID):
       super().__init__(firstName,lastName, ID)
       self.schedule=[]

    def searchCourse(self, courseInfo ):
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = ? OR TITLE= ?  """, (courseInfo, courseInfo))

        query_result = cursor.fetchone()
        return query_result 

    def addCourse(self, courseName):
       self.schedule.append(courseName)

    def dropCourse(self, courseName):
        self.schedule.remove(courseName)


    def printSchedule(self):
        pass
