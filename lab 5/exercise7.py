#Write a program that calculates the sum of the first n terms of the harmonic series. Take the n as Input.

#Hn = 1 + 1/2 + 1/3 + 1/4 .... + 1/n

print ("This program will calculates the sum of the first n terms of the harmonic series.")

n = int(input("Please enter the integer:"))
def harmonic_series (n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + 1/i
        return sum
    
harmonic_series()




