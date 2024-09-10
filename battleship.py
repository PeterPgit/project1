'''
Name: Project 1 - Battleship Game
Description: Simple Battleship game made in python
Inputs: 
Outputs: 
Collaborators/Sources: 
Michael Oliver, Peter Pham, Jack Youngquist, Andrew Uriell, Ian Wilson, ChatGPT
Aug 31 2024
'''

'''
TO ADD:
- case checking in ship placement, tracking ships of each player i.e. if one of player 1's ships are destroyed, check for winner, 
- bug in attack function where the cell attacked does not always match the input
- bug where bad input for H or V will crash program
'''

import os

# ANSI Coloring for text
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
DEFAULT = '\033[0m'

p1_game_board = [[' ']*10 for _ in range(10)]
p1_attack_board = [[' ']*10 for _ in range(10)] #track where player one has fired from their pov
p2_game_board = [[' ']*10 for _ in range(10)]
p2_attack_board = [[' ']*10 for _ in range(10)]
x = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9}
y = [str(num) for num in range(1,11)]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_single_board(game_board):
    print(BLUE, end='')
    print(f"{'':<3}| A | B | C | D | E | F | G | H | I | J |")
    for count, row in enumerate(game_board):
        print(f'{"-"*45}')
        string = ''
        for cell in row:
            string = string + f' {cell} |'
        print(f"{count+1:>2} |{string}")
    print(DEFAULT)

def print_full_board(game_board, attack_board):
    pass

# some function to update the board
def update_board():
    pass

def query_ship_placement(game_board, player):
    for ship, size in ships:
        while True:
            print_single_board(game_board)
            print(f'Player {player}, place your {ship} of size {size} [e.g., A1]:')
            start_pos = input('Enter the starting position:\n').lower()

            if size != 1:
                direction = input('Enter direction (H for horizontal, V for vertical):\n').lower()
                if direction == 'h':
                    horiz_dir = input('Enter horizontal direction (R for right, L for left):\n').lower()
                    vert_dir = None
                elif direction == 'v':
                    horiz_dir = None
                    vert_dir = input('Enter vertical direction (U for up, D for down):\n').lower()
                else:
                    print(f"Invalid direction input! Please enter 'H' for horizontal or 'V' for vertical.") # If invalid input, reprompt
                    continue
                
                if validate_ship_placement(start_pos, size, game_board, direction, horiz_dir, vert_dir):
                    place_ship(start_pos, size, game_board, direction, horiz_dir, vert_dir)
                    break
                else:
                    print(f'Invalid placement for {ship}. Try again.')
            else:
                if validate_ship_placement(start_pos, size, game_board):
                    place_ship(start_pos, size, game_board)
                    break
                else:
                    print(f'Invalid placement for {ship}. Try again.')

def validate_ship_placement(start_pos, size, game_board, direction=None, horiz_dir=None, vert_dir=None):
    if start_pos[0] in x and start_pos[1:] in y: # Verifies position is within the board dimensions
        col = x[start_pos[0]]  # Convert column letter to index
        row = int(start_pos[1:]) - 1  # Convert row number to index (0-based)

        if direction == 'h':  # Horizontal placement
            if horiz_dir == 'r':
                if col + size > 10:  # Out of bounds in column direction
                    return False
                for i in range(size):
                    if game_board[row][col + i] != ' ':  # Check overlap
                        return False
            elif horiz_dir == 'l':
                if col - size + 1 < 0:  # Out of bounds in column direction
                    return False
                for i in range(size):
                    if game_board[row][col - i] != ' ':  # Check overlap
                        return False
            elif horiz_dir != 'r' and horiz_dir != 'l': # Check for bad input. If there is bad input, reprompt user
                return False
            return True
        #need to check for good input

        elif direction == 'v':  # Vertical placement
            if vert_dir == 'd':
                if row + size > 10:  # Out of bounds in row direction
                    return False
                for i in range(size):
                    if game_board[row + i][col] != ' ':  # Check overlap
                        return False
            elif vert_dir == 'u':
                if row - size + 1 < 0:  # Out of bounds in row direction
                    return False
                for i in range(size):
                    if game_board[row - i][col] != ' ':  # Check overlap
                        return False
            elif vert_dir == 'd' and vert_dir == 'u': # Check for bad input. If there is bad input, reprompt user
                return False
            return True
        
        # Ships of size 1
        elif direction == None:
            return True
        
        raise BaseException(f'Unable to validate ship placement: {direction} {horiz_dir} {vert_dir}')
    else:
        return False

