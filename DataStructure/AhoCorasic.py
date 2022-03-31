from ArrayQueue import ArrayQueue


class AhoCorasic(object):

    class _node:
        __slots__ = ['is_word', 'nxt', 'fail', 'word', 'cnt']

        def __init__(self, is_word: bool, nxt, fail=None, word=None, cnt=0):
            self.is_word = is_word
            self.nxt = nxt
            self.fail = fail
            self.word = word
            self.cnt = cnt

    def __init__(self):
        self.root = self._node(False, {})

    def addKeyword(self, word):
        now = self.root
        for ch in list(word):
            if ch not in now.nxt.keys():
                # print(ch, now.nxt.keys())
                now.nxt[ch] = self._node(False, {}, None, None, 0)
            now = now.nxt[ch]
        now.is_word = True
        now.cnt += 1
        now.word = word

    def getFail(self):
        q = ArrayQueue()
        q.enqueue(self.root)
        while not q.is_empty():
            now = q.first()
            q.dequeue()
            for k, v in now.nxt.items():
                # print(k)
                if now is self.root:
                    now.nxt[k].fail = self.root
                    # print(k)
                else:
                    fail = now.fail
                    # print(fail.nxt)
                    while fail is not None and k not in fail.nxt:
                        fail = fail.fail
                    if fail is None:
                        now.nxt[k].fail = self.root
                    else:
                        now.nxt[k].fail = fail
                q.enqueue(now.nxt[k])

    def query(self, word) -> int:
        ans = 0
        now = self.root
        res = []
        i = 0
        while i < len(word):
            ch = word[i]
            while now is not None and ch not in now.nxt:
                now = now.fail
            if now is None:
                now = self.root
            else:
                now = now.nxt[ch]
                if now.is_word is True:
                    res.append((now.word, i - len(now.word) + 1))
                    ans += now.cnt
                    now.is_word = False
            # print(ch, now.nxt.keys(), now.is_word)
            i += 1
        # print(res)
        return ans


if __name__ == '__main__':
    n = int(input())
    ac = AhoCorasic()
    i = 0
    while i < n:
        word = input()
        ac.addKeyword(word)
        i += 1
    s = input()
    ac.getFail()
    print(ac.query(s))











