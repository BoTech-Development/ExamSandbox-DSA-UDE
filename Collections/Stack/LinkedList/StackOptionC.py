class Stack:
    __currentSize: int = 0
    __topOfStackElement: Node | None = None

    def __init__(self):
        pass

    def push(self, item: object) -> None:
        if self.isEmpty():
            self.__topOfStackElement = Node(item)
        else:
            newNode: Node = Node(item)
            newNode.setNext(self.__topOfStackElement)
            self.__topOfStackElement = newNode
        self.__currentSize += 1

    def pop(self) -> object:
        if self.isEmpty():
            raise InvalidOperationException('Stack is empty')
        else:
            elementToReturn: object = self.__topOfStackElement.getData()
            self.__topOfStackElement = self.__topOfStackElement.getNext()
            self.__currentSize -= 1
            return elementToReturn

    def isEmpty(self) -> bool:
        return self.__currentSize == 0

    def size(self) -> int:
        return self.__currentSize

    def __iter__(self):
        self.__iterator = self.__topOfStackElement
        return self

    def __next__(self):
        if self.__topOfStackElement == None:
            raise StopIteration
        else:
            self.__iterator = self.__topOfStackElement
            return self.pop()


class Node:
    __next: Node | None = None

    def __init__(self, data: object):
        self.__data = data

    def setNext(self, nextnode: Node):
        self.__next = nextnode

    def getNext(self) -> Node:
        return self.__next

    def setData(self, data: object) -> None:
        self.__data = data

    def getData(self) -> object:
        return self.__data


class InvalidOperationException(Exception):
    pass

'''
stack = Stack()
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
'''