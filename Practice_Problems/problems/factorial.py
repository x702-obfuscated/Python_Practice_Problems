'''
Write a Python function factorial(n) that computes the factorial of a non-negative integer n.

The function should:

Accept a single non-negative integer n.
Return the factorial of n, which is the product of all positive integers up to n.

factorial(5)  # Return: 120
factorial(0)  # Return: 1
factorial(1)  # Return: 1

'''



































# DO NOT EDIT THE CODE BELOW###################
if __name__ == "__main__":
    from utils.test_tools import run_tests

    try:
        run_tests(factorial, __file__)
    except NameError as e:
        print(f"{e}\nDid you name your function correctly?")
        exit()
###############################################
