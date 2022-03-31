from Exception import Empty


class LinkedQueue:
    """
    考虑到单项链表表头容易进行删除，表尾容易进行删除操作
    我们把表头作为队首，表尾作为队尾
    """

    class _Node:
        __slots__ = '_value', '_next'

        def __init__(self, val, nxt):
            self._value = val
            self._next = nxt

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, val):
        if self._head is None:
            self._head = self._Node(val, None)
            self._tail = self._head
            self._size += 1
        else:
            self._tail._next = self._Node(val, None)
            self._size += 1
            self._tail = self._tail._next

    def dequeue(self):
        if self.is_empty():
            raise Empty("The Queue is Empty!")
        answer = self._head._value
        self._head = self._head._next
        self._size -= 1
        return answer

    def first(self):
        if self.is_empty():
            raise Empty("The Queue is Empty!")
        return self._head._value


if __name__ == '__main__':
    Q = LinkedQueue()
    for i in range(5):
        Q.enqueue(i)

    print(Q.dequeue())
    print(Q.first())

    for i in range(5):
        print(Q.dequeue())
