'''
# let us do the multiplication table using range
multiplicant = 6
for multiplier in range(1, 13):
    print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)
'''


# soalan jupyter notebook 6: (Q1)
# Write a python function that takes a number as parameter 
# and prints the multiplication table of that number

multiplicant = input("Please enter the number:")
def multiplication_table(multipliers):
    multipliers_count = 1
    for multiplier in multipliers:
        multipliers_count = multiplier * multiplicant
    return multipliers_count

print(multiplication_table)
