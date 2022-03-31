from Exception import Empty


class CircularQueue:
    """
    用单向环形链表维护一个循环队列，只需维护tail指针即可，因为tail指针指向队尾，next即为head
    """

    class _Node:
        __slots__ = '_value', '_next'

        def __init__(self, val, nxt):
            self._value = val
            self._next = nxt

    def __init__(self):
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def enqueue(self, val):
        add = self._Node(val, None)
        if self.is_empty():
            add._next = add
            self._tail = add
        else:
            add._next = self._tail._next
            self._tail._next = add
            self._tail = self._tail._next
        self._size += 1

    def rotate(self):
        self._tail = self._tail._next

    def dequeue(self):
        if self.is_empty():
            raise Empty("The Queue is Empty!")
        head = self._tail._next
        answer = head._value
        self._tail._next = head._next
        self._size -= 1
        return answer

    def first(self):
        if self.is_empty():
            raise Empty("The Queue is Empty!")
        head = self._tail._next
        return head._value


if __name__ == '__main__':
    Q = CircularQueue()
    for i in range(5):
        Q.enqueue(i)
        Q.rotate()
        print(Q.first())

    for i in range(5):
        print(Q.dequeue())