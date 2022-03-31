class DoubleLinklist:

    class _node:
        __slots__ = ['val', 'next', 'prev']

        def __init__(self, val: int, next, prev):
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, x: int) -> None:
        if self.head is None:
            self.head = self._node(x, None, None)
            self.head.next = self.head
            self.head.prev = self.head
            self.size += 1
        else:
            tail = self.head.prev
            new_node = self._node(x, self.head, self.head.prev)
            tail.next = new_node
            self.head.prev = new_node
            self.size += 1

    def delete(self, x: int) -> None:        # 默认删除节点必然在链表内
        if self.size == 0:
            return
        else:
            p = self.head
            if p.val == x:
                tail = self.head.prev
                self.head = self.head.next
                self.head.prev = tail
                tail.next = self.head
            else:
                while p.val != x:
                    p = p.next
                p.prev.next = p.next
                p.next.prev = p.prev
            self.size -= 1


if __name__ == '__main__':
    l = DoubleLinklist()
    n = int(input())
    m = int(input())
    for i in range(0, n):
        l.insert(i+1)
    cnt = 0
    p = l.head
    while l.size > 1:
        # print(p.val)
        cnt += 1
        if cnt == m:
            l.delete(p.val)
            cnt = 0
        """
        i = l.size
        t = l.head
        while i > 0:
            print(t.val, end=' ')
            t = t.next
            i -= 1
        print()
        """
        p = p.next
    print(l.head.val)
