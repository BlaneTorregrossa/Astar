#- Set up nodes and graph
#- Have a getneighbors function working
#- Should work from test_neighbors


# CLASSES STILL NEED TO BE FIXED FOR THIS TO WORK

# class for nodes to be used in a graph 
# Stop putting xpos/ypos in this class
class Node(object):
    def __init__(self, position, identity):
        self.position = position
        self.identity = identity
        
    def position(self):
        return self.position 

    def identity(self):
        return self.identity

#columns and rows for a graph/grid
#preferbly 5x5 
class Graph(object):
    def __init__(self, row, col):
        self.columns = col
        self.rows = row
        self.nodes = []
        self.gengraph()
        
    def gengraph(self):
        counter = 0
        for xpos in range(0, self.rows):
            for ypos in range(0, self.columns):
                newnode = Node([xpos, ypos], counter)
                counter = counter + 1
                self.nodes.append(newnode)
                
                    
    
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


def print_info(graph):
    for node in graph.nodes :
        print str(node.position[0])  + "," + str(node.position[1])


def get_gScore(node, neighbors):
    gScore = 0
    
        
        



GRAPH = Graph(5, 5)
STARTINGNODE = Node([0, 0], 0)

print_info(GRAPH)
mylist = test_neighbors(STARTINGNODE, GRAPH)
get_gScore(STARTINGNODE, mylist)

for node in mylist:
    print str(node.position[0]) + "," + str(node.position[1]) + " Neighbor "




