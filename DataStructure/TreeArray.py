import re

data = []
C = []
n = 0


def lowbit(x):
    return x & (-x)


def add(i, x, MAXN):
    pos = i
    data[i] += x
    while pos <= MAXN:
        C[pos] += x
        pos += lowbit(pos)
        # print(pos)


def query(i):
    sum = 0
    pos = i
    while pos > 0:
        sum += C[pos]
        pos -= lowbit(pos)
    return sum


def sum(l, r):
    if l != 0:
        return query(r) - query(l-1)
    else:
        return query(r)


if __name__ == '__main__':
    readline = input()
    integer_pat = re.compile('[+-]?\d+')
    l = re.findall(integer_pat, readline)
    n = int(l[0])
    m = int(l[1])
    readline = input()
    l = re.findall(integer_pat, readline)
    data.append(0)
    C.append(0)
    for i in l:
        data.append(int(i))
        C.append(0)
    for i in range(1, n+1):
        add(i, data[i], n)
    while m > 0:
        readline = input()
        l = re.findall(integer_pat, readline)
        # print(l)
        op = int(l[0])
        a = int(l[1])
        b = int(l[2])
        if op == 1:
            add(a, b, n)
        elif op == 2:
            print(sum(a, b))
        m -= 1
