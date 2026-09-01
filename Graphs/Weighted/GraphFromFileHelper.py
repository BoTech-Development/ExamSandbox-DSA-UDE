import DSA
from Graphs.Weighted.Edge import Edge
from Graphs.Weighted.Graph import Graph


class GraphFromFileHelper:
    def __init__(self, filename):
        self.filename = filename

    def getGraph(self) -> Graph | None:
        data = DSA.In(self.filename)
        V : int = data.nextInt()
        E : int = data.nextInt()
        g : Graph = Graph(V)
        edgeToAdd : Edge | None = None
        for e in range(E):
            edgeToAdd : Edge = Edge(data.nextInt(), data.nextInt(), data.nextFloat())
            g.addEdge(edgeToAdd)
        return g
