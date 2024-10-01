'''
Write a Python function is_palindrome(s) that checks if a given string s is a palindrome. 
Punctuation, case and spaces should be ignored when checking if the string is a palindrome.

The function should:

Accept a string s.
Return True if s is a palindrome (reads the same forwards and backwards) and False otherwise.



is_palindrome("racecar")                        # Returns: True
is_palindrome("hello")                          # Returns: False
is_palindrome("A man a plan a canal Panama")    # Returns: True
'''


































# DO NOT EDIT THE CODE BELOW###################
if __name__ == "__main__":
    from utils.test_tools import *
    from tests.test_palindrome import * 

    try:
        tested_function =  is_palindrome
    except NameError as e:
        print(f"{e}\nDid you name your function correctly?")
        exit()
    
    run_tests(tested_function, tests, __file__)
###############################################