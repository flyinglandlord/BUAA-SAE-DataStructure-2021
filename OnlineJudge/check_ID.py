if __name__ == '__main__':
    id_num = input()
    id_num = id_num.strip()
    list_char = list(id_num)
    list_num = [None for i in range(0, len(list_char))]
    ans = [1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(0, len(list_char)):
        if list_char[i] == 'X':
            list_num[i] = 10
        else:
            list_num[i] = int(list_char[i])
    const_weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    sum = 0
    for i in range(0, len(list_num)-1):
        sum += list_num[i] * const_weight[i]
    if ans[sum % 11] == list_num[len(list_num)-1]:
        print("YES")
    else:
        print("NO")
