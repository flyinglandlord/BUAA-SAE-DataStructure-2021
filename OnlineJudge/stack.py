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
    st = Stack()
    try:
        s = input()
    except EOFError:
        print('')
    else:
        for i in range(0, len(s)):
            if not st.is_empty():
                if st.top() == s[i]:
                    st.pop()
                else:
                    st.push(s[i])
            else:
                st.push(s[i])
    ans = Stack()
    while not st.is_empty():
        ans.push(st.pop())
    while not ans.is_empty():
        print(ans.pop(), end='')

# (()[()
# ([)]
# (())
# (()][)