def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def substract(a, b):
    print "SUBSTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING  %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = substract(467, 30)
weight = multiply(120, 23)
iq = divide(100, 2)

arg1 = int(raw_input("enter the number: "))
answer = divide(add(arg1, 34), substract(100, 1024))
print "the answer is %d" % answer