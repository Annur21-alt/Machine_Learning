'''The Westland Game Fair is the premier event of its kind for kids interested in some intellectual and cognitive brain games. Alan, a middle school boy is visiting the fair where he is very much drawn by the Card game.

The game’s rules are:
A player needs to pick 3 cards from a big lot of cards. There are 4 types of Cards namely Spade(S), Heart(H), Club(C) and Diamond (D). If all the 3 cards that the player picks are of the same type and same number, they get a Double Bonanza. If all the 3 cards are of the same type or if they all have the same number, they get a Bonanza. Otherwise they do not get a Bonanza. Alan has now picked 3 cards and is awaiting to know if he has got a bonanza. Please help him to know if he has won the Bonanza or not.

Input Format:
There are 3 lines of input.
Each of the line consists of character and integer input, which corresponds to the type of the card and the number in it that Alan picked. The type of card and the number are separated by a single space.

Output Format:
Output should display "Double Bonanza" or "Bonanza" or "No Bonanza" based on the conditions given.
Refer sample input and output for formatting specifications.

Sample Input 1:
S 5
S 5
S 5

Sample Output 1:
Double Bonanza

Sample Input 2:
S 6
S 5
H 5


Sample Output 2:
No Bonanza# Read the three cards
'''

card1 = input().strip().split()
card2 = input().strip().split()
card3 = input().strip().split()

# Extract types and numbers
type1, num1 = card1[0], card1[1]
type2, num2 = card2[0], card2[1]
type3, num3 = card3[0], card3[1]

# Check for Double Bonanza
if type1 == type2 == type3 and num1 == num2 == num3:
    print("Double Bonanza")
# Check for Bonanza
elif type1 == type2 == type3 or num1 == num2 == num3:
    print("Bonanza")
# No Bonanza
else:
    print("No Bonanza")
