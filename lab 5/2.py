def collatz_sequence(n):
    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:  # n is even
            n = n // 2
        else:           # n is odd
            n = 3 * n + 1
    print(1)  # print the last number in the sequence which is always 1

# Get user input
n = int(input("Please enter the integer: "))

# Generate and print Collatz sequence for the input number
print("Collatz sequence for", n, "is:")
collatz_sequence(n)
