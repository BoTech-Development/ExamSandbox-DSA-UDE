import DSA
from Graphs.Directed.Graph import Graph


class GraphFromFileHelper:
    def __init__(self, filename):
        self.filename = filename

    def getGraph(self) -> Graph | None:
        data = DSA.In(self.filename)
        V : int = data.nextInt()
        E : int = data.nextInt()
        g : Graph = Graph(V)
        for e in range(E):
            g.addEdge(data.nextInt(), data.nextInt())
        return g
