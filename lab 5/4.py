import random

def get_choice_name(choice):
    """Convert numeric choice to string."""
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Paper"
    elif choice == 3:
        return "Scissors"

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "Computer wins!"

print("This program will ask you to choose between Rock, Paper, and Scissors.")
print("""1 = Rock
2 = Paper
3 = Scissors
""")

while True:
    try:
        user_choice = int(input("Please select the number (1, 2, or 3): "))
        if user_choice not in [1, 2, 3]:
            print("Invalid input. Please select 1, 2, or 3.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    computer_choice = random.randint(1, 3)
    
    user_choice_name = get_choice_name(user_choice)
    computer_choice_name = get_choice_name(computer_choice)

    print(f"You chose: {user_choice_name}")
    print(f"Computer chose: {computer_choice_name}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
