from typing import Iterator

from Collections.Dictionary import BinarySerachTree
from Collections.List.DoubleLinkedList import DoubleLinkedList


class Dictionary:

    __bst : BinarySerachTree = BinarySerachTree.BinarySearchTree()

    def __init__(self):
        pass

    def put(self, key: object, value: object) -> None:
        self.__bst.insert(key, value)

    def get(self, key : object) -> object:
        self.__bst.get(key)

    def contains(self, key: object) -> bool:
        return self.__bst.get(key) is not None

    def delete(self, key: object) -> None:
        self.__bst.delete(key)

    def isEmpty(self) -> bool:
        return self.__bst.size() == 0

    def size(self) -> int:
        return self.__bst.size()

    def keys(self) -> DoubleLinkedList[object]:
        return self.__bst.keysAscendingOrder()


    def min(self) -> object:
        self.__bst.get(self.__bst.getMinKey())

    def max(self) -> object:
        self.__bst.get(self.__bst.getMaxKey())

    def floor(self, key : object) -> object:
        pass

    def ceiling(self, key : object) -> object:
        pass

    def rank(self, key : object) -> int:
        self.__bst.rank(key)

    def select(self, rankK : int) -> object:
        pass

    def deleteMin(self) -> None:
        self.__bst.delete(self.__bst.getMinKey())

    def deleteMax(self) -> None:
        self.__bst.delete(self.__bst.getMaxKey())

    def size(self, lowKey : object, highKey : object) -> int:
        return self.keys(lowKey, highKey).size()

    def keys(self, lowKey : object, highKey : object) -> DoubleLinkedList[object]:
        resultList : DoubleLinkedList = DoubleLinkedList()
        beginToAdd : bool = False
        for key in self.keys():
            if key == lowKey:
                beginToAdd = True
            if beginToAdd:
                resultList.addToFirst(key)
            if key == highKey:
                return resultList
        return resultList
