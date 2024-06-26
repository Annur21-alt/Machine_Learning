#Write a python program that takes few numbers as command line argument. Find the average of those numbers.

import sys
integers = sys.argv[1:]
Total = 0
print("Please enter three integers:")

for number in integers:
    print (number, end='')
    Total = int(number) + Total
print ()

average_number = Total / len(integers)
print(f"The average of those integers is:{average_number:.2f}")





