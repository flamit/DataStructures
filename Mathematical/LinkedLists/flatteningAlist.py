class Node:
    def __init__(self, data):
        self.data = data 
        self.right = None
        self.down = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, head_ref, new_data):
        new_node = Node(new_data)                                                           # 1 & 2: Allocate the Node & Put in the data
        new_node.down = head_ref                                                            # 3. Make next of new Node as head
        head_ref = new_node                                                                 # 4. Move the head to point to new Node
        
        return head_ref

    # Flattening a Linked List
    '''
Given a linked list where every node represents a linked list and contains two pointers of its type:
 (i) Pointer to next node in the main list (we call it 'right' pointer in below code)
 (ii) Pointer to a linked list where this node is head (we call it 'down' pointer in below code).
 All linked lists are sorted. See the following example
       5 -> 10 -> 19 -> 28
       |    |     |     |
       V    V     V     V
       7    20    22    35
       |          |     |
       V          V     V
       8          50    40
       |                |
       V                V
       30               45


Write a function flatten() to flatten the lists into a single linked list. The flattened linked list should also be sorted. For example, for the above input list, output list should be 5->7->8->10->19->20->22->28->30->35->40->45->50.
Solution:
The idea is to use Merge() process of merge sort for linked lists. We use merge() to merge lists one by one. We recursively merge() the current list with already flattened list.
The down pointer is used to link nodes of the flattened list.
    '''
                                                                                                                # An utility function to merge two sorted linked lists
    def merge(self, a, b):
        if a is None:                                                                                           # if first linked list is empty then second is the answer
            return b
        
        if b is None:                                                                                           # if second linked list is empty then first is the result
            return a
        
        result = ""                                                                                             # compare the data members of the two lonked lists and put the larger one in the result
        if (a.data < b.data):
            result = a
            result.down =  self.merge(a.down, b)
        else:
            result = b
            result.down = self.merge(a, b.down)
        return result
    
    def flatten(self, root):
        if (root is None or root.right is None):
            return root
        
        root.right = self.flatten(root.right)
        root = self.merge(root, root.right)
        
        return root

    def printList(self):
        temp = self.head
        while (temp):
            print temp.data,
            temp = temp.down

if __name__ == "__main__":
        L = LinkedList();
 
        ''' Let us create the following linked list
            5 -> 10 -> 19 -> 28
            |    |     |     |
            V    V     V     V
            7    20    22    35
            |          |     |
            V          V     V
            8          50    40
            |                |
            V                V
            30               45
        '''
 
        L.head = L.push(L.head, 30);
        L.head = L.push(L.head, 8);
        L.head = L.push(L.head, 7);
        L.head = L.push(L.head, 5);
 
        L.head.right = L.push(L.head.right, 20);
        L.head.right = L.push(L.head.right, 10);
 
        L.head.right.right = L.push(L.head.right.right, 50);
        L.head.right.right = L.push(L.head.right.right, 22);
        L.head.right.right = L.push(L.head.right.right, 19);
 
        L.head.right.right.right = L.push(L.head.right.right.right, 45);
        L.head.right.right.right = L.push(L.head.right.right.right, 40);
        L.head.right.right.right = L.push(L.head.right.right.right, 35);
        L.head.right.right.right = L.push(L.head.right.right.right, 20);
 
        #flatten the list
        L.head = L.flatten(L.head);
        L.printList()
'''
Flatten a multilevel linked list

Given a linked list where in addition to the next pointer, each node has a child pointer, which may or may not point to a separate list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in below figure.You are given the head of the first level of the list. Flatten the list so that all the nodes appear in a single-level linked list. You need to flatten the list in way that all nodes at first level should come first, then nodes of second level, and so on.

Each node is a C struct with the following definition.

struct List
{
    int data;
    struct List *next;
    struct List *child;
};
 
https://www.geeksforgeeks.org/flatten-a-linked-list-with-next-and-child-pointers/

class LinkedList {
     
    static Node head;
     
    class Node {
         
        int data;
        Node next, child;
         
        Node(int d) {
            data = d;
            next = child = null;
        }
    }
 
    // A utility function to create a linked list with n nodes. The data
    // of nodes is taken from arr[].  All child pointers are set as NULL
    Node createList(int arr[], int n) {
        Node node = null;
        Node p = null;
         
        int i;
        for (i = 0; i < n; ++i) {
            if (node == null) {
                node = p = new Node(arr[i]);
            } else {
                p.next = new Node(arr[i]);
                p = p.next;
            }
            p.next = p.child = null;
        }
        return node;
    }
 
    // A utility function to print all nodes of a linked list
    void printList(Node node) {
        while (node != null) {
            System.out.print(node.data + " ");
            node = node.next;
        }
        System.out.println("");
    }
     
    Node createList() {
        int arr1[] = new int[]{10, 5, 12, 7, 11};
        int arr2[] = new int[]{4, 20, 13};
        int arr3[] = new int[]{17, 6};
        int arr4[] = new int[]{9, 8};
        int arr5[] = new int[]{19, 15};
        int arr6[] = new int[]{2};
        int arr7[] = new int[]{16};
        int arr8[] = new int[]{3};
 
        /* create 8 linked lists */
        Node head1 = createList(arr1, arr1.length);
        Node head2 = createList(arr2, arr2.length);
        Node head3 = createList(arr3, arr3.length);
        Node head4 = createList(arr4, arr4.length);
        Node head5 = createList(arr5, arr5.length);
        Node head6 = createList(arr6, arr6.length);
        Node head7 = createList(arr7, arr7.length);
        Node head8 = createList(arr8, arr8.length);
 
        /* modify child pointers to create the list shown above */
        head1.child = head2;
        head1.next.next.next.child = head3;
        head3.child = head4;
        head4.child = head5;
        head2.next.child = head6;
        head2.next.next.child = head7;
        head7.child = head8;
 
        /* Return head pointer of first linked list.  Note that all nodes are
         reachable from head1 */
        return head1;
    }
 
    /* The main function that flattens a multilevel linked list */
    void flattenList(Node node) {
         
        /*Base case*/
        if (node == null) {
            return;
        }
         
        Node tmp = null;
 
        /* Find tail node of first level linked list */
        Node tail = node;
        while (tail.next != null) {
            tail = tail.next;
        }
 
        // One by one traverse through all nodes of first level
        // linked list till we reach the tail node
        Node cur = node;
        while (cur != tail) {
 
            // If current node has a child
            if (cur.child != null) {
 
                // then append the child at the end of current list
                tail.next = cur.child;
 
                // and update the tail to new last node
                tmp = cur.child;
                while (tmp.next != null) {
                    tmp = tmp.next;
                }
                tail = tmp;
            }
 
            // Change current node
            cur = cur.next;
        }
    }
     
    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        head = list.createList();
        list.flattenList(head);
        list.printList(head);
    }
}
Output: 10 5 12 7 11 4 20 13 17 6 2 16 9 8 3 19 15

Time Complexity: Since every node is visited at most twice, the time complexity is O(n) where n is the number of nodes in given linked list.

'''
