import copy
import random

BOARD_HEIGHT = 3
BOARD_WIDTH = 3  # Define board height and width.


def new_board():  # Creates a new board
    board = []  # Create an empty list
    for x in range(0, BOARD_WIDTH):
        column = []  # Creates 3 empty columns
        for y in range(0, BOARD_HEIGHT):
            column.append(None)  # Appends 'NONE' to columns
        board.append(column)  # Appends all three columns to board
    return board


def render(board):  # Takes current board and renders it to console
    rows = []
    for x in range(0, BOARD_HEIGHT):  # Iterating through 0 and BOARD_HEIGHT
        row = []
        for y in range(0, BOARD_WIDTH):  # For each iteration, iterating between 0 and BOARD_WIDTH
            row.append(board[x][y])  # For each iteration, appending the value from board (0--0-2,1--0-2,2--0-2)
        rows.append(row)  # Appending to the rows list each row created in the for loops, essentially creating a new
        # board to render.

    print()
    print('        Y  0 1 2')
    print('     X   -------')  # Printing outer border to the board (just design, no function)
    row_num = 0
    for row in rows:
        output_row = ''  # Iterating through each row in rows, and defining an output row for each iteration.
        for value in row:  # For each value in row
            if value is None:  # If the value is None (blank) it adds a whitespace to the output.
                output_row += ' '
            else:
                output_row += value  # If the value isn't none - it prints the value in that index.
        print("     %d  | %s |" % (row_num, ' '.join(output_row)))  # For each row number, we print a separation,
        # the number of the row and then we print the values of each output, separated by a space.
        row_num += 1  # Once the entire loop is finished, we go to the next iteration and add 1 to the row number.
    print('         -------\n')  # Printing outer border to the board (just design, no function)
    print()


def get_move(player):
    while True:
        try:  # Asks for X co-ordinates, then uses check_move() function to check if it is valid
            x = int(input(f"What is {player}'s X co-ordinates?: "))
            validx = check_move(x)
            if not validx:
                break  # If the move is valid (check_move() returned False) - move is logged, otherwise player asked
                # for input again.
            else:
                print('Invalid move!\n')  # If check_move() returned True, we print that the move is invalid, and for
                # the player to input a valid move
                continue
        except ValueError:  # If player typed no number, or we encountered another type of ValueError, we ask the
            # player to type a correct number.
            print('Enter a number 0-2!')
    while True:
        try:  # Does the same as X did.
            y = int(input(f"What is {player}'s Y co-ordinates?: "))
            validy = check_move(x, y)
            if not validy:
                break
            else:
                print('Invalid move!\n')
                continue
        except ValueError:
            print('Enter a number 0-2!')
    return int(x), int(y)  #


def check_move(x=None, y=None):
    if y is None:  # Checks that the move is between 0 and BOARD_WIDTH
        if 0 <= x < BOARD_WIDTH and None in previous_board[x]:
            return False
        else:
            return True
    elif 0 <= y < BOARD_HEIGHT and None in previous_board[x]:  # Checks the move is between 0 and BOARD_HEIGHT
        if 'X' in str(previous_board[x][y]) or 'O' in str(previous_board[x][y]):
            return True  # If there is already a move played in X,Y coords, it is invalid, therefor True is returned
        else:
            return False
    else:  # If move isn't valid, returns True
        return True


def make_move(previous_board, move_coords, playing):
    board = copy.deepcopy(previous_board)  # Copies current board to a new board, stored in variable 'board'
    if playing.lower() == 'x':  # If player is X, places X in coords
        board[move_coords[0]][move_coords[1]] = 'X'
    else:  # If player is O, places O in coords
        board[move_coords[0]][move_coords[1]] = 'O'
    return board


def update_board():
    # Updates current board with new board given by make_move()
    global previous_board
    previous_board = board


def get_player():
    # Asks for player 1 to be X/O
    while True:
        player = input("What would you like to play as? (O/X): ").upper()
        if player == 'X':
            print()
            print("PLAYER 1   |   PLAYER 2")
            print("   X       |      O\n")
            break
        elif player == 'O':
            print()
            print("PLAYER 1   |   PLAYER 2")
            print("   O       |      X\n")
            break
        else:
            print('Please select O/X!')
            continue
    return player


