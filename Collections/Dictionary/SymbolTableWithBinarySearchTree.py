from typing import Iterator


class Dictionary:
    def __init__(self):
        pass
    def put(self, key: object, value: object) -> None:
        pass
    def get(self, key : object) -> object:
        pass
    def contains(self, key: object) -> bool:
        pass
    def delete(self, key: object) -> None:
        pass
    def isEmpty(self) -> bool:
        pass
    def size(self) -> int:
        pass
    def keys(self) -> Iterator:
        pass


    def min(self) -> object:
        pass
    def max(self) -> object:
        pass
    def floor(self, key : object) -> object:
        pass
    def ceiling(self, key : object) -> object:
        pass
    def rank(self, key : object) -> int:
        pass
    def select(self, rankK : int) -> object:
        pass
    def deleteMin(self):
        pass
    def deleteMax(self):
        pass
    def size(self, lowKey : object, highKey : object) -> int:
        pass
    def keys(self, lowKey : object, highKey : object) -> Iterator:
        pass