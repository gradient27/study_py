import json
def my_read():
    # Читаем файл и создаем двумерный массив с исходными данными, вычисляем и добавляем прибыль
    with open('data7.txt', 'r', encoding='utf-8') as f:
        my_matr = []
        for line in f:
            my_list_row = line.split()
            my_list_row.append(int(my_list_row[2]) - int(my_list_row[3]))# Добавляем прибыль
            my_matr.append(my_list_row)
    return my_matr

def mean_prof():
    my_matr = my_read()
    dict_profit = {}
    firm_profit = {}
    my_list = []
    cnt = 0
    sum = 0
    for i in range(0, len(my_matr)):
        firm_profit.update({my_matr[i][0] : my_matr[i][4]})
        if int(my_matr[i][4]) >= 0:
            sum = sum + int(my_matr[i][4])
            cnt += 1
    dict_profit.update({"Average profit" : sum / cnt})
    my_list.append(firm_profit)
    my_list.append(dict_profit)
    return my_list

def my_write():
    data = mean_prof()
    with open('data7.json', 'w') as f:
        json.dump(data, f)

print(f'Сформирована строка: {mean_prof()}')
my_write()
print("Результат записан в файл data7.json")
