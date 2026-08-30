import random


def quickSort(arrayToSort: list[object]) -> None:
    shuffle(arrayToSort)
    sort(arrayToSort, 0, len(arrayToSort) - 1)

def partition(arrayToSort : list[object], startIndex : int, endIndex : int) -> tuple[int,int]:
    lessThanIndex : int = startIndex
    currentIndex : int = startIndex
    greaterThanIndex : int = endIndex
    pivotElement: object = arrayToSort[startIndex] # man wählt immer das Pivot-Element am anfang des Arrays

    while greaterThanIndex >= currentIndex: # man wiederholt solange, bis der aktuelle Index den greatThanIndex überläuft.
        if arrayToSort[currentIndex] > pivotElement: # ist das aktuelle Element größer als das Pivot-Element so ist es danach einzusortieren
            swapElementsInArray(currentIndex, greaterThanIndex, arrayToSort)
            greaterThanIndex -= 1
        elif arrayToSort[currentIndex] < pivotElement: # ist das aktuelle Element kleiner als das Pivot-Element so ist es vor dem Pivot Element einzusortieren
            swapElementsInArray(lessThanIndex, currentIndex, arrayToSort)
            lessThanIndex += 1
            currentIndex += 1
        elif pivotElement == arrayToSort[currentIndex]: # Wenn aktuelle Element und Pivot-Element gleich sind, so ist nichts zu tuen.
            currentIndex += 1
    return (lessThanIndex, greaterThanIndex)

def sort(arrayToSort : list[object], startIndex : int, endIndex : int) -> None:
    if endIndex <= startIndex: return
    (lessThanIndex, greaterThanIndex) = partition(arrayToSort, startIndex, endIndex)
    sort(arrayToSort, startIndex, lessThanIndex - 1) # Sortiere den Teil vor dem Pivot Element
    sort(arrayToSort, greaterThanIndex + 1, endIndex) # Sortiere den Teil nach dem Pivot Element

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
#arrayToSort : list[object] = ["P","A","B","X","W","P","P","V","P","D","P","C","Y","Z"] # lecture example (works also)
quickSort(arrayToSort)
print(arrayToSort)