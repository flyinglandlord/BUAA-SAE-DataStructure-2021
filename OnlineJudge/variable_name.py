if __name__ == '__main__':
    name = input()
    l = list(name)
    for i in range(0, len(l)):
        if l[i] >= 'A' and l[i] <= 'Z' and i != 0:
            print('_', end='')
            print(l[i].lower(), end='')
        elif l[i] >= 'A' and l[i] <= 'Z' and i == 0:
            print(l[i].lower(), end='')
        else:
            print(l[i], end='')

