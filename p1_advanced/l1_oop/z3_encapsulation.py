class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Balance должен быть защищённым.

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Недостаточно средств для снятия.")
        elif amount < 0:
            print("Сумма снятия должна быть положительной.")
        else:
            self.__balance -= amount

    def info(self):
        return f"Номер счета: {self.account_number}, Баланс: {self.__balance}"


# Тестирование
acc = BankAccount(456, 0)
acc.deposit(500)
acc.withdraw(450)
print(acc.info())  # Ожидаемый результат: Номер счета: 456, Баланс: 50
