'''
Write a Python function is_leap_year(year) that takes an integer year as input and returns True if the year is a leap year and False if it is not.

A year is a leap year if:

    It is divisible by 4, and:
    It is not divisible by 100, unless:
    It is also divisible by 400.

For example:

2020 is a leap year (divisible by 4, not divisible by 100).
1900 is not a leap year (divisible by 100, but not by 400).
2000 is a leap year (divisible by 400).

print(is_leap_year(2020))  # Output: True
print(is_leap_year(1900))  # Output: False
print(is_leap_year(2000))  # Output: True

'''

































# DO NOT EDIT THE CODE BELOW###################
if __name__ == "__main__":
    from utils.test_tools import run_tests

    try:
        run_tests(is_leap_year, __file__)
    except NameError as e:
        print(f"{e}\nDid you name your function correctly?")
        exit()
    
    
###############################################