def switch_turn(playing):
    # Switches turns between player1 and player2 when called
    if playing.upper() == 'X':
        return 'O'
    else:
        return 'X'


def get_winner(board):
    for x in range(BOARD_HEIGHT):  # Check rows
        if None not in board[x] and board[x][0] == board[x][1] == board[x][2]:
            return True

    for x in range(BOARD_HEIGHT):  # Check columns
        for i in range(BOARD_WIDTH):
            if None not in [board[i][x]] and board[0][x] == board[1][x] == board[2][x]:
                return True

    # Check diagonals
    if board[1][1] is not None and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[1][1] is not None and board[2][0] == board[1][1] == board[0][2]:
        return True
    return False


def is_draw(board):
    for row in board:
        if None in row:
            return False  # If there is an empty square on the board - no draw.
    return True


def easy_bot():
    while True:
        x = random.randint(0, BOARD_HEIGHT-1)
        y = random.randint(0, BOARD_WIDTH-1)  # Picks a random number between 0 and BOARD HEIGHT,WIDTH
        valid_move = check_move(x, y)  # Checks if move is valid using check_move() function
        if not valid_move:
            break
        continue  # If the move is not valid, the computer will pick X,Y until it is valid.
    return (x, y)


def mode_selection():  # Has the player select the mode they want to play in
    try:
        while True:
            mode = input('Choose a mode (EASY/HARD/CO-OP): ')
            if mode.lower() == 'easy':
                return 0
            elif mode.lower() == 'hard':
                return 0  # Failed to implement AI
            elif mode.lower() == 'coop' or mode.lower() == 'co-op':
                return 2
            else:
                print("Invalid mode!\n")
    except Exception:
        print("Invalid mode!\n")



# GAME LOOP


playing = get_player()
mode = mode_selection()
previous_board = new_board()
if mode == 0:
    starting = random.randint(0, 1)
    if starting == 0:
        render(previous_board)
        print("You start!")
        while True:
            move_coords = get_move(playing)
            board = make_move(previous_board, move_coords, playing)
            update_board()
            if get_winner(board):
                render(board)
                print(f'WINNER IS {playing}!!!')
                break
            if is_draw(board):
                print("IT'S A DRAW!!!")
                break
            playing = switch_turn(playing)
            move_coords = easy_bot()
            print("BOT PLAYED -", '   X |',move_coords[0],'    Y|',move_coords[1])
            board = make_move(previous_board, move_coords, playing)
            update_board()
            render(board)
            if get_winner(board):
                print(f'WINNER IS {playing}!!!')
                break
            if is_draw(board):
                print("IT'S A DRAW!!!")
                break
            playing = switch_turn(playing)
            # PLAYER STARTS MOVE ORDER


    else:
        print("Computer starts!")
        while True:
            move_coords = easy_bot()
            print("BOT PLAYED -", '   X |', move_coords[0], '    Y|', move_coords[1])
            board = make_move(previous_board, move_coords, playing)
            update_board()
            render(board)
            if get_winner(board):
                print(f'WINNER IS {playing}!!!')
                break
            if is_draw(board):
                print("IT'S A DRAW!!!")
                break
            playing = switch_turn(playing)
            move_coords = get_move(playing)
            board = make_move(previous_board, move_coords, playing)
            update_board()
            if get_winner(board):
                print(f'WINNER IS {playing}!!!')
                break
            if is_draw(board):
                print("IT'S A DRAW!!!")
                break
            playing = switch_turn(playing)
            # COMPUTER STARTS MOVE ORDER


if mode == 2:
    render(previous_board)
    while True:
        move_coords = get_move(playing)
        board = make_move(previous_board, move_coords, playing)
        update_board()
        render(board)
        if get_winner(board):
            print(f'WINNER IS {playing}!!!')
            break
        if is_draw(board):
            print("IT'S A DRAW!!!")
            break
        playing = switch_turn(playing)
