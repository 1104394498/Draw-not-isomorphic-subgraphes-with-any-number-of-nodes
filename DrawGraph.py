import networkx as nx
import matplotlib.pyplot as plt
def drawgraph(matrix):
    G = nx.Graph()
    E = []
    for i in range(len(matrix)):
        G.add_node(i)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1 and (i,j) not in E:
                E.append((i,j))

    G.add_edges_from(E)
    nx.draw(G,node_size=200,node_color='k',with_labels=True,font_color='w')
    plt.show()
    return
