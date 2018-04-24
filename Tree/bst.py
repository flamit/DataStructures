'''
Binary Search Tree | Set 1 (Search and Insertion)

The following is definition of Binary Search Tree(BST) according to Wikipedia

Binary Search Tree, is a node-based binary tree data structure which has the following properties:
> The left subtree of a node contains only nodes with keys less than the nodeâ€™s key.
> The right subtree of a node contains only nodes with keys greater than the nodeâ€™s key.
> The left and right subtree each must also be a binary search tree.
> There must be no duplicate nodes.

The above properties of Binary Search Tree provide an ordering among keys so that the operations like search, minimum and maximum can be done fast. If there is no ordering, then we may have to compare every key to search a given key.

Searching a key
 To search a given key in Bianry Search Tree, we first compare it with root, if the key is present at root, we return root. If key is greater than rootâ€™s key, we recur for right subtree of root node. Otherwise we recur for left subtree.

// C function to search a given key in a given BST
struct node* search(struct node* root, int key)
{
    // Base Cases: root is null or key is present at root
    if (root == NULL || root->key == key)
       return root;
   
    // Key is greater than root's key
    if (root->key < key)
       return search(root->right, key);

    // Key is smaller than root's key
    return search(root->left, key);
}

Insertion of a key
 A new key is always inserted at leaf. We start searching a key from root till we hit a leaf node. Once a leaf node is found, the new node is added as a child of the leaf node.
         100                               100
        /   \        Insert 40            /    \
      20     500    --------->          20     500 
     /  \                              /  \  
    10   30                           10   30

# Python program to demonstrate insert operation in binary search tree 

# A utility class that represents an individual node in a BST
'''
class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key

# A utility function to insert a new node with the given key
def insert(root,node):
	if root is None:
		root = node
	else:
		if root.val < node.val:
			if root.right is None:
				root.right = node
			else:
				insert(root.right, node)
		else:
			if root.left is None:
				root.left = node
			else:
				insert(root.left, node)

# A utility function to do inorder tree traversal
def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)


# Driver program to test the above functions
# Let us create the following BST
#      50
#    /	  \
#   30     70
#   / \    / \
#  20 40  60 80
r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))

# Print inoder traversal of the BST
inorder(r)
'''
# This code is contributed by Bhavya Jain

Output:
20
30
40
50
60
70
80

Time Complexity: The worst case time complexity of search and insert operations is O(h) where h is height of Binary Search Tree. In worst case, we may have to travel from root to the deepest leaf node. The height of a skewed tree may become n and the time complexity of search and insert operation may become O(n).

Asked in: Amazon, Microsoft

Some Interesting Facts:
> Inorder traversal of BST always produces sorted output.
> We can construct a BST with only Preorder or Postorder or Level Order traversal. Note that we can always get inorder traversal by sorting the only given traversal.
> Number of unique BSTs with n distinct keys is Catalan Number

Related Links:
> Binary Search Tree Delete Operation
> Quiz on Binary Search Tree
> Coding practice on BST
> All Articles on BST
'''
