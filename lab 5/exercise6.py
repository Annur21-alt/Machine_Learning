'''
Problem 6 Perfect Number: Write a program that generates 4 perfect numbers.
Example
6: The divisors of 6 are 1, 2, 3, and 6. The sum of its proper divisors (excluding 6 itself) is 1 + 2 + 3 = 6.
28: The divisors of 28 are 1, 2, 4, 7, 14, and 28. 
    The sum of its proper divisors (excluding 28 itself) is 1 + 2 + 4 + 7 + 14 = 28.
'''

print ("This program will generates 4 perfect numbers.")

def generate_perfectNum (count):
    perfectNum = []
    number = 2

    while len(perfectNum) < count:
        total_divisor = sum([i for i in range(1, number//2 + 1)if number % i == 0])
        if total_divisor == number:
            perfectNum.append(number)
        number = number + 1

    return perfectNum

perfectNum = generate_perfectNum(4)

for i, number in enumerate(perfectNum):
    print (f"{i+1}: {number}")