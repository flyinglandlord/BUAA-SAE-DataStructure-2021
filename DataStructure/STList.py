import re
import math

integer_pat = '[+-]?\d+'
data = []
Lg = []
length = 0


if __name__ == '__main__':
    readline = input()
    l = re.findall(integer_pat, readline)
    n = int(l[0]); m = int(l[1])
    readline = input()
    l = re.findall(integer_pat, readline)
    for i in range(0, n):
        data.append(int(l[i]))
    Lg.append(0)
    Lg.append(0)
    for i in range(2, n+1):
        Lg[i] = Lg[i//2] + 1
    MAXN = int(math.log2(n)) + 1
    st = [[] for i in range(0, MAXN)]
    for i in range(0, n):
        st[0].append(data[i])
        if i != 0 and i <= MAXN:
            for j in range(0, n):
                st[i].append(0)
    for i in range(1, MAXN):
        j = 0
        while j + (1 << i) <= n:
            st[j][i] = max(st[j][i-1], st[j - (1 << (i-1)) + 1][i-1])
            j += 1


