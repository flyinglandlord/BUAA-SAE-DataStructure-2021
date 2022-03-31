import re

if __name__ == '__main__':
    s = input()
    integer = re.compile(r"[+-]?\d+")
    ans = re.findall(integer, s)
    if len(ans) == 2 and int(ans[1]) != 0:
        print(int(ans[0]) // int(ans[1]))
    else:
        print("No")