from Constant import *
from FullArray import getFullArray
from Matrix import getMatrix, hasSameMatrix

#未完成
def hasIsomorphism(allGraphes, newGraph):
    for graph in allGraphes:
        if isIsomorphism(graph, newGraph):
            return False

    return True

def isIsomorphism(g1, g2):
    for i in range(0, N):
        if len(g1.degs[i]) != len(g2.degs[i]):
            return False

    fullArrays = []
    curNo = 0

    for i in range(N):
        fullArrays[i] = getFullArray(len(g1.degs[i]), curNo)
        curNo += len(g1.degs[i])

    m1 = getMatrix(g1)
    return hasSameMatrix(m1, fullArrays)