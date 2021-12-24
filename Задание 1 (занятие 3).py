# Решение 1, нет проверки на тип введенных данных и при нуле нет повтора ввода
def my_devision(delimoe, delitel):
    ''' Функиция вычисляет результат деления'''
    return delimoe / delitel

def input_elem():
    delimoe = int(input('Введите делимое: '))
    delitel = int(input('Введите делитель: '))
    return delimoe, delitel

def validation(delimoe, delitel):
    delimoe, delitel = input_elem()
    if delitel != 0:
        return delimoe, delitel
    else:
        print('Значение вычислить не возможно, делитель равено 0')

def main():
    delimoe, delitel = input_elem()
    if delitel != 0:
        print(f'Результат деления: {my_devision(delimoe, delitel)}')
    else:
        print('Значение вычислить не возможно, делитель равено 0')


main()