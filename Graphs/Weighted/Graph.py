import DSA
from Graphs.Weighted.Edge import Edge


class Graph:
    class Bag:
        class ListNode:
            next : Graph.Bag.ListNode | None = None
            def __init__(self, value : Edge) -> None:
                self.value = value

        __countOfNodes : int = 0
        __first : Graph.Bag.ListNode | None = None

        def __init__(self):
            pass

        def add(self, value : Edge) -> None:
            newFirst = Graph.Bag.ListNode(value)
            self.__countOfNodes += 1
            if self.__first is None:
                self.__first = newFirst
                return
            newFirst.next = self.__first
            self.__first = newFirst

        def remove(self, edgeToRemove : Edge) -> None:
            previousNode : Graph.Bag.ListNode | None = None
            currentNode : Graph.Bag.ListNode | None = self.__first
            while currentNode is not None:
                if currentNode.value.other(currentNode.value.either()) == edgeToRemove.other(edgeToRemove.either()): # wichtig ist am schlausten den index des anderen Knotens zu vergleichen, da man sonst immer das gleiche Objekt ( reference) in die Methode stopfen muss.
                    if previousNode is not None:
                        previousNode.next = currentNode.next
                    break
                previousNode = currentNode
                currentNode = currentNode.next

        def size(self) -> int:
            return self.__countOfNodes

        def __iter__(self):
            self.__iterator = self.__first
            return self

        def __next__(self):
            if self.__iterator == None:
                raise StopIteration
            else:
                current : Graph.Bag.ListNode | None = self.__iterator
                self.__iterator = self.__iterator.next
                return current.value

    __adjacencyList: list[Graph.Bag] | None = None

    def __init__(self, countOfNodes : int):
        self.__vertexCount : int = countOfNodes
        self.__adjacencyList = DSA.objArray(countOfNodes)
        for index in range(countOfNodes):
            self.__adjacencyList[index] = Graph.Bag()

    def addEdge(self, edgeToAdd : Edge) -> None:
        self.__adjacencyList[edgeToAdd.either()].add(edgeToAdd)
        self.__adjacencyList[edgeToAdd.other(edgeToAdd.either())].add(edgeToAdd)

    def removeEdge(self, edgeToRemove : Edge) -> None:
        self.__adjacencyList[edgeToRemove.either()].remove(edgeToRemove)

    def adj(self, vertexId : int):
        return self.__adjacencyList[vertexId]

    def edges(self) -> Graph.Bag:
        resultList : Graph.Bag = Graph.Bag()
        for vertexId in range(self.__vertexCount):
            for edge in self.adj(vertexId):
                resultList.add(edge)
        return resultList

    def getVertexCount(self) -> int:
        return self.__vertexCount