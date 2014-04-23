from scipy.stats.distributions import ncx2_gen
from customGraph import WeightedDigraph, Edge,WeightedEdge,Digraph, Node

def load_map(mapFilename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four
        positive integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    g = WeightedDigraph()

    with open(mapFilename) as file:
        for line in file:
            val1, val2, w, ow = line.split()
            n1 = Node(val1)
            n2 = Node(val2)
            edg = WeightedEdge(n1,n2,w,ow)
            try:
                g.addNode(n1)
                g.addNode(n2)
                g.addEdge(edg)
            except ValueError, e:
                print e

    return g

print load_map("mit_map.txt")