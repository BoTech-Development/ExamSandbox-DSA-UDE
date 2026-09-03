import DSA

def sortiereAepfel(aepfel):
    sortedApples = DSA.objArray(len(aepfel))
    greenAppleEnd = 0
    redAppleEnd = len(aepfel) - 1
    for currentApple in range(len(aepfel)):
        if aepfel[currentApple][0] == "rot":
            sortedApples[redAppleEnd] = aepfel[currentApple]
            redAppleEnd -= 1
        elif aepfel[currentApple][0] == "grün":
            sortedApples[greenAppleEnd] = aepfel[currentApple]
            greenAppleEnd += 1
    return sortedApples

aepfel = [["rot", 23],["grün", 19],["rot", 4],["grün", 5],["rot", 38],["grün", 42]]
s = sortiereAepfel(aepfel)
print(s)