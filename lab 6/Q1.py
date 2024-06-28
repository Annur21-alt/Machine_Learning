#Write a python function that takes a number as parameter and prints the multiplication table of that number

# using def function
def multiplication_table(number):
    for i in range(1,11):
        print(f"{number} x {i} = {number * i}")

#instruction to user
number = int(input("Please enter the number: "))
multiplication_table(number)