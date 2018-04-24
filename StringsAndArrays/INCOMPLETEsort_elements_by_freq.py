'''
Sort elements by frequency | Set 2
Given an array of integers, sort the array according to frequency of elements. For example, if the input array is {2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12},
then modify the array to {3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5}. 

In the previous post, we have discussed all methods for sorting according to frequency. In this post, method 2 is discussed in detail and C++ implementation for the same is provided.

Following is detailed algorithm.
1) Create a BST and while creating BST maintain the count i.e. frequency of each coming element in same BST. This step may take O(nLogn) time if a self balancing BST is used.
2) Do Inorder traversal of BST and store every element and count of each element in an auxiliary array. Let us call the auxiliary array as count[].
  Note that every element of this array is element and frequency pair. This step takes O(n) time.
3) Sort count[] according to frequency of the elements. This step takes O(nLohn) time if a O(nLogn) sorting algorithm is used.
4) Traverse through the sorted array count[]. For each element x, print it freq times where freq is frequency of x. This step takes O(n) time.

Overall time complexity of the algorithm can be minimum O(nLogn) if we use a O(nLogn) sorting algorithm and use a self balancing BST with O(Logn) insert operation.
'''
# A BST node has data, freq, left and right pointers
class BSTNode:
    left = None
    right = None
    data = None
    freq = None

# A structure to store data and its frequency
class dataFreq:
    data = None
    freq = None
 
# Function for qsort() implementation. Compare frequencies to sort the array according to decreasing order of frequency
def compare(a, b):
    return ( b.freq - a.freq )

# Helper function that allocates a new node with the given data, frequency as 1 and NULL left and right pointers.
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.freq = 1

# A utility function to insert a given key to BST. If element is already present, then increases frequency
def insert(root, data):
    if (root is None):
        return Node(None)
    if (data == root.data): # If already presen
        root.freq += 1
    elif (data < root.data):
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root
 
# Function to copy elements and their frequencies to count[]
def store(root, count, index):
    if root is None:
        return

    store(root.left, count, index)
    
    count[index].freq = root.freq
    count[index].data = root.data
    index += 1

    store(root.right, count, index)
 
# The main function that takes an input array as an argument and sorts the array items according to frequency
def sortByFrequency(arr, n):
    root = Node(None)
    for i in xrange(0, n):
        root = insert(root, arr[i])
    index = 0
    df = dataFreq()
    count = [df]*n
    store(root, count, index)

    qsort(count, index, len(count[0]), compare)

    j = 0
    for i in xrange(0, index):
        for freq in reversed(xrange(1, count[i].freq)):
            arr[j]=count[i].data
            j+=1

arr = [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
print arr
n = len(arr)
sortByFrequency(arr, n)
print arr
'''
Output: 
3 3 3 3 2 2 2 12 12 5 4
'''
