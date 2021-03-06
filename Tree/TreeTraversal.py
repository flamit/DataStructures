#!/usr/bin/python
'''
BFS/Breadth First Traversal (Or Level Order Traversal) 
DFS/Depth First Traversals:
	Inorder Traversal (Left-Root-Right)
	Preorder Traversal (Root-Left-Right)
	Postorder Traversal (Left-Right-Root)
'''
INT_MAX = 4294967296
INT_MIN = -4294967296

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
 
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data),
        printInorder(root.right)
 
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data),
 
def printPreorder(root):
    if root:
        print(root.data),
        printPreorder(root.left)
        printPreorder(root.right)
 
#		 1
#
# 	 2		 3
#
# 4		 5
#        7               11
# Level order traversal of the above tree is 1 2 3 4 5 7 11

# Time complexity is O(n); but if you want to print level the follow the next solution
def printLevelOrder(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while(len(queue) > 0):
        node = queue.pop(0)
        print node.data,
        
        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

def printLevelOrderSpiral(root):
    if root is None:
        return

    queue1 = []
    queue2 = []
    queue1.append(root)
    n = 0

    while(len(queue1) > 0 or len(queue2) > 0):
        while len(queue1) > 0:
            node = queue1.pop(n)
            print node.data,
            if node.right is not None:
                queue2.append(node.right)
            if node.left is not None:
                queue2.append(node.left)

        n = -1
        while len(queue2) > 0:
            node = queue2.pop(n)
            print node.data,
            if node.left is not None:
                queue1.append(node.left)
            if node.right is not None:
                queue1.append(node.right)
				
# Time complexity is O(n^2). So prefer the queue one as above
def printLevelOrderWithLevels(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)
 
 
# Print nodes at a given level
def printGivenLevel(root , level):
    if root is None:
        return
    if level == 1:
        print "%d" %(root.data),
    elif level > 1 :
        printGivenLevel(root.left , level-1)
        printGivenLevel(root.right , level-1)

'''		
Time complexity is O(n^2). So refer printLevelOrderSpiral() which has a complexity of O(n)

		 1
		/ \
	   /   \
	  2     3
	 /\		/\
	4  5	6 7
Level order: 1, 2, 3, 4, 5, 6, 7
Spiral order: 1, 2, 3, 7, 6, 5, 4 
'''
def printSpiral(root):
    h = height(root)
    ltr = False
    for i in range(1, h+1):
        printGivenLevelSpiral(root, i, ltr)
        ltr = not ltr

def printGivenLevelSpiral(root, level, ltr):
    if root is None:
        return
    if level == 1:
        print "%d" %(root.data),
    elif level > 1:
        if ltr:
            printGivenLevelSpiral(root.left , level-1, ltr)
            printGivenLevelSpiral(root.right , level-1, ltr)
        else:
            printGivenLevelSpiral(root.right , level-1, ltr)
            printGivenLevelSpiral(root.left , level-1, ltr)
			
def size(root):
  if root is None:
    return 0
  else:
    return size(root.left) + size(root.right) + 1

def height(root):
    if root is None:
        return 0
    lHeight = height(root.left)
    rHeight = height(root.right)

    return max(lHeight, rHeight)+1

# Function to get the diamtere of a binary tree
# Time Complexity: O(n^2)
'''
The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two leaves in the tree. The diagram below shows two trees each with diameter nine,
the leaves that form the ends of a longest path are shaded (note that there is more than one path in each tree of length nine, but no path longer than nine nodes). 
The diameter of a tree T is the largest of the following quantities:

* the diameter of T's left subtree
 * the diameter of T's right subtree
 * the longest path between leaves that goes through the root of T (this can be computed from the heights of the subtrees of T) 

'''
def diameter(root):
    if root is None:
        return 0;
		
    lheight = height(root.left)
    rheight = height(root.right)
 
    # Get the diameter of left and right sub-trees
    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)
 
    # Return max of the following tree:
    # 1) Diameter of left subtree
    # 2) Diameter of right subtree
    # 3) Height of left subtree + height of right subtree +1 
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))

# Function to get the maximum width of binary tree using Level Order Traversal
'''
 This method mainly involves two functions. One is to count nodes at a given level (getWidth), and other is to get the maximum width of the tree(getMaxWidth).
 getMaxWidth() makes use of getWidth() to get the width of all levels starting from root.
Let us consider the below example tree.
         1
        /  \
       2    3
     /  \     \
    4    5     8
              /  \
             6    7


For the above tree,
 width of level 1 is 1,
 width of level 2 is 2,
 width of level 3 is 3
 width of level 4 is 2.

Time Complexity: O(n^2) in the worst case.

Note: Time complexity for this is We can use Queue based level order traversal to optimize the time complexity of this method.
The Queue based level order traversal will take O(n) time in worst case.
Refer: http://www.geeksforgeeks.org/maximum-width-of-a-binary-tree/
'''
def getMaxWidth(root):
    maxWidth = 0
    h = height(root)
    # Get width of each level and compare the width with maximum width so far
    for i in range(1,h+1):
        width = getWidth(root, i)
        if (width > maxWidth):
            maxWidth = width
    return maxWidth

# Get width of a given level
def getWidth(root,level):
    if root is None:
        return 0
    if level == 1:
        return 1
    elif level > 1:
        return (getWidth(root.left,level-1) + getWidth(root.right,level-1))


#                1
#
#        2               3
#
# 4              5
#        7               11
# Level order traversal of the above tree is 1 2 3 4 5 7 11
# Mirror Tree
#                1
#
#        3               2
#
#                5		4
#        11              7
# Level order traversal of the above tree is 1 3 2 5 4 11 7
#
# Given a binary tree, return all root-to-leaf paths.
# For example, given the following binary tree:
#
#   1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
# ["1->2->5", "1->3"]
# Time:  O(n * h)
# Space: O(h)
# Same algorithm can be used to find "Find the maximum sum leaf to root path in a Binary Tree(https://www.geeksforgeeks.org/find-the-maximum-sum-path-in-a-binary-tree/)"
def binaryTreePaths(root):
    result, path = [], []
    binaryTreePathsRecu(root, path, result)
    return result

def binaryTreePathsRecu(node, path, result):
    if node is None:
        return

    if node.left is node.right is None:
        ans = ""
        for n in path:
            ans += str(n.data) + "->"
        result.append(ans + str(node.data))

    if node.left:
        path.append(node)
        binaryTreePathsRecu(node.left, path, result)
        path.pop()

    if node.right:
        path.append(node)
        binaryTreePathsRecu(node.right, path, result)
        path.pop()
'''
Input : 
                 1
               /   \
              2     3
             / \     \
            4   5     6             
Output : 1 2 4

Input :
        1
      /   \
    2       3
      \   
        4  
          \
            5
             \
               6
Output :1 2 4 5 6
# Recursive function print left view of a binary tree(geeksforgeek's solution, https://www.geeksforgeeks.org/print-left-view-binary-tree/)

The left view contains all nodes that are first nodes in their levels. A simple solution is to do level order traversal and print the first node in every level.
The problem can also be solved using simple recursive traversal. We can keep track of level of a node by passing a parameter to all recursive calls.
The idea is to keep track of maximum level also. Whenever we see a node whose level is more than maximum level so far,
we print the node because this is the first node in its level (Note that we traverse the left subtree before right subtree). Following is the implementation

def leftView(root):
    max_level = [0]
    leftViewUtil(root, 1, max_level)
    
def leftViewUtil(root, level, max_level):
     
    # Base Case
    if root is None:
        return
 
    # If this is the first node of its level
    if (max_level[0] < level):
        print "%d\t" %(root.data),
        max_level[0] = level
 
    # Recur for left and right subtree
    leftViewUtil(root.left, level+1, max_level)
    leftViewUtil(root.right, level+1, max_level)
'''
# my solution :) for printing left view. Note the difference with "def printLevelOrder". There it's two different "ifs" where as here it is "if...elif..."
def leftView(root):
    if root is None:
        return

    queue = []
    queue.append(root)
    while len(queue)>0:
        node=queue.pop(0)
        print node.data, 

        if node.left:
            queue.append(node.left)
        elif node.right:
            queue.append(node.right)
            
# A simple function to print leaf nodes of a Binary Tree
def printLeaves(root):
    if root:
        printLeaves(root.left)
         
        # Print it if it is a leaf node
        if root.left is None and root.right is None:
            print root.data,
 
        printLeaves(root.right)
		
# Function to get the count of leaf nodes in binary tree
def getLeafCount(node):
    if node is None:
        return 0
    if(node.left is None and node.right is None):
        return 1
    else:
        return getLeafCount(node.left) + getLeafCount(node.right)

# A function to print all left boundary nodes, except a 
# leaf node. Print the nodes in TOP DOWN manner
def printBoundaryLeft(root):
    if(root):
        if (root.left):
            # to ensure top down order, print the node
            # before calling itself for left subtree
            print root.data,
            printBoundaryLeft(root.left)
        elif(root.right):
            print root.data,
            printBoundaryLeft(root.right)
         
        # do nothing if it is a leaf node, this way we
        # avoid duplicates in output
 
 
# A function to print all right boundary nodes, except
# a leaf node. Print the nodes in BOTTOM UP manner
def printBoundaryRight(root):
     
    if(root):
        if (root.right):
            # to ensure bottom up order, first call for
            # right subtree, then print this node
            printBoundaryRight(root.right)
            print root.data,
        elif(root.left):
            printBoundaryRight(root.left)
            print root.data,
 
        # do nothing if it is a leaf node, this way we 
        # avoid duplicates in output
 
 
