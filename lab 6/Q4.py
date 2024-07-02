#Write a function that inputs a number and returns the product of digits of that number.

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