'''
Write a Python function fibonacci(n) that returns the n-th number in the Fibonacci sequence.

The function should:

Accept a non-negative integer n.
Return the n-th Fibonacci number, where the sequence starts with 0 and 1.


fibonacci(0)  # Return: 0
fibonacci(1)  # Return: 1
fibonacci(5)  # Return: 5

'''


def fibonacci(n: int) -> int:
    # Validate the input
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Initialize variables for the first two Fibonacci numbers
    a, b = 0, 1
    
    # Calculate Fibonacci using iteration
    for _ in range(2, n + 1):
        a, b = b, a + b  # Update to the next Fibonacci numbers
    
    return b



# for x in range(0,100):
#     print(f"({fibonacci(x)}, {x}),")
































# DO NOT EDIT THE CODE BELOW###################
if __name__ == "__main__":
    from utils.test_tools import *
    from tests.test_fibonacci import * 

    try:
        tested_function =  fibonacci
    except NameError as e:
        print(f"{e}\nDid you name your function correctly?")
        exit()
    
    run_tests(tested_function, tests, __file__)
###############################################