import random


def quickSort(arrayToSort: list[object]) -> None:
    shuffle(arrayToSort)
    sort(arrayToSort, 0, len(arrayToSort) - 1)

def partition(arrayToSort : list[object], startIndex : int, endIndex : int) -> tuple[int,int]:
    lessThanIndex : int = startIndex + 1
    currentIndex : int = lessThanIndex
    greaterThanIndex : int = endIndex - 1

    # Initialisiere beide pivot Elemente, die sich am Anfang und am Ende des Arrays befinden.
    pivotElementA: object = arrayToSort[startIndex]
    pivotElementB: object = arrayToSort[endIndex]

    if pivotElementA > pivotElementB: # korrigiere die Reihenfolge von den beiden Pivotelementen, damit immer pivotElementA <= pivotElementB gilt. Ansonsten würden die Elemente nicht richtig einsortiert werden.
        swapElementsInArray(endIndex, startIndex, arrayToSort)
        pivotElementA = arrayToSort[startIndex]
        pivotElementB = arrayToSort[endIndex]

    while greaterThanIndex >= currentIndex:
        if arrayToSort[currentIndex] > pivotElementB:
            swapElementsInArray(currentIndex, greaterThanIndex, arrayToSort)
            greaterThanIndex -= 1
        elif arrayToSort[currentIndex] < pivotElementA:
            swapElementsInArray(lessThanIndex, currentIndex, arrayToSort)
            lessThanIndex += 1
            currentIndex += 1
        else: # wir wissen, dass das Element weder vor noch hinter den Pivot-Elementen einzusortieren ist, weshalb wir direkt den aktuellen index inkrementieren können
            currentIndex += 1

    lessThanIndex -= 1
    swapElementsInArray(startIndex, lessThanIndex, arrayToSort)
    greaterThanIndex += 1
    swapElementsInArray(endIndex, greaterThanIndex, arrayToSort)

    return (lessThanIndex, greaterThanIndex)

def sort(arrayToSort : list[object], startIndex : int, endIndex : int) -> None:
    if endIndex <= startIndex: return
    (lessThanIndex, greaterThanIndex) = partition(arrayToSort, startIndex, endIndex)
    sort(arrayToSort, startIndex, lessThanIndex)
    sort(arrayToSort, lessThanIndex + 1, greaterThanIndex - 1) # WICHITG: wir müssen hier natürlich auch den inneren Teil nocheinmal sortieren, da wie keine Aussage über die Elemente mit zwei beliebigen Pivot-Elementen getroffen haben
    sort(arrayToSort, greaterThanIndex, endIndex)

def shuffle(arrayToSort: list[object]) -> None:
    countOfElements : int = len(arrayToSort)
    for index in range(countOfElements):
        randomIndex : int = random.randrange(0, index + 1)
        swapElementsInArray(index, randomIndex, arrayToSort)

def swapElementsInArray(indexOfFirstElement: int, indexOfSecondElement: int, dataToSwap: list[object]) -> None:
    elementPuffer: object = dataToSwap[indexOfFirstElement]
    dataToSwap[indexOfFirstElement] = dataToSwap[indexOfSecondElement]
    dataToSwap[indexOfSecondElement] = elementPuffer

#arrayToSort : list[object] = [4,7,1,6,9,2,5,3,8,10,15,12,14,13,11,18,19,16,17]
arrayToSort : list[object] = ["S","E","A","Y","R","L","F","V","Z","Q","T","C","M","K"] # lecture example (works also)
quickSort(arrayToSort)
print(arrayToSort)