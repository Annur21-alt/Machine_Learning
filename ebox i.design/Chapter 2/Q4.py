

# Taking input from user
basic_salary = int(input())

def calculate_gross_salary(basic_salary):
    if basic_salary < 15000:
        HRA = 0.15 * basic_salary
        DA = 0.9 * basic_salary
    else:
        HRA = 5000
        DA = 0.98 * basic_salary
    
    gross_salary = basic_salary + HRA + DA
    return gross_salary

# Calculating gross salary
gross_salary = calculate_gross_salary(basic_salary)

# Printing output formatted to 2 decimal places
print(f"{gross_salary:.2f}")
