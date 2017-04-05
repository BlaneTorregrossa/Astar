import node
import graph
import Astar
from node import Node       #imports Node class from node.py
from graph import Graph     #imports Graph class from graph.py
import pathfinding
from pathfinding import testfunc
from pathfinding import getneighbors
#to test your astar it must follow these conventions
#preconditions: node objects must have g f h and parent variables
#node objects must access position elements through node[0] "posx" or node[1] "posy"
#so if you have a node.positionx it will be node[0]
#so if you have a node.positiony it will be node[1]
#to calculate neighbors replace your fetch for adjacents/neighbors with
#getneighbors(current, graph)
#this returns a list of nodes
#parameters: start, goal, graph
#postconditions: function will return a list
def main():
    failcount = 0
    passcount = 0
    MainGraph = pathfinding.GRAPH
    maxstar = Astar.astar(, , MainGraph)
    for _ in range(100):
        res = testfunc(maxstar)
        if res:
            passcount += 1
        else:
            failcount += 1
    print str.format('fails {0}, passes {1}', failcount, passcount)
    
if __name__ == '__main__':
    main()



# MainGraph = Graph(10, 10)
# star = AStar(MainGraph.nodes[0], MainGraph.nodes[99], MainGraph)

# star.getnode(65, MainGraph).walkable = False
# star.getnode(64, MainGraph).walkable = False
# star.getnode(63, MainGraph).walkable = False
# star.getnode(55, MainGraph).walkable = False
# star.getnode(45, MainGraph).walkable = False
# star.getnode(35, MainGraph).walkable = False




# while star.current.position != star.goal.position:
#     star.algorithm()
#     if star.current.position == star.goal.position:
#         star.closedlist.append(star.current)
#         star.retraceparents()




# print "words"

# if __name__ == '__main__':
#     import main as Main
#     Main.main()