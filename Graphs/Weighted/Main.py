from Graphs.Weighted.BreadthFirstSearch import BreadthFirstSearch
from Graphs.Weighted.ConnectedComponents import ConnectedComponents
from Graphs.Weighted.DepthFirstSearch import DepthFirstSearch
from Graphs.Weighted.GraphFromFileHelper import GraphFromFileHelper
from Graphs.Weighted.GraphVisualizer import GraphVisualizer
from Graphs.Weighted.Kruskal import Kruskal
from Graphs.Weighted.Prim import Prim

gReader = GraphFromFileHelper("tinyGraph.txt")
graph = gReader.getGraph()


print("---------DFS--------")

dfsHelper = DepthFirstSearch(graph, 0)
print(dfsHelper.hasPathTo(1))

#path to node 3
for node in dfsHelper.pathTo(3):
    print(node)

print("---------BFS--------")

bfsHelper = BreadthFirstSearch(graph, 0)
print(bfsHelper.hasPathTo(1))
for node in bfsHelper.pathTo(3):
    print(node)

print("distTo: " + str(bfsHelper.getDistanceFromStartToNode(4)))

print("---------CC---------")
ccHelper = ConnectedComponents(graph)
print(ccHelper.count())
print(ccHelper.id(7))
print(ccHelper.connected(7,5))

mstHelperKruskal = Kruskal.MinimalSpanningTree(graph)
visualizer = GraphVisualizer(mstHelperKruskal.getMinimalSpanningTree())
visualizer.createPng("minimalKruskal")

mstHelperKruskal = Prim.MinimalSpanningTree(graph)
visualizer = GraphVisualizer(mstHelperKruskal.getMinimalSpanningTree())
visualizer.createPng("minimalPrim")

visualizer = GraphVisualizer(graph)
visualizer.createPng("test")