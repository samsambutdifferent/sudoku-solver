import numpy as np


def sudoku_solver(sudoku):
    """
    Solves a Sudoku puzzle

    Input
        sudoku : 9x9 numpy array
            Empty cells are designated by 0.

    Output
        9x9 numpy array of integers
            It contains the solution, if there is one. If there is no solution, all array entries should be -1.
    """
    n_su = np.array(sudoku)

    if not check_all_valid(n_su):
        return set_failed()

    passed = is_solved(n_su)

    if passed:
        return n_su
    else:
        return set_failed()


def is_solved(sudoku):
    """ recursive function called to solve sudoku puzzle
        
        Input
            sudoku : 9x9 numpy array
        Output
            bool 
    """
    emptys = find_emptys(sudoku)

    if emptys == None:
        return True

    next_empty, possibles = find_next_empty_with_possibles(sudoku, emptys)
    row_index, col_index = next_empty
     
    for v in possibles:
        sudoku[row_index][col_index] = v
        
        if is_solved(sudoku):
            return True
        
        sudoku[row_index][col_index] = 0

    return False


def find_emptys(sudoku):
    """ finds corrdinates of all empty, zero values
        Input
            sudoku : 9x9 numpy array
        Output
            two np arrays [row index,..],[col index,..]
    """
    emptys = np.nonzero(sudoku==0)
    if len(emptys[0]) == 0:
        return None
    else:
        return emptys


def find_next_empty_with_possibles(sudoku, emptys):
    """ finds the next empty spot and it's possibilities - will choose the one with the lowest number of possibilities
        Input
            sudoku : 9x9 numpy array
            emptys: [2 x numpy arrays]
        Output
           int, int : row index, col index,
    """
    empty_possible = []
    for i, value in enumerate(emptys[0]):
        empty_possible.append(
            [(emptys[0][i], emptys[1][i]),
            [x for x in range(1, 10) if is_valid(sudoku, x, emptys[0][i], emptys[1][i])]]
        )

    empty_possible.sort(key=lambda x: len(x[1]), reverse=False)
    return empty_possible[0][0], empty_possible[0][1]


def check_all_valid(sudoku):
    """ checks if all spaces are valid based off rules of sudoku 
        
        Input
            sudoku : 9x9 numpy array
        Output
            bool
    """
    for r_i, r in enumerate(sudoku):
        for c_i, c in enumerate(sudoku):

            value = sudoku[r_i][c_i]
            cpy = sudoku.copy()
            cpy[r_i][c_i] = 0

            if not is_valid(cpy, value, r_i, c_i):
                return False
    return True


def is_valid(sudoku, value, row_index, col_index):
    """ checks if individual space is valid
        
        Input
            sudoku : 9x9 numpy array
            value : int
            row_index : int
            col_index : int
        Output
            bool
    """
    if value == 0:
        return True

    if np.any(sudoku[row_index,:] == value):
        return False
    if np.any(sudoku[:,col_index] == value):
        return False
    if np.any(get_box_area(sudoku, row_index, col_index) == value):
        return False
    
    return True


def get_box_area(sudoku, row_index, col_index):
    """gets the 3x3 sub box area of current pos
        
        Input
            sudoku : 9x9 numpy array
            row_index : int
            col_index : int
        Output
            numpy array
    """
    r_c = np.ceil((row_index + 1)/3)
    subbox_row_limit = np.int(r_c)*3
    subbox_row_base = subbox_row_limit - 3

    c_c = np.ceil((col_index + 1)/3)
    subbox_col_limit = np.int(c_c)*3
    subbox_col_base = subbox_col_limit-3

    return sudoku[subbox_row_base:subbox_row_limit, 
                             subbox_col_base:subbox_col_limit]


def set_failed():
    """return failed sudoku
            returns:
                2d numpy array of -1
    """  
    return np.full((9, 9), -1)


if __name__ == "__main__":
    from time import process_time

    # Load sudokus
    # sudokus = np.load("data/hard_puzzle.npy")
    # solutions = np.load("data/hard_solution.npy")
    sudokus = np.load("data/easy_puzzle.npy")
    solutions = np.load("data/easy_solution.npy")
    # print()

    # fails on easy 0

    nom = 0
    # nom = 4
    #hard #4 == # time taken: 8.014639137

    # # Print the first 9x9 sudoku...
    print("First sudoku:")
    print(sudokus[nom], "\n")

    # # ...and its solution
    print("Solution of first sudoku:")
    print(solutions[nom])

    start_time = process_time()
    ans = sudoku_solver(sudokus[nom])
    endtime_time = process_time()
    print(f"time taken: {endtime_time-start_time}")

    print(ans,  "\n")

    print(ans == solutions[nom])

    x = sudokus[nom]

