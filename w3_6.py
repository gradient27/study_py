class Worker():

    def __init__(self, name, surname, position, wade, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'wade': wade, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя объекта: {self.name + " " + self.surname}')

    def get_total_income(self):
        print(f'Доход объекта: {self.income.get("bonus") + self.income.get("wade")} рублей')


kuza = Position('Кузя', 'Кузькин', 'Директор', 1000, 100)
vova = Position('Вова', 'Вовин', 'Главбух', 700, 50)
borya = Position('Боря', 'Борин', 'Уборщик', 100, 10)

vova.get_full_name()
vova.get_total_income()
