from threading import Thread, Lock


class BankAccount:

    def __init__(self, name='', balance=0):
        self.name = name
        self.balance = balance
        self.__lock = Lock()

    def deposit(self, amount):
        with self.__lock:
            self.balance += amount
            print(f'{self.name}: Deposited {amount}, new balance is {self.balance}')

    def withdraw(self, amount):
        with self.__lock:
            self.balance -= amount
            print(f'{self.name}: Withdrew {amount}, new balance is {self.balance}')

    def get_balance(self):
        return self.balance


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


if __name__ == '__main__':
    account = BankAccount('Account 1', 1000)

    deposit_thread = Thread(target=deposit_task, args=(account, 100))
    withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

    deposit_thread.start()
    withdraw_thread.start()

    deposit_thread.join()
    withdraw_thread.join()
