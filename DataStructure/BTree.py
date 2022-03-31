import math


class BTreeNode:
    def __init__(self, father=None):
        self.keys = []
        self.children = []
        self.father = father

    def insert(self, val):
        if val in self.keys:
            pass
        else:
            self.keys.append(val)
            self.keys.sort()
        return len(self.keys)


class BTree:
    def __init__(self, m=3):
        self.root = None
        self.M = m      # 这里应当是阶数
        self.root: BTreeNode = BTreeNode()

    def insert(self, key):
        node = self.root
        while node.children:
            res = None
            for i in range(len(node.keys)):
                if node.keys[i] > key:
                    res = node.children[i]
                    break
                elif node.keys[i] == key:
                    return
            if key > node.keys[len(node.keys)-1]:
                res = node.children[len(node.keys)]
            if res is None:
                break
            else:
                node = res
        # print('#', node.keys)
        new_length = node.insert(key)
        if new_length == self.M:
            self.__split_tree(node)

    def __split_tree(self, node: BTreeNode):
        if len(node.keys) <= self.M - 1:
            return
        mid = (self.M - 1) // 2
        mid_val = node.keys[mid]
        new_left_node = BTreeNode()
        new_right_node = BTreeNode()
        for i in range(mid):
            new_left_node.keys.append(node.keys[i])
        for i in range(mid+1, len(node.keys)):
            new_right_node.keys.append(node.keys[i])
        # print(new_right_node.keys, new_left_node.keys)
        if node.children:
            for i in range(mid+1):
                new_left_node.children.append(node.children[i])
                new_left_node.children[i].father = new_left_node
            for i in range(mid+1, len(node.children)):
                new_right_node.children.append(node.children[i])
                new_right_node.children[i - mid - 1].father = new_right_node
        if node.father is None:
            new_root = BTreeNode()
            new_root.keys.append(mid_val)
            new_right_node.father = new_root
            new_left_node.father = new_root
            new_root.children.append(new_left_node)
            new_root.children.append(new_right_node)
            self.root = new_root
            return
        else:
            # print(new_right_node.keys, new_left_node.keys)
            parent = node.father
            new_right_node.father = parent
            new_left_node.father = parent
            i = len(parent.keys)
            parent.keys.append(mid_val)
            parent.children.append(None)
            while i > 0 and parent.keys[i-1] > mid_val:
                parent.keys[i] = parent.keys[i-1]
                parent.children[i+1] = parent.children[i]
                i -= 1
            parent.keys[i] = mid_val
            parent.children[i] = new_left_node
            parent.children[i+1] = new_right_node
            self.__split_tree(parent)

    def level_travel(self):
        if not self.root:
            return
        q = []
        q.append(self.root)
        while len(q) > 0:
            x = q.pop(0)
            for i in x.keys:
                print(i, end=' ')
            for i in range(len(x.children)):
                if x.children[i] is not None:
                    q.append(x.children[i])


if __name__ == '__main__':
    t = BTree()
    m = int(input())
    t.M = m
    l = input().strip().split()
    d = [int(x) for x in l]
    for i in d:
        t.insert(i)
        # t.level_travel()
        # print()
    t.level_travel()


