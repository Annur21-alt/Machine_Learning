'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage:
a = 48
b = 18
print("GCD of", a, "and", b, "is:", gcd(a, b))
'''

print("This program will take two integer inputs from the user and calculate their greatest common divisor (GCD) using the Euclidean algorithm.")

# Take two integer inputs from the user
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

def GCD_Euclidean_algorithm(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

# Call the function and print the result
gcd_result = GCD_Euclidean_algorithm(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd_result}")



