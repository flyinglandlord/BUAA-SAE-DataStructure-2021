import re

def BFS(g, start, N):
    q = []
    vis = [0] * (N+5)
    q.append(start)
    vis[start] = 1
    while len(q) > 0:
        x = q.pop(0)
        print(chr(x + ord('A')), end=' ')
        for i in range(N):
            if g[x][i] == 1 and vis[i] == 0:
                q.append(i)
                vis[i] = 1

if __name__ == '__main__':
    t_l = input().strip().split()
    N = int(t_l[0])
    start = t_l[1]
    mat = [[] for i in range(N+5)]
    for i in mat:
        for j in range(N+5):
            i.append(0)
    for i in range(N):
        line = input()
        p = re.compile("[A-Z]:[0-9]+")
        l = re.findall(p, line)
        for item in l:
            mat[ord(line[0]) - ord('A')][ord(item[0]) - ord('A')] = int(item[2:])
    """
    for i in range(N):
        for j in range(N):
            print(mat[i][j], end=' ')
        print()
    """

    BFS(mat, ord(start) - ord('A'), N)

