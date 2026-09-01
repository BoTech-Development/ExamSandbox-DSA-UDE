from DSA import intArray

class QuickFindUF:
    def __init__(self, n):
        self.id = intArray(n)
        for i in range(len(self.id)):
            self.id[i] = i

    def find(self, i : int) -> int:
        while i != self.id[i]: # Solange man noch nicht am wurzelkonten angekommen ist
            i = self.id[i] # gehe einen Schritt höher.
        return self.id[i]

    def connected(self, q: int, p: int) -> bool:
        return self.find(p) == self.find(q)

    def union(self, p: int, q: int):
        i = self.find(p) # Finde die Wurzel beider Konten
        j = self.find(q)
        self.id[i] = j # Knüpfe den einen Teilbaum an den anderen Teilbaum an.