import random


def quickSort(arrayToSort: list[object]) -> None:
    shuffle(arrayToSort)
    sort(arrayToSort, 0, len(arrayToSort) - 1)

def partition(arrayToSort : list[object], startIndex : int, endIndex : int) -> int:
    leftPartPointer : int = startIndex
    rightPartPointer : int = endIndex + 1
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

def sort(arrayToSort : list[object], startIndex : int, endIndex : int) -> None:
    if endIndex <= startIndex: return
    rightPartPointer : int = partition(arrayToSort, startIndex, endIndex)
    sort(arrayToSort, startIndex, rightPartPointer - 1)
    sort(arrayToSort, rightPartPointer + 1, endIndex)

def shuffle(arrayToSort: list[object]) -> None:
    countOfElements : int = len(arrayToSort)
    for index in range(countOfElements):
        randomIndex : int = random.randrange(0, index + 1)
        swapElementsInArray(index, randomIndex, arrayToSort)

def swapElementsInArray(indexOfFirstElement: int, indexOfSecondElement: int, dataToSwap: list[object]) -> None:
    elementPuffer: object = dataToSwap[indexOfFirstElement]
    dataToSwap[indexOfFirstElement] = dataToSwap[indexOfSecondElement]
    dataToSwap[indexOfSecondElement] = elementPuffer

arrayToSort : list[object] = [4,7,1,6,9,2,5,3,8,10,15,12,14,13,11,18,19,16,17]
quickSort(arrayToSort)
print(arrayToSort)


