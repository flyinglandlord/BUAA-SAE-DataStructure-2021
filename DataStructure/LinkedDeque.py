from Exception import Empty


class _DoubleLinklist:

    class _Node:
        __slots__ = '_value', '_prev', '_next'

        def __init__(self, val, pre, nxt):
            self._value = val
            self._prev = pre
            self._next = nxt

        @property
        def next(self):
            return self._next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def _insert_between(self, val, pre, nxt):
        add = self._Node(val, pre, nxt)
        pre._next = add
        nxt._prev = add
        self._size += 1
        return add

    def _delete_item(self, item):
        pre = item._prev
        nxt = item._next
        pre._next = nxt
        nxt._prev = pre
        self._size -= 1
        answer = item._value
        item._value = item._next = item._prev = None
        return answer


class LinkedDeque(_DoubleLinklist):

    def __init__(self):
        super().__init__()

    def first(self):
        if self.is_empty():
            raise Empty("The Deque is Empty!")
        return self._header._next._value

    def last(self):
        if self.is_empty():
            raise Empty("The Deque is Empty!")
        return self._trailer._prev._value

    def insert_first(self, val):
        self._insert_between(val, self._header, self._header._next)

    def insert_last(self, val):
        self._insert_between(val, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty("The Deque is Empty!")
        self._delete_item(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty("The Deque is Empty!")
        self._delete_item(self._trailer._prev)

    def __str__(self):
        answer = ""
        i = self._header
        while i is not self._trailer._prev:
            i = i._next
            answer += str(i._value) + ' '
        return answer


if __name__ == '__main__':
    L = LinkedDeque()
    L.insert_first(1)
    L.insert_last(3)
    L.insert_first(4)
    print(L)
