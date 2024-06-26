#An investor decides to invest a total of RM30,000 in two different accounts. 
#The first account offers a 5% annual interest rate, while the second account offers a 7% annual interest rate. 
#If the total annual interest earned is RM1,800, how much money was invested in each account?
#Another investor decides to invest a total of RM50,000 in two different accounts. 
#The first account offers a 3% annual interest rate, while the second account offers a 6% annual interest rate. 
#If the total annual interest earned is RM2,400, how much money was invested in each account?
#Write a simple, generic Python program to assist in calculating the amount of money invested in each account 
#to achieve the desired total annual interest. The program must take all these numbers (30000, 5, 7, 1800) 
# as input and calculate the required amounts. Finally, print the result. 
# Please note that the same program must work for the second problem as well (50000, 3, 6, 2400).

Total_investment = int(input ("Please enter total investment:RM"))
annual_rate_interest_acc1 = int(input ("Please enter annual interest rate for account 1:"))
annual_rate_interest_acc2 = int(input ("Please enter annual interest rate for account 2:"))
Total_annual_interest_earned = int(input ("Please enter total annual interest earned:RM"))

total_investment_for_acc2 = (Total_annual_interest_earned - (Total_investment * annual_rate_interest_acc1)) / (-annual_rate_interest_acc1 + annual_rate_interest_acc2)
total_investment_for_acc1 = Total_investment - total_investment_for_acc2

print ("Total investment for account 1 is:RM",int(total_investment_for_acc1))
print ("Total investment for account 2 is:RM",int(total_investment_for_acc2))

#not completed yet