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
    temp = Stack()
    check = Stack()

    for i in range(0, len(s)):
        if s[i] == '(':
            check.push(s[i])
        elif s[i] == '[':
            check.push(s[i])
        elif s[i] == ')':
            #check.push(s[i])
            flag = True
            while not check.is_empty() and check.top() != '(' and check.top() != 'r(':
                r = check.pop()
                if r[0] != 'r':
                    flag = False
                temp.push(r)
            if not check.is_empty() and flag:
                check.pop()
                check.push("r(")
                while not temp.is_empty():
                    check.push(temp.pop())
                #check.pop()
                check.push("r)")
            else:
                while not temp.is_empty():
                    check.push(temp.pop())
                check.push(s[i])
        elif s[i] == ']':
            #check.push(s[i])
            flag = True
            while not check.is_empty() and check.top() != '[' and check.top() != 'r[':
                r = check.pop()
                if r[0] != 'r':
                    flag = False
                temp.push(r)
            if not check.is_empty() and flag:
                check.pop()
                check.push("r[")
                while not temp.is_empty():
                    check.push(temp.pop())
                #check.pop()
                check.push("r]")
            else:
                while not temp.is_empty():
                    check.push(temp.pop())
                check.push(s[i])

    while not check.is_empty():
        temp.push(check.pop())

    while not temp.is_empty():
        r = temp.top()
        # print(r)
        if r[0] == 'r':
            print(r[1], end='')
        elif r == '(' or r == ')':
            print('()', end='')
        elif r == '[' or r == ']':
            print('[]', end='')
        temp.pop()
# (()[()
# ([)]
# (())
# (()][)