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
