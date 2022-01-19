class Car():

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Объект {self} начал движение')

    def stop(self):
        print(f'Объект {self} закончил движение')

    def turn(self, direction):
        print(f'Объект {self} повернул в сторону {direction}')

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена')
        else:
            print(self.speed)

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышена')
        else:
            print(self.speed)

class PoliceCar(Car):
    pass

wk = WorkCar(50, 'black', 'bebeka', False)
wk.go()
wk.turn("в левую сторону")
wk.stop()
wk.show_speed()