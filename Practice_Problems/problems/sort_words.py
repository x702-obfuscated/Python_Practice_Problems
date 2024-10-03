'''
Sort Words
Write a function sort_words that accepts a list of words (strings) and returns a new list containing the words sorted in alphabetical order.

The function should:
    Accept a single argument, a list of words (strings).
    Return a new list with the words sorted in alphabetical order.
    Handle the case where values have mixed case (uppercase and lowercase)
    Handle the case where values are not alphabetical, by comparing lexicographically(ie. based on unicode code point)
    Handle the case where the input list is empty by returning an empty list.
    Handle the case where the list includes non string data, by skipping the invalid values

Hint: Take a look at an ASCII table


Example Calls:

sort_words(["banana", "apple", "cherry"])               # Return: ["apple", "banana", "cherry"]
sort_words(["dog", "cat", "elephant"])                  # Return: ["cat", "dog", "elephant"]
sort_words([])                                          # Return: []
sort_words(["zebra", "lion", "antelope"])               # Return: ["antelope", "lion", "zebra"]
sort_words(["pear", "banana", "apple", "kiwi"])         # Return: ["apple", "banana", "kiwi", "pear"]
sort_words(["apple", 42, "banana"])                     # Return: ["apple", "banana"]
sort_words(["hello", None, "world"])                    # Return: ["hello", "world"]
sort_words(["apple", 42, None, "banana", "$$$"])        # Return: ["apple", "banana"]
sort_words(["Banana", "apple", "Cherry"])               # Return: ["Banana", "Cherry", "apple"]
sort_words(["  apple", "banana  ", " cherry "])         # Return: ["  apple", " cherry ", "banana  "]
sort_words(["123", "321", "213"])                       # Return: ["123", "213", "321"]
sort_words(["", "apple", "banana"])                     # Return: ["", "apple", "banana"]
sort_words(["apple", "banana", "apple", "banana"])      # Return: ["apple", "apple", "banana", "banana"]
sort_words(["#hash", "apple", "banana"])                # Return: ["#hash", "apple", "banana"]
sort_words([1, 2, "apple", "banana", 3])                # Return: ["apple", "banana"]
sort_words(["A", "B", "C"])                             # Return: ["A", "B", "C"]
sort_words(["a", "b", "c"])                             # Return: ["a", "b", "c"]
sort_words(["apple", "Banana", "APPLE", "banana"])      # Return: ["APPLE", "Banana", "apple", "banana"]
sort_words(["-1", "0", "1"])                            # Return: ["-1", "0", "1"]
sort_words(["", None, "hello", "world"])                # Return: ["", "hello", "world"]
'''




































# DO NOT EDIT THE CODE BELOW###################
if __name__ == "__main__":
    from utils.test_tools import run_tests

    try:
        run_tests(sort_words, __file__)
    except NameError as e:
        print(f"{e}\nDid you name your function correctly?")
        exit()   
###############################################