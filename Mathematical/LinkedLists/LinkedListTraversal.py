'''
Advantages over arrays
1) Dynamic size
2) Ease of insertion/deletion

Drawbacks:
1) Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do binary search with linked lists.
2) Extra memory space for a pointer is required with each element of the list.
'''
class Node:
 
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
 
 
# Linked List class contains a Node object
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # This function prints contents of linked list starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print temp.data,
            temp = temp.next

    # Function to print nodes in a given circular linked list
    def printCircularList(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print "%d" %(temp.data),
                temp = temp.next
                if (temp == self.head):
                    break
                
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)                                       # 1 & 2: Allocate the Node & Put in the data
        new_node.next = self.head                                       # 3. Make next of new Node as head
        self.head = new_node                                            # 4. Move the head to point to new Node

    #Inserts a new node after the given prev_node.
    def insertAfter(self, prev_node, new_data):
 
        if prev_node is None:                                           # 1. check if the given prev_node exists
            print "The given previous node must inLinkedList."
            return
        
        new_node = Node(new_data)                                       #  2. create new node & Put in the data
        new_node.next = prev_node.next                                  # 4. Make next of new Node as next of prev_node
        prev_node.next = new_node                                       # 5. make next of prev_node as new_node

    # Insert at end
    def append(self, new_data):
        
        new_node = Node(new_data)
 
        if self.head is None:                                           # If the Linked List is empty, then make the new node as head
            self.head = new_node
            return
        
        last = self.head                                                # Else traverse till the last node
        while (last.next):
            last = last.next
        
        last.next =  new_node

    # Returns data at given index in linked list
    def getNth(self, index):
        current = self.head
        count = 0
 
        # Loop while end of linked list is not reached
        while (current):
            if (count == index):
                return current.data
            count += 1
            current = current.next
 
        # if we get to this line, the caller was asking
        # for a non-existent element so we assert fail
        assert(false)
        return 0


    '''Method 2 (Use two pointers)
    Maintain two pointers - reference pointer and main pointer. Initialize both reference and main pointers to head. First move reference pointer to n nodes from head.
    Now move both pointers one by one until reference pointer reaches end. Now main pointer will point to nth node from the end. Return main pointer.'''
    '''
    # My solution
    def printNthFromLast2(self, n):
        fast_ptr = self.head
        slow_ptr = self.head

        count = 0
        while fast_ptr and count < n:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next.next
            count += 1

        while slow_ptr:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        print fast_ptr.data
    '''
    def printNthFromLast(self, n):
        main_ptr = self.head
        ref_ptr = self.head 
     
        count  = 0
        if(self.head is not None):
            while(count < n ):
                if(ref_ptr is None):
                    print "%d is greater than the no. pf \
                            nodes in list" %(n)
                    return
  
                ref_ptr = ref_ptr.next
                count += 1
 
        while(ref_ptr is not None):
            main_ptr = main_ptr.next
            ref_ptr = ref_ptr.next
 
        print "Node no. %d from last is %d " %(n, main_ptr.data)
 
   # Function to print/get middle of linked list
    def getMiddle(self, head):
        if head is None:
            return head
        fast_ptr = head.next
        slow_ptr = head

        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        print "The middle element is %d\n" %(slow_ptr.data)
        return slow_ptr
    
    '''Given only a pointer to a node to be deleted in a singly linked list, how do you delete it?'''
    def deleteNode(self, node):
        temp = node.next;
        node.data = temp.data;
        node.next = temp.next

    # Delete N nodes after M nodes of a linked list
    '''
Input:
M = 2, N = 2
Linked List: 1->2->3->4->5->6->7->8
Output:
Linked List: 1->2->5->6

Input:
M = 3, N = 2
Linked List: 1->2->3->4->5->6->7->8->9->10
Output:
Linked List: 1->2->3->6->7->8

Input:
M = 1, N = 1
Linked List: 1->2->3->4->5->6->7->8->9->10
Output:
Linked List: 1->3->5->7->9
    '''
    def skipMdeleteN(self, M, N):
        curr = self.head
        
        while(curr):
            for count in range(1, M):                   # Skip M nodes
                if curr is None:
                    return
                curr = curr.next
                     
            if curr is None :
                return
            
            t = curr.next                               # Start from next node and delete N nodes
            for count in range(1, N+1):
                if t is None:
                    break
                t = t.next
                
            curr.next = t                               # Link the previous list with reamining nodes
            curr = t                                    # Set Current pointer for next iteration
    '''
    Write a function to delete a Linked List
    Time Complexity: O(n)
    Auxiliary Space: O(1)
    '''
    def deleteLinkedList(self, node):
        self.head = None
        
    # Function to reverse the linked list. Iterate trough the linked list. In loop, change next to prev, prev to current and current to next.
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # The above and this one, both are same. Only difference is this one accepts parameter while the above doesn't
    def reverse2(self, head):
        prev = None
        current = head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev
    
    # Print reverse without reversing it. Reverse using recursion; Time Complexit: O(n)
    def printReverse(self, head):
        if head is None:
            return
        
        self.printReverse(head.next)
        print head.data,                                      # After everything else is printed

    '''
    Reverse a Linked List in groups of given size
    Given a linked list, write a function to reverse every k nodes (where k is an input to the function). 
    Example:
    Inputs:  1->2->3->4->5->6->7->8->NULL and k = 3 
    Output:  3->2->1->6->5->4->8->7->NULL. 

    Inputs:   1->2->3->4->5->6->7->8->NULL and k = 5
    Output:  5->4->3->2->1->8->7->6->NULL.
    Time Complexity: O(n) where n is the number of nodes in the given list.
    For reversing alternate nodes in a singly linked list(https://www.geeksforgeeks.org/reverse-alternate-k-nodes-in-a-singly-linked-list/) pass k=2
    '''
    def reverseKnodes(self, head, k):
        current = head
        next  = None
        prev = None
        count = 0     
                                                                    # Reverse first k nodes of the linked list
        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
            
        if next is not None:                                        # next is now a pointer to (k+1)th node recursively call for the list starting from current . And make rest of the list as next of first node
            head.next = self.reverseKnodes(next, k)
        return prev

    '''Given a linked list, reverse alternate nodes and append at the end
    Time Complexity: The above code simply traverses the given linked list. So time complexity is O(n)
    Auxiliary Space: O(1)
    Input List:  1->2->3->4->5->6
    Output List: 1->3->5->6->4->2

    Input List:  12->14->16->18->20
    Output List: 12->16->20->18->14'''
    def rearrange(self):                                            # If linked list has less than 3 nodes, no change is required 
        odd = self.head
        if (odd is None or odd.next is None or
            odd.next.next is None):
            return
        
        even = odd.next                                             # Even points to the beginning of even list
        odd.next = odd.next.next                                    # Remove the first even node
        odd = odd.next                                              # Odd points to next node in odd list
        even.next = None                                            # Set terminator for even list
        
        while (odd and odd.next):
            temp = odd.next.next                                    # Store the next node in odd list
            odd.next.next = even                                    # Link the next even node at the beginning of even list
            even = odd.next
            odd.next = temp                                         # Remove the even node from middle
            
            if temp is not None:                                    # Move odd to the next odd node
                odd = temp
 
        odd.next = even                                             # Append the even list at the end of odd list

    # This is not working; check it again; https://www.geeksforgeeks.org/alternating-split-of-a-given-singly-linked-list/
    def AlternatingSplit(self, a, b):
        current = self.head
        while (current is not None):
            self.MoveNode(a.head, current)
            if (current is not None):
                self.MoveNode(b.head, current)

    def MoveNode(self, destRef, sourceRef):
        if sourceRef is None:
            return
        if destRef is None:
            return
        newNode = sourceRef
        sourceRef = newNode.next
        newNode.next = destRef
        destRef = newNode

    '''Floyd's Cycle-Finding Algorithm:
        This is the fastest method. Traverse linked list using two pointers.  Move one pointer by one and other pointer by two.
        If these pointers meet at some node then there is a loop.  If pointers do not meet then linked list doesn't have loop.
    Time Complexity: O(n)
    Auxiliary Space: O(1)'''
    def detectLoop(self):
        slow_p = fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                print "\nFound Loop"
                return 1                                                # Return 1 to indicate that loop if found
        return 0                                                        # Return 0 to indicate that there is no loop
            
    def detectAndRemoveLoop(self):
        slow_p = fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                self.removeLoop(slow_p)
                print "\nFound Loop"
                return 1
        return 0
    
    def removeLoop(self, loop_node):
        ptr1 = self.head                                                # Set a pointer to the beginning of the linked list and move it one by one to find the first node which is part of the linked list
        while(1):
            ptr2 = loop_node                                            # Now start a pointer from loop_node and check if it ever reaches ptr2
            while(ptr2.next!= loop_node and ptr2.next !=ptr1):
                ptr2 = ptr2.next
                
            if ptr2.next == ptr1:                                       # If ptr2 reached ptr1 then there is a loop. So break the loop
                break
            
            ptr1 = ptr1.next                                            # After the end of loop ptr2 is the lsat node of the loop. So make next of ptr2 as NULL
        ptr2.next = None
