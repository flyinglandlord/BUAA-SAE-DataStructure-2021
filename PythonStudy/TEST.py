def draw(cube, num, x, y):
    if x == 0 and y != n-1:
        x, y = n-1, y+1
        cube[x][y] = num
        return x, y
    if y == n-1 and x != 0:
        x, y = x-1, 0
        cube[x][y] = num
        return x, y
    if x == 0 and y == n-1:
        x, y = x+1, y
        cube[x][y] = num
        return x, y
    if x != 0 and y != n-1:
        if cube[x-1][y+1] == 0:
            x, y = x-1, y+1
            cube[x][y] = num
            return x, y
        else:
            x, y = x+1, y
            cube[x][y] = num
            return x, y

if __name__ == '__main__':
    n = int(input())
    cube = [[] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            cube[i].append(0)
    cube[0][n//2] = 1
    x, y = 0, n//2
    i = 2
    while i <= n**2:
        x, y = draw(cube, i, x, y)
        i += 1
    for i in range(0, n):
        print(' '.join([str(i) for i in cube[i]]))