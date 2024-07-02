#Write a function that takes a number as parameter. 
# The function finds the proper divisors of that number and then finds 
# the sum of proper divisors. Proper divisors of a number are those numbers 
# by which the number is divisible, except the number itself.
#For example proper divisors of 36 are 1, 2, 3, 4, 6, 9, 18

print("This program will return the proper divisor of a number.")

number = int(input("Enter a number: "))

def sum_of_proper_divisors(n):
    if n <= 1:
        return 0  # Proper divisors for numbers <= 1 are considered 0
    proper_divisors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            proper_divisors.append(i)
    return sum(proper_divisors)


# Calculate the sum of proper divisors
result = sum_of_proper_divisors(number)

# Print the result
print(f"The sum of proper divisors of {number} is {result}.")

