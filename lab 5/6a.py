print("This program will generate 4 perfect numbers.")

def generate_perfectNum(count):
    perfectNum = []
    number = 2

    while len(perfectNum) < count:
        total_divisor = 0  # Initialize the sum of proper divisors
        
        # Iterate through the possible divisors
        for i in range(1, number // 2 + 1):
            if number % i == 0:  # Check if 'i' is a divisor of 'number'
                total_divisor += i  # Add 'i' to the sum of proper divisors
        
        # Check if the sum of proper divisors equals the number
        if total_divisor == number:
            perfectNum.append(number)
        
        number += 1  # Move to the next number

    return perfectNum

# Generate the first 4 perfect numbers
perfectNum = generate_perfectNum(4)

# Print each perfect number with its index
for i, number in enumerate(perfectNum):
    print(f"{i + 1}: {number}")
