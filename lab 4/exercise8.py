# Write a python program that takes few numbers as command line argument. 
# Use a loop to display all elements. Use another loop to display all elements in the even position. 
# Use another loop to display all elements in the odd position.

import sys
input_number = sys.argv 
print("All the number that user input")
for number in input_number:
    print(number,end='')
print ()

print("Number in even position:")
for i in range(0, len(number), 2):
    print(input_number[i], end = '')
print ()

print("Number in odd position:")
for i in range(1, len(number), 2):
    print(input_number[i], end = '')
print ()





