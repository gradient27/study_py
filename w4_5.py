with open('data.txt', 'r', encoding='utf-8') as f:
    for_my_line = ['Один', 'Два', 'Три', 'Четыре']
    my_line = []
    cnt = 0
    for line in f:
        line = line.strip('\n')
        new_line = line.split(" — ")
        my_line = [for_my_line[cnt], " — ", new_line[1], '\n']
        cnt += 1
        #print(new_line)
        #print('#' * 50)
        #print(''.join(my_line))
        with open('new_data.txt', 'a', encoding='utf-8') as n:
            n.write(''.join(my_line))
