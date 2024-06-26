#deep copy
fruits = ["apple","orange","mango","banana","grapes"]

numbers = range(1, 50)

multiplesofthree = []
for number in range (1,50):
    if (number % 3 == 0):
        multiplesofthree.append(number)
print (multiplesofthree)



def findmultiples(number):
    return True if (number % 3 == 0) else False



oddnumbers = [number for number in numbers if (number % 2 != 0)]
print(oddnumbers)

print("+++++++++++++++++++++++++++")

from functools import reduce

numbers = [1,2,3]

def findTotal (oldvalue, currentvalue):
    return oldvalue + currentvalue

print (reduce(findTotal, numbers))

