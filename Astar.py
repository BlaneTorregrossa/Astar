
from node import Node       #imports Node class from node.py
from graph import Graph     #imports Graph class from graph.py


class AStar(object):
    def __init__(self, start, goal, graph):
        self.start = start
        self.goal = goal
        self.graph = graph
        self.current = start
        self.openlist = []
        self.closedlist = []    
        
        

    #set_start(self):


    #set_goal(self):


    #sort_openlist(self):


    #update():        



    # Collects neighbors from adjacent areas to the given node on the given graph    
    def test_neighbors(node, graph):
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


    #Gets gScore for the neighboring nodes to the current node searching
    def gScore_test(node, neighbor):
        if neighbor.position[0] == node.position[0] or neighbor.position[1] == node.position[1]:
            neighbor.gscore += 10
        else:
            neighbor.gscore += 14

    #Gets the distance between neighbors and the end node 
    def hScore_test(goal, node):
        node.hscore += 10 * ( (abs(goal.position[0] - node.position[0]) )
                             + (abs(goal.position[1] - node.position[1])) )                 

    
    #Gets a total of both gscore and hscore and assigns it to a node
    def fScore_test(node):
        node.fscore = (node.gscore + node.hscore) 
    

    def sort_fscore(nodes):
        for i in range(0, len(nodes)):
            for j in range(0, len(nodes)):
                if nodes[i].fscore < nodes[j].fscore:
                    temp = nodes[i]
                    nodes[i] = nodes[j]
                    nodes[j] = temp



    GRAPH = Graph(5, 5)
    STARTINGNODE = Node([0, 0], 0)
    ENDINGNODE = Node([4, 2], 1)
    CURRENTNODE = STARTINGNODE


    mylist = test_neighbors(STARTINGNODE, GRAPH)
    for node in mylist:    
        gScore_test(STARTINGNODE, node)
        hScore_test(ENDINGNODE, node)
        fScore_test(node)
    
    sort_fscore(mylist)
    CURRENTNODE = mylist[0]
    



    #lists neighbors that appear next to the node
    for node in mylist:
        print str(node.position[0]) + "," + str(node.position[1]) + " Neighbor "




