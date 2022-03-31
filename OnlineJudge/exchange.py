if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    if len(s) != len(t):
        print("False")
        exit(0)
    pair = []
    i = 0
    cnt = 0
    while i < len(s):
        if s[i] != t[i]:
            pair.append(i)
            cnt += 1
        i += 1
    if len(s) == 2:
        if s[1] == t[0] and s[0] == t[1]:
            print("True")
        else:
            print("False")
    elif len(s) == 3 and cnt == 0:
        if s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
            print("True")
        else:
            print("False")
    elif cnt == 2 or cnt == 0:
        print("True")
    else:
        print("False")
