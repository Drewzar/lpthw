# Exercise 15: Reading Files

print "What's the file name?"
file= raw_input("> ")

txt = open(file)

print txt.read()