# A function to do boundary traversal of a given binary tree
def printBoundary(root):
    if (root):
        print root.data, 
         
        # Print the left boundary in top-down manner
        printBoundaryLeft(root.left)
 
        # Print all leaf nodes
        printLeaves(root.left)
        printLeaves(root.right)
 
        # Print the right boundary in bottom-up manner
        printBoundaryRight(root.right)

# Preorder traversal without 
# recursion and without stack
def MorrisTraversal(root):
    curr = root
 
    while curr:
        # If left child is null, print the current node data. And, update the current pointer to right child.
        if curr.left is None:
            print curr.data,
            curr = curr.right
 
        else:
            # Find the inorder predecessor
            prev = curr.left
 
            while prev.right is not None and prev.right is not curr:
                prev = prev.right
 
            # If the right child of inorder predecessor already points to the current node, update the current with it's right child
            if prev.right is curr:
                prev.right = None
                curr = curr.right
                 
            # else If right child doesn't point to the current node, then print this node's data and update the right child pointer with the current node and update the current with it's left child
            else:
                print curr.data,
                prev.right = curr 
                curr = curr.left

def mirrorTree(root):
  if root is None:
    return 0
  mirrorTree(root.left)
  mirrorTree(root.right)
  root.left, root.right = root.right, root.left
  return root

# If target is present in tree, then prints the ancestors and returns true, otherwise returns false
'''
For example, if the given tree is following Binary Tree and key is 7, then your function should print 4, 2 and 1.

              1
            /   \
          2      3
        /  \
      4     5
     /
    7
Time Complexity: O(n) where n is the number of nodes in the given Binary Tree.
'''
def printAncestors(root, target):		# Same algorithmas "findPath". In fact findPath is more correct handling more cases. Check that instead of this
    if root == None:                            # Base case
        return False
     
    if root.data == target:
        return True
    
    if (printAncestors(root.left, target) or    # If target is present in either left or right subtree of this node, then print this node
        printAncestors(root.right, target)):
        print root.data,
        return True
    
    return False

# Finds the path from root node to given root of the tree. Stores the path in a list path[], returns true if path exists otherwise false
# Same as above; just pass a list to store the variables
def findPath( root, path, k):
    if root is None:
        return False
    
    path.append(root.data)                                              # Store this node is path vector. The node will be removed if not in path from root to k
    
    if root.data == k:                                                  # See if the k is same as root's key
        return True
    
    if (findPath(root.left, path, k) or                                 # Check if k is found in left or right sub-tree
        findPath(root.right, path, k)):
        return True
    
    path.pop()                                                          # If not present in subtree rooted with root, remove root from path and return False
    return False

# Function to find LCA(Lowest Common Ancestor) of n1 and n2. The function assumes
# that both n1 and n2 are present in BST
def lca_of_BST(root, n1, n2):
     
    # Base Case
    if root is None:
        return None
 
    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(root.data > n1 and root.data > n2):
        return lca_of_BST(root.left, n1, n2)
 
    # If both n1 and n2 are greater than root, then LCA
    # lies in right 
    if(root.data < n1 and root.data < n2):
        return lca_of_BST(root.right, n1, n2)
 
    return root

'''
Lowest Common Ancestor in a Binary Tree(not a binary search tree)
We have discussed an efficient solution to find LCA in Binary Search Tree. In Binary Search Tree, using BST properties, we can find LCA in O(h) time where h is height of tree. 
Such an implementation is not possible in Binary Tree as keys Binary Tree nodes don't follow any order. Following are different approaches to find LCA in Binary Tree.

Method 1 (By Storing root to n1 and root to n2 paths):
 Following is simple O(n) algorithm to find LCA of n1 and n2.
1) Find path from root to n1 and store it in a vector or array.
2) Find path from root to n2 and store it in another vector or array.
3) Traverse both paths till the values in arrays are same. Return the common element just before the mismatch.
'''
# Returns LCA if node n1 , n2 are present in the given binary tre otherwise return -1
def findLCA(root, n1, n2):

    # To store paths to n1 and n2 fromthe root
    path1 = []
    path2 = []

    # Find paths from root to n1 and root to n2.
    # If either n1 or n2 is not present , return -1
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1

    # Compare the paths to get the first different value
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]

'''int findLevel(Node *root, int k, int level)
{
    if(root == NULL) return -1;
    if(root->key == k) return level;
 
    int left = findLevel(root->left, k, level+1);
    if (left == -1)
       return findLevel(root->right, k, level+1);
    return left;
}
 
int findDistance(Node* root, int a, int b)
{
    // Your code here
    Node* lca = LCA(root, a , b);
 
    int d1 = findLevel(lca, a, 0);
    int d2 = findLevel(lca, b, 0);
 
    return d1 + d2;
}
# Returns level of key k if it is present in
# tree, otherwise returns -1
def findLevel(root, k, level):
    if root is None:
        return 1
    if root.data == k:
        return level
 
    left = findLevel(root.left, k, level+1)
    if left == 1:
       return findLevel(root.right, k, level+1)
    return left
 
def findDistance(root, a, b):
    LCA = lca(root, a , b)
    print "lca = %d" %(LCA)
 
    d1 = findLevel(LCA, a, 0)
    d2 = findLevel(LCA, b, 0)
 
    return d1 + d2

'''
"""
 Given a tree and a sum, return true if there is a path from the root down to a leaf, such that adding up all the values along the path equals the given sum.
 Strategy: subtract the node value from the sum when recurring down, and check to see if the sum is 0 when you run out of tree.
"""
# My solution. s is the path sum here.
def hasPathSum(node, s):
    if node is None:
        return (s == 0)
    else:
        subSum = s - node.data
        if(subSum == 0):
            return True
        else:
            if hasPathSum(node.left, subSum):
                return True
            if hasPathSum(node.right, subSum):
                return True
            
        return False

'''
def hasPathSum(node, s):
     
    # Return true if we run out of tree and s = 0 
    if node is None:
        return (s == 0)
 
    else:
        ans = 0
         
        # Otherwise check both subtrees
        subSum = s - node.data
        
        # If we reach a leaf node and sum becomes 0, then 
        # return True 
        if(subSum == 0 and node.left == None and node.right == None):
            return True
 
        if node.left is not None:
            ans = ans or hasPathSum(node.left, subSum)
        if node.right is not None:
            ans = ans or hasPathSum(node.right, subSum)
 
        return ans
'''
# Find the maximum path sum between two leaves of a binary tree
'''The main function which returns sum of the maximum sum path between two leaves. This function mainly uses maxPathSumUtil()
The maximum sum path may or may not go through root. For example in the following binary tree, the maximum sum is 27(3+6+9+0-1+10). Expected time complexity is O(n).

A simple solution is to traverse the tree and do following for every traversed node X.
 1) Find maximum sum from leaf to root in left subtree of X (we can use this post for this and next steps)
 2) Find maximum sum from leaf to root in right subtree of X.
 3) Add the above two calculated values and X->data and compare the sum with the maximum value obtained so far and update the maximum value.
 4) Return the maximum value.

The time complexity of above solution is O(n2)

We can find the maximum sum using single traversal of binary tree. The idea is to maintain two values in recursive calls
 1) Maximum root to leaf path sum for the subtree rooted under current node.
 2) The maximum path sum between leaves (desired output).

For every visited node X, we find the maximum root to leaf sum in left and right subtrees of X. We add the two values with X->data, and compare the sum with maximum path sum found so far.
'''
def maxPathSum(root):
        INT_MIN = -2**32
        res = [INT_MIN]
        maxPathSumUtil(root, res)
        return res[0]

# Utility function to find maximum sum between any
# two leaves. This function calculates two values:
# 1) Maximum path sum between two leaves which are stored in res
# 2) The maximum root to leaf path sum which is returned If one side of root is empty, then it returns INT_MIN
def maxPathSumUtil(root, res):

    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.data

    # Find maximumsum in left and right subtree. Also
    # find maximum root to leaf sums in left and right
    # subtrees ans store them in ls and rs
    ls = maxPathSumUtil(root.left, res)
    rs = maxPathSumUtil(root.right, res)
    print res
    # If both left and right children exist
    if root.left is not None and root.right is not None:

        # update result if needed
        res[0] = max(res[0], ls + rs + root.data)

        # Return maximum possible value for root being
        # on one side
        return max(ls, rs) + root.data

    # If any of the two children is empty, return
    # root sum for root being on one side
    if root.left is None:
        return rs + root.data
    else:
        return ls + root.data

# Given a binary tree and a number k, print all nodes that are k distant from a leaf
# Time Complexity is O(n)
def printKDistantfromLeaf(root, k):
    path = [None] * 1000                                                                                                        # path[] --> Store ancestors of a node
    visited = [None] * 1000                                                                                                     # visited[] --> Stores true if a node is printed as output
    kDistantFromLeafUtil(root, path, visited, 0, k)		
		
def kDistantFromLeafUtil(node, path, visited, pathLen, k):
    if node is None:
        return
    
    path[pathLen] = node.data
    visited[pathLen] = False
    pathLen += 1
  
    if (node.left is None and node.right is None and pathLen - k - 1 >= 0 and visited[pathLen - k - 1] == False):               # it's a leaf, so print the ancestor at distance k only if the ancestor is not already printed
        print str(path[pathLen - k - 1]) + " "
        visited[pathLen - k - 1] = True
        return
    
    kDistantFromLeafUtil(node.left, path, visited, pathLen, k)                                                                  #   If not leaf node, recur for left and right subtrees
    kDistantFromLeafUtil(node.right, path, visited, pathLen, k)

