# ----Вариант 1 ---
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
        print(f'{_}\n')

def main():
    arg = input_elem()
    my_print(arg)

main()

# ---- Конец варианта 1 ---
