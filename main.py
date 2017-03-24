import node
import graph
import Astar
from node import Node       #imports Node class from node.py
from graph import Graph     #imports Graph class from graph.py
from Astar import AStar     #imports Astar class from AStar.py

MainGraph = Graph(10, 10)
star = AStar(MainGraph.nodes[0], MainGraph.nodes[99], MainGraph)

#will never reach goal if the unwalkable nodes are set to the ones below
star.getnode(65, MainGraph).walkable = False
star.getnode(64, MainGraph).walkable = False
star.getnode(63, MainGraph).walkable = False
star.getnode(55, MainGraph).walkable = False
star.getnode(45, MainGraph).walkable = False
star.getnode(35, MainGraph).walkable = False



while star.current.position != star.goal.position:
    star.algorithm()
    if star.current.position == star.goal.position:
        star.closedlist.append(star.current)
        star.retraceparents()

print "words"