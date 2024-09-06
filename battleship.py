'''
Name: Project 1 - Battleship Game
Description: 
Inputs: 
Outputs: 
Collaborators/Sources: 
{NAMES}
Aug 31 2024
'''

'''
TO ADD:
- 
'''

import os

# ANSI Coloring for text
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
DEFAULT = '\033[0m'

# Print colored text
# print(f'{GREEN}Hello world!{DEFAULT}')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

p1_game_board = [[' ']*10]*10
p2_game_board = [[' ']*10]*10
x = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9}
y = [str(num) for num in range(1,11)]

def print_board(game_board):
    print(BLUE, end='')
    print(f"{'':<3}| A | B | C | D | E | F | G | H | I | J |")
    for count, row in enumerate(game_board):
        print(f'{"-"*45}')
        string = ''
        for cell in row:
            string = string + f' {cell} |'
        print(f"{count+1:>2} |{string}")
    print(DEFAULT)

# some function to update the board
def update_board():
    pass

# Sets up everything needed to run the game
def game_setup():
    ships = []

    while True:
        number_of_ships = input(f'How many ships should be used? (1-5):\n')
        try:
            number_of_ships = int(number_of_ships)
        except ValueError:
            print(f'Input must be a valid number!')
            continue
        if 1 <= number_of_ships <= 5:
            break
        else:
            print(f'Please select a valid number of ships between 1 and 5!\n')

    for i in range(number_of_ships):
        ships.append(f'1x{i+1}')

    # Player 1 game board setup
    for ship in ships:
        print_board(p1_game_board)
        print(f'Player 1, place your {ship} ship [A1]:\n')

    # Player 2 game board setup

def run_game():
    while True:
        clear_screen()
        print_board(p1_game_board)

        # Player 1 Attacks
        while True:
            attack_pos = input(f'{RED}Player 1{DEFAULT}: Which cell would you like to attack?):\n')
            if check_move(attack_pos, p2_game_board):
                break
        
        # confirm whether attack was valid and make changes

        # Player 2 Attacks
    
def check_move(attack_pos, game_board): # returns True if valid move
    if attack_pos[0].lower() in x.keys() and attack_pos[1:] in y:
        # check for already attacked positions
        if p2_game_board[x[attack_pos[0].lower()]][int(attack_pos[1:])-1] != ' ':
            print(f'Cell has already been attacked!')
            return False
        else:
            return True
    else:
        print(f'Please enter a valid cell to attack! [A1]')
        return False

def main():
    game_setup()
    run_game()

if __name__ == '__main__':
    main()