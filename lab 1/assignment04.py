#Write a Python program that:
#Prompts the user to enter the principal amount, rate of interest, and time in years. 
#Calculates the simple interest. Prints the simple interest. 
#(Hint: The formula to calculate simple interest is: 
#SI = (P * R * T) / 100)

print("This program will show the result simple interest.")

principal_amount = input("Please enter the principal amount:")
rate_interest = input("Please enter the rate of interest:")
time = input("Please enter the time in years:")

print("Simple Interest:", (int(principal_amount) * int(rate_interest) * int(time)) / 100)


