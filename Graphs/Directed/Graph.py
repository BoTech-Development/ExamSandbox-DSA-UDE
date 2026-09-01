import DSA


class Graph:
    class Bag:
        class ListNode:
            next : Graph.Bag.ListNode | None = None
            def __init__(self, value : int) -> None:
                self.value = value

        __countOfNodes : int = 0
        __first : Graph.Bag.ListNode | None = None

        def __init__(self):
            pass

        def add(self, value : int) -> None:
            newFirst = Graph.Bag.ListNode(value)
            self.__countOfNodes += 1
            if self.__first is None:
                self.__first = newFirst
                return
            newFirst.next = self.__first
            self.__first = newFirst

        def remove(self, value : int) -> None:
            previousNode : Graph.Bag.ListNode | None = None
            currentNode : Graph.Bag.ListNode | None = self.__first
            while currentNode is not None:
                if currentNode.value == value:
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

    __adjacencyList : list[Graph.Bag] | None = None

    def __init__(self, countOfVertices : int):
        self.__vertexCount = countOfVertices
        self.__adjacencyList = DSA.objArray(countOfVertices)
        for index in range(countOfVertices):
            self.__adjacencyList[index] = Graph.Bag()

    def addEdge(self, fromNodeId : int, toNodeId : int) -> None:
        self.__adjacencyList[fromNodeId].add(toNodeId)
        #self.__adjacencyList[toNodeId].add(toNodeId) REMOVED to create a directed graph

    def removeEdge(self, fromNodeId : int, toNodeId : int) -> None:
        self.__adjacencyList[fromNodeId].remove(toNodeId)
        self.__adjacencyList[toNodeId].remove(fromNodeId)

    def adj(self, nodeId : int) -> Bag | None:
        return self.__adjacencyList[nodeId]

    def getVertexCount(self) -> int:
        return self.__vertexCount

    def degreeOfNode(self, specificNode : int) -> int:
        pass