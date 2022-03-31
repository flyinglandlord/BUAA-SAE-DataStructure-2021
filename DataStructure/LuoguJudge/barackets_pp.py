class Stack:
    def __init__(self):
        self.item = []
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, v):
        self.item.append(v)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Empty")
        else:
            self.size -= 1
            return self.item.pop()

    def top(self):
        if self.is_empty():
            raise Exception("Empty")
        else:
            return self.item[self.size - 1]


if __name__ == '__main__':
    s = input()
    l = [None] * len(s)
    temp = Stack()
    check = Stack()

    for i in range(0, len(s)):
        if s[i] == '(' or s[i] == '[':
            check.push(i)
        elif s[i] == ')':
            if not check.is_empty():
                r = check.top()
            if check.is_empty() or s[r] != '(':
                l[i] = '('
            else:
                check.pop()
        elif s[i] == ']':
            if not check.is_empty():
                r = check.top()
            if check.is_empty() or s[r] != '[':
                l[i] = '['
            else:
                check.pop()
    while not check.is_empty():
        if s[check.top()] == '(':
            l[check.pop()] = ')'
        elif s[check.top()] == '[':
            l[check.pop()] = ']'

    for i in range(0, len(s)):
        if l[i] is not None:
            if l[i] == '(' or l[i] == ')':
                print('()', end='')
            else:
                print('[]', end='')
        else:
            print(s[i], end='')
# (()[()
# ([)]
# (())
# (()][)