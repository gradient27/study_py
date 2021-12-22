my_str = input('Введите несколько слов, разделенных пробелами: ')
print(f'Вы ввели: {my_str}')
my_list = my_str.split(' ')
# print(my_list)
cnt = 1
for el in my_list:
    print(f'{cnt}. {el:.10}')
    cnt += 1
