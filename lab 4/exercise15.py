#Write a python program which takes a binary number as input and convert the number to decimal. 
#Note: Don't use any builtin functions.

print ("This program will takes a binary number as input and convert the it to decimal.")
input_number = (input("Please enter the number:"))
number = int(input_number)
count = len(input_number)
decimal_number = 0
print("The binary number:",input_number)

for i in range(0,count):
    modulus_answer = number % 10
    decimal_number = decimal_number + (2 ** i) * modulus_answer
    number = number // 10

print("The decimal number:",decimal_number)
