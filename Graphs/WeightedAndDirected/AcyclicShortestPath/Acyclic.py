import DSA
from Collections.PriorityQueue.IndexedMinPQ import IndexedMinPQ
from Collections.PriorityQueue.MinPriorityQueueWithBinaryHeap import MinPriorityQueue
from Graphs.WeightedAndDirected.Edge import Edge
from Graphs.WeightedAndDirected.Graph import Graph
from Collections.Stack.LinkedList.StackOptionC import Stack
from Graphs.WeightedAndDirected.TopolgicalSort import TopologicalSort


class ShortestPath:
    def __init__(self, graph : Graph, startNodeId : int) -> None:
        self.__graph : Graph = graph
        self.__distanceTo : list[int] =  list[int](self.__graph.getVertexCount() * [-1])
        self.__edgeTo : list[Edge | None] = DSA.objArray(self.__graph.getVertexCount())
        self.__startNodeId : int = startNodeId
        self.__distanceTo[startNodeId] = 0 # DIESE ZEILE IST SUPER WICHTIG: wenn man sie nicht hinschreibt, dann berechnet die Methode irgendeine Distanz aber nicht die distanz vom startknoten aus.
        self.__acylic(startNodeId)

    def __acylic(self, startNodeId : int) -> None:
        topological = TopologicalSort(self.__graph)
        for node in topological.reversedPostOrder():
            for edge in self.__graph.adj(node):
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