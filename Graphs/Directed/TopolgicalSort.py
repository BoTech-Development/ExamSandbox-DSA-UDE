import DSA
from Collections.Stack.LinkedList.StackOptionC import Stack
from Graphs.Directed.Graph import Graph


class TopologicalSort:
    def __init__(self, graph : Graph):
        self.__marked = DSA.boolArray(graph.getVertexCount())
        self.__reversedPostOrder = Stack()
        self.__graph = graph

    def __calculate(self):
        for nodeId in range(self.__graph.getVertexCount()):
            if not self.__marked[nodeId]:
                self.__depthFirstSearch(nodeId)

    def __depthFirstSearch(self, fromNodeId : int) -> None:
        self.__marked[fromNodeId] = True
        for toNode in self.__graph.adj(fromNodeId):
            if not self.__marked[toNode]:
                self.__depthFirstSearch(toNode)
        self.__reversedPostOrder.push(fromNodeId)

    def reversedPostOrder(self) -> Stack:
        return self.__reversedPostOrder