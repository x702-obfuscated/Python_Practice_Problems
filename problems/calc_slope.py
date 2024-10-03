'''
Calcate Slope
Write a function calc_slope(*points) that accepts any number of integer arguments representing the coordinates of points and 
calculates the slope between the first two points provided. 
The points are expected to be in the format (x1, y1, x2, y2).

The function should:
    Accept zero or more integer arguments.
    Return the slope between the first two points provided.
    Return "insufficient points" if fewer than four arguments are provided.
    Return "undefined" if the line between the two points is vertical (i.e., x1 == x2).

The slope of a line is given by the formula:

    slope = y2-y1 / x2-x1


Example Calls

    calc_slope(2, 0, 1, 2)           # Return: 2.0
    calc_slope(-1, 0, 0, 1)          # Return: 0.0
    calc_slope(1, 2, 1, 5)           # Return: "undefined"
    calc_slope(0, 0, 4, 8)           # Return: 2.0
    calc_slope(1, 2)                 # Return: "insufficient points"

'''



























# DO NOT EDIT THE CODE BELOW###################
if __name__ == "__main__":
    from utils.test_tools import run_tests

    try:
        run_tests(calc_slope, __file__)
    except NameError as e:
        print(f"{e}\nDid you name your function correctly?")
        exit()
###############################################