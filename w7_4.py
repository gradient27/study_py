from math import factorial
def gen():
    for el in (10, 20, 30):
        yield el
g = gen()
for el in g:
    n = factorial(el)
    print(n)