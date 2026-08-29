def insertionSort(dataToSort : list[object]) -> list[object]:
    countOfElements : int = len(dataToSort)
    for index in range(countOfElements):
        for backwardIndex in range(index, 0, -1):
            if dataToSort[backwardIndex] < dataToSort[backwardIndex - 1]:
                swapElementsInArray(backwardIndex, backwardIndex - 1, dataToSort)
            else:
                break

def swapElementsInArray(indexOfFirstElement : int, indexOfSecondElement : int, dataToSwap : list[object]) -> None:
    elementPuffer : object = dataToSwap[indexOfFirstElement]
    dataToSwap[indexOfFirstElement] = dataToSwap[indexOfSecondElement]
    dataToSwap[indexOfSecondElement] = elementPuffer


arrayToSort : list[object] = [10,8,3,2,7,9,1,5,4,6]
insertionSort(arrayToSort)
print(arrayToSort)