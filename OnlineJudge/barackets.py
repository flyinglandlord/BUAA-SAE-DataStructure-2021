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
    check = Stack()

    for i in range(0, len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{' or s[i] == '<':
            check.push(i)
        elif s[i] == ')':
            if not check.is_empty():
                r = check.top()
            if s[r] == '(':
                check.pop()
        elif s[i] == ']':
            if not check.is_empty():
                r = check.top()
            if s[r] == '[':
                check.pop()
        elif s[i] == '}':
            if not check.is_empty():
                r = check.top()
            if s[r] == '{':
                check.pop()
        elif s[i] == '>':
            if not check.is_empty():
                r = check.top()
            if s[r] == '<':
                check.pop()
    if not check.is_empty():
        print("No")
    else:
        print("Yes")

# (()[()
# ([)]
# (())
# (()][)