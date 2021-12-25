def my_input():
    my_list = input('Введите числа разделенные пробелами: ')
    my_list = my_list.split(' ')

    cnt = 0
    while cnt < len(my_list):
        my_list[cnt] = int(my_list[cnt])
        cnt += 1

    return my_list

def main():
    new_list = []

    while True:
        if input('Для выхода из приложения нажмите Q, для продолжения нажмите Enter: ').upper() == 'Q':
            #return dict(goods)
            break
        new_list.extend(my_input())
        new_sum = sum(new_list)
        print(f'Все введенные значения: {new_list}')
        print(f'Сумма всех введенных значений: {new_sum}')

main()
