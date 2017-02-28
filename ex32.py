a = raw_input("> ")
b = raw_input("> ")
numbers = []

def SetList(j,k):
    for i in range(0,int(j),int(k)):
        print "at the top i is %d" % i
        numbers.append(i)
        print "the number:", numbers
        print "at the bottom i is %d" % i

SetList(a,b)
print "the numbers: "
for num in numbers:
    print num