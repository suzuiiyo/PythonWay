# -*- coding: utf-8 -*-
from sys import argv
script, filename = argv

print "I'm going to erase the %r," % filename
print "If you want do this, hit CTRL-C(^C)"
print "if you don't want do this, hit RETURN"

raw_input("?")

print "Opening the file ..."
target = open(filename, 'w')

print "truncate the file"
target.truncate()

print "now I'm going to ask you three lines."
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "now I'm going to write these to the file"
target.write(line1, line2, line3)


print "finally, close the file"
target.close()