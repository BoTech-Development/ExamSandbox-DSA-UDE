def insertionSort(dataToSort : list[object]) -> list[object]:
    countOfElements : int = len(dataToSort)
    for index in range(countOfElements):
        targetSwapIndex : int = -1
        for backwardIndex in range(index, 0, -1):
            if dataToSort[index] < dataToSort[backwardIndex - 1]: # wenn das Element neben dem aktuellen Element nicht mehr größer ist.
                targetSwapIndex = backwardIndex - 1
        if targetSwapIndex != -1:
            elementToSwap : object = dataToSort[index] # cache the element to swap/move
            shiftElementsInArrayByOne(index, targetSwapIndex, dataToSort) # shift all elements by one box, to create an empty box for insertion
            dataToSort[targetSwapIndex] = elementToSwap # insert into the new empty box


def shiftElementsInArrayByOne(beginningAt : int, endingAt : int, dataToShift : list[object]) -> None:
    for indexToShift in range(beginningAt - 1, endingAt - 1, -1):
        if indexToShift + 1 < len(dataToShift):
            dataToShift[indexToShift + 1] = dataToShift[indexToShift]

arrayToSort : list[object] = [10,8,3,2,7,9,1,5,4,6]
insertionSort(arrayToSort)
print(arrayToSort)