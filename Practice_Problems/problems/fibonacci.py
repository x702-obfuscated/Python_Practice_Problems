'''
Write a Python function fibonacci(n) that returns the n-th number in the Fibonacci sequence.

The function should:

Accept a non-negative integer n.
Return the n-th Fibonacci number, where the sequence starts with 0 and 1.


fibonacci(0)  # Return: 0
fibonacci(1)  # Return: 1
fibonacci(5)  # Return: 5

'''

































# DO NOT EDIT THE CODE BELOW###################
if __name__ == "__main__":
    from utils.test_tools import run_tests

    try:
        run_tests(fibonacci, __file__)
    except NameError as e:
        print(f"{e}\nDid you name your function correctly?")
        exit()
    
    
###############################################