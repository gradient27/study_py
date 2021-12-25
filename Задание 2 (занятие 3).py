# Простой, но работающий вариант
def my_input ():
    name = input('введите имя: ')
    surname = input('введите фамилию: ')
    year = input('введите год рождения: ')
    city = input('введите город проживания: ')
    email = input('введите email: ')
    tel = input('введите номер телефона: ')
    return name, surname, year, city, email, tel

def my_print (name, surname, year, city, email, tel):
    print(f'Имя: {name}, Фамилия: {surname}, Год рождения: {year}, Город проживания: {city}, email: {email}, Телефон: {tel}')

def main():
    name, surname, year, city, email, tel = my_input()
    my_print(name, surname, year, city, email, tel)

main()


'''
# ----Вариант 2 ---
# Переделанный код из задания 6 к занятию 2
def input_elem():
    goods = []
    features = {'Имя': '', 'Фамилия': '', 'Год рождения': '', 'Город проживания': '', 'email': '', 'Телефон': ''}
    num = 0
    while True:
        if input('Для выхода из приложения нажмите Q, для продолжения нажмите Enter: ').upper() == 'Q':
            return dict(goods)
        num += 1
        for f in features.keys():
            prop = input(f'Введите значение свойства {f}: ')
            features[f] = prop
        goods.append((num, features.copy()))

def my_print(*arg):
    my_list = arg
    #print(type(my_list))
    for _ in my_list:
        print(f'{_}')

def main():
    arg = input_elem()
    my_print(arg)

main()

# ---- Конец варианта 1 ---
'''