# Print nodes at k distance from root
# Recursive function to print all the nodes at distance k in the tree(or subtree) rooted with given root. See
def printkDistanceNodeDown(root, k):
    if root is None or k<0:                                                                                                     # Base Case
        return
    
    if k == 0:                                                                                                                  # If we reach a k distant node, print it
        print root.data,
    else:
        printkDistanceNodeDown(root.left, k-1)
        printkDistanceNodeDown(root.right, k-1)

# Given a binary tree, a target node in the binary tree, and an integer value k, print all the nodes that are at distance k from the given target node. No parent pointers are available.
def printkDistanceNode(root, target, k):    
    if root is None:                                                                                                            # Base Case 1 : IF tree is empty return -1
        return -1
    
    if root == target:                                                                                                          # If target is same as root. Use the downward function to print 
        printkDistanceNodeDown(root, k)                                                                                         # all nodes at distance k in subtree rooted with target or root
        return 0
    
    dl = printkDistanceNode(root.left, target, k)
    if dl != -1:                                                                                                                # Check if target node was found in left subtree
        if dl+1 == k :                                                                                                          # If root is at distance k from target, print root
            print root.data                                                                                                     # Note: dl is distance of root's left child from target
        else:                                                                                                                   # Else go to right subtreee and print all k-dl-2 distant nodes
            printkDistanceNodeDown(root.right, k-dl-2)                                                                          # Note: that the right child is 2 edges away from left chlid
        return dl+1                                                                                                             # Add 1 to the distance and return value for for parent calls
    
    dr = printkDistanceNode(root.right, target, k)                                                                              # MIRROR OF ABOVE CODE FOR RIGHT SUBTREE Note that we reach here only
    if dr != -1:                                                                                                                # when node was not found in left subtree
        if (dr+1 == k):
            print root.data
        else:
            printkDistanceNodeDown(root.left, k-dr-2)
        return dr+1
    return -1                                                                                                                   # If target was neither present in left nor in right subtree

# A utility function to find min and max distances with respect to root
# Minimum distance => left of left of left of ...   (-ve sign)
# Maximum distance => right of right of right of ... (+ve sign)
def findMinMax(node, minimum, maximum, hd):
    # Base Case
    if node is None:
        return

    # Update min and max
    if hd < minimum[0] :
        minimum[0] = hd
    elif hd > maximum[0]:
        maximum[0] = hd

    # Recur for left and right subtrees
    findMinMax(node.left, minimum, maximum, hd-1)
    findMinMax(node.right, minimum, maximum, hd+1)

# A utility function to print all nodes on a given line_no
# hd is horizontal distance of current node with respect to root
def printVerticalLine(node, line_no, hd):

    # Base Case
    if node is None:
        return

    # If this node is on the given line number
    if hd == line_no:
        print node.data,

    # Recur for left and right subtrees
    printVerticalLine(node.left, line_no, hd-1)
    printVerticalLine(node.right, line_no, hd+1)

'''Print a Binary Tree in Vertical Order | Set 1
           1
        /    \
       2      3
      / \    / \
     4   5  6   7
             \   \
              8   9

The output of print this tree vertically will be:
4
2
1 5 6
3 8
7
9

The idea is to traverse the tree once and get the minimum and maximum horizontal distance with respect to root. For the tree shown above, minimum distance is -2 (for node with value 4) and
maximum distance is 3 (For node with value 9). Once we have maximum and minimum distances from root, we iterate for each vertical line at distance minimum to maximum from root, and
for each vertical line traverse the tree and print the nodes which lie on that vertical line.
'''
def verticalOrder(root):

    # Find min and max distances with respect to root
    minimum = [0]
    maximum = [0]
    findMinMax(root, minimum, maximum, 0)

    # Iterate through all possible lines starting
    # from the leftmost line and print nodes line by line
    for line_no in range(minimum[0], maximum[0]+1):
        printVerticalLine(root, line_no, 0)
        print
        
# Function to print all non-root nodes that don't have a sibling
def printSingles(root):
    if root is None:                                                    # Base Case
        return
    
    if root.left is not None and root.right is not None:                # If this is an internal node , recur for left and right subtrees
        printSingles(root.left)
        printSingles(root.right)
    elif root.right is not None:                                        # If left child is NULL, and right is not, print right child and recur for right child
        print root.right.data,
        printSingles(root.right)
    elif root.left is not None:                                         # If right child is NULL and left is not, print left child and recur for left child
        print root.left.data, 
        printSingles(root.left)

# Returs sums of all root to leaf paths. The first parameter is root of current subtree, the second parameter is value of the number formed by nodes from root to this node
def treePathsSumUtil(root, val):
    if root is None:                                                                        # Base Case
        return 0
    
    val = (val*10 + root.data)                                                              # Update val
    if root.left is None and root.right is None:                                            # If current node is leaf, return the current value of val
        return val
    
    return (treePathsSumUtil(root.left, val) + treePathsSumUtil(root.right, val))           # Recur sum of values for left and right subtree
 
# A wrapper function over treePathSumUtil()
'''
For example consider the following Binary Tree.
                                          6
                                      /      \
                                    3          5
                                  /   \          \
                                 2     5          4  
                                      /   \
                                     7     4
  There are 4 leaves, hence 4 root to leaf paths:
   Path                    Number
  6->3->2                   632
  6->3->5->7               6357
  6->3->5->4               6354
  6->5>4                    654   
Answer = 632 + 6357 + 6354 + 654 = 13997 
The above code is a simple preorder traversal code which visits every exactly once.
Therefore, the time complexity is O(n) where n is the number of nodes in the given binary tree.
'''
def treePathsSum(root):
    return treePathsSumUtil(root, 0)                                    # Pass the initial value as 0 as ther is nothing above root

# A utility function to find deepest leaf node.
# lvl:  level of current node.
# maxlvl: pointer to the deepest left leaf node found so far
# isLeft: A bool indicate that this node is left child of its parent
# resPtr: Pointer to the result
# The idea is to recursively traverse the given binary tree and while traversing, maintain level which will store the current node's level in the tree. If current node is left leaf, then check if its level is more than the level of deepest left leaf seen so far. If level is more then update the result. If current node is not leaf, then recursively find maximum depth in left and right subtrees, and return maximum of the two depths.
def deepestLeftLeafUtil(root, lvl, maxlvl, isLeft):
     
    # Base CAse
    if root is None:
        return
 
    # Update result if this node is left leaf and its level is more than the max level of the current result
    if(isLeft is True):
        if (root.left == None and root.right == None):
            if lvl > maxlvl[0] : 
                deepestLeftLeafUtil.resPtr = root 
                maxlvl[0] = lvl 
                return
 
    # Recur for left and right subtrees
    deepestLeftLeafUtil(root.left, lvl+1, maxlvl, True)
    deepestLeftLeafUtil(root.right, lvl+1, maxlvl, False)
 
# A wrapper for left and right subtree
def deepestLeftLeaf(root):
    maxlvl = [0]
    deepestLeftLeafUtil.resPtr = None
    deepestLeftLeafUtil(root, 0, maxlvl, False)
    return deepestLeftLeafUtil.resPtr
 
# A recursive function to find depth of the deepest odd level leaf node
def depthOfOddLeafUtil(root, level):
    if root is None:                                                                                        # Base Case
        return 0
    
    if root.left is None and root.right is None and level&1:                                                # If this node is leaf and its level is odd, return its level
        return level
    
    return (max(depthOfOddLeafUtil(root.left, level+1), depthOfOddLeafUtil(root.right, level+1)))           # If not leaf, return the maximum value from leftand right subtrees
 
# Main function which calculates the depth of deepest odd level leaf . 
# This function mainly uses depthOfOddLeafUtil()
def depthOfOddLeaf(root):
    level = 1
    depth = 0
    return depthOfOddLeafUtil(root, level)

# Check if the binary tree is isomorphic or not
'''Two trees are called isomorphic if one of them can be obtained from other by a series of flips, i.e. by swapping left and right children of a number of nodes. Any number of nodes at any level can have their children swapped. Two empty trees are isomorphic.

For example, following two trees are isomorphic with following sub-trees flipped: 2 and 3, NULL and 6, 7 and 8.
We simultaneously traverse both trees. Let the current internal nodes of two trees being traversed be n1 and n2 respectively. There are following two conditions for subtrees rooted with n1 and n2 to be isomorphic.
1) Data of n1 and n2 is same.
2) One of the following two is true for children of n1 and n2
a) Left child of n1 is isomorphic to left child of n2 and right child of n1 is isomorphic to right child of n2.
b) Left child of n1 is isomorphic to right child of n2 and right child of n1 is isomorphic to left child of n2.

	 1					   1
        / \                                       / \
       /   \					 /   \
      2     3				        3     2
     /\     /				      	\     /\
    4  5   6				         6   4  5
       /\					        /\
      7  8				               8  7

'''
def isIsomorphic(n1, n2):
    if n1 is None and n2 is None:                                       # Both roots are None, trees isomorphic by definition
        return True
    if n1 is None or n2 is None:                                        # Exactly one of the n1 and n2 is None, trees are not isomorphic
        return False
 
    if n1.data != n2.data :
        return False
    # There are two possible cases for n1 and n2 to be isomorphic
    # Case 1: The subtrees rooted at these nodes have NOT been "Flipped".
    # Both of these subtrees have to be isomorphic, hence the &&
    # Case 2: The subtrees rooted at these nodes have been "Flipped"
    return ((isIsomorphic(n1.left, n2.left)and
            isIsomorphic(n1.right, n2.right)) or
            (isIsomorphic(n1.left, n2.right) and
            isIsomorphic(n1.right, n2.left))
            )

