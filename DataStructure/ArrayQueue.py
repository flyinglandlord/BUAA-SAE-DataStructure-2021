from Exception import Empty


class ArrayQueue(object):    # 通过循环使用list实现一个队列

    DEFAULT_CAPACITY = 5

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0
        self._capacity = ArrayQueue.DEFAULT_CAPACITY

    def _resize(self, cap):
        """
        调整队列最大容量

        :param cap: 新的容量大小
        :return: 无
        """
        old_data = self._data
        self._data = [None] * cap
        i = 0
        while i < self._size:
            self._data[i] = old_data[(self._front + i) % self._capacity]
            i += 1
        self._front = 0
        self._capacity = cap

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        """
        向队列Q的末尾添加一个元素

        :param e: 要添加的元素
        :return: 无
        """
        if self._size == len(self._data):
            self._resize(self._size * 2)
        self._data[(self._front + self._size) % self._capacity] = e
        self._size += 1

    def dequeue(self):
        """
        从队列Q中移除并返回队首的元素，如果队列为空抛出Empty异常

        :return: 队首元素
        """
        if self.is_empty():
            raise Empty("The Queue is Empty!")
        if self._capacity >= 4 * self._size and self._size >= 5:
            self._resize(self._capacity // 2)
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return self._data[self._front - 1]

    def first(self):
        """
        返回队首元素，如果队列为空抛出Empty异常

        :return:队首元素
        """
        if self.is_empty():
            raise Empty("The Queue is Empty!")
        # print(self._front)
        return self._data[self._front]

    def __len__(self):
        return self._size


if __name__ == "__main__":
    Q = ArrayQueue()
    for i in range(10):
        Q.enqueue(i)

    for i in range(11):
        try:
            print(Q.dequeue())
        except Empty:
            print("The Queue is Empty! Now i = {0}".format(i))