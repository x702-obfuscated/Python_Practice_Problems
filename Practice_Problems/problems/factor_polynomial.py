'''
Write a function factor_polynomial that accepts two integer coefficients b, c of a quadratic polynomial
in the form:

    ax**2 + bx + c

The function should return the factored form of the polynomial as a string <class 'str'>.
If the polynomial cannot be factored using integer coefficients, return "not factorable"
It can be assumed that the value of a is = 1

The function should:
    Accept 2 integer arguments representing b and c the coefficients of a quadratic polynomial.
    For simplicity a can be assumed to always be 1. 

    Return the factored form as a string in the format (x - r1)(x - r2) where r1 and r2 are the integer
    roots of the polynomial

    Calculate the discriminant in the form of D = b**2 - 4ac  where:
        D > 0: The quadratic has two distinct real roots
        D == 0 : The quadratic has exactly one real root
        D < 0 : The quadratic equation has no real roots; instead, it has two complex (or imaginary) roots. 


    Return "not factorable" if the discriminant is negative or if the roots are not integers. 

    Not include extra spaces before, after, or, between the factors


Example Calls:
factor_polynomial(-5, 6)   # Returns: "(x - 2)(x - 3)"
factor_polynomial(2, 1)    # Returns: "(x + 1)(x + 1)"
factor_polynomial(0, -4)   # Returns: "(x - 2)(x + 2)"
factor_polynomial(0, 1)    # Returns: "not factorable"
'''



    































# DO NOT EDIT THE CODE BELOW###################
if __name__ == "__main__":
    from utils.test_tools import run_tests

    try:
        run_tests(factor_polynomial, __file__)
    except NameError as e:
        print(f"{e}\nDid you name your function correctly?")
        exit()   
###############################################