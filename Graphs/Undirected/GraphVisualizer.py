from graphviz import Digraph

from Graphs.Undirected.Graph import Graph


class GraphVisualizer:
    def __init__(self, graph : Graph):
        self.graph : Graph = graph
    def createPng(self, fileNameWithoutExtension : str):
        g = Digraph('Graph')
        # add all nodes
        for nodeId in range(self.graph.getVertexCount()):
            g.node(str(nodeId), str(nodeId))
        # add all Edges
        '''
        for fromNodeId in range(self.graph.getVertexCount()):
            for toNodeId in self.graph.adj(fromNodeId):
                g.edge(str(fromNodeId), str(toNodeId))
        '''
        added_edges = set()

        for u in range(self.graph.getVertexCount()):
            for v in self.graph.adj(u):
                edge = tuple(sorted((u, v)))
                if edge not in added_edges:
                    g.edge(str(u), str(v))
                    added_edges.add(edge)

        g.render(fileNameWithoutExtension, format='png', cleanup=True)