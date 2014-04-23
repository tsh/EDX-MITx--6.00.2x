from graph import Digraph,Edge,Node

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight, outdoor):
        self.weight = weight
        self.outdoor = outdoor
        super(WeightedEdge,self).__init__(src, dest)

    def getTotalDistance(self):
        return self.weight

    def getOutdoorDistance(self):
        return self.outdoor

    def __str__(self):
        return '{0}->{1} ({2}, {3})'.format(self.src, self.dest, self.weight, self.outdoor)


class WeightedDigraph(Digraph):
    def __init__(self):
        super(WeightedDigraph,self).__init__()

    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '{0}{1}->{2} ()\n'.format(res, k, d)
        return res[:-1]
