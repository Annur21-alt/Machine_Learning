firstName = "Khairi"
lastName = "Abu Bakar"
# usually both sides of the operator is numbers
# if they are number we can perform addition

# If both sides are string we can perform "string concatenation"
fullName = firstName + " " + lastName
print(fullName)

carPlate = "JCG"
number = 6979
# however this use case we cannot add them because one is number
# another one is string
# carPlateNumber = carPlate + number
# I can only concatenate str (not "int") to str
# in this case we cannot convert carPlate to number
# so let us convert number to string using str function
carPlateNumber = carPlate + str(number)
print(carPlateNumber)

# In python you can multiply string with integer
# When we do this it will product "times" effect
product = "book"
print(product * 5)
print("=" * 40)

# Traditionally how we handle multiline strings
# we handle it using string concatenation
# however we still miss the new line characters
# we have to introduce a special character \n
# the slash \ character is also called escape character
# the slash followed by t means tab key
# the slash followed by r means carriage return
message = "As I am not feeling well\n"
message = message + "I won't be able to attend the \tmeeting.\n"
message = message + "Please proc\reed....\n"
print(message)

myfile = "c:\newfolder\table\read.txt"
print(myfile)
# we suppose to tell python to ignore the escape sequence
# you can add extra escape sequence
myfile = "c:\\newfolder\\table\\read.txt"
print(myfile)
# however in python we also have special string called raw string
myfile = r"c:\newfolder\table\read.txt"
print(myfile)

# so far we know strings are enclosed with double quote
# or single quote
# we can also use triple double quote or triple single quote
# they are used to create multiline strings
# you no need to do \n you no need to do string concatenation
message = """As I am not feeling well
I won't be able to attend the meeting.
Please proceed...."""
print(message)