class User():
    # constructor
    def __init__(self, firstName, lastName, ID):
        self.firstName = firstName
        self.lastName = lastName
        self.ID = ID

    # methods (don't need getters and setters in python)
    def printInfoOnUser(self):
        print(f"{self.firstName} infos are:\n")
        print('ID = %s\n' % (self.ID))
        print(f"First Name = { self.firstName}\n")
        print(f"Last Name =  {self.lastName }\n")