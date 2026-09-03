import random
import string

import DSA

radix : int = 256

def sortStrings(arrayOfStrings : list[str]) -> list[str]:
    sortedStrings = DSA.objArray(len(arrayOfStrings))
    __sortStrings(arrayOfStrings, sortedStrings, 0, 0, len(arrayOfStrings))
    return arrayOfStrings

def __sortStrings(arrayOfStrings : list[str], sortedStrings : list[str], letterPosition : int, lowerBound : int, upperBound : int) -> None:
    if upperBound <= lowerBound:
        return

    # re init count
    count : list[int] = DSA.intArray(radix + 1)
    # count the letters
    for indexOfString in range(lowerBound, upperBound):
        count[specificLetterToInt(arrayOfStrings[indexOfString], letterPosition) + 2] += 1

    # Sum up ( create indexes where the letter could be in the sorted string array)
    for indexToSumUp in range(radix):
        count[indexToSumUp + 1] += count[indexToSumUp]

    # Sort the strings.
    for index in range(lowerBound, upperBound):
        sortedStrings[count[specificLetterToInt(arrayOfStrings[index], letterPosition) + 1]] = arrayOfStrings[index]
        count[specificLetterToInt(arrayOfStrings[index], letterPosition) + 1] += 1

    for indexToCopy in range(lowerBound, upperBound):
        arrayOfStrings[indexToCopy] = sortedStrings[indexToCopy]

    # die neue partitionen wieder rekursiv abarbeiten
    for index in range(radix):
        __sortStrings(arrayOfStrings, sortedStrings, letterPosition + 1, lowerBound + count[index], lowerBound + count[index + 1])

def specificLetterToInt(string : str, pos : int) -> int:
    if pos < len(string):
        return ord(string[pos])
    else:
        return -1

def generate_random_strings(count, length):
    return [
        ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        for _ in range(count)
    ]

randomStrings = generate_random_strings(10, 3)
print(randomStrings)
sortedStrings = sortStrings(randomStrings)
print(sortedStrings)