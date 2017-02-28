from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()

print "The inputfile is %d long" % len(indata)
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to contiue, CTRl-C o abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done"

out_file.close()
