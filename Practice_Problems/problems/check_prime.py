'''
Problem: Is Prime?
Write a function is_prime(n) that checks whether a given positive integer n is a prime number.
A prime number is defined as a number greater than 1 that has no positive divisors other than 1 and itself.

The function should
    Accept a positive integer n.
    Return True if n is a prime number; otherwise, return False.


Example Calls:
is_prime(2)        # Return: True
is_prime(3)        # Return: True
is_prime(4)        # Return: False
is_prime(17)       # Return: True
is_prime(18)       # Return: False
is_prime(1)        # Return: False
is_prime(29)       # Return: True
is_prime(30)       # Return: False
is_prime(97)       # Return: True
is_prime(100)      # Return: False
'''































# DO NOT EDIT THE CODE BELOW###################
if __name__ == "__main__":
    from utils.test_tools import run_tests

    try:
        run_tests(is_prime, __file__)
    except NameError as e:
        print(f"{e}\nDid you name your function correctly?")
        exit()   
###############################################