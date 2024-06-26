#Write a python program to print first 10 terms in a Fibonacci series

print("This program will print first 10 terms in a Fibonacci series.")
fibonacci_num = 10
x = 0
y = 1
for number in range(1,fibonacci_num+1):
    x,y = y, x + y
    print (y)
