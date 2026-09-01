import DSA
from Collections.Queue.LinkedList.Queue import ListQueue
from Collections.Stack.LinkedList.StackOptionC import Stack
from Graphs.Undirected.Graph import Graph


class BreadthFirstSearch:
    def __init__(self, graph : Graph, startNodeId : int):
        self.__graph = graph
        self.__marked = DSA.boolArray(graph.getVertexCount())
        self.__edgeTo = DSA.intArray(graph.getVertexCount())
        self.__distanceTo = DSA.intArray(graph.getVertexCount())
        for i in range(graph.getVertexCount()):
            self.__edgeTo[i] = -1
            self.__distanceTo[i] = -1
        self.__startNodeId = startNodeId
        self.__breathFirstSearch()

    def __breathFirstSearch(self) -> None:
        queue = ListQueue()
        queue.enqueue(self.__startNodeId)
        self.__distanceTo[self.__startNodeId] = 0
        self.__marked[self.__startNodeId] = True
        while not queue.isEmpty():
            currentNodeId = queue.dequeue()
            for nextNodeId in self.__graph.adj(currentNodeId):
                if self.__marked[nextNodeId] == False:
                    self.__marked[nextNodeId] = True
                    self.__edgeTo[nextNodeId] = currentNodeId
                    self.__distanceTo[nextNodeId] = self.__distanceTo[currentNodeId] + 1
                    queue.enqueue(nextNodeId)

    # Vorsichtig hier wird die Länge von einem Weg zurückgegeben nicht der kürzeste Weg
    def getDistanceFromStartToNode(self, toNodeId : int) -> int | None:
        if self.__distanceTo[toNodeId] != -1:
            return self.__distanceTo[toNodeId]
        return None

    def hasPathTo(self, toNodeId : int) -> bool:
        return self.__marked[toNodeId]

    def pathTo(self, toNodeId : int) -> Stack:
        stackWithPath = Stack()
        currentNodeId : int = toNodeId
        while currentNodeId != -1:
            stackWithPath.push(currentNodeId)
            currentNodeId = self.__edgeTo[currentNodeId]
        return stackWithPath
