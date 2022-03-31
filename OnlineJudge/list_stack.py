if __name__ == '__main__':
    stack = []
    ans = []
    n = int(input())
    for i in range(0, n):
        x = int(input())
        stack.append(x)
    m = int(input())
    for i in range(0, m):
        op = input()
        if op[0] == 'A':
            opt = op.split(' ')
            x = int(opt[1])
            stack.append(x)
        elif op[0] == 'B':
            if len(stack) > 0:
                ans.append(stack.pop())
            else:
                print("No")
                ans.clear()
                break
    for i in range(0, len(ans)):
        print(ans[i], end=' ')
    print()
    while len(stack) > 0:
        print(stack.pop(), end=' ')

