#Write a program that takes the lengths of three sides of a triangle 
#and determines whether the triangle is equilateral, isosceles, or scalene.
#Equilateral: All three sides are equal.
#Isosceles: Exactly two sides are equal.
#Scalene: All three sides are different.

print("This program will determine the type of triangle.")

First_Length= input("Please input first length of the triangle:")
Second_Length = input("Please input second length of the triangle:")
Third_Length = input("Please input third length of the triangle:")

if(int(First_Length) == int(Second_Length) and int(First_Length) == int(Third_Length) and int(Second_Length) == int(Third_Length)):
    print ("This triangle is Equilateral.")
else:
    if(int(First_Length) != int(Second_Length) and int(First_Length) != int(Third_Length) and int(Second_Length) != int(Third_Length)):
        print ("This triangle is Scalene")
    else:
        print("This triangle is Isosceles.")


    

