from Properties import GraphProperties
import networkx as nx

Graph = [ 
    nx.read_edgelist("Data/aves-weaver-social-16.edges", nodetype=int, data=(("Type", str),)),
    nx.read_edgelist("Data/uk.mtx", nodetype=int, data=(("Type", str),)),
    nx.read_edgelist("Data/inf-power.mtx", nodetype=int, data=(("Type", str),)),
    nx.read_edgelist("Data/bio-dmela.mtx", nodetype=int, data=(("Type", str),)),
    nx.read_edgelist("Data/email-EU.edges", nodetype=int, data=(("Type", str),)),
    nx.read_edgelist("Data/geo1k_12k.mtx", nodetype=int, data=(("Type", str),)),
]
for G in Graph:
    GraphProperties(G)

    