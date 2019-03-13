from Constant import *
from Isomorphism import hasIsomorphism
# 输入点的个数
N = int(input())

if not generateAllEdges():
    exit(1)

for i in range(0,2**edgeNum):
    newGraph = Graph()
    for j in range(N):
        if i & (1<<j) != 0:
           newGraph.addEdge(allEdges[j])

    if not hasIsomorphism(allGraphes, newGraph):
        allGraphes.append(newGraph)

# 画图