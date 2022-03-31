from Exception import Empty


class LinkedStack:      # 用单向链表实现栈

    class _Node:
        __slots__ = 'value', 'next'

        def __init__(self, val, next):
            self.value = val
            self.next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def pop(self):
        if self.is_empty():
            raise Empty("The Stack is Empty!")
        answer = self._head.value
        self._head = self._head.next
        self._size -= 1
        return answer

    def top(self):
        if self.is_empty():
            raise Empty("The Stack is Empty!")
        return self._head.value

    def push(self, e):
        """
        把元素e压入栈中

        :param e: 待压入的元素
        :return: 无
        """
        if self._head is None:
            self._head.value = e
        else:
            self._head = self._Node(e, self._head.next)
        self._size += 1


if __name__ == '__main__':
    pass