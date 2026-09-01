from random import randint

import DSA


class HashTable:
    class KeyValuePair:
        def __init__(self, key : object, value : object):
            self.key = key
            self.value = value

    class EmptyPointer:
        pass

    countOfInsertedElements : int = 0

    def __init__(self, size: int) -> None:
        self.data : list[HashTable.KeyValuePair | HashTable.EmptyPointer | None] = DSA.objArray(size)

    def get(self, key : object) -> object | None:
        possibleIndex: int = self.__getEndOfClusterIndexOrActualKeyIndex(self.__hashIndex(key), key)
        return self.data[possibleIndex]

    def put(self, key : object, value : object) -> None:
        # starte mit dem trivialen index oder wähle den nächsten freien index
        hashIndex : int = self.__hashIndex(key)
        possibleIndex : int = self.__getEndOfClusterIndexOrActualKeyIndex(hashIndex, key)
        if possibleIndex != -1:
            self.data[possibleIndex] = HashTable.KeyValuePair(key, value)
            self.countOfInsertedElements += 1
        if possibleIndex == hashIndex: # vergrößere, nur wenn nötig (wenn neues Element hinzugefügt)
            self.__resizeIfNecessary()

    def delete(self, key : object) -> None:
        # starte mit dem trivialen index oder wähle den nächsten freien möglichen Index
        possibleIndex : int = self.__getEndOfClusterIndexOrActualKeyIndex(self.__hashIndex(key), key)
        if self.data[possibleIndex] is not None: # prüfe, ob wirklich gefunden oder nur mögliches Feld zum einfügen
            if self.data[possibleIndex + 1] is not None: # prüfe ob man das cluster kaputt macht
                self.data[possibleIndex] = HashTable.EmptyPointer
                self.countOfInsertedElements -= 1
                self.__resizeIfNecessary()
            else:
                self.data[possibleIndex] = None
                self.countOfInsertedElements -= 1
                self.__resizeIfNecessary()

    def isEmpty(self) -> bool:
        return self.countOfInsertedElements == 0

    def size(self) -> int:
        return self.countOfInsertedElements

    def __hashIndex(self, key : object) -> int:
        return hash(key) % len(self.data)

    def __getEndOfClusterIndexOrActualKeyIndex(self, clusterStartingAtIndex : int, key : object) -> int:
        currentIndex : int = clusterStartingAtIndex
        while currentIndex < len(self.data):
            if self.data[currentIndex] is not None:
                if self.data[currentIndex].key == key:
                    return currentIndex
            else:
                return currentIndex
            currentIndex += 1
        currentIndex = 0
        while currentIndex < clusterStartingAtIndex:
            if self.data[currentIndex] is not None:
                if self.data[currentIndex].key == key:
                    return currentIndex
            else:
                return currentIndex
            currentIndex += 1
        return -1

    def __resizeIfNecessary(self) -> None:
        if self.countOfInsertedElements // len(self.data) > 0.5:
            copy : list[HashTable.KeyValuePair | HashTable.EmptyPointer | None] = self.__copyDataArray()
            self.data = DSA.objArray(len(self.data) * 2)
            self.__reInsertAllElements(copy)
        elif self.countOfInsertedElements // len(self.data) < 0.125:
            copy : list[HashTable.KeyValuePair | HashTable.EmptyPointer | None] = self.__copyDataArray()
            self.data = DSA.objArray(len(self.data) // 2)
            self.__reInsertAllElements(copy)

    def __reInsertAllElements(self, elemtents : list[HashTable.KeyValuePair | HashTable.EmptyPointer | None]):
        for element in elemtents:
            if element is not None and type(element) == HashTable.KeyValuePair:
                self.put(element.key, element.value)

    def __copyDataArray(self) -> list[HashTable.KeyValuePair | HashTable.EmptyPointer | None]:
        copy: list[HashTable.KeyValuePair | HashTable.EmptyPointer | None] = DSA.objArray(len(self.data))
        for i in range(len(self.data)):
            copy[i] = self.data[i]
        return copy

    def printTable(self):
        print("--------------------------------------------------------------------------------------------------------")
        topText : str = ""
        valueText : str = ""
        newValueText : str = ""
        for index in range(len(self.data)):
            if self.data[index] is not None and type(self.data[index]) == HashTable.KeyValuePair:
                newValueText = "(" + str(self.data[index].key) + ":" + str(self.data[index].value) + ")"
                topText += str(index) + "," + (len(newValueText) - len(str(index) + ",")) * " "
                valueText += newValueText
        print(topText)
        print(valueText)
        print("---------------------------------HS: countOfElements: " + str(self.countOfInsertedElements) + ", lenOfData: " + str(len(self.data)) + "--------------------------------")


hs = HashTable(10)
for i in range(100):
    key = randint(0, 100)
    value = randint(0, 100)
    #print(key,value)
    hs.put(key, value)
    hs.printTable()
"""
hs.put(0,0)
hs.printTable()
print("----------------------")
hs.delete(0)
hs.printTable()
"""