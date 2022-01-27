import random

loop = 1
while loop == 1:
    choices = ["Rock", "Paper", "Scissors"]  #List to store names for computer choices
    computer_action = random.choice(choices)

    print("Hello, Welcome to Extreme Rock Paper Scissors showdown")
    user_input = input(f"Please enter your choice between Rock, Paper, or Scissors: ")
    user_input = user_input.title()
    print(f"You're choice of {user_input} is going up against the computer's choice of {computer_action}")

    if user_input == computer_action:
        print("It's a tie!")
    elif user_input == "Rock" and computer_action == "Scissors":
        print("You win!")
    elif user_input == "Paper" and computer_action == "Rock":
        print("You win!")
    elif user_input == "Scissors" and computer_action == "Paper":
        print("You Win!")
    else:
        print("You lose, better luck next round!")

    play_again = input("Would you like to play again? (Y/N): ")
    play_again = play_again.upper()

    if play_again == "N":
        loop = 0

    else:
        print("Good luck!")


