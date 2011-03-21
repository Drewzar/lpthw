#Exercise 16: Extra credit #2

from sys import argv

script, filename = argv

print "Opening %r" % filename
output = open(filename, 'r')

print "Reading file...\n"
print output.read()
output.close()
