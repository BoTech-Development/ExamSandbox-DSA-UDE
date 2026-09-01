import graphviz

from Graphs.Weighted.Graph import Graph


class GraphVisualizer:
    def __init__(self, graph : Graph):
        self.graph : Graph = graph
    def createPng(self, fileNameWithoutExtension : str):
        g = graphviz.Digraph('Graph')
        # add all nodes
        for nodeId in range(self.graph.getVertexCount()):
            g.node(str(nodeId), str(nodeId))
        # add all Edges

        for fromNodeId in range(self.graph.getVertexCount()):
            for edge in self.graph.adj(fromNodeId):
                g.edge(str(edge.either()), str(edge.other(edge.either())), str(edge.weight()))

        g.render(fileNameWithoutExtension, format='png', cleanup=True)