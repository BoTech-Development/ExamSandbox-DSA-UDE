from typing import Iterator

import DSA
from Collections.Stack.LinkedList.StackOptionC import Stack
from Graphs.WeightedAndDirected.Graph import Graph


class DepthFirstSearch:
    def __init__(self, graph : Graph, startNodeId : int):
        self.__graph = graph
        self.__marked = DSA.boolArray(graph.getVertexCount())
        self.__edgeTo = DSA.intArray(graph.getVertexCount())
        for i in range(graph.getVertexCount()):
            self.__edgeTo[i] = -1
        self.__depthFirstSearch(startNodeId)

    def __depthFirstSearch(self, fromNodeId : int) -> None:
        self.__marked[fromNodeId] = True
        for edge in self.__graph.adj(fromNodeId):
            toNode : int = edge.target()
            if not self.__marked[toNode]:
                self.__depthFirstSearch(toNode)
                self.__edgeTo[toNode] = fromNodeId

    def hasPathTo(self, toNodeId : int) -> bool:
        return self.__marked[toNodeId]

    def pathTo(self, toNodeId : int) -> Stack:
        stackWithPath = Stack()
        currentNodeId : int = toNodeId
        while currentNodeId != -1:
            stackWithPath.push(currentNodeId)
            currentNodeId = self.__edgeTo[currentNodeId]
        return stackWithPath
