import DSA


def mergeSort(arrayToSort : list[object]) -> None:
    sortPartOfArray(arrayToSort, 0, len(arrayToSort)-1)

def sortPartOfArray(arrayToSort : list[object], startIndex : int, endIndex : int) -> None:
    if endIndex <= startIndex: # man ist fertig, wenn alles sortiert wurde
        return
    middleIndex : int = startIndex + (endIndex - startIndex) // 2 # berechne eine grenze um das Array zu zerteilen
    sortPartOfArray(arrayToSort, startIndex, middleIndex) # Sortiere oder Teile wenn noch nötig die rechte hälfte (das gleiche für die linke)
    sortPartOfArray(arrayToSort, middleIndex + 1, endIndex)
    mergeSortedParts(arrayToSort, startIndex, middleIndex, endIndex)
    print(arrayToSort[startIndex : endIndex])

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


arrayToSort : list[object] = [4,7,1,6,9,2,5,3,8]
mergeSort(arrayToSort)
print(arrayToSort)