class Triangel:

    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def TriandelInf(self):
        if self.a1 == self.a2 or self.a2 == self.a3 or self.a1 == self.a3:
            print('Треугольник равнобедренный')
        elif self.a1 == self.a2 == self.a3:
            print('Треугольник равносторонний')
        else:
            print('Треугольник разносторонний')

    def TriangleS(self):
        p = (self.a1 + self.a2 + self.a3) / 2
        s = (p * (p - self.a1) * (p - self.a2) * (p - self.a3)) * 0.5
        print('Площадь треугольника ровна: %0.2f' % s)

t2 = Triangel(3, 3, 3)
t2.TriandelInf()
t2.TriangleS()
t3 = Triangel(3, 4, 5)
t3.TriandelInf()
t3.TriangleS()