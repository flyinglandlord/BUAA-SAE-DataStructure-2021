import math

from CreditCard import CreditCard


class AdvancedCreditCard(CreditCard):

    def __init__(self, customer, bank, limit, account, apr, balance=0):
        super().__init__(customer, bank, limit, account, balance)
        self._apr = apr

    def charge(self, price):
        request = super().charge(price)
        if not request:
            self._balance += 5
        return request

    def process_monthly(self):
        if self._balance > 0:
            mpr = math.pow(1 + self._apr, 1 / 12)
        self._balance *= mpr

    def __str__(self):
        return super().__str__()


if __name__ == '__main__':
    visa = AdvancedCreditCard("John", 'Bank of China', 10000, '3451 2021 2021 22000', 0.05)
    print(str(visa))
