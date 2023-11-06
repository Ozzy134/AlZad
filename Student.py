class Student:
    a = 'a'

    def __init__(self, name='', age='', grade='', scores=[4,5,2,2,3]):
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores

    def info(self):
        print(f'ФИО: {self.name}')
        print(f'Возраст: {self.age}')
        print(f'Класс: {self.grade}')
        print(f'Оценки: {self.scores}')
        print(f'Cредний балл: {self.averege_score()}')

    def averege_score(self):
        y = sum(self.scores)
        c = len(self.scores)
        return y / c

    def infoVvod(self):
        self.name = input('ФИО: ')
        self.age = input('Возраст: ')
        self.grade = input('Класс: ')

s = Student('Львов Андрей Валентинович', '20', '11', [4,5,2,2,3])
s.info()
g = Student()
g.infoVvod()
g.info()

