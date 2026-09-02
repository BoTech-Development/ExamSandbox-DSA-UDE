from math import log2

import DSA


class MinPriorityQueue:
    __currentIndex : int = 0
    def __init__(self, capacity: int):
        self.__nodesArray = DSA.objArray(capacity)

    def isEmpty(self) -> bool:
        return self.__currentIndex == 0

    def insert(self, item : object) -> None:
        self.__currentIndex += 1
        if self.__currentIndex == len(self.__nodesArray):
            self.__increaseArrayCapacity()
        self.__nodesArray[self.__currentIndex] = item # insert item in the next free container
        self.__swimUp(self.__currentIndex)

    def __increaseArrayCapacity(self) -> None:
        newSize : int = len(self.__nodesArray) * 2
        copy: list[object | None] = DSA.objArray(newSize)
        for i in range(len(self.__nodesArray)):
            copy[i] = self.__nodesArray[i]
        self.__nodesArray = copy
        #print("increase array capacity to: ", newSize)

    def deleteMin(self) -> object:
        # Schiebe das aktuelle (ein sehr kleinenes Element nicht das kleinste) nach oben und das größte nach unten
        self.__swapElementsInArray(1, self.__currentIndex, self.__nodesArray)
        self.__currentIndex -= 1
        self.__sinkDown(1) #korrigiere wieder die Heap ordnung
        # Übergebe das größte Element mit der vermeidung von loitering
        minElement : object = self.__nodesArray[self.__currentIndex + 1]
        self.__nodesArray[self.__currentIndex + 1] = None
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

    def __sinkDown(self, indexToSwimDown : int) -> None:
        leftChildIndex : int = self.__getIndexOfLeftChildrenOfNode(indexToSwimDown)
        rightChildIndex : int = self.__getIndexOfRightChildrenOfNode(indexToSwimDown)

        #if rightChildIndex <= self.__currentIndex and leftChildIndex >= self.__currentIndex:
        if self.__currentIndex == 2:
            currentElement: object = self.__nodesArray[indexToSwimDown]
            leftChildElement: object = self.__nodesArray[leftChildIndex]
            if leftChildElement < currentElement:
                self.__swapElementsInArray(indexToSwimDown, leftChildIndex, self.__nodesArray)
            return

        if rightChildIndex >= self.__currentIndex and leftChildIndex >= self.__currentIndex: # j < self.N
            return

        rightChildElement : object = self.__nodesArray[rightChildIndex]
        leftChildElement : object = self.__nodesArray[leftChildIndex]
        currentElement : object = self.__nodesArray[indexToSwimDown]

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
        if indexToSwimUp > 1 and self.__nodesArray[indexToSwimUp] < self.__nodesArray[currentParentIndex]:
            self.__swapElementsInArray(currentParentIndex, indexToSwimUp, self.__nodesArray) # Schiebe nach oben
            self.__swimUp(currentParentIndex) # mache beim neuen parent weiter.

    def __swapElementsInArray(self, indexOfFirstElement: int, indexOfSecondElement: int, dataToSwap: list[object]) -> None:
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
        n = len(self.__nodesArray) - 1
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
                print(self.__nodesArray[idx + j], end=" " * spacing)

            print()
            idx += nodes_in_level
            level += 1


pq : MinPriorityQueue = MinPriorityQueue(3)
'''
print("+++inserting+++")
for dataToInsert in range(27):
    pq.insert(dataToInsert)
    pq.pretty_print_heap()

print("+++Deleting++++")

result= ""
while not pq.isEmpty():
    deletedElement = pq.deleteMin()
    result += "," + str(deletedElement)
    print("removed: ", deletedElement)
    pq.pretty_print_heap()

print(result)
'''

print("+++inserting+++")
for dataToInsert in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]:
    pq.insert(dataToInsert)
    pq.pretty_print_heap()

print("+++Deleting++++")

result= ""
while not pq.isEmpty():
    deletedElement = pq.deleteMin()
    result += str(deletedElement)
    print(deletedElement)
    pq.pretty_print_heap()

print(result)

