def find_perfect_numbers(count):
    perfect_numbers = []
    num = 2  # Start checking from the first even number

    while len(perfect_numbers) < count:
        sum_of_divisors = sum([i for i in range(1, num//2 + 1) if num % i == 0])
        if sum_of_divisors == num:
            perfect_numbers.append(num)
        num += 1

    return perfect_numbers

# Generate the first 4 perfect numbers
perfect_numbers = find_perfect_numbers(4)

# Output the perfect numbers and their description
for i, num in enumerate(perfect_numbers):
    print(f"{i+1}: {num}")