'''            
    # Detect and Remove Loop in a Linked List; Optimized solution
    def detectAndRemoveLoop(self):
        if self.head is None :
            return
        if self.head.next is None :
            return

        slow_p = self.head
        fast_p = self.head

        slow_p = slow_p.next
        fast_p = fast_p.next.next
        
        while(fast_p is not None):
            if fast_p.next is None:
                break
            if slow_p == fast_p :
                break

            slow_p = slow_p.next
            fast_p = fast_p.next.next
                                                                                                    # if loop exists
        if slow_p == fast_p :
            slow_p = self.head
            while (slow_p.next != fast_p.next):
                slow_p = slow_p.next
                fast_p = fast_p.next
                                                                                                    # Sinc fast.next is the looping point
            fast_p.next = None                                                                       # Remove loop
'''
    # Counts the no of occurances of a node (search_for) in a linkded list (head) Time Complexity: O(n) Auxiliary Space: O(1)
    def count(self, search_for):
        current = self.head
        count = 0
        while(current is not None):
            if current.data == search_for:
                count += 1
            current = current.next
        return count
    
    # Remove duplicates from an unsorted linked list Time Complexity: O(n) on average (assuming that hash table access time is O(1) on average).
    def removeDuplicate(self):
        D = dict()
        current = self.head
        prev = None
        while current:
            curval = current.data
            if curval not in D:
                D[curval] = 1
                prev = current
            else:
                D[curval] += 1
                prev.next = current.next

            current = current.next
            
    # Remove duplicates from a sorted linked list; Time Complexity: O(n) where n is number of nodes in the given linked list.
    def removeDuplicatesFromSortedLL(self):
        current = self.head
        while current.next != None:
            if current.data == current.next.data:
                next_next = current.next.next
                current.next = None
                current.next = next_next
            else:
                current = current.next

    # Given a linked list which is sorted, how will you insert in sorted way; Time Complexity: O(n)
    def sortedInsert(self, new_node):      
        if self.head is None:                           # Special case for the empty linked list
            new_node.next = self.head
            self.head = new_node
        elif self.head.data >= new_node.data:           # Special case for head at end
            new_node.next = self.head
            self.head = new_node
        else :                                          # Locate the node before the point of insertion
            current = self.head
            while(current.next is not None and current.next.data < new_node.data):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    # Given a circular linked list which is sorted, how will you insert in sorted way; Time Complexity: O(n)
    def sortedInsertInCircularLinkedList(self, new_node):      
        if self.head is None:                           
            new_node.next = self.head
            self.head = new_node
        elif self.head.data >= new_node.data:           
            new_node.next = self.head
            self.head = new_node
        else :                                          
            current = self.head
            while(current.next != current and current.next.data < new_node.data):   # Note the difference here "current.next != current" instead of "current.next is not None"
                current = current.next
            new_node.next = current.next
            current.next = new_node

    # This function rotates a linked list counter-clockwise and 
    # updates the head. The function assumes that k is smaller
    # than size of linked list. It doesn't modify the list if
    # k is greater than of equal to size Time complexity: O(n)
    def rotate(self, k):
        if k == 0: 
            return
         
        # Let us understand the below code for example k = 4
        # and list = 10->20->30->40->50->60
        current = self.head
         
        # current will either point to kth or NULL after
        # this loop
        # current will point to node 40 in the above example
        count = 1
        while(count <k and current is not None):
            current = current.next
            count += 1
     
        # If current is None, k is greater than or equal 
        # to count of nodes in linked list. Don't change
        # the list in this case
        if current is None:
            return
 
        # current points to kth node. Store it in a variable
        # kth node points to node 40 in the above example
        kthNode = current 
     
        # current will point to lsat node after this loop
        # current will point to node 60 in above example
        while(current.next is not None):
            current = current.next
 
        # Change next of last node to previous head
        # Next of 60 is now changed to node 10
        current.next = self.head
         
        # Change head to (k+1)th node
        # head is not changed to node 50
        self.head = kthNode.next
 
        # change next of kth node to NULL 
        # next of 40 is not NULL 
        kthNode.next = None

    # Add contents of two linked lists and return the head
    # node of resultant list; Time Complexity: O(m + n) where m and n are number of nodes in first and second lists respectively.
    # See this too https://www.geeksforgeeks.org/sum-of-two-linked-lists/
    def addTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0
 
        # While both list exists
        while(first is not None or second is not None):
 
            # Calculate the value of next digit in
            # resultant list
            # The next digit is sum of following things
            # (i) Carry
            # (ii) Next digit of first list (if ther is a
            # next digit)
            # (iii) Next digit of second list ( if there
            # is a next digit)
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            Sum = carry + fdata + sdata
 
            # update carry for next calculation
            carry = 1 if Sum >= 10 else 0
 
            # update sum if it is greater than 10
            Sum = Sum if Sum < 10 else Sum % 10
 
            # Create a new node with sum as data
            temp = Node(Sum)
 
            # if this is the first node then set it as head
            # of resultant list
            if self.head is None:
                self.head = temp
            else :
                prev.next = temp 
 
            # Set prev for next insertion
            prev = temp
 
            # Move first and second pointers to next nodes
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next
 
        if carry > 0:
            temp.next = Node(carry)

    # Function to pairwise swap elements of a linked list; Time complexity: O(n)
    def pairwiseSwap(self):
        temp = self.head
        if temp is None:
            return
        
        while(temp is not None and temp.next is not None):
            temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next.next

    # Function to split a list (starting with head) into 
    # two lists. head1 and head2 are the head nodes of the
    # two resultant linked lists
    def splitList(self, head1, head2):
        slow_ptr = self.head 
        fast_ptr = self.head
     
        if self.head is None:
            return
         
        # If htere are odd nodes in the circular list then
        # fast_ptr->next becomes head and for even nodes
        # fast_ptr->next->next becomes head
        while(fast_ptr.next != self.head and
            fast_ptr.next.next != self.head ):
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
 
        # If there are event elements in list then
        # move fast_ptr
        if fast_ptr.next.next == self.head:
            fast_ptr = fast_ptr.next
 
        # Set the head pointer of first half
        head1.head = self.head
 
        # Set the head pointer of second half
        if self.head.next != self.head:
            head2.head = slow_ptr.next
 
        # Make second half circular
        fast_ptr.next = slow_ptr.next
     
        # Make first half circular
        slow_ptr.next = self.head

    # Main function that inserts nodes of linked list q into p at alternate positions. Since head of first list never changes and head of second list/ may change, we need single pointer for first list and double pointer for second list.
    # For example, if first list is 5->7->17->13->11 and second is 12->10->2->4->6, the first list should become 5->12->7->10->17->2->13->4->11->6 and second list should become empty. The nodes of second list should only be inserted when there are positions available.
    # For example, if the first list is 1->2->3 and second list is 4->5->6->7->8, then first list should become 1->4->2->5->3->6 and second list to 7->8.
    def merge(self, q):
        p_curr = self.head
        q_curr = q.head
 
        # While there are available positions in p;
        while p_curr != None and q_curr != None:
 
            # Save next pointers
            p_next = p_curr.next
            q_next = q_curr.next
 
            # make q_curr as next of p_curr
            q_curr.next = p_next # change next pointer of q_curr
            p_curr.next = q_curr # change next pointer of p_curr
 
            # update current pointers for next iteration
            p_curr = p_next
            q_curr = q_next
        q.head = q_curr

    '''
        Time Complexity: O(n) where n is number of nodes in linked list.
        Auxiliary Space: O(1)
    '''
    def sortList(self):
 
        # initialise count of 0 1 and 2 as 0
        count = [0, 0, 0]
 
        ptr = self.head
 
        # count total number of '0', '1' and '2'
        # * count[0] will store total number of '0's
        # * count[1] will store total number of '1's
        # * count[2] will store total number of '2's  
        while ptr != None:
            count[ptr.data]+=1
            ptr = ptr.next
 
        i = 0
        ptr = self.head
 
        # Let say count[0] = n1, count[1] = n2 and count[2] = n3
        # * now start traversing list from head node,
        # * 1) fill the list with 0, till n1 > 0
        # * 2) fill the list with 1, till n2 > 0
        # * 3) fill the list with 2, till n3 > 0  
        while ptr != None:
            if count[i] == 0:
                i+=1
            else:
                ptr.data = i
                count[i]-=1
                ptr = ptr.next

    # deletes alternate nodes of a list starting with head; Time Complexity: O(n)
    def deleteAlt(self, head):
        if head is None:
            return
        node = head.next

        if node is None:
            return
        head.next = node.next
        self.deleteAlt(head.next)

    # Move last element to front of a given Linked List; Time Complexity: O(n) where n is the number of nodes in the given Linked List.
    def moveToFront(self):
        if self.head is None or self.head.next is None:
           return
        secLast = None
        last = self.head
                                                                                                # After this loop secLast contains address of second last  node and last contains address of last node in Linked List
        while (last.next != None):
           secLast = last
           last = last.next
           
        secLast.next = None
        last.next = self.head
        self.head = last
        
    # Returns true if linked lists a and b are identical,otherwise false
    # Time Complexity: O(n) for both iterative and recursive versions(next the solution below). n is the length of the smaller list among a and b.
    # Recursive solution code is much cleaner than the iterative code.
    # You probably wouldn't want to use the recursive version for production code however, because it will use stack space which is proportional to the length of the lists
    def areIdentical(self, listA, listB):
        a = listA.head
        b = listB.head;
        while (a is not None and b is not None):
            if (a.data != b.data):
                return False
            a = a.next                                  # If we reach here, then a and b are not null and their data is same, so move to next nodes in both lists
            b = b.next        
        return (a is None and b is None)                # If linked lists are identical, then 'a' and 'b' must be null at this point.

    '''
    def areIdentical(self, listA, listB):
        return areIdenticalRecur(listA.head, listB.head)
    
    def areIdenticalRecur(self, a, b):
        if (a is None and b is None):
            return True
        if (a is not None and b is not None):
            return (a.data == b.data) and self.areIdenticalRecur(a.next, b.next)
        return False
    '''

    # Function to check if given linked list is palindrome or not
    '''
METHOD 2 (By reversing the list)
 This method takes O(n) time and O(1) extra space.
1) Get the middle of the linked list.
2)  Reverse the second half of the linked list.
3) Check if the first half and second half are identical.
4)  Construct the original linked list by reversing the second half again and attaching it back to the first half

To divide the list in two halves, method 2 of this post is used.
 When number of nodes are even, the first and second half contain exactly half nodes. The challenging thing in this method is to handle the case when number of nodes are odd.
 We don't want the middle node as part of any of the lists as we are going to compare them for equality. For odd case, we use a separate variable 'midnode'. 
    '''
    def isPalindrome(self, head):
        slow_ptr = head
        fast_ptr = head
        prev_of_slow_ptr = head
        midnode = None              # To handle odd size list
        res = True                  #initialize result
 
        if (head is not None and head.next is not None):                        # Get the middle of the list. Move slow_ptr by 1 and fast_ptrr by 2, slow_ptr will have the middle node
            while (fast_ptr is not None and fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next                                   # We need previous of the slow_ptr for linked lists  with odd elements
                prev_of_slow_ptr = slow_ptr
                slow_ptr = slow_ptr.next
                
            if (fast_ptr is not None):
                midnode = slow_ptr;                                             # fast_ptr would become NULL when there are even elements in the list and not NULL for odd elements.
                slow_ptr = slow_ptr.next;                                       # We need to skip the middle node for odd case and store it somewhere so that we can restore the original list
                
            second_half = slow_ptr                                              # Now reverse the second half and compare it with first half
            prev_of_slow_ptr.next = None                                        # NULL terminate first half
            second_half = self.reverse2(second_half)                                                      # Reverse the second half
            res = self.compareLists(head, second_half)
            
            second_half = self.reverse2(second_half)                                                      # Reverse the second half again to construct the original list back
             
            if (midnode is not None):                                                       # If there was a mid node (odd size case) which was not part of either first half or second half.
                prev_of_slow_ptr.next = midnode
                midnode.next = second_half
            else:
                prev_of_slow_ptr.next = second_half
                
        return res
    '''
This can be done using recursion. 
METHOD 3 (Using Recursion)
 Use two pointers left and right. Move right and left using recursion and check for following in each recursive call.
 1) Sub-list is palindrome.
 2) Value at current left and right are matching.

If both above conditions are true then return true.
The idea is to use function call stack as container. Recursively traverse till the end of list. When we return from last NULL, we will be at last node.
The last node to be compared with first node of list.
In order to access first node of list, we need list head to be available in the last call of recursion. Hence we pass head also to the recursive function.
If they both match we need to compare (2, n-2) nodes. Again when recursion falls back to (n-2)nd node, we need reference to 2nd node from head.
We advance the head pointer in previous call, to refer to next node in the list.
However, the trick in identifying double pointer. Passing single pointer is as good as pass-by-value, and we will pass the same pointer again and again.
We need to pass the address of head pointer for reflecting the changes in parent recursive calls.
Time Complexity: O(n)
 Auxiliary Space: O(n) if Function Call Stack size is considered, otherwise O(1).
 '''
    
    # Function to check if two input lists have same data
    def compareLists(self, head1, head2):
        temp1 = head1
        temp2 = head2
 
        while (temp1 and temp2):
            if (temp1.data == temp2.data):
                temp1 = temp1.next
                temp2 = temp2.next
            else:
                return False
        if (temp1 is None and temp2 is None):                                   # Both are empty reurn 1
            return True
        
        return False                                                            # Will reach here when one is NULL and other is not

    # function to get the intersection point of two linked lists head1 and head2;    Time Complexity: O(m+n)    Auxiliary Space: O(1)
    '''
    Method 3(Using difference of node counts)
     1) Get count of the nodes in first list, let count be c1.
     2) Get count of the nodes in second list, let count be c2.
     3) Get the difference of counts d = abs(c1 - c2)
     4) Now traverse the bigger list from the first node till d nodes so that from here onwards both the lists have equal no of nodes.
     5) Then we can traverse both the lists in parallel till we come across a common node. (Note that getting a common node is done by comparing the address of the nodes)
     Also see https://www.geeksforgeeks.org/intersection-of-two-sorted-linked-lists/
     This solution should work for "intersection of two sorted linked lists" as well
    '''
    def getNode(self, head1, head2, c1, c2): 
        if (c1 > c2):
            d = c1 - c2
            return self._getIntesectionNode(d, head1, head2)
        else:
            d = c2 - c1
            return self._getIntesectionNode(d, head2, head1)

    # function to get the intersection point of two linked lists head1 and head2 where head1 has d more nodes than head2
    def _getIntesectionNode(self, d, node1, node2):
        current1 = node1
        current2 = node2
        for i in xrange(0, d):
            if current1 is None:
                return -1
            current1 = current1.next
            
        while (current1 is not None and current2 is not None):
            if (current1.data == current2.data):
                return current1.data
            current1 = current1.next
            current2 = current2.next
        return -1
    
    # Segregate even and odd in a linked list; Time complexity: O(n)
    def segregateEvenOdd(self):
        end = self.head
        prev = None
        curr = self.head

        while (end.next is not None):
            end = end.next
        new_end = end
        
        while (curr.data %2 !=0 and curr != end):               # Consider all odd nodes before getting first eve node
            new_end.next = curr
            curr = curr.next
            new_end.next.next = None
            new_end = new_end.next
            
        if (curr.data %2 ==0):                                  # do following steps only if there is an even node
            self.head = curr

            while (curr != end):
                if (curr.data % 2 == 0):
                    prev = curr;
                    curr = curr.next
                else:
                    prev.next = curr.next
                    curr.next = None
 
                    new_end.next = curr
                    new_end = curr
                    curr = prev.next
        else:
            prev = curr
 
        if (new_end != end and end.data %2 != 0):
            prev.next = end.next;
            end.next = None;
            new_end.next = end

    # Delete nodes which have a greater value on right side
    '''
    1. Reverse the list.
    2. Traverse the reversed list. Keep max till now.
        If next node < max, then delete the next node, otherwise max = next node.
    3. Reverse the list again to retain the original order. Time Complexity: O(n)
 
    Given Linked List
    12 15 10 11 5 6 2 3
    Modified Linked List
    15 11 6 3 
    '''
    def delLesserNodes(self):
        self.reverse()
        self._delLesserNodes()               # In the reversed list, delete nodes which have a node with greater value node on left side. Note that head node is never deleted because it is the leftmost node.
        self.reverse()

    # Deletes nodes which have greater value node(s) on left side
    def _delLesserNodes(self):
        current = self.head
        maxnode = self.head;
        temp = ""
 
        while (current is not None and current.next is not None):
            if (current.next.data < maxnode.data):
                temp = current.next;
                current.next = temp.next;
                temp = None
            else:
                current = current.next
                maxnode = current
                
    # A utility function that returns count of nodes in a given Linked List
    def countNodes(self):
        count = 0;
        temp = self.head
        while (temp):
            temp = temp.next
            count += 1
        return count

    # Sorted Linked List to Balanced BST
    '''
    Input:  Linked List 1->2->3
    Output: A Balanced BST 
         2   
       /  \  
      1    3
      
    Input: Linked List 1->2->3->4->5->6->7
    Output: A Balanced BST
            4
          /   \
         2     6
       /  \   / \
      1   3  4   7

      Method 1 (Simple)
     Following is a simple algorithm where we first find the middle node of list and make it root of the tree to be constructed.
        1) Get the Middle of the linked list and make it root.
        2) Recursively do same for left half and right half.
            a) Get the middle of left half and make it left child of the root
              created in step 1.
           b) Get the middle of right half and make it right child of the
              root created in step 1.
              
Time complexity: O(nLogn) where n is the number of nodes in Linked List.

Method 2 (Tricky) 
 The method 1 constructs the tree from root to leaves. In this method, we construct from leaves to root. The idea is to insert nodes in BST in the same order as the appear in Linked List, so that the tree can be constructed in O(n) time complexity. We first count the number of nodes in the given Linked List. Let the count be n. After counting nodes, we take left n/2 nodes and recursively construct the left subtree. After left subtree is constructed, we allocate memory for root and link the left subtree with root. Finally, we recursively construct the right subtree and link it with root.
 While constructing the BST, we also keep moving the list head pointer to next so that we have the appropriate pointer in each recursive call.

 Also see...
 In-place conversion of Sorted DLL to Balanced BST(https://www.geeksforgeeks.org/in-place-conversion-of-sorted-dll-to-balanced-bst/)
 The Doubly Linked List conversion is very much similar to this Singly Linked List problem and the method 1 is exactly same as the method 1 of previous post. Method 2 is also almost same. The only difference in method 2 is, instead of allocating new nodes for BST, we reuse same DLL nodes. We use prev pointer as left and next pointer as right.
    '''
    # This function counts the number of nodes in Linked List and then calls sortedListToBSTRecur() to construct BST
    def sortedListToBST(self):
        n = self.countNodes()                                       
        return self.sortedListToBSTRecur(n)                             # Construct BST
 
    # The main function that constructs balanced BST and returns root of it. n  --> No. of nodes in the Doubly Linked List
    def sortedListToBSTRecur(self, n):
        if (n <= 0):
            return None

        left = self.sortedListToBSTRecur(n / 2)                                         # Recursively construct the left subtree
        root = TNode(self.head.data)                                                    # head_ref now refers to middle node, make middle node as root of BST
        root.left = left
        self.head = self.head.next
        root.right = self.sortedListToBSTRecur(n - n / 2 - 1)                           # Recursively construct the right subtree and link it with root. The number of nodes in right subtree  is total nodes - nodes in left subtree - 1 (for root)
 
        return root

    def printPreOrder(self, root):
        if root is None:
            return
        print root.data,
        self.printPreOrder(root.left)
        self.printPreOrder(root.right)

    # Merge Sort for Linked Lists Time Complexity: O(n Log n)
    # Merge sort is often preferred for sorting a linked list. The slow random-access performance of a linked list makes some other algorithms (such as quicksort) perform poorly, and
    # others (such as heapsort) completely impossible.
    def mergeSort(self, h):
        if (h is None) or (h.next is None):                             # Base case : if head is null
            return h

        middle = self.getMiddle(h)
        nextofmiddle = middle.next

        middle.next = None                                              # set the next of middle node to null

        left = self.mergeSort(h)                                        # Apply mergeSort on left list
        right = self.mergeSort(nextofmiddle)                            # Apply mergeSort on right list
        sortedlist = mergeLists(left, right)                            # Merge the left and right lists
        return sortedlist

# Merge two lists
# Merge two sorted linked lists
def mergeLists(head1, head2):
    temp = None
    if head1 is None:                                   # List1 is empty then return List2
        return head2
    if head2 is None:                                   # if List2 is empty then return List1
        return head1
    
    if head1.data <= head2.data:                        # Again check List1's data is smaller or equal List2's data and call mergeLists function.
        temp = head1
        temp.next = mergeLists(head1.next, head2)
    else:
        temp = head2                                    # If List2's data is greater than or equal List1's data assign temp to head2
        temp.next = mergeLists(head1, head2.next)       # Again check List2's data is greater or equal List's data and call mergeLists function.
        
    return temp
'''
Merge two sorted linked lists
Write a SortedMerge() function that takes two lists, each of which is sorted in increasing order, and merges the two together into one list which is in increasing order. SortedMerge() should return the new list. The new list should be made by splicing
 together the nodes of the first two lists.

Merge is one of those nice recursive problems where the recursive solution code is much cleaner than the iterative code.
You probably wouldn't want to use the recursive version for production code however, because it will use stack space which is proportional to the length of the lists.
For example if the first linked list a is 5->10->15 and the other linked list b is 2->3->20, then SortedMerge() should return a pointer to the head node of the merged list 2->3->5->10->15->20.

Other two methods are:
Method 1 (Using Dummy Nodes)
 The strategy here uses a temporary dummy node as the start of the result list. The pointer Tail always points to the last node in the result list, so appending new nodes is easy.
 The dummy node gives tail something to point to initially when the result list is empty. This dummy node is efficient, since it is only temporary, and it is allocated in the stack.
 The loop proceeds, removing one node from either 'a' or 'b', and adding it to tail. When we are done, the result is in dummy.next.

 Method 2 (Using Local References)
 This solution is structurally very similar to the above, but it avoids using a dummy node. Instead, it maintains a struct node** pointer, lastPtrRef, that always points to the last pointer
 of the result list. This solves the same case that the dummy node did - dealing with the result list when it is empty.
 If you are trying to build up a list at its tail, either the dummy node or the struct node** "reference" strategy can be used (see Section 1 for details).
'''    
class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
li = LinkedList()
# Let us create a unsorted linked lists to test the functions Created lists shall be a: 2->3->20->5->10->15
li.push(15)
li.push(10)
li.push(5)
li.push(20)
li.push(3)
li.push(2)
print "Linked List without sorting is :", li.printList();
li.head = li.mergeSort(li.head)
print "\n Sorted Linked List is:", li.printList()

first = LinkedList()
second = LinkedList()
# Create first list
first.push(6)
first.push(4)
first.push(9)
first.push(5)
first.push(7)
print "First List is ",
first.printList()
 
# Create second list
second.push(4)
second.push(8)
print "\nSecond List is ",
second.printList()
 
# Add the two lists and see result
res = LinkedList()
res.addTwoLists(first.head, second.head)
print "\nResultant list is ",
res.printList()
           
if __name__=='__main__':
    llist = LinkedList()
    llist.push(7);
    llist.push(6);
    llist.push(5);
    llist.push(4);
    llist.push(3);
    llist.push(2);
    llist.push(1);
 
    print ("\nGiven Linked List ");
    llist.printList()
 
    root = llist.sortedListToBST();
    print ("\nPre-Order Traversal of constructed BST ");
    llist.printPreOrder(root)

    # Start with the empty list
    llist = LinkedList()
 
    llist.head  = Node(1)
    second = Node(2)
    third  = Node(3)
 
    llist.head.next = second; # Link first node with second
    second.next = third; # Link second node with the third node
    print ""
    llist.printList()
    
    llist.push(4)
    print "\nLinked list after new node(4) insertion is: ",
    llist.printList()

    llist.insertAfter(llist.head.next, 8)
    print "\nLinked list after new node(8) insertion is: ",
    llist.printList()
    
    llist.append(7)
    llist.append(8)
    llist.append(9)
    llist.append(10)
    print "\nLinked list after new node(7) append is: ",
    llist.printList()

    n = 3
    print ("Element at index 3 is :", llist.getNth(n))
    llist.printNthFromLast(n)

    llist.getMiddle(llist.head)
    print "\nLinked list before delete is: ",
    llist.printList()
    llist.deleteNode(llist.head.next.next.next)
    print "\nLinked list after delete is: ",
    llist.printList()

    llist.reverse()
    print "\nLinked list after reverse is: ",
    llist.printList()
    
    llist.pairwiseSwap()
    print  "\nLinked list after calling pairWiseSwap()",
    llist.printList()
    
    print "\nReversing the list again. Now it's using recursion. It's: ",
    llist.printReverse(llist.head)

    llist.rearrange()
    print "\nLinked list after calling  rearrange()"
    llist.printList()


    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(10)

    # Create a loop for testing
    llist.head.next.next.next.next = llist.head
    llist.detectLoop()
    llist = LinkedList()
    llist.head = Node(50)
    llist.head.next = Node(20)
    llist.head.next.next = Node(15)
    llist.head.next.next.next = Node(4)
    llist.head.next.next.next.next = Node(10)
    #Create a loop for testing
    llist.head.next.next.next.next.next =  llist.head.next.next


    llist.detectAndRemoveLoop()
    print "\nLinked List after removing looop: ", llist.printList()
    
    # 10->12->11->11->12->11->10
    llist = LinkedList()
    llist.head = Node(10)
    llist.head.next = Node(12)
    llist.head.next.next = Node(11)
    llist.head.next.next.next = Node(11);
    llist.head.next.next.next.next = Node(12);
    llist.head.next.next.next.next.next = Node(11);
    llist.head.next.next.next.next.next.next = Node(10);
    print ("Linked list before removing duplicates :");
    llist.printList()
    llist.removeDuplicate()
    print("\nLinked list after removing duplicates :")
    llist.printList()

    
    llist = LinkedList()
    llist.push(20)
    llist.push(13)
    llist.push(13)
    llist.push(11)
    llist.push(11)
    llist.push(11)
    print ("\nList :"), llist.printList()
    node12 = Node(12)
    llist.sortedInsert(node12)
    print ("\nList after sorted insert:"),llist.printList()
    llist.removeDuplicatesFromSortedLL()
    print ("\nList after removal of elements")
    llist.printList()
    llist.rotate(2)
    print "\nRotated Linked list"
    llist.printList()
    '''
      10->12->11->14->15->19->
      ^                      |
      |                      |
      |                      |
      -----------------------V
    '''    
    llist = LinkedList()
    llist.head = Node(10)
    llist.head.next = Node(12)
    llist.head.next.next = Node(11)
    llist.head.next.next.next = Node(14);
    llist.head.next.next.next.next = Node(15);
    llist.head.next.next.next.next.next = Node(19);
    llist.head.next.next.next.next.next.next = llist.head;
    print "Linked list before split is: ", llist.printCircularList()

    head1 = LinkedList()
    head2 = LinkedList()
    print ("Linked list after split is :")
    llist.splitList(head1, head2)
    head1.printCircularList()
    print ""
    head2.printCircularList()

    llist1 = LinkedList()
    llist2 = LinkedList()
    llist1.push(3)
    llist1.push(2)
    llist1.push(1)
 
    print "\nFirst Linked List:",
    llist1.printList()
 
    llist2.push(8)
    llist2.push(7)
    llist2.push(6)
    llist2.push(5)
    llist2.push(4)
 
    print "\nSecond Linked List:", 
    llist2.printList()
    llist1.merge(llist2)
 
    print "\nModified first linked list:",
    llist1.printList()
 
    print "\nModified second linked list:",
    llist2.printList()

# Create following linked list
# 1->2->3->4->5->6->7->8->9->10
llist = LinkedList()
M = 2
N = 3
llist.push(10)
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
 
print "M = %d, N = %d\nGiven Linked List is:" %(M, N)
llist.printList()
print
 
llist.skipMdeleteN(M, N)
 
print "\nLinked list after deletion is"
llist.printList()

llist = LinkedList()
llist.push(0)
llist.push(1)
llist.push(0)
llist.push(2)
llist.push(1)
llist.push(1)
llist.push(2)
llist.push(1)
llist.push(2)
 
print "Linked List before sorting"
llist.printList()
 
llist.sortList()
 
print "Linked List after sorting"
llist.printList()
llist.deleteAlt(llist.head)
print ""
llist.printList()

llist.moveToFront()
print("\nLinked List after moving last to front ")
llist.printList()

llist = LinkedList();
llist.push(5);
llist.push(4);
llist.push(11);
llist.push(9);
llist.push(8);
llist.push(3);
llist.push(0);
llist.push(10);
print("\nOrigional Linked List");
llist.printList();
llist.segregateEvenOdd();
print("\nModified Linked List");
llist.printList();

llist = LinkedList();
#Constructed Linked List is 12->15->10->11->5->6->2->3
llist.push(3);
llist.push(2);
llist.push(6);
llist.push(5);
llist.push(11);
llist.push(10);
llist.push(15);
llist.push(12);
print("\nGiven Linked List");
llist.printList();
llist.head = llist.reverseKnodes(llist.head, 2)
print "\nReversed Linked list"
llist.printList()
llist.delLesserNodes();
print("\nModified Linked List");
llist.printList()

L1 = LinkedList()
L1.head = Node(3);
L1.head.next = Node(6);
L1.head.next.next = Node(15);
L1.head.next.next.next = Node(15);
L1.head.next.next.next.next = Node(30)
n1 = L1.countNodes()

L2 = LinkedList()
L2.head = Node(10);
L2.head.next = Node(15);
L2.head.next.next = Node(30)
n2 = L2.countNodes()
print "\nThe node of intersection is ", L1.getNode(L1.head, L2.head, n1, n2)

llist = LinkedList()
arr = ['a', 'b', 'a', 'c', 'a', 'b', 'a']
for i in xrange(0, 7):
    llist.push(arr[i])
    llist.printList()
    if (llist.isPalindrome(llist.head) is not False):
        print("\nIs Palindrome")
    else:
        print ("\nNot Palindrome")

# Create linked list :
# 10->20->30->40->50
list1 = LinkedList()
list1.append(10)
list1.append(20)
list1.append(30)
list1.append(40)
list1.append(50)
 
# Create linked list 2 :
# 5->15->18->35->60
list2 = LinkedList()
list2.append(5)
list2.append(15)
list2.append(18)
list2.append(35)
list2.append(60)
 
# Create linked list 3
list3 = LinkedList()
 
# Merging linked list 1 and linked list 2 in linked list 3
list3.head = mergeLists(list1.head, list2.head)
print "\nMerged Linked List is : ",list3.printList()   

'''
Read it:
https://www.geeksforgeeks.org/lru-cache-implementation/
https://www.geeksforgeeks.org/union-and-intersection-of-two-linked-lists/
https://www.geeksforgeeks.org/the-great-tree-list-recursion-problem/
https://www.geeksforgeeks.org/a-linked-list-with-next-and-arbit-pointer/

'''
'''
C Program for Bubble Sort on Linked List
#include<stdio.h>
#include<stdlib.h>
 
/* structure for a node */
struct Node
{
    int data;
    struct Node *next;
};
 
/* Function to insert a node at the begining of a linked lsit */
void insertAtTheBegin(struct Node **start_ref, int data);
 
/* Function to bubble sort the given linked lsit */
void bubbleSort(struct Node *start);
 
/* Function to swap data of two nodes a and b*/
void swap(struct Node *a, struct Node *b);
 
/* Function to print nodes in a given linked list */
void printList(struct Node *start);
 
int main()
{
    int arr[] = {12, 56, 2, 11, 1, 90};
    int list_size, i;
 
    /* start with empty linked list */
    struct Node *start = NULL;
 
    /* Create linked list from the array arr[].
      Created linked list will be 1->11->2->56->12 */
    for (i = 0; i< 6; i++)
        insertAtTheBegin(&start, arr[i]);
 
    /* print list before sorting */
    printf("\n Linked list before sorting ");
    printList(start);
 
    /* sort the linked list */
    bubbleSort(start);
 
    /* print list after sorting */
    printf("\n Linked list after sorting ");
    printList(start);
 
    getchar();
    return 0;
}
 
 
/* Function to insert a node at the begining of a linked lsit */
void insertAtTheBegin(struct Node **start_ref, int data)
{
    struct Node *ptr1 = (struct Node*)malloc(sizeof(struct Node));
    ptr1->data = data;
    ptr1->next = *start_ref;
    *start_ref = ptr1;
}
 
/* Function to print nodes in a given linked list */
void printList(struct Node *start)
{
    struct Node *temp = start;
    printf("\n");
    while (temp!=NULL)
    {
        printf("%d ", temp->data);
        temp = temp->next;
    }
}
 
/* Bubble sort the given linked lsit */
void bubbleSort(struct Node *start)
{
    int swapped, i;
    struct Node *ptr1;
    struct Node *lptr = NULL;
 
    /* Checking for empty list */
    if (ptr1 == NULL)
        return;
 
    do
    {
        swapped = 0;
        ptr1 = start;
 
        while (ptr1->next != lptr)
        {
            if (ptr1->data > ptr1->next->data)
            { 
                swap(ptr1, ptr1->next);
                swapped = 1;
            }
            ptr1 = ptr1->next;
        }
        lptr = ptr1;
    }
    while (swapped);
}
 
/* function to swap data of two nodes a and b*/
void swap(struct Node *a, struct Node *b)
{
    int temp = a->data;
    a->data = b->data;
    b->data = temp;
}
################################
QuickSort on Doubly Linked List
// A Java program to sort a linked list using Quicksort
class QuickSort_using_Doubly_LinkedList{
    Node head;
   
/* a node of the doubly linked list */ 
    static class Node{
        private int data;
        private Node next;
        private Node prev;
         
        Node(int d){
            data = d;
            next = null;
            prev = null;
        }
    }
     
// A utility function to find last node of linked list    
    Node lastNode(Node node){
        while(node.next!=null)
            node = node.next;
        return node;
    }
     
 
/* Considers last element as pivot, places the pivot element at its
   correct position in sorted array, and places all smaller (smaller than
   pivot) to left of pivot and all greater elements to right of pivot */
    Node partition(Node l,Node h)
    {
       // set pivot as h element
        int x = h.data;
         
        // similar to i = l-1 for array implementation
        Node i = l.prev;
         
        // Similar to "for (int j = l; j <= h- 1; j++)"
        for(Node j=l; j!=h; j=j.next)
        {
            if(j.data <= x)
            {
                // Similar to i++ for array
                i = (i==null) ? l : i.next;
                int temp = i.data;
                i.data = j.data;
                j.data = temp;
            }
        }
        i = (i==null) ? l : i.next;  // Similar to i++
        int temp = i.data;
        i.data = h.data;
        h.data = temp;
        return i;
    }
     
    /* A recursive implementation of quicksort for linked list */
    void _quickSort(Node l,Node h)
    {
        if(h!=null && l!=h && l!=h.next){
            Node temp = partition(l,h);
            _quickSort(l,temp.prev);
            _quickSort(temp.next,h);
        }
    }
     
    // The main function to sort a linked list. It mainly calls _quickSort()
    public void quickSort(Node node)
    {
        // Find last node
        Node head = lastNode(node);
         
        // Call the recursive QuickSort
        _quickSort(node,head);
    }
     
     // A utility function to print contents of arr
     public void printList(Node head)
     {
        while(head!=null){
            System.out.print(head.data+" ");
            head = head.next;
        }
    }
     
    /* Function to insert a node at the beginging of the Doubly Linked List */
    void push(int new_Data)
    {
        Node new_Node = new Node(new_Data);     /* allocate node */
         
        // if head is null, head = new_Node
        if(head==null){
            head = new_Node;
            return;
        }
         
        /* link the old list off the new node */
        new_Node.next = head;
         
        /* change prev of head node to new node */
        head.prev = new_Node;
         
        /* since we are adding at the begining, prev is always NULL */
        new_Node.prev = null;
         
        /* move the head to point to the new node */
        head = new_Node;
    }
     
    /* Driver program to test above function */
    public static void main(String[] args){
            QuickSort_using_Doubly_LinkedList list = new QuickSort_using_Doubly_LinkedList();
             
             
            list.push(5);
            list.push(20);
            list.push(4);
            list.push(3);
            list.push(30);
           
             
            System.out.println("Linked List before sorting ");
            list.printList(list.head);
            System.out.println("\nLinked List after sorting");
            list.quickSort(list.head);
            list.printList(list.head);
         
    }
}
Output : 
Linked List before sorting
30  3  4  20  5
Linked List after sorting
3  4  5  20  30

Time Complexity:  Time complexity of the above implementation is same as time complexity of QuickSort() for arrays. It takes O(n^2) time in worst case and O(nLogn) in average and best cases. The worst case occurs when the linked list is already sorted.

Can we implement random quick sort for linked list?
 Quicksort can be implemented for Linked List only when we can pick a fixed point as pivot (like last element in above implementation). Random QuickSort cannot be efficiently implemented for Linked Lists by picking random pivot.

#################################
QuickSort on Singly Linked List
In partition(), we consider last element as pivot. We traverse through the current list and if a node has value greater than pivot, we move it after tail. If the node has smaller value, we keep it at its current position.
 In QuickSortRecur(), we first call partition() which places pivot at correct position and returns pivot. After pivot is placed at correct position, we find tail node of left side (list before pivot) and recur for left list. Finally, we recur for right list.




// C++ program for Quick Sort on Singly Linled List
#include <iostream>
#include <cstdio>
using namespace std;
 
/* a node of the singly linked list */
struct Node
{
    int data;
    struct Node *next;
};
 
/* A utility function to insert a node at the beginning of linked list */
void push(struct Node** head_ref, int new_data)
{
    /* allocate node */
    struct Node* new_node = new Node;
 
    /* put in the data  */
    new_node->data  = new_data;
 
    /* link the old list off the new node */
    new_node->next = (*head_ref);
 
    /* move the head to point to the new node */
    (*head_ref)    = new_node;
}
 
/* A utility function to print linked list */
void printList(struct Node *node)
{
    while (node != NULL)
    {
        printf("%d  ", node->data);
        node = node->next;
    }
    printf("\n");
}
 
// Returns the last node of the list
struct Node *getTail(struct Node *cur)
{
    while (cur != NULL && cur->next != NULL)
        cur = cur->next;
    return cur;
}
 
// Partitions the list taking the last element as the pivot
struct Node *partition(struct Node *head, struct Node *end,
                       struct Node **newHead, struct Node **newEnd)
{
    struct Node *pivot = end;
    struct Node *prev = NULL, *cur = head, *tail = pivot;
 
    // During partition, both the head and end of the list might change
    // which is updated in the newHead and newEnd variables
    while (cur != pivot)
    {
        if (cur->data < pivot->data)
        {
            // First node that has a value less than the pivot - becomes
            // the new head
            if ((*newHead) == NULL)
                (*newHead) = cur;
 
            prev = cur;  
            cur = cur->next;
        }
        else // If cur node is greater than pivot
        {
            // Move cur node to next of tail, and change tail
            if (prev)
                prev->next = cur->next;
            struct Node *tmp = cur->next;
            cur->next = NULL;
            tail->next = cur;
            tail = cur;
            cur = tmp;
        }
    }
 
    // If the pivot data is the smallest element in the current list,
    // pivot becomes the head
    if ((*newHead) == NULL)
        (*newHead) = pivot;
 
    // Update newEnd to the current last node
    (*newEnd) = tail;
 
    // Return the pivot node
    return pivot;
}
 
 
//here the sorting happens exclusive of the end node
struct Node *quickSortRecur(struct Node *head, struct Node *end)
{
    // base condition
    if (!head || head == end)
        return head;
 
    Node *newHead = NULL, *newEnd = NULL;
 
    // Partition the list, newHead and newEnd will be updated
    // by the partition function
    struct Node *pivot = partition(head, end, &newHead, &newEnd);
 
    // If pivot is the smallest element - no need to recur for
    // the left part.
    if (newHead != pivot)
    {
        // Set the node before the pivot node as NULL
        struct Node *tmp = newHead;
        while (tmp->next != pivot)
            tmp = tmp->next;
        tmp->next = NULL;
 
        // Recur for the list before pivot
        newHead = quickSortRecur(newHead, tmp);
 
        // Change next of last node of the left half to pivot
        tmp = getTail(newHead);
        tmp->next =  pivot;
    }
 
    // Recur for the list after the pivot element
    pivot->next = quickSortRecur(pivot->next, newEnd);
 
    return newHead;
}
 
// The main function for quick sort. This is a wrapper over recursive
// function quickSortRecur()
void quickSort(struct Node **headRef)
{
    (*headRef) = quickSortRecur(*headRef, getTail(*headRef));
    return;
}
 
// Driver program to test above functions
int main()
{
    struct Node *a = NULL;
    push(&a, 5);
    push(&a, 20);
    push(&a, 4);
    push(&a, 3);
    push(&a, 30);
 
    cout << "Linked List before sorting \n";
    printList(a);
 
    quickSort(&a);
 
    cout << "Linked List after sorting \n";
    printList(a);
 
    return 0;
}
 
#################################################
Design a stack with operations on middle element
How to implement a stack which will support following operations in O(1) time complexity?
 1) push() which adds an element to the top of stack.
 2) pop() which removes an element from top of stack.
 3) findMiddle() which will return middle element of the stack.
 4) deleteMiddle() which will delete the middle element.
 Push and pop are standard stack operations. 

The important question is, whether to use a linked list or array for implementation of stack? 

Please note that, we need to find and delete middle element. Deleting an element from middle is not O(1) for array. Also, we may need to move the middle pointer up when we push an element and move down when we pop(). In singly linked list, moving middle pointer in both directions is not possible. 

The idea is to use Doubly Linked List (DLL). We can delete middle element in O(1) time by maintaining mid pointer. We can move mid pointer in both directions using previous and next pointers. 

Following is implementation of push(), pop() and findMiddle() operations. Implementation of deleteMiddle() is left as an exercise. If there are even elements in stack, findMiddle() returns the first middle element. For example, if stack contains {1, 2, 3, 4}, then findMiddle() would return 2.
/* Java Program to implement a stack that supports findMiddle() and deleteMiddle
in O(1) time */
 
public class GFG 
{
    /* A Doubly Linked List Node */
    class DLLNode
    {
        DLLNode prev;
        int data;
        DLLNode next;
        DLLNode(int d){data=d;}
    }
     
    /* Representation of the stack data structure that supports findMiddle()
       in O(1) time.  The Stack is implemented using Doubly Linked List. It
       maintains pointer to head node, pointer to middle node and count of
       nodes */
    class myStack
    {
        DLLNode head;
        DLLNode mid;
        int count;
    }
     
 
    /* Function to create the stack data structure */
    myStack createMyStack()
    {
        myStack ms = new myStack();
        ms.count = 0;
        return ms;
    }
     
 
    /* Function to push an element to the stack */
    void push(myStack ms, int new_data)
    {
 
        /* allocate DLLNode and put in data */
        DLLNode new_DLLNode = new DLLNode(new_data);
         
 
        /* Since we are adding at the beginning,
          prev is always NULL */
        new_DLLNode.prev = null;
         
         /* link the old list off the new DLLNode */
        new_DLLNode.next = ms.head;
         
        /* Increment count of items in stack */
        ms.count += 1;
         
        /* Change mid pointer in two cases
           1) Linked List is empty
           2) Number of nodes in linked list is odd */
        if(ms.count == 1)
        {
            ms.mid=new_DLLNode;
        }
        else
        {
            ms.head.prev = new_DLLNode;
             
            if((ms.count % 2) != 0) // Update mid if ms->count is odd
                ms.mid=ms.mid.prev;
        }
         
        /* move head to point to the new DLLNode */
        ms.head = new_DLLNode;
         
    }
     
    /* Function to pop an element from stack */
    int pop(myStack ms)
    {
        /* Stack underflow */
        if(ms.count == 0)
        {
            System.out.println("Stack is empty");
            return -1;
        }
         
        DLLNode head = ms.head;
        int item = head.data;
        ms.head = head.next;
         
        // If linked list doesn't become empty, update prev
        // of new head as NULL
        if(ms.head != null)
            ms.head.prev = null;
         
        ms.count -= 1;
         
        // update the mid pointer when we have even number of
        // elements in the stack, i,e move down the mid pointer.
        if(ms.count % 2 == 0)
            ms.mid=ms.mid.next;
         
        return item;
    }
     
    // Function for finding middle of the stack
    int findMiddle(myStack ms)
    {
        if(ms.count == 0)
        {
            System.out.println("Stack is empty now");
            return -1;
        }
        return ms.mid.data;
    }
     
    // Driver program to test functions of myStack
    public static void main(String args[])
    {
        GFG ob = new GFG();
        myStack ms = ob.createMyStack();
        ob.push(ms, 11);
        ob.push(ms, 22);
        ob.push(ms, 33);
        ob.push(ms, 44);
        ob.push(ms, 55);
        ob.push(ms, 66);
        ob.push(ms, 77);
         
        System.out.println("Item popped is " + ob.pop(ms));
        System.out.println("Item popped is " + ob.pop(ms));
        System.out.println("Middle Element is " + ob.findMiddle(ms));
    }
}
Output: Item popped is 77
Item popped is 66
Middle Element is 33
##############################################
Swap Kth node from beginning with Kth node from end in a Linked List
Given a singly linked list, swap kth node from beginning with kth node from end. Swapping of data is not allowed, only pointers should be changed. This requirement may be logical in many situations where the linked list data part is huge (For example student details line Name, RollNo, Address, ..etc). The pointers are always fixed (4 bytes for most of the compilers).
The problem seems simple at first look, but it has many interesting cases. 

Let X be the kth node from beginning and Y be the kth node from end. Following are the interesting cases that must be handled.
1) Y is next to X
2) X is next to Y
3) X and Y are same
4) X and Y don't exist (k is more than number of nodes in linked list)

// A Java program to swap kth node from the beginning with
// kth node from the end
 
class Node
{
    int data;
    Node next;
    Node(int d) { data = d;  next = null; }
}
 
class LinkedList
{
    Node head;
 
    /* Utility function to insert a node at the beginning */
    void push(int new_data)
    {
        Node new_node = new Node(new_data);
        new_node.next = head;
        head = new_node;
    }
 
    /* Utility function for displaying linked list */
    void printList()
    {
        Node node = head;
        while (node != null)
        {
            System.out.print(node.data + " ");
            node = node.next;
        }
        System.out.println("");
    }
 
    /* Utility function for calculating length of linked list */
    int countNodes()
    {
        int count = 0;
        Node s = head;
        while (s != null)
        {
            count++;
            s = s.next;
        }
        return count;
    }
 
    /* Function for swapping kth nodes from both ends of
       linked list */
    void swapKth(int k)
    {
        // Count nodes in linked list
        int n = countNodes();
 
        // Check if k is valid
        if (n < k)
            return;
 
        // If x (kth node from start) and y(kth node from end)
        // are same
        if (2*k - 1 == n)
            return;
 
        // Find the kth node from beginning of linked list.
        // We also find previous of kth node because we need
        // to update next pointer of the previous.
        Node x = head;
        Node x_prev = null;
        for (int i = 1; i < k; i++)
        {
            x_prev = x;
            x = x.next;
        }
 
        // Similarly, find the kth node from end and its 
        // previous. kth node from end is (n-k+1)th node
        // from beginning
        Node y = head;
        Node y_prev = null;
        for (int i = 1; i < n - k + 1; i++)
        {
            y_prev = y;
            y = y.next;
        }
 
        // If x_prev exists, then new next of it will be y.
        // Consider the case when y->next is x, in this case,
        // x_prev and y are same. So the statement 
        // "x_prev->next = y" creates a self loop. This self
        // loop will be broken when we change y->next.
        if (x_prev != null)
            x_prev.next = y;
 
        // Same thing applies to y_prev
        if (y_prev != null)
            y_prev.next = x;
 
        // Swap next pointers of x and y. These statements
        // also break self loop if x->next is y or y->next
        // is x
        Node temp = x.next;
        x.next = y.next;
        y.next = temp;
 
        // Change head pointers when k is 1 or n
        if (k == 1)
            head = y;
 
        if (k == n)
            head = x;
    }
 
    // Driver code to test above
    public static void main(String[] args)
    {
        LinkedList llist = new LinkedList();
        for (int i = 8; i >= 1; i--)
            llist.push(i);
 
        System.out.print("Original linked list: ");
        llist.printList();
        System.out.println("");
 
        for (int i = 1; i < 9; i++)
        {
            llist.swapKth(i);
            System.out.println("Modified List for k = " + i);
            llist.printList();
            System.out.println("");
        }
    }
}
Output: Original Linked List: 1 2 3 4 5 6 7 8

Modified List for k = 1
8 2 3 4 5 6 7 1

Modified List for k = 2
8 7 3 4 5 6 2 1

Modified List for k = 3
8 7 6 4 5 3 2 1

Modified List for k = 4
8 7 6 5 4 3 2 1

Modified List for k = 5
8 7 6 4 5 3 2 1

Modified List for k = 6
8 7 3 4 5 6 2 1

Modified List for k = 7
8 2 3 4 5 6 7 1

Modified List for k = 8
1 2 3 4 5 6 7 8


Please note that the above code runs three separate loops to count nodes, find x and x prev, and to find y and y_prev. These three things can be done in a single loop. The code uses three loops to keep things simple and readable.
####################################
Find a triplet from three linked lists with sum equal to a given number
Given three linked lists, say a, b and c, find one node from each list such that the sum of the values of the nodes is equal to a given number. 
 For example, if the three linked lists are 12->6->29, 23->5->8 and 90->20->59, and the given number is 101, the output should be tripel 6 5 90.

In the following solutions, size of all three linked lists is assumed same for simplicity of analysis. The following solutions work for linked lists of different sizes also.

A simple method to solve this problem is to run three nested loops. The outermost loop picks an element from list a, the middle loop picks an element from b and the innermost loop picks from c. The innermost loop also checks whether the sum of values of current nodes of a, b and c is equal to given number. The time complexity of this method will be O(n^3).

Sorting can be used to reduce the time complexity to O(n*n). Following are the detailed steps.
 1) Sort list b in ascending order, and list c in descending order.
 2) After the b and c are sorted, one by one pick an element from list a and find the pair by traversing both b and c. See isSumSorted() in the following code. The idea is similar to Quadratic algorithm of 3 sum problem.

Following code implements step 2 only. The solution can be easily modified for unsorted lists by adding the merge sort code discussed here.
// Java program to find a triplet from three linked lists with
// sum equal to a given number
class LinkedList
{
    Node head;  // head of list
 
    /* Linked list Node*/
    class Node
    {
        int data;
        Node next;
        Node(int d) {data = d; next = null; }
    }
 
    /* A function to chech if there are three elements in a, b
      and c whose sum is equal to givenNumber.  The function
      assumes that the list b is sorted in ascending order and
      c is sorted in descending order. */
   boolean isSumSorted(LinkedList la, LinkedList lb, LinkedList lc,
                       int givenNumber)
   {
      Node a = la.head;
 
      // Traverse all nodes of la
      while (a != null)
      {
          Node b = lb.head;
          Node c = lc.head;
 
          // for every node in la pick 2 nodes from lb and lc
          while (b != null && c!=null)
          {
              int sum = a.data + b.data + c.data;
              if (sum == givenNumber)
              {
                 System.out.println("Triplet found " + a.data +
                                     " " + b.data + " " + c.data);
                 return true;
              }
 
              // If sum is smaller then look for greater value of b
              else if (sum < givenNumber)
                b = b.next;
 
              else
                c = c.next;
          }
          a = a.next;
      }
      System.out.println("No Triplet found");
      return false;
   }
 
 
    /*  Given a reference (pointer to pointer) to the head
       of a list and an int, push a new node on the front
       of the list. */
    void push(int new_data)
    {
        /* 1 & 2: Allocate the Node &
                  Put in the data*/
        Node new_node = new Node(new_data);
 
        /* 3. Make next of new Node as head */
        new_node.next = head;
 
        /* 4. Move the head to point to new Node */
        head = new_node;
    }
 
     /* Drier program to test above functions */
    public static void main(String args[])
    {
        LinkedList llist1 = new LinkedList();
        LinkedList llist2 = new LinkedList();
        LinkedList llist3 = new LinkedList();
 
        /* Create Linked List llist1 100->15->5->20 */
        llist1.push(20);
        llist1.push(5);
        llist1.push(15);
        llist1.push(100);
 
        /*create a sorted linked list 'b' 2->4->9->10 */
        llist2.push(10);
        llist2.push(9);
        llist2.push(4);
        llist2.push(2);
 
        /*create another sorted linked list 'c' 8->4->2->1 */
        llist3.push(1);
        llist3.push(2);
        llist3.push(4);
        llist3.push(8);
 
        int givenNumber = 25;
        llist1.isSumSorted(llist1,llist2,llist3,givenNumber);
    }
} 
Output: Triplet Found: 15 2 8

Time complexity: The linked lists b and c can be sorted in O(nLogn) time using Merge Sort (See this). The step 2 takes O(n*n) time. So the overall time complexity is O(nlogn) + O(nlogn) + O(n*n) = O(n*n). 

In this approach, the linked lists b and c are sorted first, so their original order will be lost. If we want to retain the original order of b and c, we can create copy of b and c. 
##########################################
XOR Linked List - A Memory Efficient Doubly Linked List | Set 2
In the previous post, we discussed how a Doubly Linked can be created using only one space for address field with every node. In this post, we will discuss implementation of memory efficient doubly linked list. We will mainly discuss following two simple functions.

1) A function to insert a new node at the beginning.
 2) A function to traverse the list in forward direction.
In the following code, insert() function inserts a new node at the beginning. We need to change the head pointer of Linked List, that is why a double pointer is used (See this). Let use first discuss few things again that have been discussed in the previous post. We store XOR of next and previous nodes with every node and we call it npx, which is the only address member we have with every node. When we insert a new node at the beginning, npx of new node will always be XOR of NULL and current head. And npx of current head must be changed to XOR of new node and node next to current head.

printList() traverses the list in forward direction. It prints data values from every node. To traverse the list, we need to get pointer to the next node at every point. We can get the address of next node by keeping track of current node and previous node. If we do XOR of curr->npx and prev, we get the address of next node. 




/* C/C++ Implementation of Memory efficient Doubly Linked List */
#include <stdio.h>
#include <stdlib.h>
 
// Node structure of a memory efficient doubly linked list
struct Node
{
    int data;
    struct Node* npx;  /* XOR of next and previous node */
};
 
/* returns XORed value of the node addresses */
struct Node* XOR (struct Node *a, struct Node *b)
{
    return (struct Node*) ((unsigned int) (a) ^ (unsigned int) (b));
}
 
/* Insert a node at the begining of the XORed linked list and makes the
   newly inserted node as head */
void insert(struct Node **head_ref, int data)
{
    // Allocate memory for new node
    struct Node *new_node  = (struct Node *) malloc (sizeof (struct Node) );
    new_node->data = data;
 
    /* Since new node is being inserted at the begining, npx of new node
       will always be XOR of current head and NULL */
    new_node->npx = XOR(*head_ref, NULL);
 
    /* If linked list is not empty, then npx of current head node will be XOR 
       of new node and node next to current head */
    if (*head_ref != NULL)
    {
        // *(head_ref)->npx is XOR of NULL and next. So if we do XOR of 
        // it with NULL, we get next
        struct Node* next = XOR((*head_ref)->npx,  NULL);
        (*head_ref)->npx = XOR(new_node, next);
    }
 
    // Change head
    *head_ref = new_node;
}
 
// prints contents of doubly linked list in forward direction
void printList (struct Node *head)
{
    struct Node *curr = head;
    struct Node *prev = NULL;
    struct Node *next;
 
    printf ("Following are the nodes of Linked List: \n");
 
    while (curr != NULL)
    {
        // print current node
        printf ("%d ", curr->data);
 
        // get address of next node: curr->npx is next^prev, so curr->npx^prev
        // will be next^prev^prev which is next
        next = XOR (prev, curr->npx);
 
        // update prev and curr for next iteration
        prev = curr;
        curr = next;
    }
}
 
// Driver program to test above functions
int main ()
{
    /* Create following Doubly Linked List
       head-->40<-->30<-->20<-->10   */
    struct Node *head = NULL;
    insert(&head, 10);
    insert(&head, 20);
    insert(&head, 30);
    insert(&head, 40);
 
    // print the created list
    printList (head);
 
    return (0);
}
 
Output: 
Following are the nodes of Linked List:
40 30 20 10

Note that XOR of pointers is not defined by C/C++ standard. So the above implementation may not work on all platforms.
#############################################################
Union and Intersection of two Linked Lists
Input:
   List1: 10->15->4->20
   lsit2:  8->4->2->10
Output:
   Intersection List: 4->10
   Union List: 2->8->20->4->15->10
   

'''
