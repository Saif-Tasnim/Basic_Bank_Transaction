""" Manages Bank Account
Implement By Saif Tasnim Chy """


class Account:
    acc_Id = 1
    def __init__(self, age, name, nid_no, balance):
        self.name = name
        self.age = age
        self.nid_no = nid_no
        self.balance = balance
        self.account_Id = Account.acc_Id
        Account.acc_Id += 1

    def deposit(self, amount):
        self.balance += amount
        print(f'{self.name} amount ', amount, " Tk. has been successfully added \n\n")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"{self.name} has successfully withdrew\n\n")

    def __repr__(self) -> str:
        return f'Account Id : {self.account_Id}\nAccount Holder : {self.name}\nAge : {self.age}\n\n'


acc1 = Account(12, "Account A", 9165256836, 500)
print(acc1)

acc2 = Account(13, "Account B", 12190876, 1000)
print(acc2)

acc1.deposit(500)
print(acc1.balance)

acc2.deposit(500)
print(acc2.balance)


acc2.withdraw(500)
print(acc2.balance)
