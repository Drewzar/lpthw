# Exercise 14: Prompting and Passing

from sys import argv

script, user_name, color  = argv
prompt = '> '

print "Hi %s, I'm, the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
Your color is %s.
And you have a %r computer. Nice.
""" % (likes, lives, color, computer)
