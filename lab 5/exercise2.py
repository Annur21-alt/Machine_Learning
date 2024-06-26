'''Write a program that takes an integer input from the user and generates 
the Collatz sequence for that number. The Collatz sequence is defined as follows:
start with a number n. If n is even, the next number is n/2. If n is odd, 
the next number is 3n + 1. Repeat the process until n becomes 1.

#x boleh buat cam ni klau nak loop!!!
ans = (n // 2)
remainder = (n % 2)

next_num1 = n / 2
next_num2 = (3 * n) + 1
'''
print ("This program will take the integer input from user and generates Collatz sequence for that number.")

integer = int(input("Please enter the integer:"))
def NumberOfCollatzSequence (integer):
    while integer != 1:
        print (integer, end = ',')
        if integer % 2 == 0:
            integer = integer // 2
        else:
            integer = (3 * integer) + 1
    print (1)

print("The Collatz Sequence that generates from the integer,",integer,"is") 
NumberOfCollatzSequence(integer)








  
    





    

     
        
   
    
    
        

