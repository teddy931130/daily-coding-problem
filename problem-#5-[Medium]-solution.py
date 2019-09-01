def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(func):
    return func(lambda x, y: x)


def cdr(func):
    return func(lambda x, y: y)


print(car(cons(3, 4)))
print(cdr(cons(3, 4)))
