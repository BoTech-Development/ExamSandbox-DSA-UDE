from argparse import ArgumentError

from Collections.Dictionary.RedBlackTreeVisualizer import RedBlackTreeVisualizer
from Collections.Dictionary.TreeVisualizer import TreeVisualizer
from Collections.List.DoubleLinkedList import DoubleLinkedList

RED = True
BLACK = False

class RedBlackTree:
    class Node:
        leftSubTree: RedBlackTree.Node | None = None
        rightSubTree: RedBlackTree.Node | None = None
        parentEdgeColor : bool =  BLACK

        def __init__(self, key: object, value: object) -> None:
            self.key = key
            self.value = value
            self.countOfSubNodesAndSelf = 1

        def updateCountOfSubNodesAndSelf(self):
            if self.leftSubTree is not None and self.rightSubTree is not None:
                self.countOfSubNodesAndSelf = 1 + self.leftSubTree.countOfSubNodesAndSelf + self.rightSubTree.countOfSubNodesAndSelf
            elif self.leftSubTree is None and self.rightSubTree is not None:
                self.countOfSubNodesAndSelf = 1 + self.rightSubTree.countOfSubNodesAndSelf
            elif self.leftSubTree is not None and self.rightSubTree is None:
                self.countOfSubNodesAndSelf = 1 + self.leftSubTree.countOfSubNodesAndSelf
            else:
                self.countOfSubNodesAndSelf = 1

        def isRed(self) -> bool:
            return self.parentEdgeColor

    rootNode: Node | None = None

    def __init__(self):
        pass

    def insert(self, key: object, value: object) -> None:
        if self.rootNode is None:
            self.rootNode = RedBlackTree.Node(key, value)
            return
        self.rootNode = self.__findInsertPositionAndInsert(self.rootNode, RedBlackTree.Node(key, value))

    def get(self, key: object) -> object:
        self.__getNodeByKey(self.rootNode, key)

    def delete(self, key: object) -> None:
        pass

    def getMinKey(self) -> object:
        pass

    def getMaxKey(self) -> object:
        pass

    def size(self) -> int:
        pass

    def specificSize(self, key: object) -> int:
        pass

    def rank(self, key: object) -> int:
        pass

    def keysAscendingOrder(self) -> DoubleLinkedList[object]:
        pass

    def __correctColorsFrom(self, currentNode : RedBlackTree.Node) -> RedBlackTree.Node:
        # siehe Folie 79, Fall larger
        if currentNode.leftSubTree is not None and currentNode.rightSubTree is not None:
            if currentNode.leftSubTree.isRed() and currentNode.rightSubTree.isRed():
                self.__flipColor(currentNode)
                return currentNode
        # (Folie 79, Fall Smaller) man befindet sich hier in der mitte also beim B in der Folie
        if currentNode.leftSubTree is not None and currentNode.leftSubTree.leftSubTree is not None:
            if currentNode.leftSubTree.isRed() and currentNode.leftSubTree.leftSubTree.isRed():
                newTopNode : RedBlackTree.Node = self.__rotateRight(currentNode)
                self.__flipColor(newTopNode)
                return newTopNode
        # (Folie 79, Fall between) man befindet sich hier beim C, da man die rechts rotation ausführen muss
        if currentNode.leftSubTree is not None and currentNode.leftSubTree.rightSubTree is not None:
            if currentNode.leftSubTree.isRed() and currentNode.leftSubTree.rightSubTree.isRed():
                currentNode.leftSubTree = self.__rotateLeft(currentNode.leftSubTree.rightSubTree) # in der folie: das c hat nicht mehr das a als kind, sondern das b
                newTopNode : RedBlackTree.Node = self.__rotateRight(currentNode)
                self.__flipColor(newTopNode)
                return newTopNode
        # Siehe Folie 78, wenn man unten in einen rechten Teilbaum einfügt und eine Rote kante erzeugt, dann muss man nach links rotieren
        if currentNode.rightSubTree is not None and currentNode.rightSubTree.leftSubTree is None and currentNode.rightSubTree.rightSubTree is None and currentNode.rightSubTree.isRed():
            return self.__rotateLeft(currentNode)
        # siehe Folie 72, Einfacher fall, wenn der aktuelle Knoten der Wurzelknoten ist.
        if currentNode == self.rootNode:
            if currentNode.rightSubTree is not None and currentNode.rightSubTree.isRed():
                return self.__rotateLeft(currentNode)
        # alles ist in bester ordnung nichts zu verändern
        return currentNode

    def __findInsertPositionAndInsert(self, currentNode : RedBlackTree.Node, nodeToInsert : RedBlackTree.Node) -> RedBlackTree.Node:
        if currentNode.key > nodeToInsert.key:
            if currentNode.leftSubTree is None:
                currentNode.leftSubTree = nodeToInsert
                nodeToInsert.parentEdgeColor = RED
            else:
                currentNode.leftSubTree = self.__findInsertPositionAndInsert(currentNode.leftSubTree, nodeToInsert)
        else:
            if currentNode.rightSubTree is None:
                currentNode.rightSubTree = nodeToInsert
                nodeToInsert.parentEdgeColor = RED
            else:
                currentNode.rightSubTree = self.__findInsertPositionAndInsert(currentNode.rightSubTree, nodeToInsert)
        return self.__correctColorsFrom(currentNode)

    def __getNodeByKey(self, currentNode : RedBlackTree.Node | None, key : object) -> RedBlackTree.Node | None:
        if currentNode is None:
            return None
        if currentNode.key == key:
            return currentNode
        if currentNode.key > key:
            if currentNode.leftSubTree is not None:
                return self.__getNodeByKey(currentNode.leftSubTree, key)
        else:
            if currentNode.rightSubTree is not None:
                return self.__getNodeByKey(currentNode.rightSubTree, key)

    # Diese Methode rotiert zwar zwei Knoten, passt aber nicht die Referenz des "Eltern" Knoten an.
    # Die Methode übergibt den Knoten, der als neue Referenz des "Eltern" Knoten genutzt werden kann.
    def __rotateLeft(self, nodeToRotate : RedBlackTree.Node) -> RedBlackTree.Node:
        newTopNode : RedBlackTree.Node = nodeToRotate.rightSubTree
        nodeToRotate.rightSubTree = newTopNode.leftSubTree
        newTopNode.leftSubTree = nodeToRotate
        newTopNode.parentEdgeColor = nodeToRotate.parentEdgeColor
        nodeToRotate.parentEdgeColor = RED
        return newTopNode

    # Diese Methode rotiert zwar zwei Knoten, passt aber nicht die Referenz des "Eltern" Knoten an.
    # Die Methode übergibt den Knoten, der als neue Referenz des "Eltern" Knoten genutzt werden kann.
    def __rotateRight(self, nodeToRotate : RedBlackTree.Node) -> RedBlackTree.Node:
        newTopNode : RedBlackTree.Node = nodeToRotate.leftSubTree
        nodeToRotate.leftSubTree = newTopNode.rightSubTree
        newTopNode.rightSubTree = nodeToRotate
        newTopNode.parentEdgeColor = nodeToRotate.parentEdgeColor
        nodeToRotate.parentEdgeColor = RED
        return newTopNode

    def __flipColor(self, nodeToFlipColor : RedBlackTree.Node) -> None:
        nodeToFlipColor.parentEdgeColor = not nodeToFlipColor.parentEdgeColor
        nodeToFlipColor.rightSubTree.parentEdgeColor = not nodeToFlipColor.rightSubTree.parentEdgeColor
        nodeToFlipColor.leftSubTree.parentEdgeColor = not nodeToFlipColor.leftSubTree.parentEdgeColor

rbTree = RedBlackTree()
visual = RedBlackTreeVisualizer(BLACK)

counter = 0
for key in [20, 10, 5, 15, 30, 25, 6, 8, 9, 7]:
    rbTree.insert(key, key)
    visual.visualize(rbTree.rootNode, "tree" + str(counter))
    counter += 1