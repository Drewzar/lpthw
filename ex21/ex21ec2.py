# Exercise 21

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some amth with just functions!"

age = add(30, 5)
height = subtract(78,4)
weight = multiply(90, 2)
iq = divide(100, 2)


print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

#breaking it down
otherwhat = divide(iq, 2)
print otherwhat
otherwhat = multiply(weight, otherwhat)
print otherwhat
otherwhat = subtract(height, otherwhat)
print otherwhat
otherwhat = add(age, otherwhat)
print "Is this it? %d" % otherwhat

#fully broken down
finalwhat = (35 + (74 - ((50 / 2) * 180)))
print "Is this the same? %d" % finalwhat

print "That becomes: ", what, "Can you do that by hand?"
