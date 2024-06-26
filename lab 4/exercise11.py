'''
Write a Python program that takes a string as input, 
which contains numbers separated by commas. Convert the string to a list of numbers. 
Now pick 3 unique numbers from the list whose sum is 100.
'''
print ("This program will takes string as input and separated it by commas then convert it to a list of numbers\nthen, pick 3 unique number from the list whose sum is 100")
input_number = input("The list number:")
List_num = input_number.split(",")
print (List_num)

List_num_2 = []
for num in List_num:
    List_num_2.append(int(num))
unique_number = []

for count in range(0, len(List_num_2)):
    if (List_num_2 != unique_number):
        unique_number.append(List_num_2[input_number])

index = 0
for output_variable1 in unique_number:
    inner_index = index + 1
    for output_variable2 in unique_number[inner_index:]:
        output_variable3 = 100 - (output_variable1 + output_variable2)
        if (output_variable3 in unique_number[inner_index + 1:]):
            print (output_variable1,output_variable2,output_variable3)
            break
        inner_index = inner_index + 1
    index = index + 1



