import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

pc_move = ""
player_move = input("Choose [r]ock, [p]aper and [s]cissors: ")


pc_random_num = random.randint(1, 3)

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
    print(f"You win! The pc's move was {pc_move}.")
elif player_move == pc_move:
    print(f"Draw. The pc's move was {pc_move}.")
else:
    print(f"You lose. The pc's move was {pc_move}.")

