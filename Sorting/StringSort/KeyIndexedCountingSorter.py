import DSA
import random
import string

def sortLetters(arrayOfLetters : list[str], radix : int) -> list[str]:
    sortedStrings = DSA.objArray(len(arrayOfLetters))
    count : list[int] = DSA.intArray(radix + 1)
    # count the letters
    for letter in arrayOfLetters:
        count[letterToInt(letter) + 1] += 1

    #printCountOfLetters(count)

    for index in range(radix):
        count[index + 1] += count[index]

    print("----")
    #printCountOfLetters(count)

    for index in range(len(arrayOfLetters)):
        sortedStrings[count[letterToInt(arrayOfLetters[index])]] = arrayOfLetters[index]
        count[letterToInt(arrayOfLetters[index])] += 1

    return sortedStrings

def printCountOfLetters(count : list[int]) -> None:
    for letter in string.ascii_lowercase:
        if count[letterToInt(letter) + 1] != 0:
            print(letter + ": " + str(count[letterToInt(letter) + 1]) + " times")

def letterToInt(letter : str) -> int:
    return ord(letter)


randomLetters = [random.choice(string.ascii_lowercase) for _ in range(10)]
print(randomLetters)
sortedLetters = sortLetters(randomLetters, 256)
print(sortedLetters)