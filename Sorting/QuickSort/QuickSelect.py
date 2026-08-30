import random


def quickselect(arrayToFindIn : list[object], findIndex : int) -> object:
    shuffle(arrayToFindIn)
    startIndex : int = 0
    endIndex : int = len(arrayToFindIn) - 1
    while endIndex > startIndex:
        rightPartPointer : int = partition(arrayToFindIn, startIndex, endIndex)
        if rightPartPointer < findIndex: # Grenzen anpassen
            startIndex = rightPartPointer + 1
        elif rightPartPointer > findIndex:
            endIndex = rightPartPointer - 1
        else:
            return arrayToFindIn[findIndex] # index gefunden
    return arrayToFindIn[findIndex]

def partition(arrayToSort : list[object], startIndex : int, endIndex : int) -> int:
    leftPartPointer = startIndex
    rightPartPointer = endIndex + 1
    while True:
        leftPartPointer += 1
        while arrayToSort[leftPartPointer] < arrayToSort[startIndex]:
            if leftPartPointer == endIndex: break
            leftPartPointer += 1

        rightPartPointer -= 1
        while arrayToSort[startIndex] < arrayToSort[rightPartPointer]:
            if rightPartPointer == startIndex: break
            rightPartPointer -= 1
        if leftPartPointer >= rightPartPointer: break
        swapElementsInArray(leftPartPointer, rightPartPointer, arrayToSort)
    swapElementsInArray(startIndex, rightPartPointer, arrayToSort)
    return rightPartPointer

def shuffle(arrayToSort: list[object]) -> None:
    countOfElements : int = len(arrayToSort)
    for index in range(countOfElements):
        randomIndex : int = random.randrange(0, index + 1)
        swapElementsInArray(index, randomIndex, arrayToSort)

def swapElementsInArray(indexOfFirstElement: int, indexOfSecondElement: int, dataToSwap: list[object]) -> None:
    elementPuffer: object = dataToSwap[indexOfFirstElement]
    dataToSwap[indexOfFirstElement] = dataToSwap[indexOfSecondElement]
    dataToSwap[indexOfSecondElement] = elementPuffer