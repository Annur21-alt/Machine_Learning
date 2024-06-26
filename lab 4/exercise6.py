#Write a program to print the following pattern using a loop
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

line_for_num = 5

for line_num in range (1, line_for_num + 1):
    for num in range (1, line_num + 1):
        print (num, end ='')
    print()