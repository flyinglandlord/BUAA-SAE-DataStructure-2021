if __name__ == '__main__':
    n = int(input())
    i = 0
    data = []
    while i < n:
        name = input()
        height = float(input())
        data.append((name, height))
        i += 1
    data.sort(key=lambda s: s[1], reverse=True)
    for i in range(0, len(data)):
        print(data[i][0], end=', ')
        print('%.2f' % data[i][1])