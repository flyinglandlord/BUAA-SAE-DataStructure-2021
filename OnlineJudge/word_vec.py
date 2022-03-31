if __name__ == '__main__':
    data = []
    raw_data = input().split()
    k_word = input()
    for i in raw_data:
        found = False
        for j in range(0, len(data)):
            if i == data[j][0]:
                found = True
                data[j] = (i, data[j][1]+1)
                break
        if not found:
            data.append((i, 1))
    data.sort(key=lambda s: s[1], reverse=True)
    ans = []
    for i in range(0, len(data)):
        if data[i][0] == k_word:
            ans.append(1)
        else:
            ans.append(0)
    for i in ans:
        print(i, end=' ')