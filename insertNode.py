class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
     current = head
     while current:
         
        print(current.data,end='-->')
        current = current.next
def insertNodeAtPosition(head,newnode,position):
    
    if position == 1:
        newnode.next = head
        return newnode
    current = head
    for _ in range(position -2):
        if  current is None:
            break
        current =  current.next
        
    newnode.next = current.next
    current.next = newnode
    return head                  
        
        
        

node1 = Node(7)
node2 = Node(3)
node3 = Node(2)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

print("Original list:")
traverseAndPrint(node1)

# Insert a new node with value 97 at position 2
newNode = Node(97)
node1 = insertNodeAtPosition(node1, newNode, 2)

print("\nAfter insertion:")
traverseAndPrint(node1)        