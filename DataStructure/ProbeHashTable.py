import random


class HashMapBase:
    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key

    def __init__(self, cap=11, p=109345121):
        self._table = cap * [None]
        self._size = 0
        self._prime = p
        self._scale = 1 + random.randrange(p-1)
        self._shift = random.randrange(p)

    def _bucket_getitem(self, item, h): pass
    def _bucket_setitem(self, h, k, v): pass
    def _bucket_delitem(self, h, k): pass

    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._size

    def _resize(self, newsize):
        old = list(self._table)
        self._table = newsize * [None]
        for (k, v) in old:
            self._table[k] = v

    def __getitem__(self, item):
        h = self._hash_function(item)
        return self._bucket_getitem(h, item)

    def __setitem__(self, key, value):
        h = self._hash_function(key)
        self._bucket_setitem(h, key, value)
        if self._size > len(self._table)//2:
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, key):
        h = self._hash_function(key)
        self._bucket_delitem(h, key)
        self._size -= 1


class ProbeHashTable(HashMapBase):
    _EXIST = object()

    def __init__(self, cap=11, p=109245121):
        super().__init__(cap, p)

    def is_available(self, k):
        return self._table[k] is None or self._table[k] is self._EXIST

    def _find_bucket(self, index, key):
        available = None
        while True:
            if self.is_available(index):
                if available is None:
                    available = index
                if self._table[index] is None:
                    return False, available
            elif self._table[index]._key == key:
                return True, index
            index = (index+1) % len(self._table)

    def _bucket_getitem(self, h, k):
        found, pos = self._find_bucket(h, k)
        if found is False:
            raise KeyError('Key Error')
        return self._table[pos]._value

    def _bucket_setitem(self, h, k, v):
        found, pos = self._find_bucket(h, k)
        if found is True:
            self._table[pos] = self._Item(k, v)
            return
        else:
            self._table[pos] = self._Item(k, v)
            self._size += 1

    def _bucket_delitem(self, h, k):
        found, pos = self._find_bucket(h, k)
        if found is False:
            raise KeyError('Key Error')
        else:
            self._table[pos] = self._EXIST

    def __iter__(self):
        for i in range(len(self._table)):
            if not self.is_available(i):
                yield self._table[i]._key


if __name__ == '__main__' :
    t = ProbeHashTable()
    t['TsingHua University'] = 1
    t['Peking University'] = 2
    t['Fucking National Ins'] = 3
    for i in t:
        print(i + ' ' + str(t[i]))
    print()
    del t['TsingHua University']
    for i in t:
        print(i + ' ' + str(t[i]))
