import DSA


class PriorityQueue:
    currentMaxIndex : int = 0
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dataArray = DSA.objArray(capacity)

    def isEmpty(self) -> bool:
        return self.currentMaxIndex == 0

    def insert(self, item : object) -> None:
        self.currentMaxIndex += 1
        self.__binarySearchInsert(item)

    def __getInsertIndexWithBinarySearch(self, item : object) -> int:
        startIndex : int = 0
        endIndex : int = len(self.dataArray) - 1
        while startIndex <= endIndex:
            midIndex : int = startIndex + (endIndex - startIndex) // 2
            if self.dataArray[midIndex] > item:
                if midIndex + 1 == endIndex:
                    return endIndex
                endIndex = midIndex - 1
            elif self.dataArray[midIndex] < item:
                if midIndex - 1 == startIndex:
                    return startIndex
                startIndex = midIndex + 1

        return -1


    def deleteMax(self) -> object:
        elementToReturn : object = self.dataArray[self.currentMaxIndex]
        self.dataArray[self.currentMaxIndex] = None
        self.currentMaxIndex -= 1
        return elementToReturn


def getInsertIndexWithBinarySearch(dataArray : list[object], item: object) -> int:
    startIndex: int = 0
    endIndex: int = len(dataArray) - 1
    while startIndex <= endIndex:
        midIndex: int = startIndex + (endIndex - startIndex) // 2
        if dataArray[midIndex] > item:
            if midIndex + 1 == endIndex:
                return endIndex
            endIndex = midIndex - 1
        elif dataArray[midIndex] < item:
            if midIndex - 1 == startIndex:
                return startIndex
            startIndex = midIndex + 1
    return -1

def binary_search_insert_position(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left



startIndex = 0
endIndex = 0
midIndex = 1

insert = 2

array = [1,3,7,9,10,11,14,16]

# Wenn Element größer als a[mid] und mid + 1 == endIndex, dann return endIndex

print(binary_search_insert_position(array, 5))

