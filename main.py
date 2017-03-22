import node
import graph
import Astar
from node import Node       #imports Node class from node.py
from graph import Graph     #imports Graph class from graph.py
from Astar import AStar

MainGraph = Graph(5, 5)
StartNode = Node([4, 2], 0)
EndNode = Node([0, 4], 1)
CurrentNode = StartNode



print "words"