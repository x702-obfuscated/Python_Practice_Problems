''' 
Area of a Circle
Write a function circle_area that accepts a single numeric argument representing the radius of a circle and returns the area of the circle. 
The area of a circle is given by the formula:

    Area = pi * r**2

The function should:
    Accept a numeric argument representing the radius of the circle.
    Return the area of the circle as a float, rounded to two decimal places.
    Handle cases where the radius is negative by returning "invalid radius".    

Example Calls:

    circle_area(5)       # Return: 78.54
    circle_area(10)      # Return: 314.16
    circle_area(0)       # Return: 0.00
    circle_area(-3)      # Return: "invalid radius"
    circle_area(2.5)     # Return: 19.63`
'''
















































# DO NOT EDIT THE CODE BELOW###################
if __name__ == "__main__":
    from utils.test_tools import run_tests

    try:
        run_tests(circle_area, __file__)
    except NameError as e:
        print(f"{e}\nDid you name your function correctly?")
        exit()   
###############################################