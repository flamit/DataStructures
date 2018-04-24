# A node of the doublly linked list
import gc

class Node:     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None
 
class DoublyLinkedList:
     # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None
  
    # reverse a Doubly Linked List; Time Complexity: O(n)
    def reverse(self):
        temp = None
        current = self.head
         
        # Swap next and prev for all nodes of 
        # doubly linked list
        while current is not None:
            temp = current.prev 
            current.prev = current.next
            current.next = temp
            current = current.prev
 
        # Before changing head, check for the cases like 
        # empty list and list with only one node
        if temp is not None:
            self.head = temp.prev
         
    # Given a reference to the head of a list and an
    # integer,inserts a new node on the front of list
    def push(self, new_data):
  
        # 1. Allocates node
        # 2. Put the data in it
        new_node = Node(new_data)
  
        # 3. Make next of new node as head and
        # previous as None (already None)
        new_node.next = self.head
  
        # 4. change prev of head node to new_node
        if self.head is not None:
            self.head.prev = new_node
  
        # 5. move the head to point to the new node
        self.head = new_node

    # Function to delete a node in a Doubly Linked List; Time Complexity: O(1) Time Complexity: O(1)
    def deleteNode(self, node):
        if self.head is None or node is None:
            return
        
        if self.head == node:                                       # If node to be deleted is head node
            self.head = node.next   
        if node.next is not None:                                   # Change next only if node to be deleted is NOT the last node
            node.next.prev = node.prev
        if node.prev is not None:                                   # Change prev only if node to be deleted is NOT the first node
            node.prev.next = node.next
            
        gc.collect()                                              # Finally, free the memory occupied by node Call python garbage collector
        
    def printList(self, node):
        while(node is not None):
            print node.data,
            node = node.next
 
# Driver program to test the above functions
dll = DoublyLinkedList()
dll.push(2);
dll.push(4);
dll.push(8);
dll.push(10);
 
print "\nOriginal Linked List"
dll.printList(dll.head)
 
# Reverse doubly linked list
dll.reverse()
 
print "\n Reversed Linked List"
dll.printList(dll.head)

# delete nodes from doubly linked list
dll.deleteNode(dll.head)
dll.deleteNode(dll.head.next)
dll.deleteNode(dll.head.next)
# Modified linked list will be NULL<-8->NULL
print "\n Modified Linked List",
dll.printList(dll.head)
