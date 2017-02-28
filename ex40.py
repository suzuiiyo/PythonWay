class A(object):
    pass


class B(A):
    def __init__(self):
        print "init"

    def __new__(cls, *args, **kwargs):
        print "new %s" % cls

        return object.__new__(A, *args, **kwargs)

c = B()
print type(c)