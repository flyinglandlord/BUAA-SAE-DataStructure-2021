from Exception import Empty


class ArrayDeque:

    DEFAULT_CAPACITY = 2

    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._front = 0
        self._rear = 0
        self._size = 0
        self._capacity = ArrayDeque.DEFAULT_CAPACITY

    def is_empty(self):
        return self._size == 0

    def _resize(self, cap):
        old_data = self._data
        self._data = [None] * cap
        for i in range(self._size):
            self._data[i] = old_data[(self._front + i) % self._capacity]
        self._front = 0
        self._rear = self._front + self._size
        self._capacity = cap

    def add_first(self, e):
        """
        向双端队列队首front位置添加元素e

        :param e: 待添加的元素
        :return: 无
        """
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._front = (self._front - 1) % self._capacity
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        """
        向双端队列队尾rear位置添加元素e

        :param e: 待添加的元素
        :return: 无
        """
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._rear] = e
        self._rear = (self._rear + 1) % self._capacity
        self._size += 1

    def first(self):
        if self.is_empty():
            raise Empty("The Deque is Empty!")
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Empty("The Deque is Empty!")
        return self._data[self._rear]

    def __len__(self):
        return self._size

    def delete_first(self):
        if self.is_empty():
            raise Empty("The Deque is Empty!")
        answer = self._data[self._front]
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return answer

    def delete_last(self):
        if self.is_empty():
            raise Empty("The Deque is Empty!")
        answer = self._data[self._rear]
        self._rear = (self._front + self._size - 1) % self._capacity
        self._size -= 1
        return answer

    def __str__(self):
        return ' '.join(str(self._data[(self._front + i) % self._capacity]) for i in range(self._size));


if __name__ == "__main__":
    D = ArrayDeque()
    D.add_last(5)
    print(D)
    D.add_first(3)
    print(D)
    D.add_first(7)
    print(D)
    D.delete_last()
    print(D)
    print(len(D))
    D.delete_last()
    print(D)
    D.delete_last()
    print(D)
    D.add_first(6)
    print(D)
    D.add_first(8)
    print(D)
    print(D.is_empty())