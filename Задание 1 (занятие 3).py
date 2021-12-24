def my_devision(delimoe, delitel):
    ''' Функиция вычисляет результат деления'''
    return delimoe / delitel

def input_elem():
    '''Функция запрашивает делимое и делитель у пользователя, проверяет полученные значения'''
    delimoe = int(input('Введите делимое: '))
    delitel = int(input('Введите делитель: '))
    return delimoe, delitel


def main():
    delimoe, delitel = input_elem()
    print(f'Результат деления: {my_devision(delimoe, delitel)}')

main()