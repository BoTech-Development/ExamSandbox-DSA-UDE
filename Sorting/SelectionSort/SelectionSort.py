def selectionSort(dataToSort : list[object]) -> list[object]:
    countOfElements : int = len(dataToSort)
    for index in range(countOfElements):
        indexOfMinimumElement : int = index
        # find minimum here
        for currentMinimumFindIndex in range(index, countOfElements):
            if dataToSort[currentMinimumFindIndex] < dataToSort[indexOfMinimumElement]:
                indexOfMinimumElement = currentMinimumFindIndex
        swapElementsInArray(indexOfMinimumElement, index, dataToSort)

def swapElementsInArray(indexOfFirstElement : int, indexOfSecondElement : int, dataToSwap : list[object]) -> None:
    elementPuffer : object = dataToSwap[indexOfFirstElement]
    dataToSwap[indexOfFirstElement] = dataToSwap[indexOfSecondElement]
    dataToSwap[indexOfSecondElement] = elementPuffer

