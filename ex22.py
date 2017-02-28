from sys import argv
script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(current_line, f):
    print current_line, f.readline()

current_file = open(input_file,'w+')
print "First let's print the whole file:\n"
print_all(current_file)

print "I have three lines to put into the file"
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")
print "Now I'll get the three lines into the file"
current_file.write(line1)
current_file.write("\n")
current_file.write(line2)
current_file.write("\n")
current_file.write(line3)
current_file.write("\n")

print "It's time to rewind the file"
rewind(current_file)

print "let's print three lines"
for current_line in range(1,4):
    print_a_line(current_line,current_file)
    current_line += 1

