with open('data.txt', 'r', encoding='utf-8') as f:
    my_dict = {}
    for line in f:
        my_list = line.split(":")
        my_name = my_list[0]
        switch = False
        new_list = []
        sum = 0
        for el in my_list[1]:
            if el.isdigit() and switch == False:
                    new_list.append(el)
                    switch = True
            elif el.isdigit() and switch == True:
                    new_list[len(new_list) - 1] = new_list[len(new_list) - 1] + el
            else:
                    switch = False
        for el in new_list:
            el = int(el)
            sum = sum + el
        my_dict.update({my_name : sum})
    print(my_dict)
