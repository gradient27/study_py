from sys import argv
from itertools import count

w6_1_4, a = argv
a = int(a)
for el in count(a):
    if el > 15:
        break
    else:
        print(el)
