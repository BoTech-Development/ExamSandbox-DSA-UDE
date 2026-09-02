from math import log2

import DSA


class MinPriorityQueue:
    __currentIndex : int = 0
    def __init__(self, capacity: int):
        self.__nodesArray = DSA.objArray(capacity)
        self.__positions = DSA.intArray(capacity)
        self.__keys = DSA.objArray(capacity)
        for index in range(capacity):
            self.__positions[index] = -1 # initialisiere jede position mit -1, damit klar wird, dass dieser index noch keinem Element im heap zuweisbar ist.

    def isEmpty(self) -> bool:
        return self.__currentIndex == 0

    def insert(self, index : int, item : object) -> None:
        self.__currentIndex += 1
        if self.__currentIndex == len(self.__nodesArray):
            self.__increaseArrayCapacity()

        self.__nodesArray[self.__currentIndex] = index # es wird nur ein pointer im binary heap gespeichert
        self.__keys[index] = item # Dieser pointer zeigt auf den Key.
        self.__positions[index] = self.__currentIndex # Gleichzeitig kann man mit O(1) mit einem gegebenen Index herausfinden, wo er im Heap eingeordnet ist
        self.__swimUp(self.__currentIndex)

    def contains(self, index : int) -> bool:
        return self.__positions[index] != -1

    def decreaseKey(self, index : int, key : object) -> None:
        pass

    def increaseKey(self, index : int, key : object) -> None:
        pass

    def deleteMin(self) -> object:
        # Schiebe das aktuelle (ein sehr kleinenes Element nicht das kleinste) nach oben und das größte nach unten
        self.__swapElementsInArray(1, self.__currentIndex, self.__nodesArray)
        self.__currentIndex -= 1
        self.__sinkDown(1) #korrigiere wieder die Heap ordnung
        # Übergebe das größte Element mit der vermeidung von loitering
        minElement : object = self.__getKeyForSpecificHeapEntry(self.__currentIndex + 1)
        self.__setKeyForSpecificHeapEntry(self.__currentIndex + 1,None)
        self.__positions[self.__nodesArray[self.__currentIndex]] = -1
        self.__nodesArray[self.__currentIndex] = None
        # prüfe, ob verkleinert werden kann...
        if self.__currentIndex == len(self.__nodesArray) // 4 and self.__currentIndex > 0:
            self.__decreaseArrayCapacity()
        return minElement

    def __decreaseArrayCapacity(self) -> None:
        newSize : int = self.__currentIndex + 1
        copyOfData : list[object] = DSA.objArray(newSize)
        for i in range(newSize):
            copyOfData[i] = self.__nodesArray[i]
        self.__nodesArray = copyOfData
        #print("decrease array capacity to: ", newSize)

    def __increaseArrayCapacity(self) -> None:
        newSize : int = len(self.__nodesArray) * 2
        copy: list[object | None] = DSA.objArray(newSize)
        for i in range(len(self.__nodesArray)):
            copy[i] = self.__nodesArray[i]
        self.__nodesArray = copy
        #print("increase array capacity to: ", newSize)

    def __sinkDown(self, indexToSwimDown : int) -> None:
        leftChildIndex : int = self.__getIndexOfLeftChildrenOfNode(indexToSwimDown)
        rightChildIndex : int = self.__getIndexOfRightChildrenOfNode(indexToSwimDown)

        #if rightChildIndex <= self.__currentIndex and leftChildIndex >= self.__currentIndex:
        if self.__currentIndex == 2:
            currentElement: object = self.__getKeyForSpecificHeapEntry(indexToSwimDown)
            leftChildElement: object = self.__getKeyForSpecificHeapEntry(leftChildIndex)
            if leftChildElement < currentElement:
                self.__swapElementsInArray(indexToSwimDown, leftChildIndex, self.__nodesArray)
            return

        if rightChildIndex >= self.__currentIndex and leftChildIndex >= self.__currentIndex: # j < self.N
            return

        rightChildElement : object = self.__getKeyForSpecificHeapEntry(rightChildIndex)
        leftChildElement : object = self.__getKeyForSpecificHeapEntry(leftChildIndex)
        currentElement : object = self.__getKeyForSpecificHeapEntry(indexToSwimDown)

        # müssen wir überhaupt noch sinken lassen?
        if currentElement > leftChildElement or currentElement > rightChildElement:
            # Welches Element wird parent?
            if leftChildElement > rightChildElement: # self.pq[j] < self.pq[j+1]
                # der rechte wird parent
                self.__swapElementsInArray(indexToSwimDown, rightChildIndex, self.__nodesArray)
                self.__sinkDown(rightChildIndex)
            else:
                # der linke wird parent
                self.__swapElementsInArray(indexToSwimDown, leftChildIndex, self.__nodesArray)
                self.__sinkDown(leftChildIndex)

    def __swimUp(self, indexToSwimUp : int) -> None:
        currentParentIndex : int = self.__getParentIndexOfNode(indexToSwimUp)
        # wenn das aktuelle Element immer noch kleiner ist als das Element darüber, dann ist die Heap Ordnung verletzt und man muss das aktuelle Element nach oben schieben.
        if indexToSwimUp > 1 and self.__getKeyForSpecificHeapEntry(indexToSwimUp) < self.__getKeyForSpecificHeapEntry(currentParentIndex):
            self.__swapElementsInArray(currentParentIndex, indexToSwimUp, self.__nodesArray) # Schiebe nach oben
            self.__swimUp(currentParentIndex) # mache beim neuen parent weiter.

    def __swapElementsInArray(self, indexOfFirstElement: int, indexOfSecondElement: int, dataToSwap: list[object]) -> None:
        elementPuffer : object = dataToSwap[indexOfFirstElement]
        dataToSwap[indexOfFirstElement] = dataToSwap[indexOfSecondElement]
        dataToSwap[indexOfSecondElement] = elementPuffer

    def __getKeyForSpecificHeapEntry(self, indexInHeap : int) -> object:
        return self.__keys[self.__nodesArray[indexInHeap]]

    def __setKeyForSpecificHeapEntry(self, indexInHeap : int, newKey : object) -> None:
        self.__keys[self.__nodesArray[indexInHeap]] = newKey

    def __getIndexOfLeftChildrenOfNode(self, node : int) -> int:
        return 2 * node

    def __getIndexOfRightChildrenOfNode(self, node : int) -> int:
        return 2 * node + 1

    def __getParentIndexOfNode(self, node : int) -> int:
        return node // 2

    def printTree(self):
        if self.__currentIndex == 0:
            print("<leer>")
            return

        level = 1
        pos = 1

        while pos <= self.__currentIndex:
            end = min(pos + level - 1, self.__currentIndex)

            for i in range(pos, end + 1):
                idx = self.__nodesArray[i]
                print(f"{idx}:{self.__keys[idx]}", end="   ")

            print()
            pos += level
            level *= 2


pq : MinPriorityQueue = MinPriorityQueue(13)


pq.insert(12, "T")
pq.insert(1, "P")
pq.insert(2, "R")
pq.insert(3, "N")
pq.insert(4, "H")
pq.insert(5, "O")
pq.insert(6, "A")
pq.insert(7, "E")
pq.insert(8, "I")
pq.insert(9, "G")
pq.printTree()

print("insert: X")
pq.insert(10, "X")
pq.printTree()

print("---------------Deleting---------------------")
print(pq.deleteMin())
print()
pq.printTree()
print()
print(pq.deleteMin())
print()
pq.printTree()
print()
pq.insert(11, "S")
pq.printTree()
