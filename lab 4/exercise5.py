#Write a program to print the following pattern using a loop.
#o
#oo
#ooo
#oooo
#ooooo

line_for_o = 5

for line in range (1, line_for_o + 1):
    for o_object in range (1, line + 1):
        print ('o', end = '')
    print ()