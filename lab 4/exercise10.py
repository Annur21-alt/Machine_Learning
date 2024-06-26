#Write a Python program that takes a string as input, 
#which contains numbers separated by commas. 
#Convert the string to a list of numbers and 
#determine whether all the numbers are different from each other.

print("This program will take string as input and separate it by commas\nand convert it to list and check whether all the number are different from each other or not.")
string_toNumber = input("Enter the string: ")
numberlist_A = string_toNumber.split(",")
print("List of number:",numberlist_A)

checked_num = set()

for number in numberlist_A:
    if number in checked_num:
        print ("The number has same value.")
        break
    checked_num.add(number)
else:
    print ("The number has different value.")
    




    