# http://www.geeksforgeeks.org/convert-given-binary-tree-doubly-linked-list-set-3/
# A simple recursive function to convert a given Binary tree to Doubly Linked List
# root --> Root of Binary Tree
# Time Complexity: The above program does a simple inorder traversal, so time complexity is O(n) where n is the number of nodes in given binary tree.
def bt2dll(root):
        if root is None:
            return
        
        bt2dll(root.left)                       # Recursively convert left subtree
        
        if bt2dll.prev is None:                 # Now convert this node
            bt2dll.head = root
        else:
            root.left = bt2dll.prev
            bt2dll.prev.right = root
        bt2dll.prev = root
        
        bt2dll(root.right)                      # Finally convert right subtree

        return bt2dll.head
    
# Function to print nodes in a given doubly linked list
def printList(node):
        while node: 
            print(node.data + " ")
            node = node.right

# Standard Inorder traversal of tree
def inorder(root):
    if root is not None:
        inorder(root.left)
        print "\t%d" %(root.data),
        inorder(root.right)

# Convert binary to doubly linked list 
# http://www.geeksforgeeks.org/convert-a-given-binary-tree-to-doubly-linked-list-set-2/
# Changes left pointers to work as previous pointers in converted DLL
# The function simply does inorder traversal of 
# Binary Tree and updates
# left pointer using previously visited node
def fixPrevPtr(root):
    if root is not None:
        fixPrevPtr(root.left)
        root.left = fixPrevPtr.pre
        fixPrevPtr.pre = root 
        fixPrevPtr(root.right)

# Changes right pointers to work as nexr pointers in converted DLL
def fixNextPtr(root):
 
    prev = None
    # Find the right most node in BT or last node in DLL
    while(root and root.right != None):
        root = root.right 
 
    # Start from the rightmost node, traverse back using
    # left pointers While traversing, change right pointer of nodes 
    while(root and root.left != None):
        prev = root 
        root = root.left 
        root.right = prev
 
    # The leftmost node is head of linked list, return it
    return root

# The main function that converts BST to DLL and returns head of DLL
def BTToDLL(root):
     
    # Set the previous pointer 
    fixPrevPtr(root)
 
    # Set the next pointer and return head of DLL
    return fixNextPtr(root)
 
# Traversses the DLL from left to right 
def printList(root):
    while(root != None):
        print "\t%d" %(root.data),
        root = root.right

'''
Extract Leaves of a Binary Tree in a Doubly Linked List (DLL)

Note that the DLL need to be created in-place. Assume that the node structure of DLL and Binary Tree is same, only the meaning of left and right pointers are different.
In DLL, left means previous pointer and right means next pointer. 
Let the following be input binary tree
        1
     /     \
    2       3
   / \       \
  4   5       6
 / \         / \
7   8       9   10


Output:
Doubly Linked List
7<->8<->5<->9<->10

Modified Tree:
        1
     /     \
    2       3
   /         \
  4           6

We need to traverse all leaves and connect them by changing their left and right pointers.
We also need to remove them from Binary Tree by changing left or right pointers in parent nodes.
There can be many ways to solve this. In the following implementation, we add leaves at the beginning of current linked list and update head of the list using pointer to head pointer.
Since we insert at the beginning, we need to process leaves in reverse order. For reverse order, we first traverse the right subtree then the left subtree.
We use return values to update left or right pointers in parent nodes.
# The function also sets *head_ref as head of doubly linked list.
# left pointer of tree is used as prev in DLL
# and right pointer is used as next
'''
def extractLeafList(root):
     
    # Base Case
    if root is None:
        return None
 
    if root.left is None and root.right is None:
        # This node is going to be added to doubly linked
        # list of leaves, set pointer of this node as
        # previous head of DLL. We don't need to set left
        # pointer as left is already None
        root.right = extractLeafList.head
         
        # Change the left pointer of previous head
        if extractLeafList.head is not None:
            extractLeafList.head.left = root
 
        # Change head of linked list
        extractLeafList.head = root
         
        return None # Return new root
 
    # Recur for right and left subtrees
    root.right = extractLeafList(root.right)
    root.left = extractLeafList(root.left)
     
    return root 

def printDLL(head):
    while(head):
        if head.data is not None:
            print head.data,
        head = head.right

# Recursive function which check whether all leaves are at same level
# The idea is to first find level of the leftmost leaf and store it in a variable leafLevel. Then compare level of all other leaves with leafLevel, if same, return true, else return false.
# We traverse the given Binary Tree in Preorder fashion. An argument leaflevel is passed to all calls.
# The value of leafLevel is initialized as 0 to indicate that the first leaf is not yet seen yet.
# The value is updated when we find first leaf. Level of subsequent leaves (in preorder) is compared with leafLevel.
def checkUtil(root, level):
     
    # Base Case 
    if root is None:
        return True
     
    # If a tree node is encountered
    if root.left is None and root.right is None:
         
        # When a leaf node is found first time
        if check.leafLevel == 0 :
            check.leafLevel = level # Set first leaf found
            return True
 
        # If this is not first leaf node, compare its level
        # with first leaf's level
        return level == check.leafLevel 
 
    # If this is not first leaf node, compare its level
    # with first leaf's level
    return (checkUtil(root.left, level+1)and
            checkUtil(root.right, level+1))
 
def check(root):	# For checking we can use the same logic for "root to leaf" paths algorithm
    level = 0
    check.leafLevel = 0
    return (checkUtil(root, level))

# The main function that returns difference between odd and even level nodes
# A straightforward method is to use level order traversal. In the traversal, check level of current node, if it is odd, increment odd sum by data of current node,
# otherwise increment even sum. Finally return difference between odd sum and even sum.
def getLevelDiff(root):

    if root is None:
        return 0
 
    # Difference for root is root's data - difference for
    # left subtree - difference for right subtree
    return (root.data - getLevelDiff(root.left)-
        getLevelDiff(root.right))

# Function to find ceil of a given input in BST. If input is more than the max key in BST, return -1
def ceil(root, inp):
    
    if root == None:
        return -1
     
    # We found equal key
    if root.data == inp :
        return root.data 
     
    # If root's key is smaller, ceil must be in right subtree
    if root.data < inp:
        return ceil(root.right, inp)
     
    # Else, either left subtre or root has the ceil value
    val = ceil(root.left, inp)
    return val if val >= inp else root.data

'''
Given a Binary Tree, write a function to check whether the given Binary Tree is Complete Binary Tree or not.

A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
The following trees are examples of Complete Binary Trees
    1
  /   \
 2     3
  
       1
    /    \
   2       3
  /
 4

       1
    /    \
   2      3
  /  \    /
 4    5  6

The following trees are examples of Non-Complete Binary Trees
    1
      \
       3
  
       1
    /    \
   2       3
    \     /  \   
     4   5    6

       1
    /    \
   2      3
         /  \
        4    5

The method 2 of level order traversal post can be easily modified to check whether a tree is Complete or not. To understand the approach, let us first define a term "Full Node".
A node is "Full Node" if both left and right children are not empty (or not NULL).

The approach is to do a level order traversal starting from root. In the traversal, once a node is found which is NOT a Full Node, all the following nodes must be leaf nodes.
Also, one more thing needs to be checked to handle the below case: If a node has empty left child, then the right child must be empty. 
    1
  /   \
 2     3
  \
   4
   
'''
def isCompleteBT(root):
     
    # Base Case: An empty tree is complete Binary tree
    if root is None:
        return True
 
    # Create an empty queue
    queue = []
 
    # Create a flag variable which will be set True when a non full node is seen
    flag = False
 
    # Do level order traversal using queue
    queue.append(root)
    while(len(queue) > 0):
        tempNode = queue.pop(0) # Dequeue 
 
        # Check if left child is present
        if (tempNode.left):
             
            # If we have seen a non full node, and we see
            # a node with non-empty left child, then the
            # given tree is not a complete binary tree
            if flag == True :
                return False
 
            # Enqueue left child
            queue.append(tempNode.left)
 
            # If this a non-full node, set the flag as true
        else:
            flag = True
 
        # Check if right cild is present
        if(tempNode.right):
                 
            # If we have seen a non full node, and we 
            # see a node with non-empty right child, then
            # the given tree is not a compelete BT
            if flag == True:
                return False
 
            # Enqueue right child
            queue.append(tempNode.right)
             
        # If this is non-full node, set the flag as True
        else:
            flag = True
         
    # If we reach here, then the tree is compelete BT
    return True

############### Binary tree to BST(Binary Search Tree) conversion ################
'''
Examples. 
Example 1
Input:
          10
         /  \
        2    7
       / \
      8   4
Output:
          8
         /  \
        4    10
       / \
      2   7


Example 2
Input:
          10
         /  \
        30   15
       /      \
      20       5
Output:
          15
         /  \
       10    20
       /      \
      5        30

Solution
 Following is a 3 step solution for converting Binary tree to Binary Search Tree.
 1) Create a temp array arr[] that stores inorder traversal of the tree. This step takes O(n) time.
 2) Sort the temp array arr[]. Time complexity of this step depends upon the sorting algorithm. In the following implementation, Quick Sort is used which takes (n^2) time. This can be done in O(nLogn) time using Heap Sort or Merge Sort.
 3) Again do inorder traversal of tree and copy array elements to tree nodes one by one. This step takes O(n) time.
 
'''
# Helper function to store the inroder traversal of a tree
def storeInorder(root, inorder):
     
    # Base Case
    if root is None:
        return
     
    # First store the left subtree
    storeInorder(root.left, inorder)
     
    # Copy the root's data
    inorder.append(root.data)
 
    # Finally store the right subtree
    storeInorder(root.right, inorder)
 
