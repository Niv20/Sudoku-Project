FINISH_FAILURE = -1
NOT_FINISH = 0
FINISH_SUCCESS = 1
HORIZONTAL_LEN = 28

example_board = [[5, 3, -1, -1, 7, -1, -1, -1, -1],
                 [6, -1, -1, -1, -1, -1, 1, -1, -1],
                 [-1, -1, 9, -1, -1, -1, -1, 6, -1],
                 [-1, -1, -1, -1, 6, -1, -1, -1, 3],
                 [-1, -1, -1, 8, -1, 3, -1, -1, 1],
                 [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                 [-1, 6, -1, -1, -1, -1, -1, -1, -1],
                 [-1, -1, -1, -1, 1, -1, -1, -1, -1],
                 [-1, -1, -1, -1, 8, -1, -1, -1, 9]]

perfect_board = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                 [6, 7, 2, 1, 9, 5, 3, 4, 8],
                 [1, 9, 8, 3, 4, 2, 5, 6, 7],
                 [8, 5, 9, 7, 6, 1, 4, 2, 3],
                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                 [9, 6, 1, 5, 3, 7, 2, 8, 4],
                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                 [3, 4, 5, 2, 8, 6, 1, 7, 9]]

impossible_board = [[5, 1, 6, 8, 4, 9, 7, 3, 2],
                    [3, -1, 7, 6, -1, 5, -1, -1, -1],
                    [8, -1, 9, 7, -1, -1, -1, 6, 5],
                    [1, 3, 5, -1, 6, -1, 9, -1, 7],
                    [4, 7, 2, 5, 9, 1, -1, -1, 6],
                    [9, 6, 8, 3, 7, -1, -1, 5, -1],
                    [2, 5, 3, 1, 8, 6, -1, 7, 4],
                    [6, 8, 4, 2, -1, 7, 5, -1, -1],
                    [7, 9, 1, -1, 5, -1, 6, -1, 8]]

bug_board = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
             [6, 7, 2, 1, 9, 5, 3, 4, 9],
             [1, 9, 8, 3, 4, 2, 5, 6, 7],
             [8, 5, 9, 7, 6, 1, 4, 2, 3],
             [4, 2, 6, 8, 5, 3, 7, 9, 1],
             [7, 1, 3, 9, 2, 4, 8, 5, 6],
             [9, 6, 1, 5, 3, 7, 2, 8, 4],
             [2, 8, 7, 4, 1, 9, 6, 3, 5],
             [3, 4, 5, 2, 8, 6, 1, 7, 9]]

interesting_board = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                     [6, 7, 2, 1, 9, 5, 3, 4, 8],
                     [1, 9, 8, 3, 4, 2, 5, 6, 7],
                     [-1, -1, -1, 7, 6, 1, 4, 2, 3],
                     [-1, -1, -1, 8, 5, 3, 7, 9, 1],
                     [-1, -1, -1, 9, 2, 4, 8, 5, 6],
                     [-1, -1, -1, -1, 3, 7, 2, 8, 4],
                     [-1, -1, -1, -1, 1, 9, 6, 3, 5],
                     [-1, -1, -1, -1, 8, 6, 1, 7, 9]]

board1 = [[5, -1, 4, -1, 7, -1, -1, 1, -1],
          [6, -1, 2, 1, -1, -1, 3, -1, -1],
          [1, -1, 8, -1, 4, -1, -1, 6, -1],
          [-1, 5, -1, -1, 6, -1, -1, 2, -1],
          [-1, 2, -1, 8, -1, 3, -1, -1, -1],
          [-1, -1, -1, -1, -1, 4, -1, 5, 6],
          [-1, 6, 1, 5, 3, 7, 2, 8, 4],
          [-1, 8, 7, -1, 1, 9, -1, 3, -1],
          [-1, -1, -1, 2, 8, -1, -1, -1, 9]]

