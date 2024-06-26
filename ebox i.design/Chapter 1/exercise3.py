#Sample Input and Output:
# Enter branding expenses
# 20000
# Enter travel expenses
# 40000
# Enter food expenses
# 15000
# Enter logistics expenses
# 25000
# Total expenses : Rs.100000.00
# Branding expenses percentage : 20.00%
# Travel expenses percentage : 40.00%
# Food expenses percentage : 15.00%
# Logistics expenses percentage : 25.00% 

branding_expenses = int(input ("Enter branding expenses\n"))
travel_expenses = int(input("Enter travel expenses\n"))
food_expenses = int(input("Enter food expenses\n"))
logistics_expenses = int(input("Enter logistics expenses\n"))

Total_expenses = branding_expenses + travel_expenses + food_expenses + logistics_expenses
print("Total expenses : Rs.{:.2f}".format(Total_expenses))

branding_expenses_percentage = (branding_expenses / Total_expenses) * 100
print (f"Branding expenses percentage : {branding_expenses_percentage  :.2f}%")

travel_expenses_percentage = (travel_expenses / Total_expenses) * 100
print (f"Travel expenses percentage : {travel_expenses_percentage  :.2f}%")

food_expenses_percentage = (food_expenses / Total_expenses) * 100
print (f"Food expenses percentage : {food_expenses_percentage  :.2f}%")

logistics_expenses_percentage = (logistics_expenses / Total_expenses) * 100
print (f"Logistics expenses percentage : {logistics_expenses_percentage  :.2f}%")