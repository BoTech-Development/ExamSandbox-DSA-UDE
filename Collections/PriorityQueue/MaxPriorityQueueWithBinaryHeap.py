from math import log2

import DSA


class PriorityQueue:
    currentIndex : int = 0
    def __init__(self, capacity: int):
        self.capacity = capacity
        #self.nodesArray = DSA.objArray(capacity)
        self.nodesArray : list[object] = [None, "T", "P", "R", "N", "H", "O", "A", "E", "I", "G"]

    def isEmpty(self) -> bool:
        return self.currentIndex == 0

    def insert(self, item : object) -> None:
        self.currentIndex += 1
        self.nodesArray[self.currentIndex] = item # insert item in the next free container
        self.__swimUp(self.currentIndex)

    def deleteMax(self) -> object:
        # Schiebe das aktuelle (ein sehr kleinenes Element nicht das kleinste) nach oben und das größte nach unten
        self.__swapElementsInArray(0, self.currentIndex)
        self.currentIndex -= 1
        self.__sinkDown(1) #korrigiere wieder die Heap ordnung
        # Übergebe das größte Element mit der vermeidung von loitering
        maxElement : object = self.nodesArray[self.currentIndex + 1]
        self.nodesArray[self.currentIndex + 1] = None
        return maxElement

    def __sinkDown(self, indexToSwimDown : int) -> None:
        leftChildIndex : int = self.__getIndexOfLeftChildrenOfNode(indexToSwimDown)
        rightChildIndex : int = self.__getIndexOfRightChildrenOfNode(indexToSwimDown)
        rightChildElement : object = self.nodesArray[rightChildIndex]
        leftChildElement : object = self.nodesArray[leftChildIndex]
        currentElement : object = self.nodesArray[indexToSwimDown]
        # müssen wir überhaupt noch sinken lassen?
        if currentElement < leftChildElement or currentElement < rightChildElement:
            # Welches Element wird parent?
            if leftChildElement < rightChildElement:
                # der rechte wird parent
                self.__swapElementsInArray(indexToSwimDown, rightChildElement, self.nodesArray)
                self.__sinkDown(rightChildElement)
            else:
                # der linke wird parent
                self.__swapElementsInArray(indexToSwimDown, leftChildIndex, self.nodesArray)
                self.__sinkDown(leftChildIndex)


    def __swimUp(self, indexToSwimUp : int) -> None:
        currentParentIndex : int = self.__getParentIndexOfNode(indexToSwimUp)
        # wenn das aktuelle Element immer noch größer ist als das Element darüber, dann ist die Heap Ordnung verletzt und man muss das aktuelle Element nach oben schieben.
        if indexToSwimUp > 1 and self.nodesArray[indexToSwimUp] > self.nodesArray[currentParentIndex]:
            self.__swapElementsInArray(currentParentIndex, indexToSwimUp, self.nodesArray) # Schiebe nach oben
            self.__swimUp(currentParentIndex) # mache beim neuen parent weiter.

    def __swapElementsInArray(indexOfFirstElement: int, indexOfSecondElement: int, dataToSwap: list[object]) -> None:
        elementPuffer : object = dataToSwap[indexOfFirstElement]
        dataToSwap[indexOfFirstElement] = dataToSwap[indexOfSecondElement]
        dataToSwap[indexOfSecondElement] = elementPuffer

    def __getIndexOfLeftChildrenOfNode(self, node : int) -> int:
        return 2 * node

    def __getIndexOfRightChildrenOfNode(self, node : int) -> int:
        return 2 * node + 1

    def __getParentIndexOfNode(self, node : int) -> int:
        return node // 2



    def pretty_print_heap(self):
        n = len(self.nodesArray) - 1
        if n <= 0:
            return

        height = int(log2(n)) + 1
        max_width = 2 ** height

        level = 0
        idx = 1

        while idx <= n:
            nodes_in_level = min(2 ** level, n - idx + 1)
            spacing = max_width // (2 ** level)

            print(" " * (spacing // 2), end="")

            for j in range(nodes_in_level):
                print(self.nodesArray[idx + j], end=" " * spacing)

            print()
            idx += nodes_in_level
            level += 1


pq : PriorityQueue = PriorityQueue(10)
pq.pretty_print_heap()
print("+++inserting+++")
pq.insert("S")
pq.pretty_print_heap()
print("+++Deleting++++")
print(pq.deleteMax())
pq.pretty_print_heap()