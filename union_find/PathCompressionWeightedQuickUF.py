from DSA import intArray

class WeightedQuickUnionUF:
    def __init__(self, n):
        self.id = intArray(n)
        self.size = intArray(n)
        for i in range(len(self.id)):
            self.id[i] = i
            self.size[i] = 1

    def find(self, i : int) -> int:
        while i != self.id[i]: # Solange man noch nicht am wurzelkonten angekommen ist
            self.id[i] = self.id[self.id[i]] # DIESE ZEILE IST NEU - SONST NICHTS VERÄNDERT
            i = self.id[i] # gehe einen Schritt höher.
        return self.id[i]

    def connected(self, q: int, p: int) -> bool:
        return self.find(p) == self.find(q)

    def union(self, p: int, q: int):
        i = self.find(p) # Finde die Wurzel beider Konten
        j = self.find(q)
        if i == j: return # Wenn die wurzeln gleich sind, gibt es nichts zu tuen.
        if self.size[i] < self.size[j]: # wenn die Anzahl der Knoten im linken Teilbaum kleiner ist als im rechten, dann...
            self.id[i] = j
            self.size[j] += self.size[i] # erhöhe die größe für den Elternknoten.
        else: # andersrum
            self.id[j] = i
            self.size[i] += self.size[j] # erhöhe die größe für den Elternknoten.