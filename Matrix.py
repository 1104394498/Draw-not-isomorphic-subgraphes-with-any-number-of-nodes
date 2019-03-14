import Constant

#生成邻接矩阵
def getMatrix(G):
    matrix = []
    for i in range(G.nodeNum):
        matrix.append([0]*G.nodeNum)

    for n1 in G.form:
        for n2 in G.form[n1]:
            matrix[n1.No][n2.No] = 1

    return matrix

#判断是否有一种对应关系使两个图同构
def hasSameMatrix(matrix1, fullArrays, g2):
    return signNO(matrix1, fullArrays, g2, 0)


def signNO(matrix1, fullArrays, g2, deg):
    if deg == g2.nodeNum:
        matrix2 = getMatrix(g2)
        return matrix1 == matrix2
    else:
        arrays = fullArrays[deg]
        nodes = g2.degs[deg]
        for i in range(len(arrays)):
            array = arrays[i]
            for j in range(len(array)):
                nodes[j].No = array[j]

            hasSame = signNO(matrix1, fullArrays, g2, deg+1)
            if hasSame:
                return True

        return False
    