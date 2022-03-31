class SplayTree:
    _INF = 2147483647

    class _Node:
        __slots__ = '_father', '_lson', '_rson', '_cnt', '_size', '_val'

        def __init__(self, val, fa, lson=None, rson=None, cnt=1, size=1):
            self._father = fa
            self._lson = lson
            self._rson = rson
            self._cnt = cnt
            self._size = size
            self._val = val

        def _is_left_child(self):
            return self._father._lson is self

        def _update(self):
            self._size = 0
            if self._lson is not None:
                self._size += self._lson._size
            if self._rson is not None:
                self._size += self._rson._size
            self._size += self._cnt

    # private method
    def __init__(self):
        self._root = None

    def _get_size(self, p):
        if p is not None:
            return p._size
        else:
            return 0

    def _get_cnt(self, p):
        if p is not None:
            return p._cnt
        else:
            return 0

    def _relink(self, parent, child, make_left_child):
        if make_left_child:
            parent._lson = child
        else:
            parent._rson = child
        if child is not None:
            child._father = parent

    def _rotate(self, x):
        y = x._father
        z = y._father
        if z is None:
            self._root = x
            x._father = None
        else:
            self._relink(z, x, y == z._lson)
        if x == y._lson:
            self._relink(y, x._rson, True)
            self._relink(x, y, False)
        else:
            self._relink(y, x._lson, False)
            self._relink(x, y, True)
        y._update()
        x._update()

    def _splay(self, x, to):
        to = to._father
        while x._father != to:
            if x._father._father == to:
                self._rotate(x)
            elif (x._is_left_child() and x._father._is_left_child()) or (not x._is_left_child() and not x._father._is_left_child()):
                self._rotate(x._father)
                self._rotate(x)
            else:
                self._rotate(x)
                self._rotate(x)

    # public method
    def insert(self, val):
        if self._root is None:
            self._root = self._Node(val, None)
            return
        i = self._root
        while True:
            if i._val == val:
                i._cnt += 1
                self._splay(i, self._root)
                return
            nxt = i._lson if val < i._val else i._rson
            if nxt is None:
                if val < i._val:
                    i._lson = self._Node(val, i)
                else:
                    i._rson = self._Node(val, i)
                self._splay(i._lson if val < i._val else i._rson, self._root)
                return
            i = nxt

    def searchPoint(self, val):
        i = self._root
        while i is not None:
            if i._val == val:
                self._splay(i, self._root)
                return i
            i = i._lson if val < i._val else i._rson
        return None

    def delete(self, val):
        pos = self.searchPoint(val)
        if pos is None:
            return
        if pos._cnt > 1:
            pos._cnt -= 1
            pos._size -= 1
            return
        if pos._lson is None and pos._rson is None:
            self._root = None
        elif pos._lson is None:
            self._root = pos._rson
            self._root._father = None
        else:
            i = pos._lson
            while i._rson is not None:
                i = i._rson
            self._splay(i, pos._lson)
            self._relink(i, pos._rson, False)
            i._father = None
            pos = None
            self._root = i
            self._root._update()

    def searchNext(self, val):
        i = self._root
        ans = self._INF
        while i is not None:
            if i._val <= val:
                if i._rson is None:
                    return ans
                else:
                    i = i._rson
            else:
                if i._lson is None:
                    return i._val
                else:
                    ans = i._val
                    i = i._lson
        return ans

    def searchPrev(self, val):
        i = self._root
        ans = -self._INF
        while i is not None:
            if i._val >= val:
                if i._lson is not None:
                    i = i._lson
                else:
                    return ans
            else:
                if i._rson is None:
                    return i._val
                else:
                    ans = i._val
                    i = i._rson
        return ans

    def kth(self, k):
        i = self._root
        rk = 0
        while i is not None:
            if rk + self._get_size(i._lson) >= k:
                i = i._lson
            elif rk + self._get_size(i._lson) + self._get_cnt(i) >= k:
                return i._val
            else:
                rk += self._get_size(i._lson) + self._get_cnt(i)
                i = i._rson
        return None

    def rank(self, val):
        pos = self.searchPoint(val)
        return self._get_size(pos._lson) + 1


if __name__ == '__main__':
    t = SplayTree()
    node_list = [44, 17, 8, 32, 29, 88, 65, 97, 54, 82, 76, 93]
    for i in node_list:
        t.insert(i)
    t.delete(44)
    print(t.searchNext(32))
    #print(t._root._val)
    #print(t._root._lson._lson._val, t._root._lson._lson._size)
    #print(t._root._lson._lson._rson)
    #print(t._root._lson._val)

