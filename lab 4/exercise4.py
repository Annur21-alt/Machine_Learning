#Get number of items as input and generate that many Armstrong Numbers

input_number = int(input("Please input the number:"))
armstrong_number = 0
for armsNum1 in range (1,100000):
    for repetition in range (1,9):
        if armsNum1 // (10**armsNum1) == 0:
            number = repetition
        break

    if (armsNum1 // 100000 != 0):
        print(armsNum1,"cannot print")
    else:
        total = 0
        armsNum2 = armsNum1
        while armsNum2 > 0:
            remainder = armsNum2 % 10
            total = total + remainder ** number
            armsNum2 = armsNum2 // 10

        if (armsNum1 == total):
            armstrong_number = armstrong_number + 1
            print("Armstrong number",armstrong_number,":",armstrong_number)
        if (armstrong_number == input_number):
            break

        total = 0





