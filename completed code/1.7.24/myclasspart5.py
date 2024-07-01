# Is - A Relationship
class Student:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = ""

#Alumni extends Student class
class Alumni(Student):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)

#we have create and object of Alumni class
alumni = Alumni("Nur", "Aida")
print (alumni)

