from sys import argv

w1_4, hrs, rate, prize = argv
hrs = int(hrs)# отработано часов
rate = int(rate)# цена одного часа
prize = int(prize)# премия
print(f'Заработная плата равна: {(hrs * rate) + prize} рублей')
