from random import random, randint

import DSA


class StackOptionB:
    __dataArray : list[object] = None
    __currentSize: int = 0
    __topOfStackPointer : int = 0

    def __init__(self, countOfStartElements : int):
        self.__dataArray = DSA.objArray(countOfStartElements)
        self.__currentSize = 0


    def push(self, item : object) -> None:
        self.__topOfStackPointer += 1
        if len(self.__dataArray) <= self.__topOfStackPointer:
            self.__expandArray()
        self.__dataArray[self.__topOfStackPointer - 1] = item
        self.__currentSize += 1

    def pop(self) -> object:
        if self.isEmpty():
            raise InvalidOperationException('Stack is empty')
        else:
            elementToReturn : object = self.__deleteAndReturnTop()
            if self.size() == len(self.__dataArray) // 4 and self.size() > 0:
                self.__schrinkArray()
            return elementToReturn

    def __deleteAndReturnTop(self) -> object:
        self.__topOfStackPointer -= 1
        if self.__topOfStackPointer < 0:
            self.__topOfStackPointer = 0
        elementToReturn: object = self.__dataArray[self.__topOfStackPointer]
        self.__dataArray[self.__topOfStackPointer] = None
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
        for i in range(self.size()):
            copy[i] = self.__dataArray[i]
        self.__dataArray = copy

    def getArray(self) -> list[object]:
        return self.__dataArray
    def getStackPointer(self) -> int:
        return self.__topOfStackPointer

class InvalidOperationException(Exception):
    pass


stack = StackOptionB(3)

stack.push(5)
print("push: " + str(5) + ", size:" + str(stack.size()) + ", array len:" + str(len(stack.getArray())) + ", array:" + str(stack.getArray()) + ", stackPointer:" + str(stack.getStackPointer()))
stack.push(6)
print("push: " + str(6) + ", size:" + str(stack.size()) + ", array len:" + str(len(stack.getArray())) + ", array:" + str(stack.getArray())+ ", stackPointer:" + str(stack.getStackPointer()))
stack.push(7)
print("push: " + str(7) + ", size:" + str(stack.size()) + ", array len:" + str(len(stack.getArray())) + ", array:" + str(stack.getArray())+ ", stackPointer:" + str(stack.getStackPointer()))
stack.push(8)
print("push: " + str(8) + ", size:" + str(stack.size()) + ", array len:" + str(len(stack.getArray())) + ", array:" + str(stack.getArray())+ ", stackPointer:" + str(stack.getStackPointer()))
popValue = stack.pop()
print("pop:" + str(popValue) + ", size:" + str(stack.size()) + ", array len:" + str(len(stack.getArray())) + ", array:" + str(stack.getArray())+ ", stackPointer:" + str(stack.getStackPointer()))
popValue = stack.pop()
print("pop:" + str(popValue) + ", size:" + str(stack.size()) + ", array len:" + str(len(stack.getArray())) + ", array:" + str(stack.getArray())+ ", stackPointer:" + str(stack.getStackPointer()))
popValue = stack.pop()
print("pop:" + str(popValue) + ", size:" + str(stack.size()) + ", array len:" + str(len(stack.getArray())) + ", array:" + str(stack.getArray())+ ", stackPointer:" + str(stack.getStackPointer()))
stack.push(9)
print("push: " + str(9) + ", size:" + str(stack.size()) + ", array len:" + str(len(stack.getArray())) + ", array:" + str(stack.getArray())+ ", stackPointer:" + str(stack.getStackPointer()))
stack.push(10)
print("push: " + str(10) + ", size:" + str(stack.size()) + ", array len:" + str(len(stack.getArray())) + ", array:" + str(stack.getArray())+ ", stackPointer:" + str(stack.getStackPointer()))
popValue = stack.pop()
print("pop:" + str(popValue) + ", size:" + str(stack.size()) + ", array len:" + str(len(stack.getArray())) + ", array:" + str(stack.getArray())+ ", stackPointer:" + str(stack.getStackPointer()))
popValue = stack.pop()
print("pop:" + str(popValue) + ", size:" + str(stack.size()) + ", array len:" + str(len(stack.getArray())) + ", array:" + str(stack.getArray())+ ", stackPointer:" + str(stack.getStackPointer()))

'''

i = 100
while i > 0:
    i -= 1
    if randint(0,1) == 1:
        value = randint(0,100)
        stack.push(value)
        print("push: " + str(value) + ", size:" + str(stack.size()) + ", array len:" + str(len(stack.getArray())) + ", array:" + str(stack.getArray()))
    else:
        popValue = stack.pop()
        print("pop:" + str(popValue) + ", size:" + str(stack.size()) + ", array len:" + str(len(stack.getArray())) + ", array:" + str(stack.getArray()))
'''