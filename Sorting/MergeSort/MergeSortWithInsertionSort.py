import DSA

CUTOFF : int = 4

def mergeSort(arrayToSort : list[object]) -> None:
    sortPartOfArray(arrayToSort, 0, len(arrayToSort)-1)

def sortPartOfArray(arrayToSort : list[object], startIndex : int, endIndex : int) -> None:
    if endIndex <= startIndex + CUTOFF - 1: # man ist noch nicht mit allen Element fertig, es fehlen noch 4 stück.
        insertionSortWithIndex(arrayToSort, startIndex, endIndex) # diese werden mit dem Insertion sort sortiert
        return
    middleIndex : int = startIndex + (endIndex - startIndex) // 2 # berechne eine grenze, um das Array zu zerteilen
    sortPartOfArray(arrayToSort, startIndex, middleIndex) # Sortiere oder Teile wenn noch nötig die rechte hälfte (das gleiche für die linke)
    sortPartOfArray(arrayToSort, middleIndex + 1, endIndex)
    if arrayToSort[middleIndex + 1] > arrayToSort[middleIndex]: # Hier wird sofort aufgehört, wenn beide Teile einfach nur konkateniert werden müssen (Bereits der Fall) weil sie schon sortiert sind.
        return
    mergeSortedParts(arrayToSort, startIndex, middleIndex, endIndex)


def mergeSortedParts(arrayToSort : list[object], startIndex : int, middleIndex : int, endIndex : int) -> None:
    copyOfArray : list[object] = DSA.objArray(len(arrayToSort))
    copyOfArray[startIndex:endIndex+1] = arrayToSort[startIndex:endIndex+1]
    leftPartPointer : int = startIndex
    rightPartPointer : int = middleIndex + 1
    for currentIndex in range(startIndex, endIndex + 1):
        if leftPartPointer > middleIndex: # wenn das ende des linken Teils erreicht wurde
            arrayToSort[currentIndex] = copyOfArray[rightPartPointer] # nehme das Element von der rechten Seite
            rightPartPointer += 1
        elif rightPartPointer > endIndex: # wenn das ende des rechten Teils erreicht wurde
            arrayToSort[currentIndex] = copyOfArray[leftPartPointer]
            leftPartPointer += 1
        elif copyOfArray[leftPartPointer] < copyOfArray[rightPartPointer]:
            arrayToSort[currentIndex] = copyOfArray[leftPartPointer]
            leftPartPointer += 1
        else:
            arrayToSort[currentIndex] = copyOfArray[rightPartPointer]
            rightPartPointer += 1


def insertionSortWithIndex(dataToSort : list[object], startIndex : int, stopIndex : int) -> list[object]:
    for index in range(startIndex, stopIndex + 1):
        for backwardIndex in range(index, startIndex, -1):
            if dataToSort[backwardIndex] < dataToSort[backwardIndex - 1]:
                swapElementsInArray(backwardIndex, backwardIndex - 1, dataToSort)
            else:
                break

def swapElementsInArray(indexOfFirstElement : int, indexOfSecondElement : int, dataToSwap : list[object]) -> None:
    elementPuffer : object = dataToSwap[indexOfFirstElement]
    dataToSwap[indexOfFirstElement] = dataToSwap[indexOfSecondElement]
    dataToSwap[indexOfSecondElement] = elementPuffer

arrayToSort : list[object] = [4,7,1,6,9,2,5,3,8,10,15,12,14,13,11,18,19,16,17]
mergeSort(arrayToSort)
print(arrayToSort)