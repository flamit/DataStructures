'''
XOR Linked List - A Memory Efficient Doubly Linked List

An ordinary Doubly Linked List requires space for two address fields to store the addresses of previous and next nodes. A memory efficient version of Doubly Linked List can be created using
only one space for address field with every node. This memory efficient Doubly Linked List is called XOR Linked List or Memory Efficient as the list uses bitwise XOR operation to save space
for one address. In the XOR linked list, instead of storing actual memory addresses, every node stores the XOR of addresses of previous and next nodes.

Ordinary Representation:
 Node A:
 prev = NULL, next = add(B) // previous is NULL and next is address of B

Node B:
 prev = add(A), next = add(C) // previous is address of A and next is address of C

Node C:
 prev = add(B), next = add(D) // previous is address of B and next is address of D

Node D:
 prev = add(C), next = NULL // previous is address of C and next is NULL

XOR List Representation:
 Let us call the address variable in XOR representation npx (XOR of next and previous)

Node A:
 npx = 0 XOR add(B) // bitwise XOR of zero and address of B

Node B:
 npx = add(A) XOR add(C) // bitwise XOR of address of A and address of C

Node C:
 npx = add(B) XOR add(D) // bitwise XOR of address of B and address of D

Node D:
 npx = add(C) XOR 0 // bitwise XOR of address of C and 0

Traversal of XOR Linked List:
 We can traverse the XOR list in both forward and reverse direction. While traversing the list we need to remember the address of the previously accessed node in order to calculate the
 next node's address. For example when we are at node C, we must have address of B. XOR of add(B) and npx of C gives us the add(D). The reason is simple: npx(C) is "add(B) XOR add(D)".
 If we do xor of npx(C) with add(B), we get the result as "add(B) XOR add(D) XOR add(B)" which is "add(D) XOR 0" which is "add(D)". So we have the address of next node.
 Similarly we can traverse the list in backward direction.

This can be implemented by adding
1) A function to insert a new node at the beginning.
2) A function to traverse the list in forward direction.

In the following code, insert() function inserts a new node at the beginning. We need to change the head pointer of Linked List, that is why a double pointer is used.
We store XOR of next and previous nodes with every node and we call it npx, which is the only address member we have with every node. When we insert a new node at the beginning,
npx of new node will always be XOR of NULL and current head. And npx of current head must be changed to XOR of new node and node next to current head.

printList() traverses the list in forward direction. It prints data values from every node. To traverse the list, we need to get pointer to the next node at every point.
We can get the address of next node by keeping track of current node and previous node. If we do XOR of curr->npx and prev, we get the address of next node.
This code is not working. See it https://www.geeksforgeeks.org/?p=12615 again

class Node:
    def __init__(self, data):
        self.data = data
        self.npx = None              # XOR of next and previous node

# returns XORed value of the node addresses */
def XOR (a, b):
    return a^b

# Insert a node at the begining of the XORed linked list and makes the newly inserted node as head
def insert(head_ref, data):
    # Allocate memory for new node
    new_node  = Node(data)
    
    # Since new node is being inserted at the begining, npx of new node will always be XOR of current head and NULL
    new_node.npx = XOR(head_ref, bool(None))

    # If linked list is not empty, then npx of current head node will be XOR of new node and node next to current head
    if (head_ref is not None):
        #*(head_ref)->npx is XOR of NULL and next. So if we do XOR of it with NULL, we get next
        next = XOR(head_ref.npx,  bool(None));
        head_ref.npx = XOR(new_node, next)
    
    head_ref = new_node

# prints contents of doubly linked list in forward direction
def printList (head):
    curr = head
    prev = None
    next = None

    print ("\nFollowing are the nodes of Linked List: \n");

    while (curr is not None):
        print curr.data

        # get address of next node: curr->npx is next^prev, so curr->npx^prev will be next^prev^prev which is next
        next = XOR (prev, curr.npx);

        # update prev and curr for next iteration
        prev = curr
        curr = next
        
#Create following Doubly Linked List head-->40<-->30<-->20<-->10
head = Node(1)
insert(head, 10);
insert(head, 20);
insert(head, 30);
insert(head, 40);
printList (head)
'''
