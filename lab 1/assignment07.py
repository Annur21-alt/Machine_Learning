#Write a Python program that:
#Prompts the user to enter their weight in kilograms and height in meters. 
#Calculates the Body Mass Index (BMI). 
#Prints the BMI. 
#(Hint: The formula to calculate BMI is: BMI = weight / (height * height))

print("This program will show the result of your Body Mass Index (BMI).")

weight = input("Please enter the weight in kilograms:")
height = input("Please enter the height in meters:")

print("The Body Mass Index(BMI):", int(weight) / (float(height) * float(height)))
