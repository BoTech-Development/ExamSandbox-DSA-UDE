from DSA import intArray

class QuickFindUF:
    def __index__(self, n : int):
        self.id = intArray(n)
        for i in range(len(self.id)):
            self.id[i] = i
    def find(self, p : int) -> int:
        return self.id[p]
    def connected(self, q : int, p : int) -> bool:
        return self.find(p) == self.find(q)
    def union(self, p : int, q : int):
        pid = self.find(p)
        qid = self.find(q)
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid
