class AhoCorasic_Arr:

    MAX_CHAR = 30
    MAXN = 100000

    def __init__(self) -> None:
        self.tr = [[0 for i in range(0, self.MAX_CHAR)] for j in range(0, self.MAXN)]
        self.root = 0
        self.is_word = [False for i in range(0, self.MAXN)]
        self.cnt = [0 for i in range(0, self.MAXN)]
        self.word = [None for i in range(0, self.MAXN)]
        self.tot = 0
        self.fail = [0 for i in range(0, self.MAXN)]
    
    def add(self, word: str) -> None:
        p = self.root
        for ch in word:
            if self.tr[p][ord(ch) - ord('a')] == 0:
                self.tot += 1
                self.tr[p][ord(ch) - ord('a')] = self.tot
                p = self.tot
            else: p = self.tr[p][ord(ch) - ord('a')]
        self.word[p] = word
        self.is_word[p] = True
        self.cnt[p] += 1
    
    def build(self) -> None:
        q = []
        i = 0
        while i < 26:
            if self.tr[0][i] != 0:
                q.append(self.tr[0][i])
                self.fail[self.tr[0][i]] = self.root
            i += 1
        while len(q) > 0:
            p = q.pop(0)
            for i in range(0, 26):
                if self.tr[p][i] != 0:
                    self.fail[self.tr[p][i]] = self.tr[self.fail[p]][i]
                    q.append(self.tr[p][i])
                else:
                    self.tr[p][i] = self.tr[self.fail[p]][i]
        
    def query(self, text: str) -> list:
        p = self.root
        res = []
        i = 0
        while i < len(text):
            ch = text[i]
            p = self.tr[p][ord(ch) - ord('a')]
            t = p
            # print(t, self.is_word[t], self.word[t])
            while self.is_word[t] == True and t != self.root:
                res.append((self.word[t], i - len(self.word[t]) + 1))
                t = self.fail[t]
            i += 1
        return res

if __name__ == '__main__':
    n = int(input())
    ac = AhoCorasic_Arr()
    i = 0
    while i < n:
        word = input()
        ac.add(word)
        i += 1
    s = input()
    ac.build()
    print(ac.query(s))

                

