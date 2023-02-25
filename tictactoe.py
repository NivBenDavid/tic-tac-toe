import copy

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
            print("PLAYER 1   |   PLAYER 2")
            print("   X       |      O\n")
            player2 = 'O'
            break
        elif player == 'O':
            print("PLAYER 1   |   PLAYER 2")
            print("   O       |      X\n")
            player2 = 'X'
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
            return False
    return True


# To start a game        ----------------------
# get_player() = Asks the player to be either X or O, stores choice in 'playing'
# previous_board = new_board() - CREATE A NEW BOARD

# ORDER OF FUNCTIONS LOOP ---------------------
# move_coords = get_move() - GET MOVE FOR PLAYER
# board = make_move(previous_board, move_coords, player) - MAKE THE MOVE FOR PLAYER PLAYING
# update_board() = UPDATE CURRENT BOARD WITH NEW MOVE
# render(board) = RENDER THE CURRENT BOARD TO CONSOLE
# get_winner() = checks if the board has a winner.
# If there is a winner, game over, otherwise, switch_turn() switches between turns
# and the order of function is started over.
# ---------------------------------------------


playing = get_player()
previous_board = new_board()
render(previous_board)
while True:
    move_coords = get_move(playing)
    board = make_move(previous_board, move_coords, playing)
    update_board()
    render(board)
    if get_winner(board):
        print(f'WINNER IS {playing}!!!')
        break
    print(board)
    if is_draw(board):
        print("IT'S A DRAW!!!")
        break
    playing = switch_turn(playing)
