def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False


def is_even(k):         #Cannot use /, *, % in the function?
    if not isinstance(k, (int, float)):
        raise TypeError('Wrong data format')
    if k & 1 == 0:
        return True
    else:
        return False


def minmax(data):
    minn = data[0]
    maxn = data[0]
    for i in data:
        try:
            maxn = i if i > maxn else maxn
            minn = i if i < minn else minn
        except TypeError:
            print('Wrong data format')
            return None
    return minn, maxn


n = 10

print(sum([i * i for i in range(1, n+1) if is_even(i) is False]))       # calculate the sum of odd number

print([2**x for x in range(0, 9)])

print(list(range(50, 81, 10)))

print(list(range(8, -10, -2)))

from random import randrange, seed
from time import time

def choice(data):
    seed(time())
    return data[randrange(0, len(data))]

print(choice([1,2,3,4,5]))

d = [1,2,3,4,5]
for i in d:
    i = 1
    print('$')

print(d)