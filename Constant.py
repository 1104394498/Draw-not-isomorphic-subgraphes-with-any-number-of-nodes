# 定义常量
N = None
edgeNum = None
allEdges = []
allGraphes = []

def generateAllEdges():
    global N, allEdges, edgeNum
    if N == None:
        return False

    for i in range(N):
        for j in range(i,N):
            allEdges.append((i,j))

    edgeNum = N*(N-1)/2
    return True

class Node:
    def __init__(self, NodeName, NodeNo):
        self.name = NodeName
        self.No = NodeNo        #初始化为-1，表示没有分配编号

class Graph:
    def __init__(self):
        self.form = {}  #邻接表
        self.degs = {}  #度数表
        global  N
        for i in range(N):
            self.degs[i] = set()
            node = Node('v'+str(i), i)
            self.form[node] = set()
            self.degs[0].add(node)

    def addEdge(self, edge):
        oldDeg0 = len(self.form[edge[0]])
        oldDeg1 = len(self.form[edge[1]])
        self.form[edge[0]].add(edge[1])
        self.form[edge[1]].add(edge[0])
        newDeg0 = len(self.form[edge[0]])
        newDeg1 = len(self.form[edge[1]])
        if newDeg0 > oldDeg0:
            self.degs[oldDeg0].remove(edge[0])
            self.degs[newDeg0].add(edge[0])
        if newDeg1 > oldDeg1:
            self.degs[oldDeg0].remove(edge[1])
            self.degs[newDeg0].add(edge[1])