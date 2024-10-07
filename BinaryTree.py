#Binary tree is tree data structrue each node has maxmimum os two child nodes


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
        
root =Node('R')
nodeA =Node('A')
nodeB = Node("B")
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')
nodeG = Node('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeD
nodeA.right = nodeC

nodeB.left = nodeE
nodeB.right = nodeF  

nodeF.left = nodeG    
        
        
print(root.right.right.left.data)        