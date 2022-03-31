if __name__ == '__main__':
    n = int(input())
    i = 0
    flag = True
    while i < n:
        try:
            data = input().strip().split(' ')
        except EOFError:
            break
        if len(data) != n:
            print("False")
            flag = False
            break
    if flag:
        print("True")
