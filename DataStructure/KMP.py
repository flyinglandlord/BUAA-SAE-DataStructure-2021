def KMP(s, t):
    fail = [0 for i in range(0, len(t))]
    fail[0] = -1
    ans = []
    i = 1

    # 计算fail失配数组
    while i < len(t):
        j = fail[i-1]
        while j != -1 and t[j+1] != t[i]: j = fail[j]
        if t[j+1] == t[i]: fail[i] = j + 1
        else: fail[i] = -1
        i += 1

    print(fail)

    # 利用fail失配数组匹配
    i = 0
    j = 0
    while i < len(s):
        print(i, j)
        if s[i] == t[j]:
            i += 1
            j += 1
            if j == len(t):
                ans.append(i - len(t) + 1)
                j = fail[j - 1] + 1
        elif j != -1: j = fail[j-1] + 1
        else: i += 1
    return ans
# Final Version, when we need to solve a KMP Problem, we should use the template above
# Remember the template!!!

def KMP_try(s, t):
    ans = []
    fail = [0 for i in range(0, len(t))]
    fail[0] = -1
    i = 1
    while i < len(t):
        j = fail[i-1]
        while t[j+1] != t[i] and j != -1: j = fail[j]
        if t[j+1] == t[i]: fail[i] = j+1
        else: fail[i] = -1
        i += 1
    i = 0
    j = 0
    while i < len(s):
        if s[i] == t[j]:
            i += 1
            j += 1
            if j == len(t):
                ans.append(i - len(t) + 1)
                j = fail[j-1]+1
        elif j > 0: j = fail[j-1]+1
        else: i += 1
    return ans


def another_KMP(s: str, t: str) -> list:
    fail = [0 for i in range(0, len(t))]        #fail数组的含义是t串最长的相同前后缀的长度
    ans = []
    i = 1
    while i < len(t):
        j = fail[i-1]
        while t[j] != t[i] and j != 0: j = fail[j]
        if t[j] == t[i]: fail[i] = j+1
        else: fail[i] = 0
        i += 1
    i = 0
    j = 0
    while i < len(s):
        if s[i] == t[j]:
            i += 1
            j += 1
            if j == len(t):
                ans.append(i - len(t) + 1)
                j = fail[j-1]
        elif j > 0: j = fail[j-1]
        else: i += 1
    return ans
    



if __name__ == '__main__':
    s = input()     # s - 待匹配字符串
    t = input()     # t - 要在s中匹配的字符串
    ans = another_KMP(s, t)
    print(ans)
