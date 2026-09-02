import DSA
from Collections.PriorityQueue.IndexedMinPQ import IndexedMinPQ
from Collections.PriorityQueue.MinPriorityQueueWithBinaryHeap import MinPriorityQueue
from Graphs.WeightedAndDirected.Edge import Edge
from Graphs.WeightedAndDirected.Graph import Graph
from Collections.Stack.LinkedList.StackOptionC import Stack


class ShortestPath:
    def __init__(self, graph : Graph, startNodeId : int) -> None:
        self.__graph : Graph = graph
        self.__distanceTo : list[int] =  list[int](self.__graph.getVertexCount() * [-1])
        self.__edgeTo : list[Edge | None] = DSA.objArray(self.__graph.getVertexCount())
        self.__startNodeId : int = startNodeId
        self.__dijkstra(startNodeId)

    def __dijkstra(self, startNodeId : int) -> None:
        minPQ = IndexedMinPQ(self.__graph.getVertexCount() * (self.__graph.getVertexCount() - 1))
        minPQ.insert(startNodeId, 0)
        while not minPQ.isEmpty():
            currentNodeId : int = minPQ.delMin()
            for edge in self.__graph.adj(currentNodeId):
                self.__relax(edge, minPQ)

    def __relax(self, edge : Edge, minPQ : IndexedMinPQ) -> None:
        v : int = edge.source()
        w : int = edge.target()
        if self.__distanceTo[w] > self.__distanceTo[v] + edge.weight() or self.__distanceTo[w] == -1:
            if self.__distanceTo[v] != -1:
                self.__distanceTo[w] = self.__distanceTo[v] + edge.weight()
            else:
                self.__distanceTo[w] = edge.weight()
            self.__edgeTo[w] = edge
            if minPQ.contains(w):
                minPQ.decreaseKey(w, self.__distanceTo[w])
            else:
                minPQ.insert(w, self.__distanceTo[w])

    def distanceTo(self, vertexId : int) -> float | int:
        return self.__distanceTo[vertexId]
    def pathTo(self, vertexId : int):
        stackWithPath = Stack()
        currentNodeId: int = vertexId
        while currentNodeId != self.__startNodeId:
            stackWithPath.push(currentNodeId)
            currentNodeId = self.__edgeTo[currentNodeId].source()
        stackWithPath.push(self.__startNodeId)
        return stackWithPath

    def hasPathTo(self, vertexId : int) -> bool:
        return self.__distanceTo[vertexId] != -1