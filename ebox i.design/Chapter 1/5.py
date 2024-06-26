# Read the side length of the square tile
side_length = int(input("Enter the side in cm of a square tile\n"))

# Read the number of square tiles available
num_tiles = int(input("Enter the number of square tiles available\n"))

# Calculate the maximum number of tiles that can form a perfect square
max_side = int(num_tiles ** 0.5)

# Calculate the area of the largest possible square
largest_square_area = (max_side * side_length) ** 2

# Print the result
print(f"Area of the largest possible square is {largest_square_area}sqcm")
