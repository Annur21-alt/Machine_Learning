#Write a program that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" 
# instead of the number,and for the multiples of five, print "Buzz". 
# For numbers which are multiples of both three and five, print "FizzBuzz".

print ("""This program will prints the numbers 1 to 100, for multiples of three, 
it will print 'Fizz' and for multiples of five it will print 'Buzz' and for both 
multiple three and five, it will print 'FizzBuzz'. """)

for num in range(1,101):
    if num % 3 == 0:
        print ("Fizz")
    elif num % 5 == 0:
        print ("Buzz")
    elif num % 3 and num % 5 == 0:
        print ("FizzBuzz")
    else:
        print (num)
    continue

