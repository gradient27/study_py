class Stationery:


    def draw(self):
        print("Произошло рисование")

    def __init__(self, title):
        self.title = title

class Pen (Stationery):
    def draw(self):
        print("Ручка пишет синеми чернилами")

class Pencil(Stationery):
    def draw(self):
        print('Карандаш начертил линию')

class Handle(Stationery):
    def draw(self):
        print("Маркер все испачкал")

pn = Pen("Ручка")
pn.draw()
pnc = Pencil("Карандаш")
pnc.draw()
hnd = Handle("Маркер")
hnd.draw()



