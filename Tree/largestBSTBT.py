#!/usr/bin/python
import sys

# Time Complexity: O(n)

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
 
class Value:
    max_size = 0 #for size of largest BST
    is_bst = False
    #int min = Integer.MAX_VALUE;  // For minimum value in right subtree
    #int max = Integer.MIN_VALUE;  // For maximum value in left subtree

    minVal =  -sys.maxint - 1      # -2147483648 For minimum value in right subtree
    maxVal = sys.maxint      #For maximum value in left subtree
 
# Returns size of the largest BST subtree in a Binary Tree
def largestBST(node):
    val = Value()
    largestBSTUtil(node, val, val, val, val)
    return val.max_size
 
    ''' largestBSTUtil() updates *max_size_ref for the size of the largest BST
     subtree.   Also, if the tree rooted with node is non-empty and a BST,
     then returns size of the tree. Otherwise returns 0.'''
def largestBSTUtil(node, min_ref, max_ref, max_size_ref, is_bst_ref):
    if node is None:
        is_bst_ref.is_bst = True # An empty tree is BST
        return 0    # Size of the BST is 0
 
    minVal = sys.maxint  #2147483647 #Integer.MAX_VALUE;
 
    ''' A flag variable for left subtree property
     i.e., max(root->left) < root->data'''
    left_flag = False
 
    ''' A flag variable for right subtree property
     i.e., min(root->right) > root->data'''
    right_flag = False
 
    ls = rs = 0 # To store sizes of left and right subtrees
 
    ''' Following tasks are done by recursive call for left subtree
     a) Get the maximum value in left subtree (Stored in *max_ref)
     b) Check whether Left Subtree is BST or not (Stored in *is_bst_ref)
     c) Get the size of maximum size BST in left subtree (updates *max_size)'''
    max_ref.maxVal = -sys.maxint - 1 # Integer.MIN_VALUE;
    ls = largestBSTUtil(node.left, min_ref, max_ref, max_size_ref, is_bst_ref)
    if (is_bst_ref.is_bst is True and  node.data > max_ref.maxVal):
        left_flag = True
 
    ''' Before updating *min_ref, store the min value in left subtree. So that we
     have the correct minimum value for this subtree '''
    minVal = min_ref.minVal
 
    ''' The following recursive call does similar (similar to left subtree) 
     task for right subtree '''
    min_ref.minVal = sys.maxint #Integer.MAX_VALUE;
    rs = largestBSTUtil(node.right, min_ref, max_ref, max_size_ref, is_bst_ref)
    if (is_bst_ref.is_bst is True and node.data < min_ref.minVal):
        right_flag = True
 
    # Update min and max values for the parent recursive calls
    if (minVal < min_ref.minVal):
        min_ref.minVal = minVal
    if (node.data < min_ref.minVal):# // For leaf nodes
        min_ref.minVal = node.data
    if (node.data > max_ref.maxVal):
        max_ref.maxVal = node.data
 
    # If both left and right subtrees are BST. And left and right
    # subtree properties hold for this node, then this tree is BST.
    # So return the size of this tree
    if (left_flag and right_flag):
        if (ls + rs + 1 > max_size_ref.max_size):
            max_size_ref.max_size = ls + rs + 1
        return ls + rs + 1;
    else:
        # Since this subtree is not BST, set is_bst flag for parent calls
        is_bst_ref.is_bst = False
        return 0
 
'''    public static void main(String[] args) {
        /* Let us construct the following Tree
                50
             /      \
            10        60
           /  \       /  \
          5   20    55    70
         /     /  \
        45   65    80
'''
 
root = Node(50)
root.left = Node(10);
root.right = Node(60);
root.left.left = Node(5);
root.left.right = Node(20);
root.right.left = Node(55);
root.right.left.left = Node(45);
root.right.right = Node(70);
root.right.right.left = Node(65);
root.right.right.right = Node(80);
 
'''        /* The complete tree is not BST as 45 is in right subtree of 50.
         The following subtree is the largest BST
             60
            /  \
          55    70
          /     /  \
        45     65   80
'''
print "Size of largest BST is ", largestBST(root)
root = Node(60);
root.left = Node(65);
root.right = Node(70);
root.left.left = Node(50);
print " Size of the largest BST is ", largestBST(root)
