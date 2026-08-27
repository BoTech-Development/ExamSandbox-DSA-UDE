from random import random, randint

import DSA


class StackOptionB:
    __dataArray : list[object] = None
    __currentSize: int = 0
    __topOfStackPointer : int = 0

    def __init__(self, countOfStartElements : int):
        self.__dataArray = DSA.objArray(countOfStartElements)
        self.__currentSize = countOfStartElements


    def push(self, item : object) -> None:
        self.__topOfStackPointer += 1
        if len(self.__dataArray) == self.__topOfStackPointer:
            self.__expandArray()
        self.__dataArray[self.__topOfStackPointer -1] = item
        self.__currentSize += 1

    def pop(self) -> object:
        if self.isEmpty():
            print("Empty Stack")
            #raise InvalidOperationException('Stack is empty')
        else:
            elementToReturn : object = self.__deleteAndReturnTop()
            if self.size() == len(self.__dataArray) // 4:
                self.__schrinkArray()
            return elementToReturn

    def __deleteAndReturnTop(self) -> object:
        elementToReturn: object = self.__dataArray[self.__topOfStackPointer]
        self.__dataArray[self.__topOfStackPointer] = None
        self.__topOfStackPointer -= 1
        self.__currentSize -= 1
        return elementToReturn


    def isEmpty(self) -> bool:
        return self.__currentSize == 0

    def size(self) -> int:
        return self.__currentSize

    def __expandArray(self) -> None:
        self.__resizeArrayWithCopy(len(self.__dataArray) * 2)
    def __schrinkArray(self) -> None:
        self.__resizeArrayWithCopy(len(self.__dataArray) // 2)

    def __resizeArrayWithCopy(self, countOfElements : int) -> None:
        copy = DSA.objArray(countOfElements)
        for i in range(self.size() - 1):
            copy[i] = self.__dataArray[i]
        self.__dataArray = copy

class InvalidOperationException(Exception):
    pass

stack = StackOptionB(3)


i = 100
while i > 0:
    i -= 1
    if randint(0,1) == 1:
        value = randint(0,100)
        print("push: " + str(value))
        stack.push(value)
    else:
        print("pop:" + str(stack.pop()))


