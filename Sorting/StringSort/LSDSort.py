import random
import string

import DSA


def sortLetters(arrayOfLetters : list[str], radix : int, lengthOfString : int) -> list[str]:
    sortedStrings = DSA.objArray(len(arrayOfLetters))

    for letterPosition in range(lengthOfString - 1, -1, -1):
        # re init count
        count : list[int] = DSA.intArray(radix + 1)
        # count the letters
        for letter in arrayOfLetters:
            count[specificLetterToInt(letter, letterPosition) + 1] += 1

        # Sum up ( create indexes where the letter could be in the sorted string array)
        for indexToSumUp in range(radix):
            count[indexToSumUp + 1] += count[indexToSumUp]


        for index in range(len(arrayOfLetters)):
            sortedStrings[count[specificLetterToInt(arrayOfLetters[index], letterPosition)]] = arrayOfLetters[index]
            count[specificLetterToInt(arrayOfLetters[index], letterPosition)] += 1

        for indexToCopy in range(len(arrayOfLetters)):
            arrayOfLetters[indexToCopy] = sortedStrings[indexToCopy]

    return sortedStrings

def printCountOfLetters(count : list[int]) -> None:
    for letter in string.ascii_lowercase:
        if count[specificLetterToInt(letter) + 1] != 0:
            print(letter + ": " + str(count[specificLetterToInt(letter) + 1]) + " times")

def specificLetterToInt(letter : str, pos : int) -> int:
    return ord(letter[pos])


def generate_random_strings(count, length):
    return [
        ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        for _ in range(count)
    ]


randomLetters = generate_random_strings(10, 3)
print(randomLetters)
sortedLetters = sortLetters(randomLetters, 256, 3)
print(sortedLetters)