class Trie:

    class _node:
        def __init__(self, is_root: bool, ch: str, cnt: int, child: list):
            self.is_root = is_root
            self.ch = ch
            self.cnt = cnt
            self.child = child


    def __init__(self):
        self.root = self._node(True, '#', 0, [])

    def insert(self, word: str) -> None:
        now = self.root
        i = 0
        while i < len(word):
            found = False
            for son in now.child:
                if son.ch == word[i]:
                    now = son
                    found = True
                    break
            if not found:
                now.child.append(self._node(False, word[i], 0, []))
                now = now.child[len(now.child)-1]
            i += 1
        now.cnt += 1

    def search(self, word: str) -> bool:
        i = 0
        now = self.root
        while i < len(word):
            found = False
            for son in now.child:
                if son.ch == word[i]:
                    now = son
                    found = True
                    break
            if not found:
                return False
            i += 1
        if now.cnt > 0:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        i = 0
        now = self.root
        while i < len(prefix):
            found = False
            for son in now.child:
                if son.ch == prefix[i]:
                    now = son
                    found = True
                    break
            if not found:
                return False
            i += 1
        return True

    def getFrequncy(self, word: str) -> int:
        i = 0
        now = self.root
        while i < len(word):
            found = False
            for son in now.child:
                if son.ch == word[i]:
                    now = son
                    found = True
                    break
            if not found:
                return 0
            i += 1
        if now.cnt > 0:
            return now.cnt
        else:
            return 0


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    trie.insert("apple")
    trie.insert("app")
    print(trie.search("apple"))
    print(trie.search("appl"))
    print(trie.startsWith("appl"))
    print(trie.getFrequncy("apple"))

