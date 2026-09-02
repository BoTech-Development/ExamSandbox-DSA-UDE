class Edge:
    def __init__(self, fromNodeId: int, toNodeId: int, weight : float | int) -> None:
        self.__fromNodeId = fromNodeId
        self.__toNodeId = toNodeId
        self.__weight = weight
    def source(self) -> int:
        return self.__fromNodeId
    def target(self) -> int:
        return self.__toNodeId
    def weight(self) -> float | int:
        return self.__weight
    def __lt__(self, other : Edge) -> bool:
        if other is None:
            return False
        if type(other) is not Edge:
            return False
        return self.__weight < other.weight()