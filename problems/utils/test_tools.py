import os

tests_passed = False


def test_return(function, expected, *args):
    global tests_passed

    arg_str = ""

    for arg in args:
        if isinstance(arg,str):
            arg = f"\"{arg}\""
            
        arg_str += f"{arg},"
    
    arg_str = arg_str[:-1]
    
    try: 
        assert function(*args) == expected
        print(f"\u2705 PASSED, {str(function.__name__)}({arg_str})")

    except AssertionError as e:
        tests_passed = False

        print(f"\u274C FAILED, called {str(function.__name__)}({arg_str}), expected:  {expected} , but got:  {function(*args)}")

def run_tests(function, tests, path = None):
    global tests_passed

    if not function:
        print("The Function to test has not be defined. Exiting.")
        exit()
        
    tests_passed = True

    for test in tests:
        test_return(function,*test)

    try:
        print(f"\nTested {os.path.basename(path)}")
    except Exception as e:
        print(f"An Error Occured While Getting Test Path: {e}")
        exit()

    if(not tests_passed):
        
        print("\u274C SOME TESTS FAILED, PLEASE TRY AGAIN. \u274C")
    else:
        print("\u2705 ALL TESTS PASSED \u2705")
