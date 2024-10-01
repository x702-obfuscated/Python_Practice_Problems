'''
Write a Python function add(*args) that accepts any number of integer arguments and returns their sum.

The function should:

Accept zero or more integer arguments.
Return the total sum of all the provided integers.


print(add(1, 2, 3))        # Output: 6
print(add(10, -5, 5))      # Output: 10
print(add())               # Output: 0
print(add(1, 2, 3, 4, 5))  # Output: 15

'''











































# DO NOT EDIT THE CODE BELOW###################
if __name__ == "__main__":
    from utils.test_tools import *
    from tests.test_add import * 

    try:
        tested_function =  add
    except NameError as e:
        print(f"{e}\nDid you name your function correctly?")
        exit()
    
    run_tests(tested_function, tests, __file__)
###############################################



