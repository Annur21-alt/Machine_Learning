'''Write a program that randomly generates a number between 1 and 100. 
The user has to guess the number. 
After each guess, the program tells the user whether the guess is too high, too low, or correct. 
The game continues until the user guesses the correct number.

To generate random number use random module
import random
random.randint(1,3)
'''
print ("This program will ask the user to guess the number that computer generate till user find the correct number.")

import random
generate_number = random.randint(1,100)

input_num = int(input("Please enter the number:"))

while input_num != generate_number:
    if input_num > generate_number:
        print ("Number is too high. Please try again")
    if input_num < generate_number:
        print ("Number is too high. Please try again")
    if input_num == generate_number:
        print ("The number is correct!!!")
        break

input_num = input_num + 1





    
    




