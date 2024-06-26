#Write a program that calculates the Body Mass Index (BMI) 
#and categorizes it into different weight statuses. The formula for BMI is weight / height^2, 
#where weight is in kilograms and height is in meters.
#Categories:
#Underweight: BMI < 18.5
#Normal weight: 18.5 <= BMI < 24.9
#Overweight: 25 <= BMI < 29.9
#Obesity: BMI >= 30

print("This program will show the result of your Body Mass Index (BMI) and categorize it into weight statues.")

weight = input("Please enter the weight in kilograms:")
height = input("Please enter the height in meters:")
BMI = int(weight) / (float(height) ** 2)

if(BMI < 18.5):
    print("The Body Mass Index(BMI):",BMI,"Category: Underweight")
elif(BMI >= 18.5 and BMI <24.9):
    print("The Body Mass Index(BMI):",BMI,"Category: Normal weight")
elif(BMI >= 25 and BMI < 29.9):
    print("The Body Mass Index(BMI):",BMI,"Category: Overweight")
else:
    print("The Body Mass Index(BMI):",BMI,"Category: Obesity")



