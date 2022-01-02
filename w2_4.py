# ---- Решение через цикл ----
'''
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = []
i = 1
while i < len(my_list):
    if my_list[i] > my_list[i - 1]:
      new.append(my_list[i])
    i += 1
print(new)
'''

# ---- Решение через генератор ----
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for el in my_list if el > my_list[my_list.index(el) - 1] and my_list.index(el) != 0]
print(new_list)
