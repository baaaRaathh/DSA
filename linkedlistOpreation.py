# # linked List Traversal
# class node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
        
# def traversal(head):
#     current = head
#     while current:
#         print(current.data,end='-->')
#         current = current.next
#     print('null')  
    
              
# node1 = node(1)
# node2 = node(9)
# node3 = node(3)
# node4 = node(4)


# node1.next = node2
# node2.next = node3
# node3.next = node4

# traversal(node1)              





# the Lowest value in the linkedlist

class node:
    def __init__(self,data):
        self.data =data
        self.next = None
        
def lowestvalue(head):
    low = head.data
    current = head.next
    while current:
        if current.data < low:
            low = current.data
        current = current.next
    return low       
               
              
node1 = node(7)
node2 = node(9)
node3 = node(3)
node4 = node(4)


node1.next = node2
node2.next = node3
node3.next = node4

print(lowestvalue(node1))                