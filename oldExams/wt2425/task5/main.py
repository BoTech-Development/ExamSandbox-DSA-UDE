import DSA


def keyIndexedStringSort(listOfStrings : list[str], radix : int, stringLen : int) -> None:
    sortedStringsArray : list[str] = [""] * len(listOfStrings)
    for letterPosition in range(stringLen-1,-1,-1):
        count: list[int] = DSA.intArray(radix + 1)
        for indexToCount in range(len(listOfStrings)):
            count[letterToInt(listOfStrings[indexToCount], letterPosition) + 1] += 1

        for indexToSumUp in range(radix):
            count[indexToSumUp + 1] += count[indexToSumUp]

        for indexToSort in range(len(listOfStrings)):
            sortedStringsArray[count[letterToInt(listOfStrings[indexToSort], letterPosition)]] = listOfStrings[indexToSort]
            count[letterToInt(listOfStrings[indexToSort], letterPosition)] += 1

        for indexToCopy in range(len(listOfStrings)):
            listOfStrings[indexToCopy] = sortedStringsArray[indexToCopy]

def letterToInt(letter : str, pos : int) -> int:
    return ord(letter[pos])

stringsToSort = ["abc", "cba", "bca"]
keyIndexedStringSort(stringsToSort,256,3)
print(stringsToSort)