if __name__ == '__main__':
    text = input()
    text = text.lower()
    l = list(text)
    i = 0
    while i < len(l):
        if i == 0:
            print(l[i].upper(), end='')
        elif l[i] == 'i' and (l[i-1] == ' ' or l[i-1] == '.' or l[i-1] == ',') and (l[i+1] == ' ' or l[i+1] == '.' or l[i+1] == ','):
            print(l[i].upper(), end='')
        elif (l[i] == '.') and i != len(l)-1:
            while i < len(l) and not l[i].isalpha():
                print(l[i], end='')
                i += 1
            print(l[i].upper(), end='')
        else:
            print(l[i], end='')
        i += 1
