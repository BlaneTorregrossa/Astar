# class for nodes to be used in a graph 
class Node(object):
    def __init__(self, position, identity):
        self.position = position
        self.identity = identity
        self.gscore = 0
        self.hscore = 0
        self.fscore = 0
        self.count_gscore(self, node)
        self.count_hscore()
        self.count_fscore()


    def count_gscore(self, neighbor):
        

    #def count_hscore(self):
        
    #def count_fscore(self):
  
