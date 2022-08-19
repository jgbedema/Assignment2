from Classes.User import User

import sys
# setting path
sys.path.append('../LeopardWeb')
from dbConnection import *

class Instructor(User):
    # constructor
    def __init__(self, firstName, lastName, ID):
       super().__init__(firstName,lastName, ID)
       self.courseRoster= []

    def printSchedule(self):
        print(f"Prof. {self.lastName} is printing his/her schedule....")

    def printClassList(self):
        print(
            f"Prof. {self.lastName} has the following class to teach this semester ....")

    def searchCourse(self, courseInfo):
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = ? OR TITLE= ?  """, (courseInfo, courseInfo))

        query_result = cursor.fetchone()
        return query_result 
