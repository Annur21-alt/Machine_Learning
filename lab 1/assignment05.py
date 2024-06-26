#Write a Python program that:
#Prompts the user to enter two numbers. Swaps the values of the two variables. 
#Prints the values before and after swapping.

print("This program will show the swaps of the two variables.")

firstnum = input("Please enter first integer number:")
secondnum = input("Please enter second integer number:")

result = int(firstnum) + int(secondnum)
after2 = int(result) - int(secondnum)
after1 = int(result) - int(firstnum)

before_swapping = print("Before swapping number:", firstnum, secondnum)
after_swapping = print("After swapping number:", after1, after2)