import node
import graph
import Astar
from node import Node       #imports Node class from node.py
from graph import Graph     #imports Graph class from graph.py
from Astar import AStar     #imports Astar class from AStar.py

MainGraph = Graph(5, 5)
star = AStar(MainGraph.nodes[0], MainGraph.nodes[24], MainGraph)
star.getnode(MainGraph.nodes[18])
star.getnode(MainGraph.nodes[17])
star.getnode(MainGraph.nodes[13])

#will never reach goal if the unwalkable nodes are set to the ones below
    #star.getnode(MainGraph.nodes[18])
    #star.getnode(MainGraph.nodes[17])
    #star.getnode(MainGraph.nodes[16])
    #star.getnode(MainGraph.nodes[13])
    #star.getnode(MainGraph.nodes[8])



while star.current.position != star.goal.position:
    star.algorithm()
    if star.current.position == star.goal.position:
        star.closedlist.append(star.current)
        star.retraceparents()

print "words"