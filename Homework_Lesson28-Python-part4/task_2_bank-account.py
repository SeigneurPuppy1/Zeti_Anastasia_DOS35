#!/usr/bin/env python3

class BankAccount:
    def __init__(self, account_num, name, balance):
        self.account_num = account_num
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Счет {self.account_num} пополнен на {amount} руб.")
            print(f"Новый баланс {self.balance}")
        
    def take_money(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Счет {self.account_num}: снятие {amount} руб.")
                print(f"Новый баланс: {self.balance}")

account_1 = BankAccount(465738195745374, "Иван Иванов", 12780)
account_2 = BankAccount(465921000034000, "Екатерина Великая", 1000267)

print(f"Номер банковского счета: {account_1.account_num}")
print(f"Владелец счета: {account_1.name}")
print(f"Баланс: {account_1.balance}")

account_1.deposit(10000)
account_1.take_money(4000)

account_2.deposit(100000)
account_2.take_money(1000000)
