class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def traverseAndPrint(head):
    current = head
    while current:
        print(current.data,end='->')
        current = current.next        
      
def deleteSpecificNode(head,nodedelete):
  
    if head == nodedelete:
        return head.next
    
      
    current = head
    
    while current.next and current.next != nodedelete:
        current = current.next
    
    if current.next is None:
        return head    
    
    current.next = current.next.next
    
    return head    




node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before deletion:")
traverseAndPrint(node1)

# Delete node4
node1 = deleteSpecificNode(node1, node4)

print("\nAfter deletion:")
traverseAndPrint(node1)