board2 = [[-1, 6, -1, 4, 3, -1, -1, -1, 1],
          [5, -1, -1, -1, 7, -1, -1, -1, -1],
          [-1, 1, -1, 9, -1, -1, 8, -1, -1],
          [-1, -1, -1, -1, -1, 2, 3, -1, 9],
          [-1, 8, -1, -1, -1, -1, -1, 6, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [9, -1, 2, 3, -1, -1, -1, -1, 4],
          [-1, -1, 4, 7, 2, -1, -1, -1, 8]]

'''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                        Section 1                         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
'''
'''
This function recive a number and a list. 
If the number is different from -1, we add it to the list.
'''


def add_to_list(num: int, lst: list) -> list:
    if num != -1:
        lst.append(num)
    return lst


'''
This function return a list that contains all the numbers from a specific row.
It skips empty cells (represented by -1). This list may contain duplicates.
'''


def num_in_row(sudoko_board: list, row: int) -> list:
    lst = []
    for num in sudoko_board[row]:
        add_to_list(num, lst)
    return lst


'''
This function return a list that contains all the numbers from a specific column.
It skips empty cells (represented by -1). This list may contain duplicates.
'''


def num_in_col(sudoko_board: list, col: int) -> list:
    lst = []
    for i in range(9):
        add_to_list(sudoko_board[i][col], lst)
    return lst


'''
This function return a list that contains all the numbers from a specific square.
It skips empty cells (represented by -1). This list may contain duplicates.
'''


def num_in_square(sudoko_board: list, row: int, col: int) -> list:
    lst = []
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            add_to_list(sudoko_board[i][j], lst)
    return lst


'''
This function return list that contains all the numbers from 
a specific row, column, and 3x3 square in a Sudoku board.
This list may contain duplicates.
'''


def get_numbers_in_region(sudoko_board: list, row: int, col: int) -> list:
    lst = []
    lst += num_in_row(sudoko_board, row)
    lst += num_in_col(sudoko_board, col)
    lst += num_in_square(sudoko_board, row, col)
    return lst


'''
This function finds and return list that contain all 
the possible numbers for a given spot in the Sudoku board.
'''


def options(sudoko_board: list, loc: tuple):
    # Get the row and column from the tuple "loc"
    row, col = loc

    # Edge case: the spot already has a number
    if sudoko_board[row][col] != -1:
        return []

    # Create a list of valid numbers for the given Sudoku cell
    cur_set = set(get_numbers_in_region(sudoko_board, row, col))
    option_lst = list({i for i in range(1, 10)}.difference(cur_set))

    # If there are no numbers left in the list, return None
    if option_lst == []:
        return None

    # If you get here, that mean there are still options left
    return option_lst  # so return the list of possible numbers


'''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                        Section 2                         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
'''
'''
The function receives a Sudoku board and returns a new board of the same size, 
where each cell contains a list of possible numbers that can be placed in that cell.
'''


def possible_digits(sudoku_board: list) -> list:
    # Creating an Empty Sudoku Board
    possible_board = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append([])
        possible_board.append(row)

    # For each cell in the empty board, we will use a function from Section 1.
    for i in range(9):
        for j in range(9):
            possible_board[i][j] = options(sudoku_board, (i, j))

    # Return the
    return possible_board


'''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                        Section 3                         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
'''
'''
The function checks if there are any duplicate values in a list.
It compares the length of the original list with the length of the set 
(which removes duplicates). If the lengths are different - 
it means there were duplicates in the list.
'''


def are_there_duplicates(lst: list) -> bool:
    return len(lst) != len(set(lst))


'''
This function checks whether a given Sudoku board is legal or not.
A board is considered illegal if there are duplicate numbers 
in any row, column, or 3x3 square. The function returns False 
if any duplicates are found and True otherwise.
'''


def is_legal_board(sudoku_board: list, possibilities: list) -> bool:
    # Check if there is "None" in possibilities borad
    for row in range(9):
        for col in range(9):
            if possibilities[row][col] == None:
                return False

    # Check for duplicates in each row
    for row in range(9):
        if are_there_duplicates(num_in_row(sudoku_board, row)):
            return False

    # Check for duplicates in each column
    for col in range(9):
        if are_there_duplicates(num_in_col(sudoku_board, col)):
            return False

    # Check for duplicates in each square
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if are_there_duplicates(num_in_square(sudoku_board, row, col)):
                return False

    # If we got here, that means no duplicates appeared in the board
    return True


'''
This function updates the board by filling cells with only one possibility.
The function returns the updated `possibilities` board.
'''


def fill_cells_with_single_option(sudoku_board: list, possibilities: list) -> list:
    # We will use these indexes to run on the board
    i, j = 0, 0
    while i < 9 and possibilities[i][j] != None:
        # If a cell has exactly one possible value, so:
        if len(possibilities[i][j]) == 1:
            sudoku_board[i][j] = possibilities[i][j][0]  # update the board
            possibilities = possible_digits(sudoku_board)  # Recalculate possibilities
            i, j = 0, 0  # Reset indices to start from the beginning
            continue  # Move to the next iteration

        # If we got here, that means this cell has more than one option, so:
        j = (j + 1) % 9  # Move to the next cell
        if j == 0: i += 1  # Wrap around to the next row if necessary

    return possibilities


'''
This function checks whether the Sudoku board is fully solved.
It determines if all cells in the `possibilities` list are empty, 
indicating that no further possibilities are available, meaning the board is complete.
WARNING: The function assumes that the borad is legal!
'''


def is_finish_board(possibilities: list) -> bool:
    for i in range(9):
        for j in range(9):
            # If this cell still has possibilities, the board is not finished
            if len(possibilities[i][j]) != 0:
                return False

    # If you get here, all cells are empty
    return True


'''
This function finds the cell with the fewest possible (excluding cells with 0 options). 
The function returns the tuple of the row and column of the above cell
'''


def find_cell_with_fewest_options(possibilities: list) -> tuple:
    # Start with an initial "high" value for the minimum and default row/column
    min_len = 10  # A number larger than any valid cell length (0-9)
    row, col = -1, -1  # Default values if no suitable cell is found

    # Go through each cell in the Sudoku board
    for i in range(9):
        for j in range(9):

            # Get the length of the possibilities for the current cell
            cur_len = len(possibilities[i][j])

            # Skip cells with zero possibilities
            if cur_len == 0:
                continue

            # If a smaller length is found - update the minimum length and cell position
            if cur_len < min_len:
                min_len = cur_len
                row, col = i, j

    # Return the result as a tuple
    return row, col


'''
This function represents a single stage in solving the Sudoku board.
It performs three tasks:
    1. Fills cells with a single possible value.
    2. Checks if the board is still legal after the update.
    3. Determines if the board is complete or still requires solving.

The function returns A tuple containing: 
    I) Status constant (FINISH_FAILURE, FINISH_SUCCESS, or NOT_FINISH).
    II) A tuple indicating the next cell to work on or `(-1, -1)` if finished/illegal.
'''


def one_stage(sudoku_board: list, possibilities: list) -> tuple:
    # 1. Fill cells with a single possible value and update possibilities
    possibilities = fill_cells_with_single_option(sudoku_board, possibilities)

    # 2. Check if the board is legal
    if not is_legal_board(sudoku_board, possibilities):
        return FINISH_FAILURE, (-1, -1)

    # 3a. Check if the board is fully solved
    if is_finish_board(possibilities):
        return FINISH_SUCCESS, (-1, -1)

    # 3b. If the board isn't finished, find the cell with fewest options
    return NOT_FINISH, find_cell_with_fewest_options(possibilities)


'''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                        Section 4                         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
'''
'''
This function takes a list of options and x, y coordinates and prints them
'''


def print_the_potions(options_to_choose_from: list, x: int, y: int) -> None:
    # Sort the options in ascending order just for fun
    options_to_choose_from.sort()

    # Print a message asking the user to choose a number
    print("-" * HORIZONTAL_LEN)
    print("For the cell at (", x, ",", y, ")", sep="")
    print("choose a number: ", end="")

    # Loop through the sorted options and print them
    for i in range(len(options_to_choose_from)):
        if i < len(options_to_choose_from) - 1:
            print(options_to_choose_from[i], end=", ")
        else:
            print(options_to_choose_from[i])


'''
This function repeatedly ask the user for input until a valid number is entered. 
A valid number is one that is found in the provided list of options. 
Once a valid input is received, the function returns the entered number.
'''


def ask_for_input(options_to_choose_from: list) -> int:
    user_choice = int(input())

    '''
    ┌──────────────────────────────────────────────────┐
    │██████████████████████████████████████████████████│
    │██████████████████████████████████████████████████│
    │███████████████This is Maor's task████████████████│
    │██████████████████████████████████████████████████│
    │██████████████████████████████████████████████████│
    │██████████████████████████████████████████████████│
    └──────────────────────────────────────────────────┘

    צריך לוודא שהקלט שהמתמש מכניס הוא בכלל נמצא ברשימת האפשרויות
    כל עוד הוא מזין שטויות, לבקש ממנו שוב ושוב להזין
    כדאי גם להדפיס הודעת שגיאה מתאימה (יעני, תקליד שוב)
    '''

    return user_choice


'''
This function try to fill the sudoku board by repeatedly solving individual stages. 
The function continues until the board is successfully filled or get error. 
Each iteration, the function print the cell with the fewest options remaining, 
and ask the user to choose the number they want to place in it.
The function returns either FINISH_SUCCESS or FINISH_FAILURE based on the outcome.
'''


def fill_board(sudoku_board: list, possibilities: list):
    # Continuously try to fill the board
    while True:

        # Call one_stage to perform a step in solving the Sudoku
        status, (x, y) = one_stage(sudoku_board, possibilities)

        # If the status indicates a failure to finish, return FINISH_FAILURE
        if status == FINISH_FAILURE:
            return FINISH_FAILURE

        # If the status indicates success, return FINISH_SUCCESS
        if status == FINISH_SUCCESS:
            return FINISH_SUCCESS

        # If you get here, that means the board is legal and we can still play

        # Calc the list of possible digits for the cell (x, y)
        options_to_choose_from = possible_digits(sudoku_board)[x][y]

        # Display the available options for the user to choose from
        print_the_potions(options_to_choose_from, x, y)

        # And ask the user to choose a number from the list of options
        user_choice = ask_for_input(options_to_choose_from)

        # Update the Sudoku and possibilities bord the with the chosen number
        sudoku_board[x][y] = user_choice
        possibilities = possible_digits(sudoku_board)


print(fill_board(board2, possible_digits(board2)))

'''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                        Section 5                         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
'''


def create_random_board(sudoku_board: list):
    pass


'''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                        Section 6                         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
'''
'''
This function print a 9x9 Sudoku board.
Empty cells (represented by -1) will be displayed as blank spaces.
'''


def print_board(sudoku_board: list) -> None:
    # Loop through each row of the board
    for i in range(9):

        # Print a horizontal divider line between rows
        print("-" * HORIZONTAL_LEN)

        # Start each row with a vertical line
        print("|", end="")

        # Loop through each column in the current row
        for j in range(9):

            # Print the cell value (replacing -1 with a blank space)
            if sudoku_board[i][j] != -1:
                print(sudoku_board[i][j], "|", end="")
            else:
                print("  |", end="")

        # Move to the next line after finishing the row
        print("")

    # Print the bottom horizontal divider line after the last row
    print("-" * HORIZONTAL_LEN)


'''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                        Section 7                         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
'''


def print_board_to_file(sudoku_board, file_name):
    pass
