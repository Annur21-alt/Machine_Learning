#Write a Python program that takes a score (between 0 and 100) as input and prints the corresponding grade based on the following criteria:
# A for scores 90 and above
# B for scores 80-89
# C for scores 70-79
# D for scores 60-69
# F for scores below 60

print("This program will show the grade based on the score that user input:")

grade = input("Please enter your score:")

if (int(grade)<= 100) and (int(grade)>=90):
    print ("Score:", grade, "Grade:A")
elif (int(grade)<= 89) and (int(grade)>=80):
    print ("Score:", grade, "Grade:B")
elif (int(grade)<= 79) and (int(grade)>=70):
    print ("Score:", grade, "Grade:C")
elif (int(grade)<= 69) and (int(grade)>=60):
    print ("Score:", grade, "Grade:D") 
else:
     print ("Score:", grade, "Grade:F")






      