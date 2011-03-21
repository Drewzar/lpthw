#Exercise 17: More Files: Extra Credit 2

from sys import argv
from os.path import exists

script, from_file, to_file = argv

# We could do these two in one line too, how?
input = open(from_file)
indata = input.read()

output = open(to_file, 'w')
output.write(indata)

output.close()
input.close()
