'''Write a program that plays the game of Rock, Paper, Scissors with the user. 
The user makes a choice, the program randomly chooses, and the winner is determined.
To generate random number use random module
import random
random.randint(1,3)
'''
import random

def choiceNum(Num):
    if Num == 1:
        return "Rock"
    elif Num == 2:
        return "Paper"
    elif Num == 3:
        return "Scissors"
    
def winner_game(user_choiceNum,computer_choiceNum):
    if user_choiceNum == computer_choiceNum:
        return "It's a tie!"
    elif (user_choiceNum == 1 and computer_choiceNum == 3) or \
         (user_choiceNum == 2 and computer_choiceNum == 1) or \
         (user_choiceNum == 3 and computer_choiceNum == 2):
        return "Congratulations!! You win."
    else:
        return "Computer wins!!"

print ("This program will ask user to choice between Rock, Paper, Scissors.")
print("""1 = Rock
2 = Paper
3 = Scissors
""")

while True:
    try:
        input_num = int(input("Please select the number:"))
        if input_num > generate_ans not in [1, 2, 3]:
            print("Invalid input. Please select the number between 1 , 2 and 3 only.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    generate_ans = random.randint(1,3)
    user_choice = choiceNum(input_num)
    computer_choice = choiceNum(generate_ans)

    # user_choiceNumName = choiceNum(user_choiceNum)
    # computer_choiceNumName = choiceNum(computer_choiceNum)

    print(f"Your choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")

    result = winner_game(user_choice, computer_choice)
    print(result)

    play_again = input("Do you want")


    

