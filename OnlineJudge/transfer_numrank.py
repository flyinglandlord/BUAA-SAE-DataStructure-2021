if __name__ == '__main__':
    readline = input()
    mn = readline.strip().split(' ')
    n = int(mn[0])
    m = int(mn[1])
    stack = []

    if n == 0:
        stack.append(0)

    while n > 0:
        stack.append(n % m)
        n = n//m

    while len(stack) > 0:
        x = stack.pop()
        if x < 10:
            print(x, end='')
        else:
            print(chr(x - 10 + ord("A")), end='')

