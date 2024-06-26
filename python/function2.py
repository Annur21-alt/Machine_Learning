def simpleInterest (principle, period, rate):
    interest = (principle * period * rate) / 100
    return interest

print ("Interest Amount:", simpleInterest (1000, 1, 6))



def participantList (nameone,nametwo,namethree):
    nameone = nameone + "Data Science"
    nametwo = nametwo + "Data Science"
    namethree = namethree + "Data Science"
    return nameone,nametwo,namethree

result = 