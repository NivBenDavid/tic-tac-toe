# tic-tac-toe


A simple game of Tic Tac Toe coded in Python, coded after ~1 week of experience.
To play the game, run the code, you will be prompted to select O/X -
after selecting your player you will be prompted to choose an X co-ordinate, choose one from 0-2
depending on where you'd like to place your move on the board, afterwards, do the same for the Y co-ordinate.

You will then be prompted to select the coordinates for the second player, do so just as you did the first.
The game will then go on in a loop until a winner is crowned, or a draw is reached.

This game was my first 'major' project I've worked on, took me about a day of tearing my hairs out to get it done, I
plan on adding a single-player feature, to be able to play against the computer, which will select X/O randomly between 0-2.

However a bigger goal of mine is to code up an AI that will play the game over many iterations, and will eventually be practically unbeatable.
This is a bigger project that I strive to achieve in the coming days/weeks. But I first need to figure out
how this whole 'AI' thing works.

About the code ---
The code is made up of mostly functions that work together to create the game, first function being ran
has the player selecting between X/O using simple input variables.
The code next generates an empty board, by having a for loop run between 0 and the BOARD_HEIGHT,
predetermined by a variable at the beginning of the code, for each iteration - another for loop is being executed
between 0 and BOARD_WIDTH, for each outer loop a column is being created, and for each inner loop, three None values
are being appended to the current column, totalling to a list of 3 lists, with 3 None values within each list.

The game then uses the render function to render the board out to the console, the render function essentially creates
a new board using the values of the new_board() function but it prints it in a way that is nicer to look at, with padding
and indicators as to which index points to which square. This function is being used each time a turn is played, after being
updated by the update_board() function, which just updates the previous board to the new one.

After that, the player is being prompted to input their move using the get_move() function, within the get_move() function resides the check_move()
function which takes the player's input and puts it through a series of tests to check whether it is valid or not, tests like
is the move between 0-2? is the move a digit? is the move in an empty space? If all of these are true, the move is valid and function will return False,
which will break the loop and move on to the next function which will update the board with the given move, the board will then be printed on to the console
with the render() function to show the player the move they have played.

The program will then check the win conditions, if it finds that a win has been reached, the game loop will break and the winner will be crowned and displayed.
If a win hasn't been reached the program will check for a draw. If neither a win or a draw has been reached, the program will call the switch_turn() function
which will give player2 his turn, looping the functions until a draw or win is present on the board.

Please note that all the functions are explained thoroughly in the program itself with comments, so if you want to know how a certain function works,
you can take a look at the program itself.
Thank you for reading.
