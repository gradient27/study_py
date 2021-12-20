# -------------Решение мое через перебор символов строки------
'''
a_str = (input('Введите число: '))
cnt_num = len(a_str)
# i - счетчик для символов строки
# j - счетчик для перебора цифр от 9 до 0
j = 9
result = -1
while j >= 0:
    i = 0
    while i < cnt_num:
        # print(f'Начало проверки, i = {i}, j = {j}')
        if int(a_str[i]) == j:
            #print(a_str[i], j)
            result = j
            break
        else:
            i = i + 1
    if result != -1:
        break
    else:
        j = j - 1

print(f'Наибольшее число равно: {result}')
'''
# ----Конец моего решения

# ----Решение Евгения
num_init = int(input('Введите целое положительное число: '))
maximum = num_init % 10
num = num_init
while num > 0:
    digit = num % 10
    if digit > maximum:
        maximum = digit

    if digit == 9:
        break

    num //= 10 # num = num // 10
    print(num)
print(f'Наибольшая цифра в числе {num_init} равна {maximum}')