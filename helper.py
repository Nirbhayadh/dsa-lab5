import matplotlib.pyplot as plt
import math 
import networkx as nx

def DegreeDistribution(G):
    nodes=G.nodes()
    maxDegree =max(y for (x,y) in G.degree())
    degreeDistribution= [0 for _ in range(0,maxDegree+1)]
    for (x,y) in G.degree():
        degreeDistribution[y]+=1
    for i in range(0,len(degreeDistribution)):
        degreeDistribution[i]=round(degreeDistribution[i] / len(nodes),2)

    return degreeDistribution

def PlotXY(data, title, xlabel, ylabel):
    plt.plot(data, marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def AverageDegree(G):
    sum=0
    nodes=G.nodes
    for node in G.degree():
        sum=sum+node[1]
    avg_degree=math.floor(sum/len(nodes))
    return avg_degree


def _nodes_connected(G, u, v):
     return u in G.neighbors(v)
def AverageClusteringCoefficient(G):
    nodes=G.nodes()
    s=0
    for node in G.degree():
        k= node[1]
        e=0
        
        # for i in G.out_degree(node[0]):
        #     neighbors.append(i)
        # neighbors=list(G.neighbors(node[0]))
        # print(G.out_degree(node[0]))
        neighbors=list(G.neighbors(node[0]))          
         
        # for i in range(0,len(neighbors)-1):
        #     for j in range(i+1,len(neighbors)):
        #         if(_nodes_connected(G,neighbors[i],neighbors[j])):
        #             e=e+1
        for i in neighbors:
            for j in neighbors:
                if(_nodes_connected(G,i,j)):
                    e=e+1
        e=e/2
        c=(2*e)/(k*(k-1)) if k>1 else 0
        s=s+c
    avg_clustering_coefficient =s/len(nodes)
    return avg_clustering_coefficient



# def AverageClusteringCoefficient(G):
#     nodes = G.nodes
#     total_cluster = 0
#     for i in nodes:
#         neighbour = list(nx.neighbors(G, i))
#         connection = 0
#         for j in neighbour:
#             for k in neighbour:
#                 # if _nodes_connected(G,j,k):
#                 if nx.is_path(G, [j,k]):
#                     connection += 1

#         # connection should be fivided by 2 here because
#         # the loop counts 1,2 as a connection and also counts
#         # 2,1 as another connection since it is an undirected graph.

#         if len(neighbour) > 1:
#             total_cluster += (2*(connection/2))/ (len(neighbour) * (len(neighbour)-1))
    
#     c = total_cluster / len(nodes)
#     return c

def Diameter(G):
    if(nx.is_connected(G) == False):
        return -1
    nodes = G.nodes
    nodes=list(nodes)    
    s=0
    for i in range(0,len(nodes)):
        for j in range(0,len(nodes)):
            if i==j:
                continue
            distance=nx.shortest_path_length(G, source=nodes[i], target=nodes[j])
            if distance>s:
                s=distance
    return s

def PlotGraph(G):
    nx.draw_random(G, with_labels=False)
    plt.show()
