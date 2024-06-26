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


# we can also use tripple double quote
#they use

