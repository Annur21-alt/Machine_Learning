# Write a python function that takes variable length parameters and 
# returns maximum and minimum number in the parameter numbers.
# For example if we call the function: maximumMinimum(10, 20, 30, 40, 50)
# The function must return: [10, 50]

print("This program will take variable length parameters and return maximum and minimum number in the parameter numbers.")

def maximumMinimum(*numbers):
    if not numbers:
        return None
    min_num = min(numbers)
    max_num = max(numbers)
    return [min_num, max_num]

input_num = input("Please enter numbers separated by space:\n")
numbers = map(int, input_num.split())
print_result = maximumMinimum(*numbers)
print(f"The minimum and maximum numbers are: {print_result}")