'''
2D List Matrix Addition
Write a function add_matrices that accepts two 2D lists of integers (matrices) of the same dimensions 
and returns a new 2D list where each element is the sum of the corresponding elements in matrix1 and matrix2.

Example:

[1 2 3]   +     [3 4 5]    =      [4  6  8 ]
[4 5 6]         [6 7 8]           [10 12 14] 


Precondition:
    matrix1 and matrix2 will only be 2d lists that contain integer values. 

The function should:
    Accept two 2D lists matrix1 and matrix2, both with the same dimensions.
    Add the corresponding elements from the two matrices and return the resulting 2D list.
    If the matrices are not of the same dimensions, return "Matrices must have the same dimensions".

Example Calls:
    add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])                # Return: [[6, 8], [10, 12]]
    add_matrices([[1]], [[2]])                                      # Return: [[3]]
    add_matrices([[1, 2, 3], [4, 5, 6]], [[6, 5, 4], [3, 2, 1]])    # Return: [[7, 7, 7], [7, 7, 7]]
    add_matrices([[0, 0], [0, 0]], [[0, 0], [0, 0]])                # Return: [[0, 0], [0, 0]]
    add_matrices([[1, 2], [3, 4]], [[1, 2]])                        # Return: "Matrices must have the same dimensions"
'''












































# DO NOT EDIT THE CODE BELOW###################
if __name__ == "__main__":
    from utils.test_tools import run_tests

    try:
        run_tests(add_matrices, __file__)
    except NameError as e:
        print(f"{e}\nDid you name your function correctly?")
        exit()   
###############################################