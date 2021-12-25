# --- Вариант 1 (**) ---
'''
def my_input():
    x = -1
    y = 1
    while x < 0:
        x = int(input('Введите положительное действительное число: '))

    while y > 0:
        y = int(input('Введите целое отрицательное число: '))
    return x, y

def my_func(x, y):
    print(f'Результат: {x ** y}')

def main():
    x, y = my_input()
    my_func(x, y)

main()
'''

# --- Вариант 2 (без **) ---
def my_input():
    x = -1
    y = 1
    while x < 0:
        x = int(input('Введите положительное действительное число: '))

    while y > 0:
        y = int(input('Введите целое отрицательное число: '))
    return x, y

def my_func(x, y):
    y = abs(y)
    #print(y)
    cnt = 1
    denom = x
    while cnt < y:
        denom = denom * x
        cnt += 1
    #print(denom)
    print(f'Результат: {1 / denom}')

def main():
    x, y = my_input()
    my_func(x, y)

main()