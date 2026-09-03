import DSA

w=[
    [],
    [2],
    [3, 5],
    [4],
    [5],
    []
]
s=1


def erreichbar(w : list[list[int]], s : int) -> bool:
    marked : list[bool] = DSA.boolArray(len(w))
    dfs(w, s, marked)
    print(marked)
    for markedStatus in marked:
        if not markedStatus:
            return False
    return True

def dfs(wald : list[list[int]], currentNodeId : int, marked : list[bool]) -> None:
    marked[currentNodeId] = True
    for nextNodeId in wald[currentNodeId]:
        if not marked[nextNodeId]:
            dfs(wald, nextNodeId, marked)


print(erreichbar(w,s))