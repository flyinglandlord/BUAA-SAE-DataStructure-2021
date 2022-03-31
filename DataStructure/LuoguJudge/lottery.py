if __name__ == '__main__':
    n = int(input())
    mag_num = []
    prize = []
    for i in range(0, 8):
        prize.append(0)
    readline = input()
    readline = readline.strip('\n').strip('\r').strip()     #Python读取整行数据时务必删除行首行尾的回车与空格，否则读整数会出问题
    data = readline.split(' ')
    for i in data:
        mag_num.append(int(i))
    for i in range(0, n):
        lottery = []
        readline = input()
        readline = readline.strip('\n').strip('\r').strip()
        data = readline.split(' ')
        for j in data:
            lottery.append(int(j))
        cnt = 0
        for j in mag_num:
            if j in lottery:
                cnt += 1
        prize[7 - cnt] += 1
    print(' '.join([str(prize[i]) for i in range(0, 7)]))
