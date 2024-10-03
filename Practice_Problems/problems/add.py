''' 
Write a Python function add that accepts any number of integer arguments and returns their sum.

The function should:

Accept zero or more integer arguments.
Return the total sum of all the provided integers.


add(1, 2, 3)       # Return: 6
add(10, -5, 5)     # Return: 10
add()              # Return: 0
add(1, 2, 3, 4, 5) # Return: 15

'''












































# DO NOT EDIT THE CODE BELOW###################
if __name__ == "__main__":
    from utils.test_tools import run_tests

    try:
        run_tests(add, __file__)
    except NameError as e:
        print(f"{e}\nDid you name your function correctly?")
        exit()   
###############################################



