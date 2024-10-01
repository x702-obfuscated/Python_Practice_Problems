'''
Write a Python function count_vowels(s) that counts the number of vowels in a given string s.

The function should:

Accept a string s.
Return the total count of vowels (a, e, i, o, u) in the string.


count_vowels("hello")           # Returns: 2
count_vowels("programming")     # Returns: 3
count_vowels("AEIOU")           # Returns: 5
'''


def count_vowels(s: str) -> int:
    # Define a set of vowels
    vowels = set("aeiouAEIOU")
    
    # Use a generator expression to count vowels
    return sum(1 for char in s if char in vowels)

































# DO NOT EDIT THE CODE BELOW###################
if __name__ == "__main__":
    from utils.test_tools import *
    from tests.test_count_vowels import * 

    try:
        tested_function =  count_vowels
    except NameError as e:
        print(f"{e}\nDid you name your function correctly?")
        exit()
    
    run_tests(tested_function, tests, __file__)
###############################################