# A helper funtion to count nodes in a binary tree
def countNodes(root):
    if root is None:
        return 0 
    return countNodes(root.left) + countNodes(root.right) + 1

# Helper function that copies contents of sorted array to Binary tree
def arrayToBST(arr, root):
 
    # Base Case
    if root is None:
        return
     
    # First update the left subtree
    arrayToBST(arr, root.left)
 
    # now update root's data delete the value from array
    root.data = arr[0]
    arr.pop(0)
 
    # Finally update the right subtree
    arrayToBST(arr, root.right)
 
# This function converts a given binary tree to BST
def binaryTreeToBST(root):
     
    # Base Case: Tree is empty
    if root is None:
        return
     
    # Count the number of nodes in Binary Tree so that we know the size of temporary array to be created
    n = countNodes(root)
 
    # Create the temp array and store the inorder traveral of tree
    arr = []
    storeInorder(root, arr)
     
    # Sort the array
    arr.sort()
 
    # copy array elements back to binary tree
    arrayToBST(arr, root)

##################################################################################
'''
Check if a binary tree is subtree of another binary tree | Set 1

For example, in the following case, tree S is a subtree of tree T.
        Tree 2
          10  
        /    \ 
      4       6
       \
        30



        Tree 1
              26
            /   \
          10     3
        /    \     \
      4       6      3
       \
        30

'''
# A utility function to check whether trees with roots as root 1 and root2 are identical or not
def areIdentical(root1, root2):
     
    # Base Case
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
 
    # Check if the data of both roots is same and data of
    # left and right subtrees are also same
    return (root1.data == root2.data and
            areIdentical(root1.left , root2.left)and
            areIdentical(root1.right, root2.right)
            ) 
 
# This function returns True if S is a subtree of T, otherwise False
def isSubtree(T, S):
     
    # Base Case
    if S is None:
        return True
 
    if T is None:
        return True
 
    # Check the tree with root as current node
    if (areIdentical(T, S)):
        return True
 
    # IF the tree with root as current node doesn't match
    # then try left and right subtree one by one
    return isSubtree(T.left, S) or isSubtree(T.right, S)

# The function prints all the keys in the given range [k1..k2]. Assumes that k1 < k2
def Print(root, k1, k2):
     
    # Base Case
    if root is None:
        return
 
    # Since the desired o/p is sorted, recurse for left
    # subtree first. If root.data is greater than k1, then
    # only we can get o/p keys in left subtree
    if k1 < root.data :
        Print(root.left, k1, k2)
 
    # If root's data lies in range, then prints root's data
    if k1 <= root.data and k2 >= root.data:
        print root.data,
 
    # If root.data is smaller than k2, then only we can get
    # o/p keys in right subtree
    if k2 > root.data:
        Print(root.right, k1, k2)

# Returns true if the given tree is a binary search tree (efficient version)
# Time Complexity: O(n)
# Auxiliary Space : O(1) if Function Call Stack size is not considered, otherwise O(n)
def isBST(node):
    return (isBSTUtil(node, INT_MIN, INT_MAX))
 
# Retusn true if the given tree is a BST and its values >= min and <= max
def isBSTUtil(node, mini, maxi):
     
    # An empty tree is BST
    if node is None:
        return True
 
    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False
 
    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, mini, node.data -1) and isBSTUtil(node.right, mini, node.data -1))

# Time Complexity: O(n)
def sortedArrayToBST(arr, start, end):
    if start > end:
        return None
     
    mid = (start + end) / 2                             # Get the middle element and make it root
    node = Node(arr[mid])
    
    node.left = sortedArrayToBST(arr, start, mid - 1)   # Recursively construct the left subtree and make it left child of root
    node.right = sortedArrayToBST(arr, mid + 1, end)    # Recursively construct the right subtree and make it right child of root

# Time Complexity: O(n^2) Worst case occurs in case of skewed tree.
# See the more optimized one at https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/ (O(n) solution)
def isBalanced(node):
    lh = 0  										#for height of left subtree
    rh = 0  										# for height of right subtree
    if node is None:
        return True
    lh = height(node.left)      					# Get the height of left and right sub trees
    rh = height(node.right)

    if ((lh - rh) <= 1 and isBalanced(node.left) and isBalanced(node.right)):
        return True

    return False    								# If we reach here then tree is not height-balanced

'''
Convert a given tree to its Sum Tree
Convert a given tree to a tree where every node contains sum of values of nodes in left and right subtrees in the original tree

                   10
                  / \
                 /   \
               -2     6
               /\     /\ 
              8 -4   7  5


should be changed to
                 20(4-2+12+6)
               /      \
              /        \
       4(8-4)      12(7+5)
           /\      /\ 
          0  0    0  0
Time complexity O(n) where n is the number of nodes in the given Binary Tree
'''
def toSumTree(node):
    if node is None:
        return 0
    old_val = node.data
    node.data = toSumTree(node.left) + toSumTree(node.right)
    return node.data + old_val

def Sum(node):
    if node is None:
        return 0
    return Sum(node.left) + node.data + Sum(node.right)

'''
A SumTree is a Binary Tree where the value of a node is equal to sum of the nodes present in its left subtree and right subtree.
An empty tree is SumTree and sum of an empty tree can be considered as 0. A leaf node is also considered as SumTree.

Following is an example of SumTree.
          26
        /   \
      10     3
    /    \     \
  4      6      3

returns 1 if sum property holds for the given node and both of its children
Time Complexity: O(n^2) in worst case. Worst case occurs for a skewed tree.
Check https://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-sumtree/ for the tricky solution with O(n) time
'''
def isSumTree(root):
    left_data = 0
    right_data = 0
    if (root is None or (root.left is None and root.right is None)):
        return 1

    # Get sum of nodes in left and right subtrees
    left_data = Sum(root.left)
    right_data = Sum(root.right)

    # if the node and both of its children satisfy the property return 1 else 0
    if ((root.data == left_data + right_data) and (isSumTree(root.left) != 0) and (isSumTree(root.right)) != 0):
        return 1
    return 0

'''
Check for Children Sum Property in a Binary Tree
		 10
		/ \
	   /   \
	  8	    2
	 /\	   /
	3  5  2
Time Complexity: O(n)
returns 1 if children sum property holds for the given node and both of its children
'''
def isSumProperty(root):
    left_data = 0
    right_data = 0  																												# left_data is left child data and right_data is for right child data
    if (root is None or (root.left is None and root.right is None)):
        return 1
    else:
        if (root.left is not None):
            left_data = root.left.data
        if (root.right is not None):
            right_data = root.right.data
        if ((root.data == left_data + right_data) and (isSumProperty(root.left)!=0) and isSumProperty(root.right)!=0):
            return 1                                                                                                               # if the node and both of its children satisfy the property return 1 else 0
        else:
            return 0

# Convert an arbitrary Binary Tree to a tree that holds Children Sum Property
def convertTree(node):
    left_data = 0
    right_data = 0
    diff = 0

    #If tree is empty or it's a leaf node then return true
    if ((node is None) or (node.left is None and node.right is None)):
        return
    else:
        convertTree(node.left)                                                  # convert left and right subtrees
        convertTree(node.right)
        if (node.left is not None):                                             # If left child is not present then 0 is used as data of left child
            left_data = node.left.data                                          # If right child is not present then 0 is used as data of right child
        if (node.right is not None):
            right_data = node.right.data
                                                                                # get the diff of node's data and children sum */
        diff = left_data + right_data - node.data
                                                                                # If node's children sum is greater than the node's data
        if (diff > 0):
            node.data = node.data + diff;
                                                                                # THIS IS TRICKY --> If node's data is greater than children sum, then increment subtree by diff
        if (diff < 0):                                                          # -diff is used to make diff positive
            increment(node, -diff)
  
# This function is used to increment subtree by diff 
def increment(node, diff):
                                                                                # IF left child is not NULL then increment it
    if (node.left is not None):
        node.left.data = node.left.data + diff                                  # Recursively call to fix the descendants of node->left
        increment(node.left, diff)
    elif (node.right is not None):                                           # Else increment right child
        node.right.data = node.right.data + diff                                #Recursively call to fix the descendants of node->right
        increment(node.right, diff)
