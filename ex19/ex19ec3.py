# Exercise 19 Extra Credit 3
from sys import argv

script, number = argv

def in_2_ft(inches):
    inches = float(inches)
    feet = inches / 12
    print "There are %f feet in %f inches" % (feet, inches)

# Way number 1, called with just a number
in_2_ft(45)

# Way number 2, called with a variable
inch = 35
in_2_ft(inch)

# Way number 3, last minute math
in_2_ft(35 + 45)

# Way number 4, math with variables
in_2_ft(35 + inch)

# Way number 5, from input
rawinch = raw_input("Enter the number of inches: ")
in_2_ft(rawinch)

# Way number 6, from input and with math
in_2_ft(float(rawinch) + 30)

# Way number 7, from input and with variables
in_2_ft(float(rawinch) + inch)

# Way number 8, from with in a function
def a_function():
    in_2_ft(50)

a_function()

# Way number 9, from argvs
in_2_ft(number)

# Way number 10, from argvs from within a function that also has math, inputs and a variable!!!
def another_function():
    subnum = 2
    in_2_ft(float(number) + 33 - subnum + float(rawinch))

another_function()
