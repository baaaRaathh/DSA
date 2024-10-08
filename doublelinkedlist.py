class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.pre = None
        
node1 = node(1)
node2 = node(23)
node3 = node(3)    
node4 = node(55)

node1.next = node2
node2.pre = node1
node2.next = node3
node3.next = node4
node3.pre = node2
node4.pre = node3


current = node1
while current:
    print(current.data,end='-->')
    current = current.next
print('Null')

current= node4
while current:
    print(current.data,end='-->')
    current = current.pre
print('Null')    
    