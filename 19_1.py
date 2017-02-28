from sys import argv
script, filename = argv

print "let's erase the file %r" % filename
print "if you don't want to do this, hit CTRL_C(^ C)."
print "if you do want do this,just hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "now I'm going to ask you three questions."

line1 = raw_input("line1 : ")
line2 = raw_input("line2 : ")
line3 = raw_input("line3 : ")

print "I'm going to write these to the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
