if __name__ == '__main__':
    stack = []
    readline = input().strip().split()
    nums = []
    for i in readline:
        nums.append(int(i))
    for i in nums:
        while len(stack) > 0 and stack[len(stack)-1] <= i:
            stack.pop()
        stack.append(i)
    while len(stack) > 0:
        print(stack.pop(), end=' ')
