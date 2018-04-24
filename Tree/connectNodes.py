#!/usr/bin/python
#http://www.geeksforgeeks.org/connect-nodes-at-same-level/

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        self.nextRight = None

'''This function returns the leftmost child of nodes at the same level
       as p. This function is used to getNExt right of p's right child
       If right child of is NULL then this can also be sued for the 
       left child '''
def getNextRight(p):
    temp = p.nextRight
    #Traverse nodes at p's level and find and return the first node's first child
    while temp is not None:
        if temp.left is not None:
            return temp.left
        if temp.right is not None:
            return temp.right
        temp = temp.nextRight
    #If all the nodes at p's level are leaf nodes then return NULL
    return None

# Connect nodes at the same level at constant space
def connect(p):                     #Sets nextRight of all nodes of a tree with root as p
    temp = None
    if p is None:
        return

    p.nextRight = None              #Set nextRight for root
    while (p is not None):          #set nextRight of all levels one by one
        q = p                       #Connect all children nodes of p and children nodes of all other nodes at same level as p
        while (q is not None):
            if (q.left is not None):            #Set the nextRight pointer for p's left child
                if (q.right is not None):       # If q has right child, then right child is nextRight of p and we also need to set nextRight of right child
                    q.left.nextRight = q.right
                else:
                    q.left.nextRight = getNextRight(q)
  
            if (q.right is not None):
                q.right.nextRight = getNextRight(q)
  
            q = q.nextRight                     #Set nextRight for other nodes in pre order fashion
  
            # start from the first node of next level
            if (p.left is not None):
                p = p.left
            elif (p.right is not None):
                p = p.right
            else:
                p = getNextRight(p)
'''
Method 2 (Extend Pre Order Traversal)
 This approach works only for Complete Binary Trees.

 In this method we set nextRight in Pre Order fashion to make sure that the nextRight of parent is set before its children.
 When we are at node p, we set the nextRight of its left and right children. Since the tree is complete tree, nextRight of p's left child (p->left->nextRight) will always be p's right child,
 and nextRight of p's right child (p->right->nextRight) will always be left child of p's nextRight (if p is not the rightmost node at its level).
 If p is the rightmost node, then nextRight of p's right child will be NULL.

Time Complexity: O(n)

Why doesn't method 2 work for trees which are not Complete Binary Trees?
 Let us consider following tree as an example.
 In Method 2, we set the nextRight pointer in pre order fashion. When we are at node 4, we set the nextRight of its children which are 8 and 9 (the nextRight of 4 is already set as node 5).
 nextRight of 8 will simply be set as 9, but nextRight of 9 will be set as NULL which is incorrect. We can't set the correct nextRight, because when we set nextRight of 9,
 we only have nextRight of node 4 and ancestors of node 4, we don't have nextRight of nodes in right subtree of root.
            1
          /    \
        2        3
       / \      /  \
      4   5    6    7
     / \           / \  
    8   9        10   11

def connect(root):
    root.nextRight = None
    connectRecur(root)
    
def connectRecur(node):
    if node is None:
        return
        
    if node.left:
        node.left.nextRight = node.right
        
    if node.right:
        if node.nextRight:
            node.right.nextRight = node.nextRight.left
        else:
            node.right.nextRight = None
    connectRecur(node.left)
    connectRecur(node.right)
'''
# Populate Inorder Successor for all nodes
# Time Complexity: O(n)
# https://www.geeksforgeeks.org/populate-inorder-successor-for-all-nodes/
# Solution (Use Reverse Inorder Traversal)
# Traverse the given tree in reverse inorder traversal and keep track of previously visited node. When a node is being visited, assign previously visited node as next
def populateNext(node):
    nextPtr = None
    populateNextRecur(node, nextPtr)            # The first visited node will be the rightmost node next of the rightmost node will be NULL
    
def populateNextRecur(p, next_ref):             # Set next of all descendents of p by traversing them in reverse Inorder
    if p is not None:                           # First set the next pointer in right subtree
        populateNextRecur(p.right, next_ref)
        p.next = next_ref                       #Set the next as previously visited node in reverse Inorder
        next_ref = p
        populateNextRecur(p.left, next_ref)     #inally, set the next pointer in right subtree
            
root = Node(-15)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(-8)
root.left.right = Node(1)
root.left.left.left = Node(2)
root.left.left.right = Node(6)
root.right.left = Node(3)
root.right.right = Node(9)
root.right.right.right= Node(0)
root.right.right.right.left = Node(4)
root.right.right.right.right = Node(-1)
root.right.right.right.right.left = Node(11)
root.right.right.right.right.right = Node(10)
root.right.right.right.right.right.right = Node(12)
'''
       -15------->None
      /    \
     5----->6---->None
    / \    /  \
   -8->1->3--->9---->None
   /\           \
  2->6 --------->0---->None
                /  \
               4-->-1---->None
                   / \
                 11-->10---->None
                       \
                        12---->None
'''
connect(root)
print root.nextRight
print root.left.nextRight.data
populateNext(root)
