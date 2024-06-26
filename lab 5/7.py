def harmonic_sum(n):
    sum = 0.0
    for i in range(1, n + 1):
        sum += 1 / i
    return sum

# Taking input from the user
n = int(input("Enter the number of terms (n): "))

# Calculating the harmonic sum
result = harmonic_sum(n)

# Displaying the result
print(f"The sum of the first {n} terms of the harmonic series is: {result}")
