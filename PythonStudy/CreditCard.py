class CreditCard:

    def __init__(self, customer, bank, limit, account, balance=0):
        self._customer = customer
        self._balance = balance
        self._bank = bank
        self._limit = limit
        self._account = account

    def get_customer(self):
        return self._customer

    def get_balance(self):
        return self._balance

    def get_limit(self):
        return self._limit

    def get_account(self):
        return self._account

    def make_payment(self, price):
        self._balance -= price

    def charge(self, price):
        if self._balance + price > self._limit:
            return False
        else:
            self._balance += price
            return True

    def __str__(self):
        return self._account

if __name__ == '__main__':
    visa = CreditCard("John", 'Bank of China', 10000, '3451 2021 2021 22000')
    print(str(visa))