#Write a program that takes three numbers 
#as input and prints the largest one.

print("This program will show the largest number between the three numbers")

integer1 = input("Please enter the first number :")
integer2 = input("Please enter the second number :")
integer3 = input("Please enter the third number :")

if(int(integer1) >int(integer2) and int(integer1) > int(integer3)):
    print ("The largest number is:", int(integer1))
elif(int(integer2) > int(integer1) and int(integer2) > int(integer3)):
    print ("The largest number is:", int(integer2))
elif(int(integer3) > int(integer1) and int(integer3) > int(integer2)):
    print ("The largest number is:", int(integer3))
else:
    print ("All three numbers is same value.")










