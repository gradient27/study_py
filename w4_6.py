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
        print(f'Объект {self} поернул в сторону {direction}')

class TownCar(Car):
    pass

class SportCar(Car):
    pass

class WorkCar(Car):
    pass

class PoliceCar(Car):
    pass
