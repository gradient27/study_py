a = input('Введите число: ')
summand_1 = int(a)
summand_2 = int(a + a)
summand_3 = int(a + a + a)
summ = summand_1 + summand_2 + summand_3

print(f'Результат странных вычислений равен: {summ}')

# ----Вариант решения Евгения---
'''
n = input('Введите положительное число - ')
print(f'{n} + {n + n} + {n + n + n} = {int(n) + int(n+n) + int(n + n + n)}')
'''