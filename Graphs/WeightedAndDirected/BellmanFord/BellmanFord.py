import DSA
from Collections.PriorityQueue.IndexedMinPQ import IndexedMinPQ
from Collections.PriorityQueue.MinPriorityQueueWithBinaryHeap import MinPriorityQueue
from Collections.Queue.Array.QueueOptionB import QueueOptionB
from Graphs.WeightedAndDirected.Edge import Edge
from Graphs.WeightedAndDirected.Graph import Graph
from Collections.Stack.LinkedList.StackOptionC import Stack


class ShortestPath:
    def __init__(self, graph : Graph, startNodeId : int) -> None:
        self.__graph : Graph = graph
        self.__distanceTo : list[int] =  list[int](self.__graph.getVertexCount() * [-1])
        self.__edgeTo : list[Edge | None] = DSA.objArray(self.__graph.getVertexCount())
        self.__startNodeId : int = startNodeId
        self.__bellmanFordFast()
       # self.__bellmanFord(startNodeId)

    def __bellmanFordFast(self) -> None:
        self.__distanceTo[self.__startNodeId] = 0
        queue = QueueOptionB(self.__graph.getVertexCount())
        queue.enqueue(self.__startNodeId)
        onQ = DSA.boolArray(self.__graph.getVertexCount())
        while not queue.isEmpty():
            currentNodeId: int = queue.dequeue()
            onQ[currentNodeId] = False
            for edge in self.__graph.adj(currentNodeId):
                self.__relax(edge)


    def __relax(self, edge : Edge, queue : QueueOptionB, onQ : list[bool]) -> None:
        v : int = edge.source()
        w : int = edge.target()
        if self.__distanceTo[w] > self.__distanceTo[v] + edge.weight() or self.__distanceTo[w] == -1:
            if self.__distanceTo[v] != -1:
                self.__distanceTo[w] = self.__distanceTo[v] + edge.weight()
            else:
                self.__distanceTo[w] = edge.weight()
            self.__edgeTo[w] = edge
            if not onQ[w]:
                queue.enqueue(w)
                onQ[w] = True

    def __bellmanFord(self, startNodeId : int) -> None:
        self.__distanceTo[startNodeId] = 0
        for someNode in range(self.__graph.getVertexCount()):
            for nodeIndex in range(self.__graph.getVertexCount()):
                for edge in self.__graph.adj(nodeIndex):
                    self.__relax(edge)

    def __relax(self, edge : Edge) -> None:
        v : int = edge.source()
        w : int = edge.target()
        if self.__distanceTo[w] > self.__distanceTo[v] + edge.weight() or self.__distanceTo[w] == -1:
            if self.__distanceTo[v] != -1:
                self.__distanceTo[w] = self.__distanceTo[v] + edge.weight()
            else:
                self.__distanceTo[w] = edge.weight()
            self.__edgeTo[w] = edge

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