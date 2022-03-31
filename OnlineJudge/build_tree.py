def get_son(tr, x):
    if x >= len(tr) or tr[x] == 'None':
        return None
    return tr[x]


def postorder_travel_nonrecursion(tr):
    st_a = []
    st_a.append(0)
    st_b = []
    while len(st_a) > 0:
        p = st_a.pop()
        st_b.append(p)
        if get_son(tr, 2*p+1) is not None:
            st_a.append(2*p+1)
        if get_son(tr, 2*p+2) is not None:
            st_a.append(2*p+2)
    while len(st_b) > 0:
        print(tr[st_b.pop()], end=' ')


def layerorder_travel(tr):
    qu = []
    qu.append(0)
    while len(qu) > 0:
        p = qu.pop(0)
        print(tr[p], end=' ')
        if get_son(tr, 2*p+1) is not None:
            qu.append(2*p+1)
        if get_son(tr, 2*p+2) is not None:
            qu.append(2*p+2)


def inorder_travel_nonrecursion(tr):
    st = []
    r = 0
    while len(st) > 0 or get_son(tr, r) is not None:
        if get_son(tr, r) is not None:
            st.append(r)
            r = 2*r+1
        else:
            r = st.pop()
            print(tr[r], end=' ')
            r = 2*r+2


def inorder_travel_recursion(tr, p):
    if get_son(tr, 2*p+1) is not None:
        inorder_travel_recursion(tr, 2*p+1)
    print(tr[p], end=' ')
    if get_son(tr, 2*p+2) is not None:
        inorder_travel_recursion(tr, 2*p+2)


def preorder_travel_nonrecursion(tr):
    st = []
    r = 0
    while get_son(tr, r) is not None or len(st) > 0:
        if get_son(tr, r) is not None:
            print(tr[r], end=' ')
            st.append(r)
            r = 2*r+1
        else:
            r = st.pop()
            r = 2*r+2


if __name__ == '__main__':
    total = 0
    tr = input().strip().split()
    postorder_travel_nonrecursion(tr)