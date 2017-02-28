people = 30
cars = 30
buses = 15

if cars > people:
    print "we should take the cars!"
elif cars < people:
    print "we should not take the cars."
else:
    print "we can't decide."

if buses> cars:
    print "tha's too many buses."
elif buses < cars:
    print "maybe we could take the buses."
else:
    print "we still can't decide!"

if people > buses:
    print "All right, let's take the buses."
else:
    print "Fine, let's stay home then."