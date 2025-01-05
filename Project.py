import random

def winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 1 and computer == 3) or \
         (player == 2 and computer == 1) or \
         (player == 3 and computer == 2):
        return "Congratulations, You Win!"
    else:
        return "You Lose!, Try Again."

def Game():
    print("Welcome to Rock, Paper, Scissors!\n Lets Start!")
    while True:
        try:
            Player_choosed = int(input("Enter your choice: \nPress '1' for Rock, Press '2' for Paper, Press '3' for Scissors \nPress '0' to Quit the Game\n: "))
            if Player_choosed == 0:
                print("Thank You for Playing this Game! Lots of Respect.")
                print("-" * 40)
                break
            if Player_choosed not in [1, 2, 3]:
                print("Invalid! Please Press 1, 2, or 3.")
                print("-" * 40)
                continue
            
            Computer_choosed = random.randint(1, 3)
            choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

            print(f"You chose: {choices[Player_choosed]}")
            print(f"Computer chose: {choices[Computer_choosed]}")
            
            result = winner(Player_choosed, Computer_choosed)
            print(result)
            print("-" * 40)
            print("-" * 40)
        except ValueError:
            print("Invalid input. Please enter a number.")
Game()



