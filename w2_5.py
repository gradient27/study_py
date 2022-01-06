with open('data.txt', 'r') as f:
    cnt = 0
    for line in f:
        if len(line) != 0:
            new_line = line.split()
            print(f'В строке {cnt + 1} количество слов - {len(new_line)}')
            cnt += 1

    print(f'Количество строк: {cnt}')