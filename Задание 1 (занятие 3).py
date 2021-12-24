# Решение 1, нет проверки на тип введенных данных и при нуле нет повтора ввода
'''
def my_devision(delimoe, delitel):
    return delimoe / delitel

def input_elem():
    delimoe = int(input('Введите делимое: '))
    delitel = int(input('Введите делитель: '))
    return delimoe, delitel

def main():
    delimoe, delitel = input_elem()
    if delitel != 0:
        print(f'Результат деления: {my_devision(delimoe, delitel)}')
    else:
        print('Значение вычислить не возможно, делитель равено 0')

main()
'''
# Решение 2, если 0 предлагается ввести делитель повторно
def input_elem():
    '''Функция запрашивает данные у пользователя'''
    delitel = 0
    delimoe = int(input('Введите делимое: '))
    while delitel == 0:
        delitel = int(input('Введите делитель (число не равное 0): '))
    return delimoe, delitel

def my_devision(delimoe, delitel):
    ''' Функиция вычисляет результат деления'''
    return delimoe / delitel

def main():
    delimoe, delitel = input_elem()
    print(f'Результат деления: {my_devision(delimoe, delitel)}')

main()
