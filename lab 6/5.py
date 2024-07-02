'''def sum_of_proper_divisors(n):
    if n <= 1:
        return 0  # Proper divisors for numbers <= 1 are considered 0
    divisors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

# Example usage
print(sum_of_proper_divisors(36))  # Output: 55
print(sum_of_proper_divisors(12))  # Output: 16 (1 + 2 + 3 + 4 + 6)
print(sum_of_proper_divisors(1))   # Output: 0
print(sum_of_proper_divisors(28))  # Output: 28 (1 + 2 + 4 + 7 + 14)
'''



number = int(input("Enter a number: "))

def sum_of_proper_divisors(n):
    if n <= 1:
        return 0  # Proper divisors for numbers <= 1 are considered 0
    divisors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)


# Calculate the sum of proper divisors
result = sum_of_proper_divisors(number)

# Print the result
print(f"The sum of proper divisors of {number} is {result}.")