'''
Remove all nodes which donâ€™t lie in any path with sum>= k

Given a binary tree, a complete path is defined as a path from root to a leaf. The sum of all nodes on that path is defined as the sum of that path. Given a number K, 
you have to remove (prune the tree) all nodes which donâ€™t lie in any path with sum>=k. 
Note: A node can be part of multiple paths. So we have to delete it only in case when all paths from it have sum less than K.
Consider the following Binary Tree
          1 
      /      \
     2        3
   /   \     /  \
  4     5   6    7
 / \    /       /
8   9  12      10
   / \           \
  13  14         11
      / 
     15 

For input k = 20, the tree should be changed to following
(Nodes with values 6 and 8 are deleted)
          1 
      /      \
     2        3
   /   \        \
  4     5        7
   \    /       /
    9  12      10
   / \           \
  13  14         11
      / 
     15 

For input k = 45, the tree should be changed to following.
      1 
    / 
   2   
  / 
 4  
  \   
   9    
    \   
     14 
     /
    15 
Time Complexity: O(n)
Solution: The idea is to keep reducing the sum when traversing down. When we reach a leaf and sum is greater than the leafâ€™s data, then we delete the leaf. 
Note that deleting nodes may convert a non-leaf node to a leaf node and if the data for the converted leaf node is less than the current sum, 
then the converted leaf should also be deleted. 

'''
def prune(root, Sum):
    if (root is None):
        return None

    root.left = prune(root.left, Sum - root.data)
    root.right = prune(root.right, Sum - root.data)
 
    # If we reach leaf whose data is smaller than sum, we delete the leaf.  An important thing to note is a non-leaf node can become leaf when its chilren are deleted.
    if (root.left is None and root.right is None):
        if (root.data < Sum):
            root = None
            return None
 
    return root

'''
Add all greater values to every node in a given BST
Given a Binary Search Tree (BST), modify it so that all greater values in the given BST are added to every node. For example, consider the following BST. 
              50
           /      \
         30        70
        /   \      /  \
      20    40    60   80 

The above tree should be modified to following 

              260
           /      \
         330        150
        /   \       /  \
      350   300    210   80
O(n^2) time

The below solution is same for https://www.geeksforgeeks.org/convert-bst-to-a-binary-tree/, 
(Convert a BST to a Binary Tree such that sum of all greater keys is added to every key)

insert2BST can be useful for https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversal-set-2/
'''
class Sum:
    sum = 0
    
def insert2BST(root, data):							# Creates a BST
													#If the tree is empty, return a new node
    if (root is None):
        root = Node(data)
        return root

    if (data <= root.data):							# Otherwise, recur down the tree
        root.left = insert2BST(root.left, data)
    else:
        root.right = insert2BST(root.right, data)
    return root

def modifyBSTUtil(root, Sum):
    if root is None:
        return
    modifyBSTUtil(root.right, Sum)
    Sum.sum = Sum.sum + root.data
    root.data = Sum.sum
    modifyBSTUtil(root.left, Sum)
    
# A wrapper over modifyBSTUtil()
def modifyBST(root):
    S = Sum()
    modifyBSTUtil(root, S)

'''A recursive function to construct Full from pre[] and post[].
preIndex is used to keep track of index in pre[].
l is low index and h is high index for the current subarray in post[]'''
def constructTreeUtil(pre, post, l, h, size, index):
    if (index.preindex >= size or l > h):
        return None
 
    # The first node in preorder traversal is root. So take the node at preIndex from preorder and make it root, and increment preIndex
    root = Node(pre[index.preindex])
    index.preindex += 1

    # If the current subarry has only one element, no need to recur or preIndex > size after incrementing
    if (l == h or index.preindex >= size):
        return root

    # Search the next element of pre[] in post[]
    for i in xrange(l, h+1):
        if (post[i] == pre[index.preindex]):
            break

    # Use the index of element found in postorder to divide postorder array in two parts. Left subtree and right subtree
    if (i <= h):
        root.left = constructTreeUtil(pre, post, l, i, size, index)
        root.right = constructTreeUtil(pre, post, i + 1, h, size, index)
        
    return root
 
# The main function to construct Full Binary Tree from given preorder and postorder traversals. This function mainly uses constructTreeUtil()
# Note: The inorder traversal doesn't match with the output mentioned here https://www.geeksforgeeks.org/full-and-complete-binary-tree-from-given-preorder-and-postorder-traversals/
# Check it again though the logic here is same as it's mentioned in the above url and is correct
def constructTree(pre, post, size):
    index = Index()
    return constructTreeUtil(pre, post, 0, size - 1, size, index)
	
# Returns true if the given tree can be folded
# A tree can be folded if left and right subtrees of the tree are structure wise mirror image of each other. An empty tree is considered as foldable. 
def IsFoldable(root):
    if root is None:
        return true
    return IsFoldableUtil(root.left, root.right)
  
# A utility function that checks if trees with roots as n1 and n2 are mirror of each other
def IsFoldableUtil(node1, node2):                                                                       # If both left and right subtrees are NULL, then return true
    if (node1 is None and node2 is None):
        return True
    if (node1 is None or node2 is None):                                                                # If one of the trees is NULL and other is not, then return false
        return False
    return IsFoldableUtil(node1.left, node2.right) and IsFoldableUtil(node1.right, node2.left)          # Otherwise check if left and right subtrees are mirrors of their counterparts

'''
Construct Special Binary Tree from given Inorder traversal
Given Inorder Traversal of a Special Binary Tree in which key of every node is greater than keys in left and right children, construct the Binary Tree and return root.

Examples:
Input: inorder[] = {5, 10, 40, 30, 28}
Output: root of following tree
         40
       /   \
      10     30
     /         \
    5          28 

Input: inorder[] = {1, 5, 10, 40, 30, 15, 28, 20}
Output: root of following tree
          40
        /   \
       10     30
      /         \
     5          28
    /          /  \
   1         15    20

The idea used in  Construction of Tree from given Inorder and Preorder traversals can be used here. Let the given array is {1, 5, 10, 40, 30, 15, 28, 20}.
The maximum element in given array must be root. The elements on left side of the maximum element are in left subtree and elements on right side are in right subtree.
         40
      /       \  
   {1,5,10}   {30,15,28,20}

We recursively follow above step for left and right subtrees, and finally get the following tree. 
          40
        /   \
       10     30
      /         \
     5          28
    /          /  \
   1         15    20

Algorithm: buildTree()
 1) Find index of the maximum element in array. The maximum element must be root of Binary Tree.
 2) Create a new tree node 'root' with the data as the maximum value found in step 1.
 3) Call buildTree for elements before the maximum element and make the built tree as left subtree of 'root'.
5) Call buildTree for elements after the maximum element and make the built tree as right subtree of 'root'.
6) return 'root'.
'''
def buildTree(inorder, start, end, node):
    if (start > end):
        return None
                                                                                                                # Find index of the maximum element from Binary Tree
    i = getMax(inorder, start, end)                                                                             #Pick the maximum value and make it root
    node = Node(inorder[i])
                                                                                                                #If this is the only element in inorder[start..end], then return it
    if (start == end):
        return node
                                                                                                                # Using index in Inorder traversal, construct left and right subtress
    node.left = buildTree(inorder, start, i - 1, node.left)
    node.right = buildTree(inorder, i + 1, end, node.right)
    return node

# Function to find index of the maximum value in arr[start...end]
def getMax(arr, strt, end):
    maximum = arr[strt]
    maxind = strt
    for i in xrange(strt+1, end+1):
        if (arr[i] > maximum):
            maximum = arr[i]
            maxind = i
    return maxind
	
class BinarySearchTree:
    first = middle = last = prev = None

'''
A function to fix a given BST where two nodes are swapped.  This function uses correctBSTUtil() to find out two nodes and swaps the nodes to fix the BST
             6
            / \
           10  2
          / \ / \
         1  3 7 12
         
        10 and 2 are swapped

Correct it to
             6
            / \
           2   10
          / \ / \
         1  3 7 12

Time Complexity: O(n)
'''
def correctBST(root):
    BST = BinarySearchTree()
    
    correctBSTUtil( root, BST )

    if BST.first and BST.last:                                          # or if first is not None and last is not None:
        BST.first.data, BST.last.data = BST.last.data, BST.first.data
    elif first and middle:
        BST.first.data, BST.middle.data = BST.middle.data, BST.first.data
    # else nodes have not been swapped, passed tree is really BST

def correctBSTUtil(root, BST):
    if root is not None:
        correctBSTUtil( root.left, BST )
        if (BST.prev and root.data < BST.prev.data):                                    # If this node is smaller than the previous node, it's violating the BST rule.
            if BST.first is None:
                BST.first = BST.prev
                BST.middle = root
            else:
                BST.last = root
        BST.prev = root
        correctBSTUtil( root.right, BST )

class Index:
    index = 0
    preindex=0
    
def constructTreeSpecialUtil(pre, preLN, index_ptr, n, temp):
    index = index_ptr.index                                                     # store the current value of index in pre[]
    if (index == n):                                                            # Base Case: All nodes are constructed
        return None
    
    temp = Node(pre[index])                                                     # Allocate memory for this node and increment index for subsequent recursive calls
    index_ptr.index += 1

    if (preLN[index] == 'N'):
            temp.left = constructTreeSpecialUtil(pre, preLN, index_ptr, n, temp.left)
            temp.right = constructTreeSpecialUtil(pre, preLN, index_ptr, n, temp.right)
    return temp
  
# A wrapper over constructTreeUtil()
'''
Construct a special tree from given preorder traversal
Given an array pre[] that represents Preorder traversal of a spacial binary tree where every node has either 0 or 2 children.
One more array preLN[] is given which has only two possible values L and N. The value L in preLN[] indicates that the corresponding
node in Binary Tree is a leaf node and value N indicates that the corresponding node is non-leaf node. Write a function to construct the tree from the given two arrays.
Time Complexity: O(n)
'''
def constructTreeSpecial(pre, preLN, n, node):
    #Initialize index as 0. Value of index is used in recursion to maintain the current index in pre[] and preLN[] arrays.
    myindex = Index()
    return constructTreeSpecialUtil(pre, preLN, myindex, n, node)

