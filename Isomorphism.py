import Constant
from FullArray import getFullArray
from Matrix import getMatrix, hasSameMatrix

#未完成
def hasIsomorphism(allGraphes, newGraph):
    for graph in allGraphes:
        if isIsomorphism(graph, newGraph):
            return True

    return False

def isIsomorphism(g1, g2):
    if g1.nodeNum != g2.nodeNum:
        return False

    for i in range(0, g1.nodeNum):
        if len(g1.degs[i]) != len(g2.degs[i]):
            return False

    fullArrays = []
    curNo = 0

    for i in range(g1.nodeNum):
        fullArrays.append(getFullArray(len(g1.degs[i]), curNo))
        curNo += len(g1.degs[i])

    curNO = 0
    for i in range(g1.nodeNum):
        for node in g1.degs[i]:
            node.No = curNO
            curNO += 1
    m1 = getMatrix(g1)
    return hasSameMatrix(m1, fullArrays, g2)