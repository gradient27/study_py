my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = [int(el) for el in my_list if (int(el) > int(el - 1))]
print(new)

