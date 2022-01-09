def my_inp():
    return input('Введите числа разделенные пробелами: ')

def my_rec():
    with open('new_data.txt', 'w') as f:
        f.write(my_inp())

def my_rd():
    with open('new_data.txt', 'r') as f:
        my_list = f.read().split()
        sum = 0
        for el in my_list:
            el = int(el)
            sum = sum + el
        print(my_list)
        print(f'Сумма равна: {sum}')

my_rec()
my_rd()
