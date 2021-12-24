# --- Решение Евгения --
my_l = [9, 8, 7, 6, 5, 4, 3, 2, 1]
new_number = int(input("Введите новый элемент рейтинга в виде натурального числа: "))
i = 0

for n in my_l:
    if new_number <= n:
        i += 1

    elif new_number > n:
        break

my_l.insert(i, float(new_number))
print(my_l)
