# Take input from user
input_string = input("Enter numbers separated by commas: ")

# Split the input string by commas to get individual number strings
num_strings = input_string.split(',')

# Initialize a flag to track duplicates
all_different = True

# Convert these strings to integers
numbers = []
for num_str in num_strings:
    num = int(num_str)
    # Check if the number is already in the numbers list
    if num in numbers:
        all_different = False
        break
    numbers.append(num)

# Check the flag to determine the result
if all_different:
    print("All numbers are different from each other.")
else:
    print("There are duplicate numbers.")
