import networkx as nx
from helper import AverageClusteringCoefficient, AverageDegree, DegreeDistribution, PlotGraph, PlotXY, Diameter

def GraphProperties(G):
    nodes = G.nodes
    edges = G.edges

    degreedistribution= DegreeDistribution(G)
    averageDegree=AverageDegree(G)

    density = (2*len(edges)) / (len(nodes) * (len(nodes)-1)) if len(nodes)>1 else 0

    averageclusteringcoefficient=AverageClusteringCoefficient(G)
    diameter=Diameter(G)
    try:
        builtinDiameter=nx.diameter(G)
    except:
        builtinDiameter=-1
    print(f"Graph Directed?: {nx.is_directed(G)}")
    print(f"Number of nodes = {len(nodes)}")
    print(f"Number of edges= {len(edges)}")
    print(f"Average Degree = {averageDegree}")
    print(f"Density from Manual Calculation = {density}")
    print(f"Density from Built-in Function = {nx.density(G)}")
    print(f"Clustering Coeffienent from Manual Calculation : {averageclusteringcoefficient}")
    print(f"Clustering Coeffienent from Built-in Function= {nx.average_clustering(G)}")
    print(f"Diameter from Manual Calculation: {diameter}")
    print(f"Diameter from Built-in Function: {builtinDiameter}")

    PlotGraph(G)
    PlotXY(degreedistribution,"Degree Distribution of the Graph", "Degree(k)", "P(K)")
