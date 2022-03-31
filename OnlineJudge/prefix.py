if __name__ == '__main__':
    n: int = int(input())
    data: list = []
    for i in range(0, n):
        data.append(input().strip())

    prefix_len = 0

    for i in range(0, min([len(i) for i in data])):
        ch = data[0][i]
        # print(ch, prefix_len)
        flag = True
        for j in range(1, len(data)):
            if data[j][i] != ch:
                flag = False
                break
        if not flag:
            break
        prefix_len = i

    if prefix_len != 0:
        for i in range(0, prefix_len+1):
            print(data[0][i], end='')
    else:
        print("No")
