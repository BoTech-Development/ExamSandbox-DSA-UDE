class ListQueue:
    __first: Node = None
    __last: Node = None

    def __init__(self):
        pass

    def enqueue(self, data : object) -> None:
        oldlast : Node = self.__last
        self.__last = Node(data)
        if self.isEmpty():
            self.__first = self.__last
        else:
            oldlast.setNext(self.__last)

    def dequeue(self):
        item : object = self.__first.getData()
        self.__first = self.__first.getNext()
        if self.isEmpty():
            self.__last = None
        return item

    def isEmpty(self):
        return self.__first == None

class Node:
    __next: Node = None
    def __init__(self, data : object):
        self.__data = data
    def setNext(self, nextnode : Node):
        self.__next = nextnode
    def getNext(self) -> Node:
        return self.__next
    def setData(self, data : object) -> None:
            self.__data = data
    def getData(self) -> object:
        return self.__data
    def __lt__(self, other):
        pass