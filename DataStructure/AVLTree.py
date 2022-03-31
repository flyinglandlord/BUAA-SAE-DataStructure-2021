class AVLTree:

    class _Node:
        __slots__ = ['lson', 'rson', 'cnt', 'size', 'val', 'height']

        def __init__(self, val, lson=None, rson=None, cnt=1, size=1, height=1):
            self.lson = lson
            self.rson = rson
            self.cnt = cnt
            self.size = size
            self.val = val
            self.height = height

        def update(self):
            self.size = 0
            if self.lson is not None:
                self.size += self.lson.size
            if self.rson is not None:
                self.size += self.rson.size
            self.size += self.cnt
            self.height = max(self.lson.height if self.lson is not None else 0, self.rson.height if self.rson is not None else 0) + 1

    def __init__(self):
        self.root = None

    def get_val(self, p):
        if p is None:
            return None
        else:
            return p.val

    def get_size(self, p):
        if p is None:
            return 0
        else:
            return p.size

    def get_cnt(self, p):
        if p is None:
            return 0
        else:
            return p.cnt

    def get_height(self, p):
        if p is None:
            return 0
        else:
            return p.height

    def lrotate(self, node):
        tmp = node.rson
        node.rson = tmp.lson
        tmp.lson = node
        node.update()
        tmp.update()
        return tmp

    def rrotate(self, node):
        tmp = node.lson
        node.lson = tmp.rson
        tmp.rson = node
        node.update()
        tmp.update()
        return tmp

    def _add(self, node, key):
        # print(node)
        if node is None:
            node = self._Node(key)
            # print(node)
            return node
        if key < node.val:
            node.lson = self._add(node.lson, key)
            node.update()
            if self.get_height(node.lson) - self.get_height(node.rson) >= 2:
                if key <= node.lson.val:
                    node = self.rrotate(node)
                    node.update()
                else:
                    node.lson = self.lrotate(node.lson)
                    node = self.rrotate(node)
                    node.update()
        elif key > node.val:
            node.rson = self._add(node.rson, key)
            node.update()
            # print(node.rson, key)
            if self.get_height(node.rson) - self.get_height(node.lson) >= 2:
                if key >= node.rson.val:
                    node = self.lrotate(node)
                    node.update()
                else:
                    node.rson = self.rrotate(node.rson)
                    node = self.lrotate(node)
                    node.update()
        else:
            self.cnt += 1
        return node

    def add(self, key):
        if self.root is None:
            self.root = self._Node(key)
        else:
            self.root = self._add(self.root, key)


def Travel(node):
    if node == None:
        return
    print(node.val, end=' ')
    Travel(node.lson)
    Travel(node.rson)

if __name__ == '__main__':
    t = AVLTree()
    d = input().strip().split();
    l = [int(x) for x in d]
    for i in l:
        t.add(i)
        # Travel(t.root)
        # print(t.get_height(t.root.lson), t.get_height(t.root.rson))
        # print()
        # print(t.root.val)
    Travel(t.root)
    #print(t.root.lson.val)

