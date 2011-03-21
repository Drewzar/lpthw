#Exercise 17: More Files

from sys import argv; from os.path import exists; script, from_file, to_file = argv; indata = open(from_file).read(); open(to_file, 'w').write(indata)


