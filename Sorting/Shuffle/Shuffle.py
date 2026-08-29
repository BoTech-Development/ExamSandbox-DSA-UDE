import random


def shuffle(arrayToShuffle : list[object]):
    countOfElements : int = len(arrayToShuffle)
    for index in range(countOfElements):
        randomIndex : int = random.randint(0, index)
        swapElementsInArray(index, randomIndex, arrayToShuffle)

def swapElementsInArray(indexOfFirstElement: int, indexOfSecondElement: int, dataToSwap: list[object]) -> None:
    elementPuffer: object = dataToSwap[indexOfFirstElement]
    dataToSwap[indexOfFirstElement] = dataToSwap[indexOfSecondElement]
    dataToSwap[indexOfSecondElement] = elementPuffer

arrayToSort : list[object] = [1,2,3,4,5,6,7,8,9]
shuffle(arrayToSort)
print(arrayToSort)