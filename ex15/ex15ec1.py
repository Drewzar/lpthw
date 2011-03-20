# Exercise 15: Reading Files

# imports the argv from the system
from sys import argv

# defines the argv
script, filename = argv

# defines the variable 'txt' as the open file name that was recieved from the argv
txt = open(filename)

# Just prints the file name you gave as an argv.
print "Here's your file %r:" % filename
# prints the variable 'txt' that's being passed through the function .read() 
print txt.read()

# prints a qestion asking for a another filename
print "I'll also ask you to type it again:"
# defines the variable 'file_again' by prompting the user.
file_again = raw_input("> ")

# defines 'txt_again' as an open file.
txt_again = open(file_again)

# print the variable 'txt_again' that's being passed through the function .read()
print txt_again.read()
