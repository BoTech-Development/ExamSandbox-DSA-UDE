from Collections.PriorityQueue.MinPriorityQueueWithBinaryHeap import MinPriorityQueue
from Graphs.Weighted.Edge import Edge
from Graphs.Weighted.Graph import Graph
from UnionFind.PathCompressionWeightedQuickUF import WeightedQuickUnionUF


class MinimalSpanningTree:
    __minimalSpanningTree : Graph
    def __init__(self, graph : Graph):
        self.__graph = graph
        self.__minimalSpanningTree = Graph(graph.getVertexCount())
        self.__unionFind = WeightedQuickUnionUF(graph.getVertexCount())
        self.__kruskal()
        print("kruskal")

    def __kruskal(self) -> None:
        minEdgesPriorityQueue : MinPriorityQueue = MinPriorityQueue(3)
        for edge in self.__graph.edges():
            minEdgesPriorityQueue.insert(edge)
        minEdge : Edge
        while not minEdgesPriorityQueue.isEmpty():
            minEdge = minEdgesPriorityQueue.deleteMin()
            print("Edge: " + str(minEdge.either()) + " -> " + str(minEdge.other(minEdge.either())) + " weight: " + str(minEdge.weight()), end="")
            if not self.__unionFind.connected(minEdge.other(minEdge.either()), minEdge.either()): # would not create a cycle
                self.__unionFind.union(minEdge.other(minEdge.either()), minEdge.either())
                self.__minimalSpanningTree.addEdge(minEdge)
                print("added.")
            else:
                print("not added.")


    def getMinimalSpanningTree(self) -> Graph:
        return self.__minimalSpanningTree


    def edges(self) -> Graph.Bag:
        return self.__minimalSpanningTree.edges()
    def weight(self) -> float | int:
        result : float| int = 0
        for edge in self.edges():
            result += edge.weight()
        return result
