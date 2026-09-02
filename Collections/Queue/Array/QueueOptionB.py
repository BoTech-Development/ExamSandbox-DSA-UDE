from random import randint

import DSA


class QueueOptionB:
    __frontOfQueueIndex : int = 0
    __backOfQueueIndex : int = 0

    def __init__(self, initialCapacity : int):
        self.__data = DSA.objArray(initialCapacity)

    def enqueue(self, data : object) -> None:
        if self.__backOfQueueIndex == len(self.__data): # sind wir am Ende des arrays angekommen?
            if self.size() < len(self.__data): # ist vorne noch Platz
                self.__moveAllDataToFront() # Dann verschiebe alle Elemente in den frei gewordenen Platz (wird frei bei dequeue())
            elif self.size() == len(self.__data): # sind schon alle Speicherzellen befüllt?
                self.__increaseArrayCapacity() # Dann müssen wir das Array erweitern
        self.__data[self.__backOfQueueIndex] = data
        self.__backOfQueueIndex += 1

    def dequeue(self) -> object:
        if self.isEmpty():
            raise InvalidOperationException
        if self.size() == len(self.__data) // 4 and self.size() > 0:
            self.__decreaseArrayCapacity()
        dataToReturn = self.__data[self.__frontOfQueueIndex]
        self.__data[self.__frontOfQueueIndex] = None
        if self.__frontOfQueueIndex + 1 <= self.__backOfQueueIndex:
            self.__frontOfQueueIndex += 1
        return dataToReturn

    def __increaseArrayCapacity(self) -> None:
        copyOfData : list[object] = DSA.objArray(len(self.__data) * 2)
        for i in range(len(self.__data)):
            copyOfData[i] = self.__data[i]
        self.__data = copyOfData

    def __moveAllDataToFront(self) -> None:
        newIndex : int = 0
        for currentIndex in range(self.__frontOfQueueIndex, self.__backOfQueueIndex):
            self.__data[newIndex] = self.__data[currentIndex]
            newIndex += 1
        #Pointer anpassen:
        self.__backOfQueueIndex = self.__backOfQueueIndex - self.__frontOfQueueIndex
        self.__frontOfQueueIndex = 0

    def __decreaseArrayCapacity(self) -> None:
        self.__moveAllDataToFront()
        copyOfData : list[object] = DSA.objArray(self.size())
        for i in range(self.size()):
            copyOfData[i] = self.__data[i]
        self.__data = copyOfData

    def isEmpty(self) -> bool:
        return self.__frontOfQueueIndex == 0 and self.__backOfQueueIndex == 0 and self.__data[0] is None

    def size(self) -> int:
        return self.__backOfQueueIndex - self.__frontOfQueueIndex

    def printStatus(self):
        print("front Index: " + str(self.__frontOfQueueIndex), "back Index: " + str(self.__backOfQueueIndex), self.__data, "len: " + str(len(self.__data)))

class InvalidOperationException(Exception):
    pass

if __name__ == '__main__':
    queue : QueueOptionB = QueueOptionB(10)

    countOfValues : int = 11

    print("---ENQUEUE---")
    for i in range(countOfValues):
        queue.enqueue(i)
        queue.printStatus()
    print("---DEQUEUE---")
    for i in range(countOfValues):
        print(str(queue.dequeue()))
        queue.printStatus()

    print("--------------RANDOM----------------")

    countOfLoops : int = 100
    while countOfLoops > 0:
        countOfLoops -= 1
        if randint(0,1) == 1:
            print("ENQUEUE: " + str(countOfLoops))
            queue.enqueue(countOfLoops)
        else:
            print("DEQUEUE: " + str(countOfLoops) + ", val:" + str(queue.dequeue()))
        queue.printStatus()

