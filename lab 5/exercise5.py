print ("This program will ask the user to guess the number that computer generate till user find the correct number.")
import random

generate_number = random.randint(1, 100)

while True:
    input_num = int(input("Please enter the number:"))
    
    if input_num > generate_number:
        print("Number is too high. Please try again.")
    elif input_num < generate_number:
        print("Number is too low. Please try again.")
    else:
        print("The number is correct!!!")
        break
