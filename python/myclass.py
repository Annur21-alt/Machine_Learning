'''def calculateSInterest(principle,period,rate):
    simpleInterest = (principle*period*rate) / 100
    return simpleInterest

principle = 1000
period = 1
rate = 6

result = calculateSInterest
'''

class Student:

    def __init__(self):
        print ("object is created")

    def attendClass(self):
        print ("Object started attending the class")

    def doProject(self, projectname):
        print ("Object started doing the project:",projectname)

    def attendExam(self,exam):
        grade = "A"
        return f"object has attended the exam: {exam} and obtained the score {grade}"
    


zul = Student()
zul.attendClass()
zul.doProject("Pokemon")
print(zul.attendExam("Python 102"))

