import DSA
from Collections.PriorityQueue.MinPriorityQueueWithBinaryHeap import MinPriorityQueue
from Graphs.Weighted.Edge import Edge
from Graphs.Weighted.Graph import Graph
from UnionFind.PathCompressionWeightedQuickUF import WeightedQuickUnionUF


class MinimalSpanningTree:
    __minimalSpanningTree : Graph
    def __init__(self, graph : Graph):
        self.__graph = graph
        self.__minimalSpanningTree = Graph(graph.getVertexCount())
        self.__marked = DSA.boolArray(graph.getVertexCount())
        self.__minEdgesPriorityQueue : MinPriorityQueue = MinPriorityQueue(3)
        self.__prim()
        print("prim")

    def __prim(self) -> None:
        countOfAddedNodes : int = 0
        self.__addAllEdgesToPriorityQueueAndVisitNode(0)
        while not self.__minEdgesPriorityQueue.isEmpty() and countOfAddedNodes < self.__graph.getVertexCount() - 1:
            edge : Edge = self.__minEdgesPriorityQueue.deleteMin()
            firstNodeId : int = edge.either()
            secondNodeId : int = edge.other(firstNodeId)
            if self.__marked[firstNodeId] and self.__marked[secondNodeId]:
                continue
            self.__minimalSpanningTree.addEdge(edge)
            countOfAddedNodes += 1
            if not self.__marked[firstNodeId]:
                self.__addAllEdgesToPriorityQueueAndVisitNode(firstNodeId)
            if not self.__marked[secondNodeId]:
                self.__addAllEdgesToPriorityQueueAndVisitNode(secondNodeId)

    def __addAllEdgesToPriorityQueueAndVisitNode(self, nodeId : int) -> None:
        self.__marked[nodeId] = True
        for edge in self.__graph.adj(nodeId):
            if not self.__marked[edge.other(nodeId)]:
                self.__minEdgesPriorityQueue.insert(edge)

    def getMinimalSpanningTree(self) -> Graph:
        return self.__minimalSpanningTree
    def edges(self) -> Graph.Bag:
        return self.__minimalSpanningTree.edges()
    def weight(self) -> float | int:
        result : float| int = 0
        for edge in self.edges():
            result += edge.weight()
        return result
