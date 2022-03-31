if __name__ == '__main__':
    data = []
    ans = []
    N = 0
    t = 0
    while True:
        try:
            readline = input()
            readline = readline.strip('\n').strip('\r').strip()
        except EOFError:
            break
        if readline == '':
            break
        data.append(list(readline))
        N = len(readline)
    i = 1
    print(N, end=' ')
    if data[0][0] == '1':
        print(0, end=' ')
    while i <= N*N:
        dig = data[(i-1)//N][(i-1)%(N)]
        cnt = 0
        while data[(i-1)//N][(i-1)%(N)] == dig:
            cnt += 1
            i += 1
            if i > N*N:
                break
        ans.append(cnt)
    print(' '.join([str(i) for i in ans]))

    