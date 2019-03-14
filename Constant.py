# 定义常量
N = None
edgeNum = None
allEdges = []
allGraphes = []
allNodes = []
allMatrix = []

def generateAllEdges():
    global N, allEdges, edgeNum
    if N == None:
        return False
    
    for i in range(N):
        allNodes.append(Node('v'+str(i), i))

    edgeNum = 0
    for i in range(N):
        for j in range(i+1,N):
            allEdges.append((allNodes[i], allNodes[j]))
            edgeNum += 1
    print(edgeNum)
    #edgeNum = N*(N-1)//2
    return True

class Node:
    def __init__(self, NodeName, NodeNo):
        self.name = NodeName
        self.No = NodeNo        #初始化为-1，表示没有分配编号

class Graph:
    def __init__(self,nodeNum):
        self.form = {}  #邻接表
        self.degs = {}  #度数表
        self.nodeNum = nodeNum
        global  N, allNodes
        for i in range(nodeNum):
            self.degs[i] = []
            node = allNodes[i]
            self.form[node] = []
            self.degs[0].append(node)

    def addEdge(self, edge):
        global allNodes
        if edge[0] not in allNodes[0:self.nodeNum] or edge[1] not in allNodes[0:self.nodeNum]:
            return

        oldDeg0 = len(self.form[edge[0]])
        oldDeg1 = len(self.form[edge[1]])
        if edge[1] not in self.form[edge[0]]:
            self.form[edge[0]].append(edge[1])
        if edge[0] not in self.form[edge[1]]:
            self.form[edge[1]].append(edge[0])
        newDeg0 = len(self.form[edge[0]])
        newDeg1 = len(self.form[edge[1]])
        if newDeg0 > oldDeg0:
            self.degs[oldDeg0].remove(edge[0])
            self.degs[newDeg0].append(edge[0])
        if newDeg1 > oldDeg1:
            self.degs[oldDeg1].remove(edge[1])
            self.degs[newDeg1].append(edge[1])