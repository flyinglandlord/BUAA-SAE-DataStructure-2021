from Progression import Progression


class GeometricProgression(Progression):

    def __init__(self, base=2, start=1):
        self._base = base
        self._current = start
        self._start = start

    def _advanced(self):
        self._current *= self._base

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            t = self._current
            self._advanced()
            return t

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(self.__next__()) for i in range(n + 1)))


a = GeometricProgression()
a.print_progression(10)

GeometricProgression(1, 2).print_progression(10)    # Python也支持匿名对象

for i in GeometricProgression(8, 2):
    print(i)
    if i > 100000:
        break
