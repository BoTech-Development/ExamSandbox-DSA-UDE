from DSA import *


class IndexedMinPQ:
    def __init__(self, maxN):
        self.__pq = intArray(maxN + 1)  # binary heap using 1-based indexing
        self.__qp = intArray(maxN + 1)  # inverse of pq - qp[pq[i]] = pq[qp[i]] = i
        self.__keys = objArray(maxN + 1)  # keys[i] = priority of i
        self.__N = 0
        for i in range(maxN): self.__qp[i] = -1

    def isEmpty(self):
        return self.__N == 0

    def size(self):
        return self.__N

    def contains(self, i):
        return self.__qp[i] != -1

    def insert(self, i, x):
        self.__N += 1
        self.__qp[i] = self.__N
        self.__pq[self.__N] = i
        self.__keys[i] = x
        self.__swim(self.__N)

    def delMin(self):
        min = self.__pq[1]
        self.__exch(1, self.__N)
        self.__N -= 1
        self.__sink(1)
        self.__pq[self.__N + 1] = -1
        self.__qp[min] = -1
        self.__keys[min] = None
        return min

    def decreaseKey(self, i, key):
        self.__keys[i] = key
        self.__swim(self.__qp[i])

    def __swim(self, k):
        while k > 1 and self.__keys[self.__pq[k]] < self.__keys[self.__pq[k // 2]]:
            self.__exch(k, k // 2)
            k = k // 2

    def __sink(self, k):
        while 2 * k <= self.__N:
            j = 2 * k
            if j < self.__N and self.__keys[self.__pq[j + 1]] < self.__keys[self.__pq[j]]: j += 1
            if not self.__keys[self.__pq[j]] < self.__keys[self.__pq[k]]: break
            self.__exch(k, j)
            k = j

    def __repr__(self):
        return "heap:" + str(self.__pq) + "\nposition im heap:" + str(self.__qp) + "\nkeys:" + str(self.__keys)

    def __exch(self, i, j):
        swap = self.__pq[i]
        self.__pq[i] = self.__pq[j]
        self.__pq[j] = swap
        self.__qp[self.__pq[i]] = i
        self.__qp[self.__pq[j]] = j


if __name__ == "__main__":
    m = IndexedMinPQ(20)
    m.insert(12, "T")
    m.insert(1, "P")
    m.insert(2, "R")
    m.insert(3, "N")
    m.insert(4, "H")
    m.insert(5, "O")
    m.insert(6, "A")
    m.insert(7, "E")
    m.insert(8, "I")
    m.insert(9, "G")
    print(m)
    print()

    m.insert(10, "X")
    print(m)
    print(m.delMin())
    print()
    print(m)
    print()
    print(m.delMin())
    print()
    print(m)
    print()
    m.insert(11, "S")
    print(m)