#Initialize two variables, x = 0b10101100 and y = 0b11010010.
#Write Python code to:
#Swap the values of x and y without using a temporary variable.
#Toggle the 3rd and 5th bits of x.
#Check if two given numbers a = 29 and b = 15 are different.

x = 0b10101100
y = 0b11010010

# x XOR x = 0
# x XOR 0 = x

x = x ^ y    #x1 = x ^ y
y = x ^ y    #y = x1
x = x ^ y    #x = y

print (f"Value x after the swap process: {bin(x)}")
print (f"Value y after the swap process: {bin(y)}")

x = x ^(1 << 2)
x = x ^(1 << 4)

print (f"Value after the toggle process: {bin(x)}")

a = 29
b = 15

if (a != b):
    print (f"The value of {a} and {b} are different.")
else:
    print (f"The value of {a} and {b} are same.")


