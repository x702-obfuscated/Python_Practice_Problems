import os
import importlib


from utils.helpers import *

tests_passed = False


def test_return(function, expected, *args):
    global tests_passed

    arg_str = ""

    for arg in args:
        if isinstance(arg,str):
            arg = f"\"{arg}\""
            arg = repr(arg)[1:-1]
            
        arg_str += f"{arg},"
    
    arg_str = arg_str[:-1]
    

    try: 
        assert function(*args) == expected
        print(f"\u2705 PASSED, {str(function.__name__)}({arg_str})")

    except AssertionError as e:
        tests_passed = False

        print(f"\u274C FAILED, called {str(function.__name__)}({arg_str}), expected:  {expected} , but got:  {function(*args)}")

def run_tests(function, path = None):
    import importlib
    global tests_passed

    try:
        file = os.path.basename(path)
        module = f"tests.test_{file.removesuffix('.py')}"
        tests = importlib.import_module(module).tests
    except ModuleNotFoundError as e:
        print(f"Test File Could Not Be Found.\n{e}")
        exit()


    update_report()

    if not function:
        print("The Function to test has not be defined. Exiting.")
        exit()
        
    tests_passed = True

    for test in tests:
        test_return(function,*test)

 
    print(f"\nTested {file}")
    if(not tests_passed):
        print("\u274C SOME TESTS FAILED, PLEASE TRY AGAIN. \u274C")
    else:
        report = read_json()
        report["progress"][file]="\u2705 Passed"
        write_json(data = report)
        update_report()
        print("\u2705 ALL TESTS PASSED \u2705")
