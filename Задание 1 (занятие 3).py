# ---- Мое Решение, если 0 предлагается ввести делитель повторно ----

def input_elem():
    delitel = 0
    delimoe = int(input('Введите делимое: '))
    while delitel == 0:
        delitel = int(input('Введите делитель (число не равное 0): '))
    return delimoe, delitel

def my_devision(delimoe, delitel):
    return delimoe / delitel

def main():
    delimoe, delitel = input_elem()
    print(f'Результат деления: {my_devision(delimoe, delitel)}')

main()

# ---- Конец моего решения ----

# ---- Решение Евгения ----
'''
def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        div_num = s_1 / s_2
    except ValueError:
        return 'Некорректные данные'
    except ZeroDivisionError:
        return 'Делить на ноль нельзя'
    return round(div_num, 4)

print(div(input('Введите первое число: '), input('Введите второе число: ')))
'''