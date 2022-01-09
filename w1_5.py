def rec(str):
    with open('data.txt', 'a') as f:
        f.write(f'\nnew string: {str}')
    print(f'Выполнена запись в файл data.txt строки: {str}')

def my_inp():
    str = input('Введите текст (для выхода нажмите Enter): ')
    if len(str) != 0:
        rec(str)
    return str

while len(my_inp()) != 0:
    my_inp()