def place_ship(start_pos, size, game_board, direction=None, horiz_dir=None, vert_dir=None):
    col = x[start_pos[0]]  # Convert column letter to index
    row = int(start_pos[1:]) - 1  # Convert row number to index (0-based)

    if direction == 'h':  # Horizontal placement
        if horiz_dir == 'r':
            for i in range(size):
                game_board[row][col + i] = 'S'
        elif horiz_dir == 'l':
            for i in range(size):
                game_board[row][col - i] = 'S'

    elif direction == 'v':  # Vertical placement
        if vert_dir == 'd':
            for i in range(size):
                game_board[row + i][col] = 'S'
        elif vert_dir == 'u':
            for i in range(size):
                game_board[row - i][col] = 'S'

    # ships of size 1
    elif direction == None:
        game_board[row][col] = 'S'

def check_attack(attack_pos, game_board): # returns True if valid move
    if attack_pos[0] in x and attack_pos[1:] in y:
        attack_col = x[attack_pos[0]]
        attack_row = int(attack_pos[1:]) - 1
        # check for already attacked positions
        if game_board[attack_row][attack_col] == ' ' or 'S':
            return True
        else:
            print(f'Cell has already been attacked!')
            return False
    else:
        print(f'Please enter a valid cell to attack! [A1]')
        return False

def game_setup():
    # Ask for the number of ships
    while True:
        try:
            number_of_ships = int(input('How many ships should be used? (1-5):\n'))
            if 1 <= number_of_ships <= 5:
                break
            else:
                print(f'Please select a valid number of ships between 1 and 5!\n')
        except ValueError:
            print(f'Input must be a valid number!')

    ship_sizes = {"Liberty": 1, "Destroyer": 2, "Submarine": 3, "Battleship": 4, "Carrier": 5}
    global ships
    ships = list(ship_sizes.items())[:number_of_ships]  # Only take the required number of ships
    
    # Player 1 game board setup
    query_ship_placement(p1_game_board, 1)
    clear_screen()

    # Player 2 game board setup
    query_ship_placement(p2_game_board, 2)

def run_game():
    while True:
        clear_screen()
        print(f"{RED}Attack board:{DEFAULT}")
        print_single_board(p1_attack_board)
        print(f"{GREEN}Your board:{DEFAULT}")
        print_single_board(p1_game_board)

        # Player 1 Attacks
        while True:
            attack_pos = input(f'{RED}Player 1{DEFAULT}: Which cell would you like to attack? [A1]:\n').lower()
            attack_col = x[attack_pos[0]]
            attack_row = int(attack_pos[1:]) - 1
            if check_attack(attack_pos, p2_game_board):
                if p2_game_board[attack_row][attack_col] == 'S':
                    shot = "Hit!"
                    p2_game_board[attack_row][attack_col] = f'{RED}X{BLUE}'
                    p1_attack_board[attack_row][attack_col] = f'{RED}X{BLUE}'
                else:
                    shot = "Miss"
                    p2_game_board[attack_row][attack_row] = f'{RED}O{BLUE}'
                    p1_attack_board[attack_row][attack_row] = f'{RED}O{BLUE}'
                break
        clear_screen()
        print(f"{RED}Attack board:{DEFAULT}")
        print_single_board(p1_attack_board)
        print(f"{GREEN}Your board:{DEFAULT}")
        print_single_board(p1_game_board)
        print(shot)
        input("Press enter to end turn: ")
        clear_screen()
        input("Press enter to begin turn player 2: ")
        clear_screen()
        print(f"{RED}Attack board:{DEFAULT}")
        print_single_board(p2_attack_board)
        print(f"{GREEN}Your board:{DEFAULT}")
        print_single_board(p2_game_board)
        
        # confirm whether attack was valid and make changes

        # Player 2 Attacks
        while True:
            attack_pos = input(f'{RED}Player 2{DEFAULT}: Which cell would you like to attack? [A1]:\n').lower()
            attack_col = x[attack_pos[0]]
            attack_row = int(attack_pos[1:]) - 1
            if check_attack(attack_pos, p1_game_board):
                if p1_game_board[attack_row][attack_col] == 'S':
                    shot = "Hit!"
                    p1_game_board[attack_row][attack_col] = f'{RED}X{BLUE}'
                    p2_attack_board[attack_row][attack_col] = f'{RED}X{BLUE}'
                else:
                    shot = "Miss"
                    p1_game_board[attack_row][attack_col] = f'{RED}O{BLUE}'
                    p2_attack_board[attack_row][attack_col] = f'{RED}O{BLUE}'
                break
        clear_screen()
        print(f"{RED}Attack board:{DEFAULT}")
        print_single_board(p2_attack_board)
        print(f"{GREEN}Your board:{DEFAULT}")
        print_single_board(p2_game_board)
        print(shot)
        end_turn = input("Press Enter to end turn: ")
        clear_screen()
        player1_ready = input("Press Enter to begin turn player 1: ")

def main():
    game_setup()
    run_game()

if __name__ == '__main__':
    main()
