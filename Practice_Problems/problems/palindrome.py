'''
Write a Python function is_palindrome that accepts a string and checks if that string is a palindrome. 
Punctuation, case and spaces should be ignored when checking if the string is a palindrome.

The function should:

Accept a string argument.
Return True if the string is a palindrome (reads the same forwards and backwards) and False otherwise.



is_palindrome("racecar")                        # Returns: True
is_palindrome("hello")                          # Returns: False
is_palindrome("A man a plan a canal Panama")    # Returns: True
'''


































# DO NOT EDIT THE CODE BELOW###################
if __name__ == "__main__":
    from utils.test_tools import run_tests

    try:
        run_tests(is_palindrome, __file__)
    except NameError as e:
        print(f"{e}\nDid you name your function correctly?")
        exit()
    
    
###############################################