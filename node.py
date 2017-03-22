class Node(object):
    def __init__(self, position, identity):
        self.position = position
        self.identity = identity
        self.parent = None
        self.gscore = 0
        self.hscore = 0
        self.fscore = 0    




    def calculategscore(self, currentnode):
        tenatativeg = 0        
        if currentnode.position[0] == self.position[0] or currentnode.position[1] == self.position[1]:
            tenatativeg = (currentnode.gscore + 10)
        else:
            tenatativeg = (currentnode.gscore + 14)
        if self.parent is None:
            self.gscore = tenatativeg
            self.parent = currentnode
        else:
            if self.gscore > tenatativeg:
                self.parent = currentnode
                self.gscore = tenatativeg
            

    #def calculatehscore(self):
        



    #def calculatefscore(self):





    

