from Constant import *

#生成邻接矩阵
def getMatrix(G):
    matrix = []
    for i in range(N):
        matrix.append([0]*N)

    for n1 in G.form:
        for n2 in G.form[n1]:
            matrix[n1.No][n2.No] = 1

    return matrix

#判断是否有一种对应关系使两个图同构
def hasSameMatrix(matrix1, fullArrays):
    pass


