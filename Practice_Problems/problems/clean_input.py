'''
Write a function clean_input(input_str) that accepts a single string from user input and returns a cleaned-up version of the string. The function should remove leading and trailing whitespace, convert the string to lowercase, and remove any non-alphanumeric characters except for spaces.

The function should:
    Accept a single string input_str from user input.
    Remove any leading or trailing whitespace.
    Convert all characters to lowercase.
    Remove all non-alphanumeric characters, except for spaces.
    Convert "_" and "-" into spaces


clean_input("  Hello, World!  ")      # Return: "hello world"
clean_input("   Python@3.9 ")         # Return: "python39"
clean_input("    CLEAN 123 ")         # Return: "clean 123"
clean_input("Special$$$ Characters!") # Return: "special characters"
clean_input("!  Spaces ? and Tabs\t") # Return: "spaces and tabs"
clean_input("No$trailing_spaces!")    # Return: "notrailing_spaces"
clean_input("")                       # Return: "" 
clean_input("ALL CAPS")               # Return: "all caps"
'''


















































# DO NOT EDIT THE CODE BELOW###################
if __name__ == "__main__":
    from utils.test_tools import run_tests

    try:
        run_tests(clean_input, __file__)
    except NameError as e:
        print(f"{e}\nDid you name your function correctly?")
        exit()   
###############################################