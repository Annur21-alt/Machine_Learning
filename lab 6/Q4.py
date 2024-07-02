#Write a function that inputs a number and returns the product of digits of that number.
'''
print ("This program will return product of the digit")
def product_of_digits(n):
    product = 1
    # Make sure n is positive
    n = abs(n)
    # Multiply each digit
    while n > 0:
        digit = n % 10
        product = product * digit
        n //= 10
    return product

# Example usage
print(product_of_digits(1234))  # Output: 24
'''

print("This program will return the product of the digits")

# Prompt the user for input
user_input = int(input("Please enter a number: "))

def product_of_digits(n):
    # Handle the case when n is 0
    if n == 0:
        return 0
    
    product = 1
    # Multiply each digit
    while n > 0:
        digit = n % 10
        product =product * digit
        n //= 10
    return product


# Calculate and print the product of digits
result = product_of_digits(user_input)
print(f"The product of the digits of {user_input} is {result}")
