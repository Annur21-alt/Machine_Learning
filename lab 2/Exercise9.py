#Write a Python program to check whether a given number is an Adam number.
#An Adam number is a number for which the square of the number and 
#the square of its reverse are themselves reverses of each other. 
#In other words, if you take a number, reverse it, square 
#both the original number and the reversed number, and the results are still reverse of each other, 
#then the original number is called an Adam number.

print("This program will check whether a given number is an Adam number.")
givenNumber = int(input("Please input the number:"))

reverse_number = givenNumber % 10
givenNumber = givenNumber // 10
reverse_number = reverse_number * 10 + (givenNumber % 10)

givenNumberSquare = givenNumber ** 2
reverse_numberSquare = reverse_number ** 2

reverse_numberSquare2 = reverse_numberSquare % 10
reverse_numberSquare = reverse_number // 10
reverse_numberSquare2 = reverse_numberSquare2 * 10 + (reverse_numberSquare % 10)

if (reverse_numberSquare2 == givenNumberSquare):
    print ("The given number is Adam number.")
else:
    print ("The given number is not Adam number.")







