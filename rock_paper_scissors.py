import random
from termcolor import colored

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m".format(skk))

play_again_flag = True
while play_again_flag:
    pc_score = 0
    player_score = 0

    while True:
        rock = 'Rock'
        paper = 'Paper'
        scissors = 'Scissors'
        pc_random_num = random.randint(1, 3)

        pc_move = ""
        player_move = input("Choose [r]ock, [p]aper and [s]cissors: ")


        if player_move == 'r':
            player_move = rock
        elif player_move == 'p':
            player_move = paper
        elif player_move == 's':
            player_move = scissors
        else:
            raise SystemExit("Invalid input. Please try again...")

        if pc_random_num == 1:
            pc_move = rock
        elif pc_random_num == 2:
            pc_move = paper
        else:
            pc_move = scissors

        if (player_move == rock and pc_move == scissors) or \
                (player_move == paper and pc_move == rock) or \
                (player_move == scissors and pc_move == paper):
            player_score += 1
            prGreen(f"You win! The pc's move was {pc_move}. Your score is {player_score} to the pc's {pc_score}")
        elif player_move == pc_move:
            prYellow(f"Draw. The pc's move was {pc_move}.")
        else:
            pc_score += 1
            prRed(f"You lose. The pc's move was {pc_move}. Your score is {player_score} to the pc's {pc_score}")

        if player_score >= 3:
            prGreen("You beat the PC. Congrats!")
            play_again = input("Do you want to play again? (yes/no):").lower()
            if play_again != "yes":
                prCyan("Thank you for playing!")
                play_again_flag = False
                break
            else:
                prCyan("Let's GO!")
                break
        elif pc_score >= 3:
            prRed("You lost to the PC.")
            play_again = input("Do you want to play again? (yes/no):").lower()
            if play_again != "yes":
                prCyan("Thank you for playing!")
                play_again_flag = False
                break
            else:
                prCyan("Let's GO!")
                break





