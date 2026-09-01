from random import randint

import DSA


class HashTable:
    class KeyValuePair:
        def __init__(self, key : object, value : object):
            self.key = key
            self.value = value

    class ListNode:
        next : HashTable.ListNode | None = None

        def __init__(self, keyValuePair : HashTable.KeyValuePair):
            self.keyValuePair = keyValuePair

        def getKey(self) -> object:
            return self.keyValuePair.key

    countOfInsertedElements : int = 0

    def __init__(self, size: int) -> None:
        self.data : list[HashTable.ListNode | None] = DSA.objArray(size)

    def get(self, key : object) -> object | None:
        keyValuePair : HashTable.KeyValuePair | None = self.__getKeyValuePairForKey(key)
        if keyValuePair is not None:
            return keyValuePair.value
        return None

    def put(self, key : object, value : object) -> None:
        keyValuePair: HashTable.KeyValuePair | None = self.__getKeyValuePairForKey(key)
        if keyValuePair is not None: #update value
            keyValuePair.value = value
        else: # insert
            insertIndex = self.__hashIndex(key)
            keyValuePair : HashTable.KeyValuePair = HashTable.KeyValuePair(key, value)
            listNode : HashTable.ListNode = HashTable.ListNode(keyValuePair)
            listNode.next = self.data[insertIndex]
            self.data[insertIndex] = listNode
            self.countOfInsertedElements += 1
            self.__resizeIfNecessary()

    def delete(self, key : object) -> None:
        possibleIndex: int = self.__hashIndex(key)
        if self.data[possibleIndex] == None:
            return

        nodeBefore : HashTable.ListNode | None = None
        nodeToDelete: HashTable.ListNode | None = self.data[possibleIndex]
        while nodeToDelete is not None and nodeToDelete.getKey() != key:
            nodeBefore = nodeToDelete
            nodeToDelete = nodeToDelete.next

        if nodeToDelete is None:
            return
        if nodeBefore is not None:
            nodeBefore.next = nodeToDelete.next
            return
        self.data[possibleIndex] = nodeToDelete.next
        self.countOfInsertedElements -= 1
        self.__resizeIfNecessary()

    def isEmpty(self) -> bool:
        return self.countOfInsertedElements == 0

    def size(self) -> int:
        return self.countOfInsertedElements

    def __getKeyValuePairForKey(self, key : object) -> KeyValuePair | None:
        possibleIndex : int = self.__hashIndex(key)
        if self.data[possibleIndex] == None:
            return None
        currentNode : HashTable.ListNode | None = self.data[possibleIndex]
        while currentNode is not None and currentNode.getKey() != key:
            currentNode = currentNode.next
        if currentNode is None:
            return None
        return currentNode.keyValuePair

    def __hashIndex(self, key : object) -> int:
        return hash(key) % len(self.data)

    def __resizeIfNecessary(self):
        if self.countOfInsertedElements/len(self.data) >= 8:
            copy : list[HashTable.ListNode | None] = self.__copyDataArray()
            self.data = DSA.objArray(len(self.data) * 2)
            self.__reInsertAllElements(copy)
        elif self.countOfInsertedElements/len(self.data) <= 2:
            copy: list[HashTable.ListNode | None] = self.__copyDataArray()
            self.data = DSA.objArray(len(self.data) // 2)
            self.__reInsertAllElements(copy)

    def __reInsertAllElements(self, elemtents : list[HashTable.ListNode | None]):
        for element in elemtents:
            if element is not None:
                while element is not None:
                    self.put(element.keyValuePair.key, element.keyValuePair.value)
                    element = element.next

    def __copyDataArray(self) -> list[HashTable.ListNode | None]:
        copy : list[HashTable.ListNode | None] = DSA.objArray(len(self.data))
        for i in range(len(self.data)):
            copy[i] = self.data[i]
        return copy


    def printTable(self):
        print("--------------------------------------------------------------------------------------------------------")
        for node in self.data:
            while node is not None:
                print("(" + str(node.keyValuePair.key) + ":" + str(node.keyValuePair.value) + "),", end=" ")
                node = node.next
            print("")
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