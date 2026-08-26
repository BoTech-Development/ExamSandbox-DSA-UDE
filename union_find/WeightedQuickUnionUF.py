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
            i = self.id[i] # gehe einen Schritt höher.
        return self.id[i]

    def connected(self, q: int, p: int) -> bool:
        return self.find(p) == self.find(q)

    def union(self, p: int, q: int):
        i = self.find(p) # Finde die Wurzel beider Konten
        j = self.find(q)
        if i == j: return # Wenn die wurzeln gleich sind gibt es nichts zu tuen.
        if self.size[i] < self.size[j]: # wenn die Anzahl der Knoten im linken Teilbaum kleiner ist als im rechten, dann...
            self.id[i] = j
            self.size[j] += self.size[i] # erhöhe die größe für den Elternknoten.
        else: # andersrum
            self.id[j] = i
            self.size[i] += self.size[j] # erhöhe die größe für den Elternknoten.

    def print(self):
        for i in range(len(self.id)):
            print("The node " + str(i) + " has the parent: " + str(self.id[i]))


tree = WeightedQuickUnionUF(10)
tree.union(4,3)
tree.union(3,8)
tree.union(6,5)
tree.union(9,4)
tree.union(2,1)
tree.union(5,0)
tree.union(7,2)
tree.union(6,1)
tree.union(7,3)
tree.print()