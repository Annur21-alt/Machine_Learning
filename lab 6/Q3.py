#Write a simple python function that takes a number as parameter and returns the prime factors of that number. 
#Prime Factorization is finding which prime numbers multiply together to make the original number.
#Example: prime factors of 56 - 2, 2, 2, 7

print ("This program will takes a number as parameter and returns the prime factors of that number.")

def prime_factors(n):
    factors = []
    # Divide by 2 until n is odd
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Check for odd factors from 3 onwards
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    return factors

# Example usage
print(prime_factors(56))  # Output: [2, 2, 2, 7]
