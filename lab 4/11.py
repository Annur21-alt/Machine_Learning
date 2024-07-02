print("This program takes a string as input, separates it by commas, converts it to a list of numbers, then picks 3 unique numbers from the list whose sum is 100.")
input_number = input("The list number: ")
List_num = input_number.split(",")
print(List_num)

# Convert the list of strings to a list of integers
List_num_2 = [int(num) for num in List_num]

# Remove duplicate numbers to get a list of unique numbers
unique_number = list(set(List_num_2))

# Find and print the combination of three unique numbers that sum to 100
found = False
for i in range(len(unique_number)):
    for j in range(i + 1, len(unique_number)):
        for k in range(j + 1, len(unique_number)):
            if unique_number[i] + unique_number[j] + unique_number[k] == 100:
                print(unique_number[i], unique_number[j], unique_number[k])
                found = True
                break
        if found:
            break
    if found:
        break
if not found:
    print("No combination of three unique numbers sums to 100.")
