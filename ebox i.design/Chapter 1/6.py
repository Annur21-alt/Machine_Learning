'''# Function to calculate the hours worked on weekdays and weekends
def calculate_hours(total_salary):
    # Calculate the number of weekend hours
    weekend_hours = (total_salary - 800) / 130
    # Calculate the number of weekday hours
    weekday_hours = weekend_hours + 10
    return weekday_hours, weekend_hours

# Read the total salary from input
total_salary = float(input("Enter the total salary paid\n"))

# Calculate the hours
weekday_hours, weekend_hours = calculate_hours(total_salary)

# Print the results
print(f"Number of weekday hours is {int(weekday_hours)}")
print(f"Number of weekend hours is {int(weekend_hours)}")
'''


