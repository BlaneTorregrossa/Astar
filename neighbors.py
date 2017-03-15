


#- Set up nodes and graph
#- Have a getneighbors function working
#- Should work from test_neighbors

# CLASSES STILL NEED TO BE FIXED FOR THIS TO WORK

# class for nodes to be used in a graph 
# Stop putting xpos/ypos in this class
class Node(object):

    def __init__(self, position, identity):
        self.__position = position
        self.__identity = identity
        
    def position(self, ):
        return self.__position 

    def identity(self, ):
        return self.__identity


#columns and rows for a graph/grid
#preferbly 5x5 
class Graph(object):

    def __init__(self, grid):
        nodes
        columns = self.__grid[0]
        rows = self.__grid[0]
        self.__nodes = {}

        

        
def test_neighbors(node, graph):
    neighbors = []
    left = [node.position[0] - 1, node.position[1]]
    bot = [node.position[0], node.position[1] - 1]
    right = [node.position[0] + 1, node.position[1]]
    top = [node.position[0], node.position[1] + 1]

    top_left = [node.position[0] - 1, node.position[1] + 1]
    bot_left = [node.position[0] - 1, node.position[1] - 1]
    top_right = [node.position[0] + 1, node.position[1] + 1]
    bot_right = [node.position[0] + 1, node.position[1] - 1]

    validposition = [left, bot, right, top, top_left, bot_left, top_right, bot_right] 

    for graphnode in graph.nodes:
        for position in validneighbors:
            if graphnode.position = position:
                neighbors.append(graphnode)

    return neighbors