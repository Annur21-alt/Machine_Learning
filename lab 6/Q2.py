#Write a simple python function that returns twin primes less than 1000. 
#If two consecutive odd numbers are both prime then they are known as twin primes.
#Pairs of primes that differ by 2. For example, 3 and 5, 5 and 7, 11 and 13, and 17 and 19 are twin primes.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def twin_primes(limit):
    twins = []
    for n in range(3, limit, 2):
        if is_prime(n) and is_prime(n + 2):
            twins.append((n, n + 2))
    return twins

# Get all twin primes less than 1000
twin_primes_under_1000 = twin_primes(1000)
print(twin_primes_under_1000)
