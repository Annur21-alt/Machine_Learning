# Functions are not for solving problems like operators, if, for, while
# Functions are used to organize our code

# When to create our own function ?
# Whenever you copy and paste a block of code
# then you know already it has to be a function
# remember the first code we did in python is
print("Hello World !!!")

# The above statement can we just write as 1 line
# or do we have to create a function put this line inside the
# function and call the function
# Well it depends on your requirement
# Lets say if you copy this line and paste it in 5 places
# then it must be converted to a function
def sayHelloWorld():
    print("Hello World inside the function !!!")

# Declaring a function
# functions are created using the keyword def
# followed by function name
# which is again followed by paranthesis ()
# which is again followed by colon :
# place your block of code inside the function with indentation

# Calling a function
# what will happen if we never call/invoke the function
# Nothing happens the code inside the function never gets executed
# how do i call the function ?
# function name followed by paranthesis ()
sayHelloWorld()

# When we create a function if that function takes some value
# then we must create a variable (placeholder) in between the bracket
# if the function takes more than 1 value then we must create
# more than 1 variable(s) (placeholders) seperated by comma
# these variable/variables is called "parameter"
# if the parameter is dull color then it means we are taking parameter
# but not using that parameter inside the function
def greeting(name):
    print("Good morning",  name)

# When we call the function since the function is taking a parameter/parameter(s)
# we must pass value to the parameter/parameters
# the value we are passing is called argument
# the number of argument(s) must match with number of parameter(s)
greeting("Jegan")

def total(x, y, z):
    result = x + y + z
    print("Result:", result)

total(10, 20, 30)

# we ask him to buy, technically after buy he must give it back to us
# so that we can eat
# for example I have this function and inside this function we have code
# to identify the price for each food and return the prices
# so that the caller can do the payment
def buyLunch(makan, minum):
    prices = [] # empty list
    for food in makan:
        if (food == "nasi"):
            # append is a function inside the object prices (instance of list)
            # so append is a method
            prices.append(2.80)
        elif (food == "sayur"):
            prices.append(2.20)
    for food in minum:
        if (food == "nescafe"):
            prices.append(2.50)
    # print(prices)
    return prices

# now calcuate the amount to be paid
# unless the function return/give you back the receipt
# there is no way for us to find the amount to be paid
# since the buyLunch function is returning some value
# it becomes compulsory for us the hold the value
# we must declare the placeholder
itemprices = buyLunch(["nasi", "sayur"], ["nescafe"])
total = 0
for price in itemprices:
    total = total + price
print("Amount to be paid:", total)

# whether the return value must be a list
# no you can always return single value
def simpleInterest(principle, period, rate):
    interest = (principle * period * rate) / 100
    # return [interest, principle, period, rate]
    return interest

print("Interest Amount:", simpleInterest(1000, 1, 6))

# however when you return more than one value seperated by comma
# it will be a tuple (tuple is nothing but readonly list)
def participantList(nameone, nametwo, namethree):
    nameone = nameone + " Data Science"
    nametwo = nametwo + " Data Science"
    namethree = namethree + " Data Science"
    return nameone, nametwo, namethree

result = participantList("John", "Peter", "Parker")
print(type(result))


#
def calculatesimpleInterest(principle, period=1, rate=6):
    interest = (principle * period * rate) / 100
    return interest

#
print (calculatesimpleInterest (1000,1))

#
print (calculatesimpleInterest (1000))

#
print (calculatesimpleInterest (principle=1000, rate=5))



def findtotal(givenNumbers):
    Total = 0
    for givenNumber in givenNumbers:
        total = total + givenNumber
    return total

print (findtotal(10,20,30))
print (findtotal(10,20,30,40,50,60))


def listSixLetterFruits (*fruits):
    for fruit in fruits:
        if len(fruit) == 6: print(fruit)

listSixLetterFruits ("apple","orange","mango","banana","durian","grapes")

