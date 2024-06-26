print("This program will generate 4 perfect numbers.")

def generate_perfectNum(count):
    perfectNum = []
    number = 2  # Starting from the first possible perfect number candidate

    while len(perfectNum) < count:
        # Calculate the sum of proper divisors of 'number'
        total_divisor = sum([i for i in range(1, number // 2 + 1) if number % i == 0])
        
        # Check if 'number' is a perfect number
        if total_divisor == number:
            perfectNum.append(number)
        
        number += 1  # Move to the next number

    return perfectNum

# Generate the first 4 perfect numbers
perfectNum = generate_perfectNum(4)

# Print each perfect number with its index
for i, number in enumerate(perfectNum):
    print(f"{i + 1}: {number}")


