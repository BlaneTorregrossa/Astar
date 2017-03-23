import node
import graph
import Astar
from node import Node       #imports Node class from node.py
from graph import Graph     #imports Graph class from graph.py
from Astar import AStar


MainGraph = Graph(5, 5)
star = AStar(MainGraph.nodes[0], MainGraph.nodes[24], MainGraph)

star.algorithm()

print "words"