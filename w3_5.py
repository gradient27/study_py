with open('data.txt', 'r', encoding='utf-8') as f:
    low_pay = []
    cnt = 0
    sum = 0
    for line in f:
        #print(line)
        new_line = line.split()
        if int(new_line[1]) < 20:
            low_pay.append(new_line[0])
        cnt += 1
        sum = sum + int(new_line[1])
        print(new_line)
print(f'Сотрудники с зп менее 20: {low_pay}')
print(f'Средний доход составляет {sum / cnt : .1f}')
