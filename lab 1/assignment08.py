#Prompts the user to enter the principal amount, rate of interest, time in years, 
#and number of times interest is compounded per year. 
#Calculates the compound interest. Prints the compound interest.
#(Hint: The formula to calculate compound interest is:
# A=P(1+R/100n)nt where A is the amount, P is the principal amount, R is the annual interest rate, 
# t is the time the money is invested for, and n is the number of times interest is compounded per year)

print("This program will show the result of the compound interest.")

principal_amount = input("Please enter the principal amount:")
rate_interest = input("Please enter the rate of interest:")
time_in_years = input("Please enter the time in years:")

print("The compound interest is:", (int(principal_amount) * ((1 + int(rate_interest)) / 100 * int(time_in_years))) )

