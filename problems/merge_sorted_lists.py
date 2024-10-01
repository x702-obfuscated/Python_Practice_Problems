'''
Write a Python function merge(list1, list2) that merges two sorted lists into a single sorted list.

The function should:

Accept two sorted lists of integers, list1 and list2.
Return a new list containing all elements from both lists, sorted in ascending order.


merge([1, 3, 5], [2, 4, 6])  # Returns: [1, 2, 3, 4, 5, 6]
merge([], [1, 2, 3])         # Returns: [1, 2, 3]
merge([1, 2, 3], [])         # Returns: [1, 2, 3]
'''





































# DO NOT EDIT THE CODE BELOW###################
if __name__ == "__main__":
    from utils.test_tools import *
    from tests.test_merge_sorted_lists import * 

    try:
        tested_function =  merge
    except NameError as e:
        print(f"{e}\nDid you name your function correctly?")
        exit()
    
    run_tests(tested_function, tests, __file__)
###############################################