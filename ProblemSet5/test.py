from customGraph import WeightedEdge, WeightedDigraph
from graph import Node

g = WeightedDigraph()
na = Node('a')
nb = Node('b')
nc = Node('c')
g.addNode(na)
g.addNode(nb)
g.addNode(nc)
e1 = WeightedEdge(na, nb, 15, 10)
print e1

#a->b (15, 10)

print e1.getTotalDistance()

#15

print e1.getOutdoorDistance()

#10

e2 = WeightedEdge(na, nc, 14, 6)
e3 = WeightedEdge(nb, nc, 3, 1)
print e2

#a->c (14, 6)

print e3

#b->c (3, 1)

