#Get a number as input and calculate the sum of all numbers from 1 to the given number.

input_number = int(input("Enter a number:"))
sum_of_numbers = 1

for num in range (1, input_number + 1):
    sum_of_numbers += num

print ("The sum of all numbers from 1 to" , input_number ,"is", sum_of_numbers)