#Get number of items as input and generate that many ADAM Numbers

input_number = int(input("Please input the number:"))
adam_number = 0

for i in range(1,1000):
    total = 0
    num = i
    while num > 0:
        ans = num % 10
        total = (total * 10) + ans
        num = num // 10
    
    Adam_Num = total ** 2
    square_i = i ** 2

    total_1 = 0
    num_1 = Adam_Num
    while num_1 > 0:
        total_1 = (total_1 * 10) + (num_1 % 10)
        num_1 = num_1 // 10

    if (square_i == total_1):
        adam_number = adam_number + 1
        print ("Adam number",adam_number,":",i)
    if (adam_number == input_number):
        break


    

    

    
