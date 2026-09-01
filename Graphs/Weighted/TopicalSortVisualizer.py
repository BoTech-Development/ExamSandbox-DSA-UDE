import graphviz
from graphviz import Digraph

from Collections.Stack.LinkedList.StackOptionC import Stack
from Graphs.Weighted.Graph import Graph
from Graphs.Weighted.TopolgicalSort import TopologicalSort


class TopologicalSortVisualizer:
    def __init__(self, graph : Graph, topologicalSort : Stack):
        self.graph : Graph = graph
        self.topologicalSort = topologicalSort
    def createPng(self, fileNameWithoutExtension : str):
        g = Digraph('Graph')
        g.attr(rankdir='LR')
        # add all nodes
        for nodeId in self.topologicalSort:
            g.node(str(nodeId), str(nodeId))
        # add all Edges

        for fromNodeId in range(self.graph.getVertexCount()):
            for toNodeId in self.graph.adj(fromNodeId):
                g.edge(str(fromNodeId), str(toNodeId))


        g.render(fileNameWithoutExtension, format='png', cleanup=True)