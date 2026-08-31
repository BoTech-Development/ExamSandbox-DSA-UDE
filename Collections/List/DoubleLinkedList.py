from typing import TypeVar, Generic

T = TypeVar('T') # DECLARING GENERICS IN JAVA / C# IS SIGNIFICANTLY EASIER AND CLEANER
# C# OR JAVA IS BETTER THAN PYTHON FOR OOP

class DoubleLinkedListNode(Generic[T]):
    def __init__(self, previousNode : DoubleLinkedListNode, nextNode : DoubleLinkedListNode, data : T):
       self.next : DoubleLinkedListNode = nextNode
       self.prev : DoubleLinkedListNode = previousNode
       self.data : T = data

class DoubleLinkedList[T]:
    def __init__(self):
       self.first : DoubleLinkedListNode[T] = None
       self.last : DoubleLinkedListNode = None
       self.count = 0

    def isEmpty(self) -> bool:
       return self.first is None and self.last is None and self.count == 0

    def size(self) -> int:
       return self.count

    def addToLast(self, data : object) -> None:
       self.last = self.__insertBetween(data, self.last, None)
       if (self.count == 1):  # Added first Element
          self.first = self.last

    def addToFirst(self, data : object) -> None:
       self.first = self.__insertBetween(data, None, self.first)
       if(self.count == 1): # Added first Element
          self.last = self.first

    def __insertBetween(self, dataToInsert : object, previousNode : DoubleLinkedListNode, nextNode : DoubleLinkedListNode) -> DoubleLinkedListNode:
       newNode : DoubleLinkedListNode = DoubleLinkedListNode(previousNode, nextNode, dataToInsert)
       if previousNode is not None:
          previousNode.next = newNode
       if nextNode is not None:
          nextNode.prev = newNode
       self.count += 1
       return newNode

    def removeFromLast(self, dataToRemove : object) -> None:
       if self.isEmpty(): return
       currentNode : DoubleLinkedListNode = self.last
       while currentNode is not None:
          if currentNode.data == dataToRemove:
             if currentNode == self.last:
                self.last = self.last.prev
             else:
                self.__join(currentNode.next, currentNode.prev)
             return
          currentNode = currentNode.prev

    def removeFromFirst(self, dataToRemove: object) -> None:
       if self.isEmpty(): return
       currentNode: DoubleLinkedListNode = self.first
       while currentNode is not None:
          if currentNode.data == dataToRemove:
             if currentNode == self.first:
                self.first = self.first.next
             else:
                self.__join(currentNode.next, currentNode.prev)
             return
          currentNode = currentNode.next

    def __join(self, nextNode : DoubleLinkedListNode, prevNode : DoubleLinkedListNode) -> None:
       if nextNode is None or prevNode is None: return
       nextNode.prev = prevNode
       prevNode.next = nextNode

    def __iter__(self):
        current = self.first
        while current is not None:
            yield current.data
            current = current.next



class Deque[T]:
    def __init__(self):
       self.linkedList = DoubleLinkedList[T]()

    def isEmpty(self) -> bool:
       return self.linkedList.isEmpty()

    def size(self) -> int:
       return self.linkedList.size()

    def pushLeft(self,data : T) -> None:
       self.linkedList.addToFirst(data)

    def pushRight(self,data : T) -> None:
       self.linkedList.addToLast(data)

    def popLeft(self) -> T:
       if self.linkedList.isEmpty(): return None
       oldData : T = self.linkedList.first.data
       self.linkedList.removeFromFirst(oldData)
       return oldData

    def popRight(self) -> T:
       if self.linkedList.isEmpty(): return None
       oldData: T = self.linkedList.last.data
       self.linkedList.removeFromLast(oldData)
       return oldData
