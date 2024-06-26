#Write a Python program to get 2 positive numbers as input and multiply them without using the '*' operator.
print("This program ask 2 postive numbers from user and multiply them without using * operator")
num1 = input("Please enter number 1 (positive numbers):")
num2 = input("Please enter number 2 (positive numbers):")

total = 0

for i in range(int(num2)):
    total = int(num1) + total

print ("The answer for",num1,"multiply by",num2,"is",total)




