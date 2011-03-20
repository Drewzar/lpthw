# Exercise 6: Strings and Text (extra credit #1)

# defining a variable as a string with a single format character
x = "There are %d types of people." % 10
# defining a variable as a string
binary = "binary"
# defining another variable as a string 
do_not = "don't"
# defining a variable as a string that has a list of format characters
y = "Those who know %s and those who %s." % (binary, do_not)

# we now print the first variable
print x
# we print this variable that has 2 the other 2 variables 
print y

# Now we reprint the x variable but this time it's formated to be a string using the %r format character
print "I said: %r." % x
# We do the same with y but use the %s format character
print "I also said: '%s'." % y

# defining a variable as a boolen value
hilarious = False
# defining a varible as string with a sneaky format character in it.
joke_evaluation = "Isn't that joke so funny?! %r"

# prints this line using that sneaky formating character, and turning the boolen value in to a string.
print joke_evaluation % hilarious

# defining one half of a string
w = "This is the left side of..."
# defining the other half of a string
e = "a strong with a right side."

# prints the 2 variables using the + to concat them.
print w + e
