# Initialize two variables, x = 0b10101100 and y = 0b11011001.
# Write Python code to:
# Extract the lower 4 bits from x.
# Check if y is even or odd.
# Clear the upper 4 bits of x.
# Check if the 5th bit of y is set.

x = 0b10101100
y = 0b11011001

x_mask = 0b00001111
print(bin(x & x_mask))

if (y % 2 == 0):
    print ("y is even number.")
else:
    print ("y is odd number.")

y_mask = 0b00010000
print(bin(y & y_mask))
print("5th bit of y is a set.")
