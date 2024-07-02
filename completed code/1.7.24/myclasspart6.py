# Polymorphism

class Gender:
    def __init__(self):
        pass
    def doCarryObjects(self):
        pass

class Male (Gender):
    def __init__(self):
        pass
    def doCarryObjects(self):
        print("Carry Heavy Objects")

    
class Female (Gender):
    def __init__(self):
        print("Carry Light Objects")


def getGender (name):
    if "A/L" in name:
        return Male()
    else:
        return Female()
    

gender = getGender ("Khairi A/L Abu Bakar")
gender.doCarryObjects()
print (type(Gender))

gender = getGender("Aida A/P ABu Bakar")
gender.doCarryObjects()
print (type(gender))