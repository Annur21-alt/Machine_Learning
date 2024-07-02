# multiple inheritance
class Card():
    def __init__(self):
        pass

    def doSomething(self):
        print ("Inside Card ")

class AtmCard(Card):
    def __init__(self):
        pass

    def doSomething(self):
        print ("Inside AtmCard Class")

class CreditCard(Card):
    def __init__(self):
        pass

    def doSomething(self):
        print ("Inside CreditCard Class")

class DebitCard(Card):
    def __init__(self):
        pass

    def doSomething(self):
        print ("Inside DebitCard Class")

class BankCard(AtmCard, CreditCard, DebitCard):
    def __init__(self):
        pass
    def doSomething(self):
        super().doSomething()

bankCard = BankCard()
bankCard.doSomething()

#Method Resolution Order (MRO)
print(BankCard.__mro__)

# <class '__main__.BankCard'> 
# <class '__main__.AtmCard'> 
# <class '__main__.CreditCard'> 
# <class '__main__.DebitCard'> 
# <class '__main__.Card'> 
# <class 'object'>

# BIGGEST CONCLUSION
# Every class we create in python is inherited from a class called object
# class object:
#   def __init__():
#       pass
#   def __str__():
#        return (memory address)

#which print by print function


#class Student(object):
class Student():
    def __str__(self):
        return "Student"

class Alumni(Student):
    pass
    #def __str__(self):
        #return "Alumni"

alumni = Alumni()
print(alumni)







