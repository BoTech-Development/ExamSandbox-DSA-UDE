import DSA
from Graphs.WeightedAndDirected.DepthFirstSearch import DepthFirstSearch
from Graphs.WeightedAndDirected.Graph import Graph


class ConnectedComponents:
    __componentCount : int = 0

    def __init__(self, graph : Graph):
        self.__graph = graph
        self.__components = DSA.intArray(graph.getVertexCount())
        for i in range(graph.getVertexCount()):
            self.__components[i] = -1
        self.__initConnectedComponents()

    def __initConnectedComponents(self) -> None:
        marked : list[bool] = DSA.boolArray(self.__graph.getVertexCount())
        currentComponentId : int = 0
        for nodeId in range(self.__graph.getVertexCount()):
            if not marked[nodeId]:
                dfs : DepthFirstSearch = DepthFirstSearch(self.__graph, nodeId)
                for nodeInComponent in range(self.__graph.getVertexCount()):
                    if dfs.hasPathTo(nodeInComponent):
                        marked[nodeInComponent] = True
                        self.__components[nodeInComponent] = currentComponentId
                currentComponentId += 1
        self.__componentCount = currentComponentId

    # Prüfe ob zwei Knoten die gleiche Komponente haben
    def connected(self, fromNodeId : int,  toNodeId : int) -> int | None:
        return self.__components[fromNodeId] != -1 and self.__components[toNodeId] != -1 and self.__components[fromNodeId] == self.__components[toNodeId]

    # zähle wie viele Komponenten existieren
    def count(self) -> int:
        return self.__componentCount

    # Übergebe die Id des Components
    def id(self, vertexId: int) -> int:
        return self.__components[vertexId]