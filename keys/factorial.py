'''
Write a Python function factorial(n) that computes the factorial of a non-negative integer n.

The function should:

Accept a single non-negative integer n.
Return the factorial of n, which is the product of all positive integers up to n.

print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
print(factorial(1))  # Output: 1

'''


def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n-1)


# for n in range(0, 26):
#     print(f"({factorial(n)},{n}),")


































# DO NOT EDIT THE CODE BELOW###################
if __name__ == "__main__":
    from utils.test_tools import *
    from tests.test_factorial import * 

    try:
        tested_function =  factorial
    except NameError as e:
        print(f"{e}\nDid you name your function correctly?")
        exit()
    
    run_tests(tested_function, tests, __file__)
###############################################
