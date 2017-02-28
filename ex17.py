from sys import argv

script, user_name, uhh = argv
prompt = 'answer:'

print "Hi, %s. I'm script %s" % (user_name, script)
print "I have a few questions to ask you"
print "Do you like me,%s,don't you think so,%s" % (user_name, uhh)
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "what kind of computer do you have %s?" % user_name
computers = raw_input(prompt)

print """
Alright, so you said %s about liking me.
You lives in %s ,well not know much about that place.
And you have a %r computer,that sounds interesting.
""" % (likes, lives, computers)


