#Write a Python program to check whether a given number is an Armstrong number.
#An Armstrong number (also known as a Narcissistic number or a Pluperfect number) 
#is a number that is equal to the sum of its own digits each raised to the power of the number of digits. 
#For example, 153 is an Armstrong number because 1 ** 3 + 5 ** 3 + 3 ** 3 = 153


print("This program will check whether a given number is an Armstrong number.")
givenNumber = int(input("Please input the number:"))

total = 0
ans = givenNumber
ans_str = str(givenNumber)
length_num = len(ans_str)

remainder = givenNumber % 10
ans = ans // 10
total = total + remainder ** length_num

remainder = givenNumber % 10
ans = ans // 10
total = total + remainder ** length_num

remainder = givenNumber % 10
ans = ans // 10
total = total + remainder ** length_num

if givenNumber == total:
    print ("The given number is not Armstrong number.")
else:
    print("The given number is Armstrong number.")




