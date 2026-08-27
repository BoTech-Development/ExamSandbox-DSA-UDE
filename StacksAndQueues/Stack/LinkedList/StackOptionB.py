class StackOptionB:
    __currentSize: int = 0
    __topOfStackElement: Node = None
    __firstElement: Node = None
    def __init__(self):
        pass

    def push(self, item : object) -> None:
        if self.__firstElement is None:
            self.__firstElement = Node(item)
            self.__topOfStackElement = self.__firstElement
        else:
            newNode : Node = Node(item)
            self.__topOfStackElement.setNext(newNode)
            self.__topOfStackElement = newNode
        self.__currentSize += 1

    def pop(self) -> object:
        if self.isEmpty():
            raise InvalidOperationException('Stack is empty')
        else:
            elementToReturn : object = self.__topOfStackElement.getData()
            self.__removeTopStackElement()
            return elementToReturn

    def __removeTopStackElement(self) -> None:
        currentNode : Node = self.__firstElement
        while currentNode is not None and currentNode.getNext() != self.__topOfStackElement:
            currentNode = currentNode.getNext()
        if currentNode is not None:
            currentNode.setNext(None)
        self.__topOfStackElement = currentNode
        self.__currentSize -= 1

    def isEmpty(self) -> bool:
        return self.__currentSize == 0

    def size(self) -> int:
        return self.__currentSize

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

class InvalidOperationException(Exception):
    pass

stack = StackOptionB()
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())