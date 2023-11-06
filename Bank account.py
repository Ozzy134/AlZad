class BankAccount:

    history = []

    def __init__(self, fio, balance, int_rate, trans):
        self.fio = fio
        self.__balance = balance
        self.__int_rate = int_rate
        self.__trans = trans

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print(f'Внесение наличных на счет: {amount}')
        self.history.append('Внесение наличных')

    def withdraw(self, amount):
        self.__balance = self.__balance - amount
        print(f'Снятие наличных: {amount}')
        self.history.append('Cнятие наличных')

    def history_list(self):
        for i in self.history:
            print("-", i)

account = BankAccount('Бабинов Алексей Евгеньевич', 100000, 0.05, 1)
account.deposit(15000)
account.withdraw(7500)
account.history_list()
