import Constant
from Isomorphism import hasIsomorphism
import Matrix
import DrawGraph

# 输入点的个数
Constant.N = int(input())

if not Constant.generateAllEdges():
    exit(1)

for nodeNum in range(0,Constant.N+1):
    for i in range(0,2**(Constant.edgeNum+1)):
        newGraph = Constant.Graph(nodeNum)
        for j in range(Constant.edgeNum):
            if i & (1<<j) != 0:
               newGraph.addEdge(Constant.allEdges[j])

        judge = hasIsomorphism(Constant.allGraphes, newGraph)
        if not judge:
            Constant.allGraphes.append(newGraph)
            Constant.allMatrix.append(Matrix.getMatrix(newGraph))
            print(Matrix.getMatrix(newGraph))

for M in Constant.allMatrix:
    DrawGraph.drawgraph(M)

print('共有{}个图'.format(len(Constant.allGraphes)))



