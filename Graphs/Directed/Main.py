from Graphs.Directed.BreadthFirstSearch import BreadthFirstSearch
from Graphs.Directed.ConnectedComponents import ConnectedComponents
from Graphs.Directed.DepthFirstSearch import DepthFirstSearch
from Graphs.Directed.GraphFromFileHelper import GraphFromFileHelper
from Graphs.Directed.GraphVisualizer import GraphVisualizer
from Graphs.Directed.TopicalSortVisualizer import TopologicalSortVisualizer
from Graphs.Directed.TopolgicalSort import TopologicalSort

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
print(ccHelper.connected(7,10))


topologicalSortHelper = TopologicalSort(graph)
topologicalVisualizer = TopologicalSortVisualizer(graph, topologicalSortHelper.reversedPostOrder())
print("topologicalSort: ")
for nodeId in topologicalSortHelper.reversedPostOrder():
    print(nodeId, end=",")
topologicalVisualizer.createPng("topologicalSort")

visualizer = GraphVisualizer(graph)
visualizer.createPng("test")