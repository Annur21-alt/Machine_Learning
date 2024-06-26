#Problem2
#Print first 10 prime numbers using for loop

count = 1
print (1)
givenNumber = 2
while count < 10:
    isPrime = True
    divisors = range(2, givenNumber)
    for divisor in divisors:
        if (givenNumber % divisor == 0):
            isPrime = False
            break
    if (isPrime == True):
        print (givenNumber)
        count = count + 1
    givenNumber = givenNumber + 1


