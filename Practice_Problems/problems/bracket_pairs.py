''' 
Problem: Bracket Pairs
Write a function is_balanced(expression) that checks whether the parentheses in a given string are balanced. 
Hint: use a list to simulate a stack data structure for this task.

The function should:
    Accept a string expression containing characters (, ), and other characters.
    Return True if the parentheses are balanced and False otherwise.
    Consider parentheses balanced if:
    Every opening parenthesis ( has a corresponding closing parenthesis ).
    The closing parentheses ) do not come before their matching opening parentheses (.

Example Calls
    is_balanced("(a + b) * (c + d)")                # Return: True
    is_balanced("((a + b))")                        # Return: True
    is_balanced("(a + b) * (c + d))")               # Return: False
    is_balanced("((a + b) * (c + d)")               # Return: False
    is_balanced("a + b")                            # Return: True
    is_balanced("")                                 # Return: True
    is_balanced(")(")                               # Return: False
    is_balanced("(())()")                           # Return: True
    is_balanced("(()())")                           # Return: True
    is_balanced("(((a + b)) + (c + d))")            # Return: True
'''



































# DO NOT EDIT THE CODE BELOW###################
if __name__ == "__main__":
    from utils.test_tools import run_tests

    try:
        run_tests(is_balanced, __file__)
    except NameError as e:
        print(f"{e}\nDid you name your function correctly?")
        exit()   
###############################################