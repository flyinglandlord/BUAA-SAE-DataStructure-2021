class Node(object):
    def __init__(self, val, cnt=1, left_child=None, right_child=None):
        self.left_child = left_child
        self.right_child = right_child
        self.val = val
        self.cnt = cnt


'''
二叉搜索树BST的实现
'''


class BST(object):
    def __init__(self, root=None):
        self.root = root

    def in_order_processor(self):
        in_order_processor(self.root)

    def maximum(self):
        return maximum(self.root)

    def minimum(self):
        return minimum(self.root)

    def successor(self, x):
        return successor(x)

    def search(self, x):
        return search(self.root, x)

    def insert(self, x):
        self.root = insert(self.root, x)

    def delete(self, x):
        self.root = delete(self.root, x)

    def insert_after_x(self, x, y):
        insert_after_x(self.root, x, y)


def maximum(root):
    while root.right_child is not None:
        root = root.right_child
    return root


def minimum(root):
    while root.left_child is not None:
        root = root.left_child
    return root


def in_order_processor(root):
    if root.left_child is not None:
        in_order_processor(root.left_child)
    print(root.val, root.cnt)
    if root.right_child is not None:
        in_order_processor(root.right_child)


def search(root, x):
    if root.val == x:
        return root
    elif root.val < x:
        return search(root.right_child, x)
    else:
        return search(root.left_child, x)


def insert(root, x):
    if not root:
        return Node(x)
    if x < root.val:
        root.left_child = insert(root.left_child, x)
    elif x > root.val:
        root.right_child = insert(root.right_child, x)
    else:
        root.cnt += 1
    return root


def insert_after_x(root, x, y):
    node = search(root, x)
    if y < x:
        node.left_child = Node(y)
    else:
        node.right_child = Node(y)


def delete(root, x):
    if root is None:
        return None
    if root.val < x:
        root.right_child = delete(root.right_child, x)
    elif root.val > x:
        root.left_child = delete(root.left_child, x)
    else:
        if root.cnt > 1:
            root.cnt -= 1
        elif root.left_child and root.right_child:
            t = root.right_child
            while t.left_child is not None:
                t = t.left_child
            root.val = t.val
            root.cnt = t.cnt
            root.right_child = delete(root.right_child, t.val)
        else:
            if root.left_child is None:
                root = root.right_child
            elif root.right_child is None:
                root = root.left_child
    return root


def successor(root, x):
    while root.val != x:
        par = root
        if x < root.val:
            root = root.left_child
        elif x > root.val:
            root = root.right_child
    if root.right_child is None:
        return root.right_child
    else:
        return par


zz
t = BST()
arr = [5, 1, 3, 2, 6, 4]
for i in arr:
    t.insert(i)

t.in_order_processor()

print(t.search(2).val)

t.insert_after_x(2, 7)

t.in_order_processor()
