#Write a program that takes two integers from the user and 
#calculates their greatest common divisor (GCD) using the Euclidean algorithm

print ("This program will take two integer input from user and calculate their\ngreatest common divisor (GCD) using the Euclidean algorithm.")

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

def GCD_Euclidean_algorithm (x, y):
    while y != 0:
        x , y = y, x % y
    return x

GCD_result = GCD_Euclidean_algorithm(num1,num2)

print(f"The GCD of {num1} and {num2} is: {GCD_result}")


