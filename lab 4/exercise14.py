#Write a python program which takes a number as input and convert the number to binary.
#Note: Don't use any builtin functions.

print("This program will takes a number as input and convert the decimal number to binary.")
input_number = int(input("Please enter the number:"))
print("The decimal number:",input_number)
binary_number = " "

while (input_number > 0):
    binary_number = str(input_number % 2) + binary_number
    input_number = input_number // 2

print("The binary number:",binary_number)



