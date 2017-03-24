import node
import graph
import Astar
from node import Node       #imports Node class from node.py
from graph import Graph     #imports Graph class from graph.py
from Astar import AStar     #imports Astar class from AStar.py


MainGraph = Graph(5, 5)
star = AStar(MainGraph.nodes[0], MainGraph.nodes[24], MainGraph)

while star.current.position != star.goal.position:
    star.algorithm()
    if star.current.position == star.goal.position:
        star.closedlist.append(star.current)
        star.retraceparents()

print "words"