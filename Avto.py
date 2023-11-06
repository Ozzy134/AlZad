class Avto:

    def __init__(self, mark=None, model=None, year=None, prob=None):
        self.mark = mark
        self.model = model
        self.year = year
        self.prob = prob

    def Vvod(self):
        print('Автомобиль:')
        print(f'Марка: {self.mark}')
        print(f'Модель: {self.model}')
        print(f'Год выпуска: {self.year}')
        print(f'Пробег: {self.prob}')

    def redict(self):
        self.mark = input('Марка: ')
        self.model = input('Модель: ')
        self.year = input('Год выпуска: ')
        self.prob = int(input('Пробег: '))

bus = Avto('Mersedes-benz', 'O405', 2005, '229339')
bus.Vvod()
avto = Avto()
avto.redict()
avto.Vvod()