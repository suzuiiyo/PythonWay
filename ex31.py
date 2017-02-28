the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'pears', 'oranges', 'apricots']
changes = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print "the count is %d" % number

for fruit in fruits:
    print "the type of fruit is %s" % fruit

for i in changes:
    print "I got %r" % i

#build a list, first start with a empty one
element = range(0,6)

for i in element:
    print "Element was: %d" % i