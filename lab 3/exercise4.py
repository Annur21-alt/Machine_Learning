#Initialize two variables, a = 0b10101000 and b = 0b01010100.
#Write Python code to:
#Set the lower 4 bits of a.
#Combine the bits of a and b using OR.
#Create a mask to set the 2nd and 6th bits of a.

a = 0b10101000
b = 0b01010100

a_mask = 0b00001111
print(bin(a & a_mask))

print(bin(a | b))
a_mask_2nd_6th = 0b00100010
print (bin(a_mask_2nd_6th))