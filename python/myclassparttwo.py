'''def calculateSInterest(principle,period,rate):
    simpleInterest = (principle*period*rate) / 100
    return simpleInterest

principle = 1000
period = 1
rate = 6

result = calculateSInterest
'''

class Student:

    def __init__(self,firstname,lastname,icnumber):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = icnumber
        self.program = ""
        self.address = ""

    def attendClass(self):
        print ("Object started attending the class")

    def doProject(self, projectname):
        print ("Object started doing the project:",projectname)

    def attendExam(self,exam):
        grade = "A"
        return f"""{self.firstname}{self.lastname} has\
 attended the exam:{exam} and obtained the score {grade}"""
    
    def info(self):
        print("First Name:", self.firstname)
        print("Last Name:", self.lastname)
        print("IC Number:",self.icnumber)
        for program in self.program:
            print("Program:",program)
        print("Address:",self.address)
       # print(self.)

    #def 

    

Aida = Student("Nur","Aida",990823066496)
Aida.attendClass()
Aida.doProject("Pokemon")
print(Aida.attendExam("Python 105"))

Aida.program = ["Python","Data Science","Machine Learning"]
Aida.info()
Aida. address = {
    "Street": "F 42 A",
    "Area": "Kuala Rompin"
    #"Postcode:": 26800,

}


