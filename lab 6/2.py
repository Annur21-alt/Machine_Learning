'''def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
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
'''

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
