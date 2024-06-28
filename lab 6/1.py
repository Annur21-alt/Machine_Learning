def print_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
        
number = int(input("Please enter the number: "))
print_multiplication_table(number)
