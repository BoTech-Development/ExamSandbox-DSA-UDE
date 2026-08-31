from Collections.Dictionary.TreeVisualizer import TreeVisualizer
from Collections.List.DoubleLinkedList import DoubleLinkedList


class BinarySearchTree:
    class Node:
        leftSubTree : BinarySearchTree.Node = None
        rightSubTree : BinarySearchTree.Node = None

        def __init__(self, key : object, value : object) -> None:
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

    rootNode : Node = None

    def __init__(self):
        pass
    def insert(self, key : object, value : object) -> None:
        if self.rootNode is None:
            self.rootNode = BinarySearchTree.Node(key, value)
            return
        self.__insertAt(self.rootNode, BinarySearchTree.Node(key, value))

    def get(self, key : object) -> object:
        return self.__getNodeByKey(self.rootNode, key)

    def delete(self, key : object) -> None:
        self.rootNode = self.__delete(self.rootNode, key)

    def getMinKey(self) -> object:
        return self.__getMinNode(self.rootNode).key

    def getMaxKey(self) -> object:
        return self.__getMaxNode(self.rootNode).key

    def size(self) -> int:
        if self.rootNode is None:
            return 0
        return self.rootNode.countOfSubNodesAndSelf

    def specificSize(self, key : object) -> int:
        node : BinarySearchTree.Node = self.get(key)
        if node is None:
            return 0
        return node.countOfSubNodesAndSelf

    def rank(self, key : object) -> int:
        return self.__rank(key, self.rootNode)

    def keysAscendingOrder(self) -> DoubleLinkedList[object]:
        resultList : DoubleLinkedList[object] = DoubleLinkedList()
        self.__inorder(self.rootNode, resultList)
        return resultList

    def __inorder(self, currentNode : BinarySearchTree.Node, resultList : DoubleLinkedList[object]) -> None:
        if currentNode is None:
            return
        self.__inorder(currentNode.leftSubTree, resultList)
        resultList.addToFirst(currentNode.key)
        self.__inorder(currentNode.rightSubTree, resultList)

    def __insertAt(self, currentNode : BinarySearchTree.Node, nodeToInsert : BinarySearchTree.Node) -> None:
        if currentNode.key > nodeToInsert.key:
            if currentNode.leftSubTree is None:
                currentNode.leftSubTree = nodeToInsert
            else:
                self.__insertAt(currentNode.leftSubTree, nodeToInsert)
        else:
            if currentNode.rightSubTree is None:
                currentNode.rightSubTree = nodeToInsert
            else:
                self.__insertAt(currentNode.rightSubTree, nodeToInsert)
        currentNode.updateCountOfSubNodesAndSelf()

    def __getNodeByKey(self, currentNode : BinarySearchTree.Node, key : object) -> BinarySearchTree.Node:
        if currentNode.key == key:
            return currentNode
        if currentNode.key > key:
            if currentNode.leftSubTree is not None:
                return self.__getNodeByKey(currentNode.leftSubTree, key)
        else:
            if currentNode.rightSubTree is not None:
                return self.__getNodeByKey(currentNode.rightSubTree, key)

    def __delete(self, currentNode : BinarySearchTree.Node, key : object) -> BinarySearchTree.Node:
        if currentNode is None:
            return None
        if currentNode.key < key:
            currentNode.rightSubTree = self.__delete(currentNode.rightSubTree, key)
        elif currentNode.key > key:
            currentNode.leftSubTree = self.__delete(currentNode.leftSubTree, key)
        else:
            if currentNode.leftSubTree is None: 
                return currentNode.rightSubTree
            if currentNode.rightSubTree is None: 
                return currentNode.leftSubTree
            nodeToDelete : BinarySearchTree.Node = currentNode
            minNodeInRigthTreeOfNodeToDelete : BinarySearchTree.Node = self.__getMinNode(nodeToDelete.rightSubTree)
            # exchange this node with the min node of the right tree
            minNodeInRigthTreeOfNodeToDelete.rightSubTree = self.__deleteMinAndReturnNewTree(nodeToDelete.rightSubTree)
            minNodeInRigthTreeOfNodeToDelete.leftSubTree = nodeToDelete.leftSubTree
            currentNode.updateCountOfSubNodesAndSelf()
        return currentNode

    def __getMinNode(self, currentNode : BinarySearchTree.Node) -> BinarySearchTree.Node:
        if currentNode.leftSubTree is None:
            return currentNode
        return self.__getMinNode(currentNode.leftSubTree)
            
    def __deleteMinAndReturnNewTree(self, currentNode : BinarySearchTree.Node) -> BinarySearchTree.Node:
        if currentNode.leftSubTree is None:
            currentNode.updateCountOfSubNodesAndSelf()
            return currentNode.rightSubTree # Der Letzte (kleinste Knoten) enthält keinen linken Teilbaum mehr
        currentNode.leftSubTree = self.__deleteMinAndReturnNewTree(currentNode.leftSubTree)
        currentNode.updateCountOfSubNodesAndSelf()
        return currentNode

    def __getMaxNode(self, currentNode: BinarySearchTree.Node) -> BinarySearchTree.Node:
        if currentNode.rightSubTree is None:
            return currentNode
        return self.__getMaxNode(currentNode.rightSubTree)

    def __rank(self, key : object, currentNode : BinarySearchTree.Node) -> int:
        if currentNode is None:
            return 0
        if key < currentNode.key:
            return self.__rank(key, currentNode.leftSubTree)
        elif key > currentNode.key:
            if currentNode.leftSubTree is None:
                return self.__rank(key, currentNode.rightSubTree) + 1
            return 1 + currentNode.leftSubTree.countOfSubNodesAndSelf + self.__rank(key, currentNode.rightSubTree)
        elif currentNode.leftSubTree is None:
            return 0
        return currentNode.leftSubTree.countOfSubNodesAndSelf


bst = BinarySearchTree()

for key in [20,10,5,15,30,25]:
    bst.insert(key,key)

for key in [20,10,5,15,30,25]:
    print(str(key) + ":" + str(bst.rank(key)))

visual = TreeVisualizer(bst.rootNode)
visual.run()