'''
Check if each internal node of a BST has exactly one child
Given Preorder traversal of a BST, check if each non-leaf node has only one child. Assume that the BST contains unique entries.

Examples:
Input: pre[] = {20, 10, 11, 13, 12}
Output: Yes
The give array represents following BST. In the following BST, every internal
node has exactly 1 child. Therefor, the output is true.
        20
       /
      10
       \
        11
          \
           13
           /
         12
In Preorder traversal, if all internal nodes have only one child in a BST, then all the descendants of every node are either smaller or larger than the node.
Approach 1 (Naive) 
 This approach simply follows the above idea that all values on right side are either smaller or larger. Use two loops, the outer loop picks an element one by one,
 starting from the leftmost element. The inner loop checks if all elements on the right side of the picked element are either smaller or greater.
 
Time complexity: O(n^2)
'''
def hasOnlyOneChild(pre, size):
    nextDiff = lastDiff = None
    for i in xrange(0, size-1):
        nextDiff = pre[i] - pre[i + 1]
        lastDiff = pre[i] - pre[size - 1]
        if (nextDiff * lastDiff < 0):
            return False
    return True
	
'''
Print Postorder traversal from given Inorder and Preorder traversals
Given Inorder and Preorder traversals of a binary tree, print Postorder traversal. 

Example: 
Input:
Inorder traversal in[] = {4, 2, 5, 1, 3, 6}
Preorder traversal pre[] = {1, 2, 4, 5, 3, 6}

Output:
Postorder traversal is {4, 5, 2, 6, 3, 1}

Trversals in the above example represents following tree 
         1
      /        
     2       3
   /         
  4     5      6
A naive method is to first construct the tree, then use simple recursive method to print postorder traversal of the constructed tree.
We can print postorder traversal without constructing the tree. The idea is, root is always the first item in preorder traversal and it must be the last item in postorder traversal.
We first recursively print left subtree, then recursively print right subtree. Finally, print root.
To find boundaries of left and right subtrees in pre[] and in[], we search root in in[], all elements before root in in[] are elements of left subtree and
all elements after root are elements of right subtree. In pre[], all elements after index of root in in[] are elements of right subtree.
And elements before index (including the element at index and excluding the first element) are elements of left subtree.
'''
def printPostOrderFromInOrderAndPreOrder(inOrder, pre, n):
    # The first element in pre[] is always root, search it in in[] to find left and right subtrees
    root = search(inOrder, pre[0], n)
    if root != 0:                                                                   # If left subtree is not empty, print left subtree
      printPostOrderFromInOrderAndPreOrder(inOrder, pre[1:], root)
    if (root != n-1):                                                               # If right subtree is not empty, print right subtree
      printPostOrderFromInOrderAndPreOrder(inOrder[root+1:], pre[root+1:], n-root-1)
    print pre[0],
 
# A utility function to search x in arr[] of size n
def search(arr, x, n):
    for i in xrange(0, n):#(int i = 0; i < n; i++)
      if (arr[i] == x):
         return i
    return -1

# The function returns size of the largest independent set in a given binary tree
# Time complexity is exponential here. To reduce it i.e. to make it O(n^2) refer the other solution https://www.geeksforgeeks.org/largest-independent-set-problem/
def LISS(root):
    if root is None:
        return 0
    
    size_excl = LISS(root.left) + LISS(root.right)                  # Caculate size excluding the current node
    size_incl = 1                                                   # Calculate size including the current node
    
    if root.left:
       size_incl += LISS(root.left.left) + LISS(root.left.right)
    if root.right:
       size_incl += LISS(root.right.left) + LISS(root.right.right)
    return max(size_incl, size_excl)
'''
Double Tree
Write a program that converts a given tree to its Double tree. To create Double tree of the given tree, create a new duplicate for each node, and
insert the duplicate as the left child of the original node.

So the tree
    2
   / \
  1   3


is changed to
       2
      / \
     2   3
    /   /
   1   3
  /
 1


And the tree
            1
          /   \
        2      3
      /  \
    4     5


is changed to
               1
             /   \
           1      3
          /      /
        2       3
      /  \
     2    5
    /    /
   4   5
  /
 4

Algorithm:
 Recursively convert the tree to double tree in postorder fashion. For each node,
 first convert the left subtree of the node, then right subtree,
 finally create a duplicate node of the node and fix the left child of the node and left child of left child.
 Time Complexity: O(n) where n is the number of nodes in the tree.
'''
# Function to convert a tree to double tree
def doubleTree(node):
    oldLeftNode = None
    if node is None:
        return
    doubleTree(node.left)
    doubleTree(node.right)

    oldLeftNode = node.left
    node.left = Node(node.data)
    node.left.left = oldLeftNode
    
'''
Merge Two Balanced Binary Search Trees(BSTs) (https://www.geeksforgeeks.org/merge-two-balanced-binary-search-trees/)

You are given two balanced binary search trees e.g., AVL or Red Black Tree. Write a function that merges the two given balanced BSTs into a balanced binary search tree.
Let there be m elements in first tree and n elements in the other tree. Your merge function should take O(m+n) time.

Method 1 (Insert elements of first tree to second) 
 Take all elements of first BST one by one, and insert them into the second BST. Inserting an element to a self balancing BST takes Long time (See this) where n is size of the BST.
 So time complexity of this method is Log(n) + Log(n+1) â€¦ Log(m+n-1). The value of this expression will be between mLogn and mLog(m+n-1). As an optimization, we can pick the smaller tree as first tree.

Method 2 (Merge Inorder Traversals)
1) storeInorder(): Do inorder traversal of first tree and store the traversal in one temp array arr1[]. This step takes O(m) time.
 2) storeInorder(): Do inorder traversal of second tree and store the traversal in another temp array arr2[]. This step takes O(n) time.
 3) The arrays created in step 1 and 2 are sorted arrays. Merge the two sorted arrays into one array of size m + n. This step takes O(m+n) time.
 4) arrayToBST(): Construct a balanced tree from the merged array using the technique discussed in this post. This step takes O(m+n) time.

Time complexity of this method is O(m+n) which is better than method 1. This method takes O(m+n) time even if the input BSTs are not balanced.
'''
'''
Find k-th smallest element in BST (Order Statistics in BST)
Method 1: Using Inorder Traversal.

Inorder traversal of BST retrieves elements of tree in the sorted order. The inorder traversal uses stack to store to be explored nodes of tree (threaded tree avoids stack and recursion for traversal, see this post). The idea is to keep track of popped elements which participate in the order statics. Hypothetical algorithm is provided below,
Time complexity: O(n) where n is total nodes in tree..
'''	
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
root = sortedArrayToBST(arr, 0, n - 1)
printLevelOrder(root)
'''
          4
        /   \
       /     \
      2       6
     /\       /\
    1  3     5  7

Other solution:
1) Do In-Order Traversal of the given tree and store the result in a temp array.
3) Check if the temp array is sorted in ascending order, if it is, then the tree is BST.
Time Complexity: O(n)
'''

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
'''
          20
         /  \
        8    22
       / \
      4   12
         /  \
        10   14
'''
print "Preorder traversal of binary tree is"
printPreorder(root)
MorrisTraversal(root)
 
print "\nInorder traversal of binary tree is"
printInorder(root)
 
print "\nPostorder traversal of binary tree is"
printPostorder(root)
print "\n"

print "\nLevelorder traversal of binary tree is"
printLevelOrder(root)							# Output: 20 8 22 4 12 10 14

print "\nLevelorder traversal of binary tree is"
printSpiral(root)								# Output: 20 8 22 12 4 10 14
printLevelOrderSpiral(root)						# Output: 20 8 22 12 4 10 14

print "\n"
print size(root)
print "\n"
print height(root)

print "\nDiameter of given binary tree is %d" %(diameter(root))
print "\nMaximum width is %d" %(getMaxWidth(root))

print "Paths of leaf from root are: ", binaryTreePaths(root)
print "\nLeft view of binary tree is "
leftView(root)

print "\nAncestors of 12 are: ",
printAncestors(root, 12)

n1 = 10 ; n2 = 14
t = lca_of_BST(root, n1, n2)
print "\nLCA of %d and %d is %d" %(n1, n2, t.data)
 
n1 = 14 ; n2 = 8
t = lca_of_BST(root, n1, n2)
print "LCA of %d and %d is %d" %(n1, n2 , t.data)
 
n1 = 10 ; n2 = 22
t = lca_of_BST(root, n1, n2)
print "LCA of %d and %d is %d" %(n1, n2, t.data)

mirror = mirrorTree(root)
print "\nLevelorder traversal of mirror tree is "
printLevelOrder(mirror)

s = 21
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.right = Node(5)
root.left.left = Node(3)
root.right.left = Node(2)
 
if hasPathSum(root, s):
    print "There is a root-to-leaf path with sum %d" %(s)
else:
    print "There is no root-to-leaf path with sum %d" %(s)

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

print "Max pathSum of the given binary tree is", maxPathSum(root)
'''
       -15
      /    \
     5      6
    / \    /  \
   -8  1  3    9
   /\           \
  2  6           0
                /  \
               4   -1
                   / \
                 11   10
                       \
                        12
'''

bt2dll.prev = None
bt2dll.head= None
head = bt2dll(root)
print "\n"
printList(head)

print "K distance node from root: ",
printkDistanceNodeDown(root, 2)

print "\nK distance node from target"
target = root.left
printkDistanceNode(root, target, 2)

