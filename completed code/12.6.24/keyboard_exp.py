numbers = input("Enter the numbers to do Total: ")
numberlist = numbers.split(",")
print(numberlist)
total = 0
for number in numberlist:
    # int function trim the string value
    # remove the spaces in the string and then convert
    # string to integer
    total = total + int(number)
print(total)