def shellSort(dataToSort : list[object]):
    countOfElements: int = len(dataToSort)
    h : int = calcMaxHDependingOnArraySize(countOfElements)
    while h >= 1:
        hInsertionSort(dataToSort, h)
        h = h//3

def hInsertionSort(dataToSort : list[object], h : int) -> None:
    for index in range(h, len(dataToSort)):
        print(index)
        backwardIndex : int = index
        while backwardIndex >= h and dataToSort[backwardIndex] < dataToSort[backwardIndex - h]:
            swapElementsInArray(backwardIndex, backwardIndex - h, dataToSort)
            backwardIndex -= h

def swapElementsInArray(indexOfFirstElement: int, indexOfSecondElement: int, dataToSwap: list[object]) -> None:
    elementPuffer: object = dataToSwap[indexOfFirstElement]
    dataToSwap[indexOfFirstElement] = dataToSwap[indexOfSecondElement]
    dataToSwap[indexOfSecondElement] = elementPuffer

def calcMaxHDependingOnArraySize(countOfElements : int) -> int:
    h : int = 1
    while h < countOfElements // 3:
        h = 3 * h + 1
    return h

arrayToSort : list[object] = [10,8,3,2,7,9,1,5,4,6]
shellSort(arrayToSort)
print(arrayToSort)