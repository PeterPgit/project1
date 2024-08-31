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
- Input validity checks
'''

# ANSI Coloring for text
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
DEFAULT = '\033[0m'

# Print colored text
# print(f'{GREEN}Hello world!{DEFAULT}')

p1_game_board = [[' ']*10]*10
p2_game_board = [[' ']*10]*10

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


def main():
    game_setup()
    # print_board(p1_game_board)

if __name__ == '__main__':
    main()