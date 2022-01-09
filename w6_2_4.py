from itertools import cycle
gener = cycle([1, 2, 3, 4])
cnt = 0
for _ in gener:
    if cnt == 20:
        break
    cnt += 1
    print(_)