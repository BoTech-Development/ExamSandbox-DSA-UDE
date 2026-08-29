def insertionSort(dataToSort : list[object]) -> list[object]:
    countOfElements : int = len(dataToSort)
    for index in range(countOfElements):
        targetSwapIndex : int = binarySearchInRange(0, index -1, dataToSort[index], dataToSort)
        if targetSwapIndex != -1:
            elementToSwap : object = dataToSort[index] # cache the element to swap/move
            shiftElementsInArrayByOne(index, targetSwapIndex, dataToSort) # shift all elements by one box, to create an empty box for insertion
            dataToSort[targetSwapIndex] = elementToSwap # insert into the new empty box

def binarySearchInRange(beginningAt : int, endingAt : int, elementToFind : object, dataToSort : list[object]) -> int:
    midIndex : int = 0
    if(endingAt <= beginningAt):
        if elementToFind > dataToSort[beginningAt]:
            return beginningAt + 1
        else:
            return beginningAt
    midIndex = beginningAt + (endingAt - beginningAt) // 2
    if elementToFind == dataToSort[midIndex]:
        return midIndex + 1
    if elementToFind > arrayToSort[midIndex]:
        return binarySearchInRange(midIndex + 1, endingAt, elementToFind, dataToSort)
    return  binarySearchInRange(beginningAt, midIndex - 1, elementToFind, dataToSort)

def shiftElementsInArrayByOne(beginningAt : int, endingAt : int, dataToShift : list[object]) -> None:
    for indexToShift in range(beginningAt - 1, endingAt - 1, -1):
        if indexToShift + 1 < len(dataToShift):
            dataToShift[indexToShift + 1] = dataToShift[indexToShift]

arrayToSort : list[object] = [10,8,3,2,7,9,1,5,4,6]
insertionSort(arrayToSort)
print(arrayToSort)