class Rectangle:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def RectangleP(self):
        p = self.x + self.x + self.y + self.y
        return p

    def RectangleS(self):
        s = self.x * self.y
        return s

    def RectangleInfo(self):
        print(f'Стороны прямоугольника равны: {self.x}, {self.y}')
        print(f'Перимитр прямоугольника равен: {self.RectangleP()}')
        print(f'Площадь прямоугольника равна: {self.RectangleS()}')

r1 = Rectangle(5, 5)
r1.RectangleInfo()