#toSumTree(root)
#printLevelOrder(root)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
print "LCA(4, 5) = %d" %(findLCA(root, 4, 5,))
print "LCA(4, 6) = %d" %(findLCA(root, 4, 6))
print "LCA(3, 4) = %d" %(findLCA(root,3,4))
print "LCA(2, 4) = %d" %(findLCA(root,2, 4))

result = deepestLeftLeaf(root) 
if result is None:
    print "There is not left leaf in the given tree"
else:
    print "The deepst left child is", result.data

print "%d is the required deepest odd level depth" %(depthOfOddLeaf(root))

''' 
//http://www.geeksforgeeks.org/find-distance-between-two-nodes-of-a-binary-tree/
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right= Node(7)
root.right.left = Node(6)
root.left.right = Node(5)
root.right.left.right = Node(8)

dist = findDistance(root, 4, 5)
print "Distance between node %d & %d: %d" %(4, 5, dist)
dist = findDistance(root, 4, 6)
print "Distance between node %d & %d: %d" %(4, 6, dist)
 
dist = findDistance(root, 3, 4)
print "Distance between node %d & %d: %d" % (3, 4, dist) 
 
dist = findDistance(root, 2, 4)
print "Distance between node {} & {}: {}".format(2, 4, dist) 
 
dist = findDistance(root, 8, 5)
print "Distance between node {} & {}: {}".format(8, 5, dist) 

'''
print "Vertical order traversal is"
verticalOrder(root)

print "Leaf count of the tree is %d" %(getLeafCount(root))

print "All non-root nodes that don't have a sibling: "
printSingles(root)

print "\nSum of all paths is", treePathsSum(root)

n1 = Node(1)
n1.left = Node(2)
n1.right = Node(3)
n1.left.left = Node(4)
n1.left.right = Node(5)
n1.right.left = Node(6)
n1.left.right.left = Node(7)
n1.left.right.right = Node(8)
 
n2 = Node(1)
n2.left = Node(3)
n2.right = Node(2)
n2.right.left = Node(4)
n2.right.right = Node(5)
n2.left.right = Node(6)
n2.right.right.left = Node(8)
n2.right.right.right  = Node(7)
 
print "Yes it's isomorphic" if (isIsomorphic(n1, n2) == True) else "No it's NOT isomorphic"
 
root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)

print "\n\t\t Inorder Tree Traversal\n"
inorder(root)

# Static variable pre for function fixPrevPtr
fixPrevPtr.pre = None
head = BTToDLL(root)

print "\n\n\t\tDLL Traversal\n"
printList(head)

extractLeafList.head = Node(None)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.left.left = Node(7)
root.left.left.right = Node(8)
root.right.right.left = Node(9)
root.right.right.right = Node(10)
 
print "\nInorder traversal of given tree is:"
printInorder(root)
 
root = extractLeafList(root)

print "\nExtract Double Linked List is:"
printDLL(extractLeafList.head)

print "\nInorder traversal of modified tree is:"
printInorder(root)

# 
# Read these
# https://www.geeksforgeeks.org/splay-tree-set-1-insert/
# https://www.geeksforgeeks.org/splay-tree-set-2-insert-delete/
# https://www.geeksforgeeks.org/b-tree-set-1-introduction-2/
# https://www.geeksforgeeks.org/b-tree-set-1-insert-2/
# https://www.geeksforgeeks.org/b-tree-set-3delete/
# https://www.geeksforgeeks.org/custom-tree-problem/
# https://www.geeksforgeeks.org/tournament-tree-and-binary-heap/
# https://www.geeksforgeeks.org/decision-trees-fake-coin-puzzle/
# https://www.geeksforgeeks.org/construct-full-k-ary-tree-preorder-traversal/
# https://www.geeksforgeeks.org/custom-tree-problem/
# https://www.geeksforgeeks.org/tournament-tree-and-binary-heap/
# https://www.geeksforgeeks.org/decision-trees-fake-coin-puzzle/
# https://www.geeksforgeeks.org/linked-complete-binary-tree-its-creation/
#
#

root = Node(12)
root.left = Node(5)
root.left.left = Node(3)
root.left.right = Node(9)
root.left.left.left = Node(1)
root.left.right.left = Node(2)
 
if(check(root)):
    print "Leaves are at same level"
else:
    print "Leaves are not at same level"

print "%d is the required difference" %(getLevelDiff(root))

root = Node(8)
root.left = Node(4)
root.right = Node(12)
root.left.left = Node(2)
root.left.right = Node(6)
root.right.left = Node(10)
root.right.right = Node(14)
 
for i in range(16):
    print "%d %d" %(i, ceil(root, i))

if (isCompleteBT(root)):
    print "\nComplete Binary Tree"
else:
    print "\nNOT Complete Binary Tree"

print ("Inorder traversal before conversion is :");
printInorder(root);
convertTree(root);
print ("");
print ("Inorder traversal after conversion is :");
printInorder(root);

root = Node(10)
root.left = Node(30)
root.right = Node(15)
root.left.left = Node(20)
root.right.right= Node(5)
 
# Convert binary tree to BST 
binaryTreeToBST(root)
 
print "Following is the inorder traversal of the converted BST"
printInorder(root)

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

if areIdentical(root1, root2):
    print "\nBoth trees are identical"
else:
    print "\nTrees are not identical"

""" TREE 1
     Construct the following tree
              26
            /   \
          10     3
        /    \     \
      4      6      3
       \
        30
    """
 
T = Node(26)
T.right = Node(3)
T.right.right  = Node(3)
T.left = Node(10)
T.left.left = Node(4)
T.left.left.right = Node(30)
T.left.right = Node(6)
 
""" TREE 2
     Construct the following tree
          10
        /    \
      4      6
       \
        30
    """
S = Node(10)
S.right = Node(6)
S.left = Node(4)
S.left.right = Node(30)
 
if isSubtree(T, S):
    print "\n\nTree 2 is subtree of Tree 1"
else :
    print "\n\nTree 2 is not a subtree of Tree 1"

print "printing bst keys in the given range: ",
k1 = 10
k2 = 25
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
 
Print(root, k1, k2)

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
 
if (isBST(root)):
    print "\nIs BST"
else:
    print "\nNot a BST"

root = Node(10);
root.left = Node(8);
root.right = Node(2);
root.left.left = Node(3);
root.left.right = Node(5);
root.right.right = Node(2);

if (isSumProperty(root) != 0):
    print "The given tree satisfies children sum property"
else:
    print "The given tree does not satisfy children sum property"
	
if IsFoldable(root):
    print "Tree is foldable"
else:
    print "Tree is NOT foldable"

doubleTree(root)
print "Inorder traversal of double tree is : "
printInorder(root)
	
k = 45
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(12)
root.right.right.left = Node(10)
root.right.right.left.right = Node(11)
root.left.left.right.left = Node(13)
root.left.left.right.right = Node(14)
root.left.left.right.right.left = Node(15)

print ("Tree before truncation\n")
printInorder(root)						# 8 4 13 9 15 14 2 12 5 1 6 3 10 11 7  

root = prune(root, k)
print("\n\nTree after truncation\n");
printInorder(root)						# 4 9 15 14 2 1

root = None
root=insert2BST(root, 50)
insert2BST(root, 30);
insert2BST(root, 20);
insert2BST(root, 40);
insert2BST(root, 70);
insert2BST(root, 60);
insert2BST(root, 80);
print "printing BST..."
printInorder(root)
print "\nModifying BST"
modifyBST(root)
printInorder(root)

pre = [ 1, 2, 4, 8, 9, 5, 3, 6, 7 ]
post = [ 8, 9, 4, 5, 2, 6, 7, 3, 1 ]
 
size = len(pre)
root = constructTree(pre, post, size)
print ("Inorder traversal of the constructed tree:")
printInorder(root)

inorder = [5, 10, 40, 30, 28]
length = len(inorder)
root = None
mynode = buildTree(inorder, 0, length-1, root)
print "Inorder traversal of the constructed tree is "
printInorder(mynode)

'''   
		 6
        /  \
       10    2
      / \   / \
     1   3 7  12
     10 and 2 are swapped
'''
 
root = Node(6);
root.left        = Node(10);
root.right       = Node(2);
root.left.left  = Node(1);
root.left.right = Node(3);
root.right.right = Node(12);
root.right.left = Node(7);
print ("Inorder Traversal of the original tree \n");
printInorder(root);									# 1 10 3 6 7 2 12
correctBST(root);
print ("\nInorder Traversal of the fixed tree \n");
printInorder(root);									# 1 2 3 6 7 10 12

root = None
pre = [10, 30, 20, 5, 15]
preLN = ['N', 'N', 'L', 'L', 'L']
n = len(pre)
mynode = constructTreeSpecial(pre, preLN, n, root)
print ("Following is Inorder Traversal of the Constructed Binary Tree: ")
printInorder(mynode)

pre = [8, 3, 5, 7, 6]
size = len(pre)
if (hasOnlyOneChild(pre, size) is True):
    print "Yes"
else:
    print "No"

inOrder = [4, 2, 5, 1, 3, 6]
pre =  [1, 2, 4, 5, 3, 6]
n = len(inOrder)
print "Postorder traversal "
printPostOrderFromInOrderAndPreOrder(inOrder, pre, n)

root = Node(20);
root.left                = Node(8);
root.left.left          = Node(4);
root.left.right         = Node(12);
root.left.right.left   = Node(10);
root.left.right.right  = Node(14);
root.right               = Node(22);
root.right.right        = Node(25);
 
print ("Size of the Largest Independent Set is %d ", LISS(root))


