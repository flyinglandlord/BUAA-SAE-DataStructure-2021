from Exception import Empty


class ArrayStack:
    """
    使用Python自带的list实现一个栈
    """

    def __init__(self):
        self._data = []

    def push(self, e):
        """
        把一个元素e添加到栈顶

        :param e: 即将被添加的元素
        :return: 无
        """
        self._data.append(e)

    def is_empty(self):
        """
        返回栈是否为空

        :return: True/False
        """
        return len(self._data) == 0;

    def top(self):
        """
        返回栈顶元素，如果栈为空，则会抛出一个Empty异常

        :return: 栈顶元素
        """
        if self.is_empty():
            raise Empty("The Stack is Empty!")
        return self._data[-1]

    def pop(self):
        """
        返回栈顶元素，同时移除栈顶元素

        :return: 栈顶元素
        """
        if self.is_empty():
            raise Empty("The Stack is Empty!")
        answer = self._data[-1]
        self._data.pop()
        return answer


if __name__ == "__main__":
    s = ArrayStack()
    s.push(1)
    s.push(2)
    print(s.pop())
    print(s.pop())
    s.pop()
