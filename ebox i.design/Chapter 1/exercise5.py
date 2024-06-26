'''
In connection to the National Mathematics Day celebration, the Regional Mathematical Scholars Society had 
arranged for a Mathematics Challenge Event where school kids participated in large number. 
Many interesting math games were conducted, one such game that attracted most kids was the tile game 
where the kids were given 'n' square tiles of the same size and were asked to form the largest possible 
square using those tiles.

Help the kids by writing a program to find the area of the largest possible square that can be formed, 
given the side of a square tile (in cms) and the number of square tiles available.

Input Format:
First line of the input is an integer that corresponds to the side of a square tile (in cms).
Second line of the input is an integer that corresponds to the number of square tiles available.

Output Format:
Output should display the area of the largest possible square that can be formed (in square cms) 
with the available tiles.
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and rest corresponds to output.]

Sample Input and Output :
Enter the side in cm of a square tile
5
Enter the number of square tiles available
8
Area of the largest possible square is 100sqcm
'''

side_in_cm = int(input("Enter the side in cm of a square tile\n"))
n = int(input = ("Enter the number of square tiles available\n"))

max_side_square = int(n ** 0.5)

largest_possible_square = (max_side_square * side_in_cm) ** 2

print(f"Area of the largest possible square is {largest_possible_square}sqcm")

