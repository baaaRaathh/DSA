class node:
    def __init__(self,data):
        self.data =data
        self.left = None
        self.right = None
        
        
def inordertree(node):
    if node is None:
        return
    inordertree(node.left)
    print(node.data,end=', ')
    inordertree(node.right)
    

root = node('R')       
nodeA = node('A')
nodeB = node('B')
nodeC =node('C')
nodeD = node('D')
nodeE  = node('E')
nodeF = node('F')
nodeG = node('G') 

root.left = nodeA
root.right =nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeE.left = nodeG


inordertree(root)    



