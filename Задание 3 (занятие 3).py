# ---- Мой вариант решения ----

def my_input():
    my_l = ['start_pos']
    # Заполняем список значениями
    # Создаем счетчик, чтобы пользователь видел какое значение по счету он вводит
    cnt = 1
    # Заполняем список
    while my_l[(len(my_l) - 1)] != 'q':
        my_l.append(input(f'введите значение № {cnt} (для выхода введите q): '))
        cnt += 1
    # удаляем start_pos и q
    my_l.pop(0)
    my_l.pop((len(my_l) - 1))
    return my_l


def my_print(my_list):
    #print(my_list)
    cnt = 0
    while cnt < len(my_list):
        my_list[cnt] = int(my_list[cnt])
        cnt += 1

    new_list = []
    new_list.append(my_list.pop(my_list.index(max(my_list))))
    new_list.append(my_list.pop(my_list.index(max(my_list))))
    print(f'Сумма двух максимальных числе равна: {new_list[0] + new_list[1]}')


def main():
    my_list = my_input()
    my_print(my_list)

main()
# ---- Конец моего решения ----
'''
# ---- Решение Евгения 1----
def my_func(num_1: int, num_2: int, num_3: int):
    my_list = [num_1, num_2, num_3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return 'Введите только числа'
print(my_func(2, 11, -30))

# ---- Решение Евгения 2 ----
def my_func(arg1, arg2, arg3):
    my_list = [arg1, arg2, arg3]
    return sum(sorted(my_list)[1:])
    #print(sorted(my_list))

print(my_func(2, 11, -30))
'''
