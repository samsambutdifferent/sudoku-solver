import numpy as np
from solve_sudoku import sudoku_solver


def print_board(bo):    
    """delete this
    """
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


if __name__ == "__main__":
    from time import process_time
    difficulties = ['very_easy', 'medium', 'easy', 'hard']
    failed = []
    total_length = 0
    total_count = 0

    for difficulty in difficulties:
        print(f"Testing {difficulty} sudokus")
        
        sudokus = np.load(f"data/{difficulty}_puzzle.npy")
        solutions = np.load(f"data/{difficulty}_solution.npy")
        total_length += len(sudokus)
        total_time = 0

        count = 0
        for i in range(len(sudokus)):
            sudoku = sudokus[i].copy()
            print(f"This is {difficulty} sudoku number", i)

            start_time = process_time()
            your_solution = sudoku_solver(sudoku)
            end_time = process_time()
            
            time = end_time - start_time
            
            print("Is your solution correct?")
            if np.array_equal(your_solution, solutions[i]) and time <= 20.0:
                print("Yes! Correct solution.")
                count += 1
            elif time > 20.0:
                print("Yes, but the it is out of time.")
                failed.append({"solution": solutions[i], "difficulty": difficulty, "index": i, "time": time})
            else:
                print("No thats wrong")
                print(print_board(solutions[i]))
                failed.append({"solution": solutions[i], "difficulty": difficulty, "index": i, "time": time})
            
            print(f"original: ")
            print(print_board(sudoku))
            print("the correct solution is:")
            print(print_board(solutions[i]))
            print(f"solution: ")
            print(print_board(your_solution))
            
            print("This sudoku took", time, "seconds to solve.\n")
            total_time += time
            print("")
            print(f"total passed{total_count}/{total_length}")
            print(f"total time passed{total_time}")
            print("")
        
        total_count += count

        print("")
        print(f"total passed{total_count}/{total_length}")
        print(f"total time passed{total_time}")
        print("")

        print(f"{count}/{len(sudokus)} {difficulty} sudokus correct")
        #if count < len(sudokus):
            #break: 
    print("")
    print(f"total passed{total_count}/{total_length}")
    print(f"total time passed{total_time}")
    print("")
    
    for fail in failed:
        print(f'solutions: {print_board(fail["solution"])}, difficulty: {fail["difficulty"]}, index: {fail["index"]}, time: {fail["index"]}')
