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


def infix_to_postfix(expr):
    expr_ans = []
    priority = {}
    priority['+'] = 2
    priority['-'] = 2
    priority['('] = 1
    priority['*'] = 3
    priority['/'] = 3
    optStack = Stack()
    i = 0
    if expr[i] == '-':
        optStack.push(expr[i])
        expr_ans.append('0')
        expr_ans.append(' ')
        i += 1
    while i < len(expr):
        if expr[i] == '(':
            optStack.push(expr[i])
        elif expr[i] == '+' or expr[i] == '-' or expr[i] == '*' or expr[i] == '/':
            if expr[i] == '-' and expr[i-1] == '(':
                optStack.push('(')
                expr_ans.append('0')
                expr_ans.append(' ')
                optStack.push(expr[i])
                i += 1
                continue
            while not optStack.is_empty() and priority[optStack.top()] >= priority[expr[i]]:
                expr_ans.append(optStack.pop())
            optStack.push(expr[i])
        elif expr[i] == ')':
            while not optStack.is_empty() and optStack.top() != '(':
                expr_ans.append(optStack.pop())
            if optStack.is_empty():
                raise Exception("Expression Invalid!")
            else:
                optStack.pop()
        elif ord('0') <= ord(expr[i]) <= ord('9'):
            while i < len(expr) and ord('0') <= ord(expr[i]) <= ord('9'):
                expr_ans.append(expr[i])
                i += 1
            expr_ans.append(' ')
            i -= 1
        else:
            pass
        i += 1
    while not optStack.is_empty():
        expr_ans.append(optStack.pop())
    return expr_ans


def calc(expr):
    numStack = Stack()
    i = 0
    while i < len(expr):
        if ord('0') <= ord(expr[i]) <= ord('9'):
            temp = 0
            while i < len(expr) and ord('0') <= ord(expr[i]) <= ord('9'):
                temp *= 10
                temp += ord(expr[i]) - ord('0')
                i += 1
            i -= 1
            numStack.push(temp)
        elif expr[i] == '+' or expr[i] == '-' or expr[i] == '*' or expr[i] == '/':
            if numStack.is_empty(): raise Exception("Expression Invalid")
            val1 = numStack.pop()
            if numStack.is_empty(): raise Exception("Expression Invalid")
            val2 = numStack.pop()
            if expr[i] == '+':
                numStack.push(val1 + val2)
            elif expr[i] == '-':
                numStack.push(val2 - val1)
            elif expr[i] == '*':
                numStack.push(val1 * val2)
            elif expr[i] == '/':
                numStack.push(val1 // val2)
        else:
            pass
        i += 1
    return numStack.top()


if __name__ == '__main__':
    expr = input()
    expr_postfix = infix_to_postfix(expr)
    # print(expr_postfix)
    print(calc(expr_postfix))
# (12+5)*(-(25+5)) (())()()