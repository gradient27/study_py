class road():
    def __init__(self, len, wid, massa):
        self._length = len
        self._width = wid
        self.massa = massa

    def calculate(self):
        result = self._length * self._width * self.massa
        print(f'Масса асфальта равна {result} килограмм')

rd = road(20, 30, 10)
#print(rd.length)
rd.calculate()