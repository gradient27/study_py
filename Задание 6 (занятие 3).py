def my_input():
    my_str = input('Введите слова через пробел: ')
    return my_str

def int_func():
    my_str = my_input()
    new_str = my_str.title()

    print(new_str)

int_func()