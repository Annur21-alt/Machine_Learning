# Write a program that simulates an ATM withdrawal. 
# The user enters the withdrawal amount and the program checks if the amount is a multiple of 10. 
# If it is, the program prints the number of each denomination (50, 20, 10) required to dispense the amount. 
# If not, it prints an error message. 
# For example if the amount is 233 then 
# it must print "4 50 dollar bills, 1 20 dollar bills, 1 10 dollar bills, 3 1 dollar bills

print("This program simulates an ATM withdrawal.")

input_amount= input ("Please input the amount:RM ")

result = int(input_amount)// 50
remainder = int(input_amount) % 50

result1 = int(remainder)// 20
remainder1 = int(remainder) % 20

result2 = int(remainder1)// 10
remainder2 = int(remainder1) % 10

if (remainder == 0 or remainder != 0):
    print (result, "X RM 50")

if (remainder1 == 0 or remainder1 != 0):
    print (result1, "X RM 20")

if (remainder2 == 0 or remainder2 != 0):
    print (result2, "X RM 10")


