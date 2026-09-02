from Graphs.WeightedAndDirected.AcyclicShortestPath import Acyclic
from Graphs.WeightedAndDirected.BellmanFord import BellmanFord
from Graphs.WeightedAndDirected.BreadthFirstSearch import BreadthFirstSearch
from Graphs.WeightedAndDirected.ConnectedComponents import ConnectedComponents
from Graphs.WeightedAndDirected.DepthFirstSearch import DepthFirstSearch
from Graphs.WeightedAndDirected.Dijkstra import Dijkstra
from Graphs.WeightedAndDirected.Dijkstra.Dijkstra import ShortestPath
from Graphs.WeightedAndDirected.GraphFromFileHelper import GraphFromFileHelper
from Graphs.WeightedAndDirected.GraphVisualizer import GraphVisualizer


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


print("---------SP(Dijkstra)---------")
spHelper = Dijkstra.ShortestPath(graph, 0)
print(spHelper.hasPathTo(3))
print(spHelper.distanceTo(3))
print("path to")
for node in spHelper.pathTo(3):
    print(node)


print("---------SP(Acyclic)---------")
spHelper = Acyclic.ShortestPath(graph, 0 )
print(spHelper.hasPathTo(3))
print(spHelper.distanceTo(3))
print("path to")
for node in spHelper.pathTo(3):
    print(node)


print("---------SP(BellmanFord)---------")
spHelper = BellmanFord.ShortestPath(graph, 0 )
print(spHelper.hasPathTo(3))
print(spHelper.distanceTo(3))
print("path to")
for node in spHelper.pathTo(3):
    print(node)

visualizer = GraphVisualizer(graph)
visualizer.createPng("test")