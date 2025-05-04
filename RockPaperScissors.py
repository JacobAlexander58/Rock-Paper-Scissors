import random

print("\nWelcome to Rock, Paper, Scissors!")

options=['rock', 'paper', 'scissors']

while True:
    user_choice = (input('\nChoose your option, or type "quit" to stop the game: ')).lower()
    if user_choice == "quit":
        print("Thank you for playing!")
        break
    if user_choice not in options:
        print("Invalid choice")

    computer_choice = random.choice(options)
    print(f"Computer chose {computer_choice}")

    if computer_choice == user_choice:
        print("It's a draw!")
    elif(
        (user_choice=="rock" and computer_choice=="scissors") or
        (user_choice=="paper" and computer_choice=="rock") or
        (user_choice=="scissors" and computer_choice=="paper")):
        print("You win!")

    else:
        print("You lose!")

