
from node import Node       #imports Node class from node.py
from graph import Graph     #imports Graph class from graph.py

class AStar(object):
    def __init__(self, start, goal, graph):
        self.start = start
        self.goal = goal
        self.graph = graph
        self.current = start
        self.openlist = [self.current]
        self.closedlist = [] 
        self.parentlist = self.closedlist

    # Collects neighbors from adjacent areas to the given node on the given graph
    def test_neighbors(self, node, graph):
        neighbors = []
        left = [node.position[0] - 1, node.position[1]]
        bottom = [node.position[0], node.position[1] - 1]
        right = [node.position[0] + 1, node.position[1]]
        top = [node.position[0], node.position[1] + 1]

        top_left = [node.position[0] - 1, node.position[1] + 1]
        bottom_left = [node.position[0] - 1, node.position[1] - 1]
        top_right = [node.position[0] + 1, node.position[1] + 1]
        bottom_right = [node.position[0] + 1, node.position[1] - 1]

        validposition = [left, bottom, right, top, top_left, bottom_left, top_right, bottom_right]

        for graphnode in graph.nodes:
            for position in validposition:
                if graphnode.position[0] == position[0] and graphnode.position[1] == position[1]:
                    neighbors.append(graphnode)

        return neighbors

    def algorithm(self):
        self.openlist.remove(self.current)
        self.closedlist.append(self.current)
        for node in self.test_neighbors(self.current, self.graph):            
            if node not in self.openlist:
                self.openlist.append(node)
            node.calculategscore(self.current)
            node.calculatehscore(self.goal)
            node.calculatefscore()
        self.sortopen()
        self.sortparents()
        self.current = self.openlist[0]
    
    def sortopen(self):
        for node in range(0, len(self.openlist)):
            for nodecmp in range(0, len(self.openlist)):
                if self.openlist[node].fscore < self.openlist[nodecmp].fscore:
                    temp = self.openlist[nodecmp]
                    self.openlist[nodecmp] = self.openlist[node]
                    self.openlist[node] = temp
                    
    def sortparents(self):
        for node in range(0, len(self.parentlist)):
            for nodecmp in range(0, len(self.parentlist)):
                 if self.parentlist[node].fscore < self.parentlist[nodecmp].fscore:
                    temp = self.parentlist[nodecmp]
                    self.parentlist[nodecmp] = self.parentlist[node]
                    self.parentlist[node] = temp
                    