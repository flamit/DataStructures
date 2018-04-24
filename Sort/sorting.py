'''
Selection Sort

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.
The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

Following example explains the above steps:
arr[] = 64 25 12 22 11

Find the minimum element in arr[0...4] and place it at beginning
11 25 12 22 64

Find the minimum element in arr[1...4] and place it at beginning of arr[1...4]
11 12 25 22 64

Find the minimum element in arr[2...4] and place it at beginning of arr[2...4]
11 12 22 25 64

Find the minimum element in arr[3...4] and place it at beginning of arr[3...4]
11 12 22 25 64
Time Complexity: O(n2) as there are two nested loops.
Auxiliary Space: O(1)
The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation. 
'''
a = [64, 25, 12, 22, 11]
print "Before sorting: ", a

def selectionSort(a):
    n = len(a)
    for i in range(0, n):                                   # for i in range(0, n-1): we can write n-1 instead of n as
        for j in range(i+1, n):                             # for the last element we don't need to iterate; as by this time sorting is already done and the last element is the biggest one.
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

selectionSort(a)
print "After selection sort: ", a

def bubbleSort(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(0, n-1):
            if a[j] > a[j+1]:
                a[j+1], a[j] = a[j], a[j+1]

arr = [100, 64, 34, 25, 2000, 12, 22, 11, 90, 3]
print "Before sorting: ",arr
bubbleSort(arr)
print "After bubble sort: ",arr
'''
Bubble Sort
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

Example:
First Pass:
 ( 5 1 4 2 8 ) > ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
 ( 1 5 4 2 8 ) >  ( 1 4 5 2 8 ), Swap since 5 > 4
 ( 1 4 5 2 8 ) >  ( 1 4 2 5 8 ), Swap since 5 > 2
 ( 1 4 2 5 8 ) > ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

Second Pass:
 ( 1 4 2 5 8 ) > ( 1 4 2 5 8 )
 ( 1 4 2 5 8 ) > ( 1 2 4 5 8 ), Swap since 4 > 2
 ( 1 2 4 5 8 ) > ( 1 2 4 5 8 )
 ( 1 2 4 5 8 ) >  ( 1 2 4 5 8 )
 Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.

Third Pass:
 ( 1 2 4 5 8 ) > ( 1 2 4 5 8 )
 ( 1 2 4 5 8 ) > ( 1 2 4 5 8 )
 ( 1 2 4 5 8 ) > ( 1 2 4 5 8 )
 ( 1 2 4 5 8 ) > ( 1 2 4 5 8 )
 
Output: Sorted array:
11 12 22 25 34 64 90
Worst and Average Case Time Complexity: O(n2). Worst case occurs when array is reverse sorted.
Best Case Time Complexity: O(n). Best case occurs when array is already sorted.
Auxiliary Space: O(1)
Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted.
Sorting In Place: Yes
Stable: Yes

Due to its simplicity, bubble sort is often used to introduce the concept of a sorting algorithm.
In computer graphics it is popular for its capability to detect a very small error (like swap of just two elements) in almost-sorted arrays and fix it with just linear complexity (2n).
For example, it is used in a polygon filling algorithm, where bounding lines are sorted by their x coordinate at a specific scan line (a line parallel to x axis) and with incrementing y
their order changes (two elements are swapped) only at intersections of two lines (Source: Wikipedia)

Insertion Sort
Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.

Algorithm: Sort an arr[] of size n
 Loop from i = 1 to n-1.
a) Pick element arr[i] and insert it into sorted sequence arr[0...i-1]

Example:
12, 11, 13, 5, 6

Let us loop for i = 1 (second element of the array) to 5 (Size of input array)

i = 1. Since 11 is smaller than 12, move 12 and insert 11 before 12
11, 12, 13, 5, 6

i = 2. 13 will remain at its position as all elements in A[0..I-1] are smaller than 13
11, 12, 13, 5, 6

i = 3. 5 will move to the beginning and all other elements from 11 to 13 will move one position ahead of their current position.
5, 11, 12, 13, 6

i = 4. 6 will move to position after 5, and elements from 11 to 13 will move one position ahead of their current position.
5, 6, 11, 12, 13 
Time Complexity: O(n2) 
Auxiliary Space: O(1)
Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes minimum time (Order of n) when elements are already sorted.
Algorithmic Paradigm: Incremental Approach
Sorting In Place: Yes
Stable: Yes
Online: Yes
Uses: Insertion sort is used when number of elements is small. It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.
'''
def insertionSort(a):
  n = len(a)
  
  for i in range(1, n):
    j = i
    while j > 0 and a[j - 1] > a[j]:
      a[j - 1], a[j] = a[j], a[j - 1]
      j -= 1

arr = [12, 11, 13, 5, 6]
print "Before sorting: ",arr
insertionSort(arr)
print ("Sorted array is:"), arr

def binary_search(arr, left, right, x):
  if left == right:                                     # we need to distinugish whether we should insert before or after the left boundary
    if arr[left] > x:                                   # imagine [0] is the last step of the binary search and we need to decide where to insert -1
      return left
    else:
      return left+1

  if left > right:                                      # this occurs if we are moving beyond left's boundary meaning the left boundary is the least position to find a number greater than val
    return left

  mid = (left + right)/2
  if arr[mid] == x:
      return mid   
  elif arr[mid] > x:
    return binary_search(arr, left, mid-1, x)
  else:
    return binary_search(arr, mid+1, right, x)

def binaryInsertionSort(a):
  n = len(a)
  for i in xrange(1, n):
    j = binary_search(a, 0, i-1, a[i])
    a = a[:j] + [a[i]] + a[j:i] + a[i+1:]
  return a

arr=[37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
print("Before sorting: "), arr
arr=binaryInsertionSort(arr)
print("Sorted array: "), arr
'''
What is Binary Insertion Sort?
 We can use binary search to reduce the number of comparisons in normal insertion sort. Binary Insertion Sort find use binary search to find the proper location to insert the selected item at
 each iteration. In normal insertion, sort it takes O(i) (at ith iteration) in worst case. we can reduce it to O(logi) by using binary search. The algorithm as a whole still has a running
 worst case running time of O(n2) because of the series of swaps required for each insertion. Refer this for implementation.

How to implement Insertion Sort for Linked List?
 Below is simple insertion sort algorithm for linked list. 
1) Create an empty sorted (or result) list
2) Traverse the given list, do following for every node.
......a) Insert current node in sorted way in sorted or result list.
3) Change head of given linked list to head of sorted (or result) list. 
'''
'''
Merge Sort

Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.
The merge() function is used for merging two halves. The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.
See following C implementation for details.

MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = (l+r)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
Time Complexity: Sorting arrays on different machines. Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation.
 T(n) = 2T(n/2) + Theta(n)
 The above recurrence can be solved either using Recurrence Tree method or Master method. It falls in case II of Master Method and solution of the recurrence is Theta(nLogn).
 Time complexity of Merge Sort is Theta(nLogn) in all 3 cases (worst, average and best) as merge sort always divides the array in two halves and take linear time to merge two halves.

Time complexity: O(nLogn)       <= Actually it's Theta(nLogn). Check the difference...
Auxiliary Space: O(n)
Algorithmic Paradigm:  Divide and Conquer
Sorting In Place: No in a typical implementation
Stable: Yes

Applications of Merge Sort:
===========================
1. Merge Sort is useful for sorting linked lists in O(nLogn) time.In case of linked lists the case is different mainly due to difference in memory allocation of arrays and linked lists.
    Unlike arrays, linked list nodes may not be adjacent in memory. Unlike array, in linked list, we can insert items in the middle in O(1) extra space and O(1) time.
    Therefore merge operation of merge sort can be implemented without extra space for linked lists.

    In arrays, we can do random access as elements are continuous in memory. Let us say we have an integer (4-byte) array A and let the address of A[0] be x then to access A[i],
    we can directly access the memory at (x + i*4). Unlike arrays, we can not do random access in linked list. Quick Sort requires a lot of this kind of access.
    In linked list to access ith index, we have to travel each and every node from the head to ith node as we don't have continuous block of memory.
    Therefore, the overhead increases for quick sort. Merge sort accesses data sequentially and the need of random access is low. 

2.  Inversion Count Problem 
3.  Used in External Sorting
'''
def mergeSort(arr):
    if len(arr)>1:          # Note this line. Without this line it will fall into an infinite loop
        mid = len(arr)//2
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i=0
        j=0
        k=0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]
                i+=1
            else:
                arr[k] = rightHalf[j]
                j+=1
            k+=1

        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i+=1
            k+=1

        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            j+=1
            k+=1
            
    return arr

arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print ("Given array is"), arr

mergeSort(arr)
print ("After merge sort: "), arr
'''
# Geeks for geeks solution
# 'low' is for left index and 'high' is right index of the sub-array of arr to be sorted
def mergeSort(arr, low, high):
    if low < high:
        mid =( low+(high - 1))/2                      # Same as (low + high)/2, but avoids overflow for large low and high
        mergeSort(arr, low, mid)
        mergeSort(arr, mid+1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    n1 = mid - low + 1                                # Find sizes of two subarrays to be merged
    n2 = high - mid
    
    L = [0] * (n1)
    R = [0] * (n2)
    
    for i in range(0, n1):                          # Copy data to temp arrays L[] and R[]
        L[i] = arr[low + i]
    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]
        
    i = 0                                           # Initial index of first subarray                       
    j = 0                                           # Initial index of second subarray
    k = low                                         # Initial index of merged subarray
    
    while i < n1 and j < n2 :                       # Merge the temp arrays back into arr[l..r]
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        
    while i < n1:                                   # Copy the remaining elements of L[], if there are any
        arr[k] = L[i]
        i += 1
        k += 1
        
    while j < n2:                                   # Copy the remaining elements of R[], if there are any
        arr[k] = R[j]
        j += 1
        k += 1
        
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print ("Given array is"), arr

mergeSort(arr,0,n-1)
print ("After merge sort: "), arr
'''
'''
Heap Sort

Heap sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum
element at the end. We repeat the same process for remaining element.

What is Binary Heap?
 Let us first define a Complete Binary Tree. A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and
 all nodes are as far left as possible (Source Wikipedia)
 
A Binary Heap is a Complete Binary Tree where items are stored in a special order such that value in a parent node is greater(or smaller) than the values in its two children nodes.
The former is called as max heap and the later is called min heap. The heap can be represented by binary tree or array.

Why array based representation for Binary Heap?
 Since a Binary Heap is a Complete Binary Tree, it can be easily represented as array and array based representation is space efficient. If the parent node is stored at index I,
 the left child can be calculated by 2 * I + 1 and right child by 2 * I + 2 (assuming the indexing starts at 0).

Heap Sort Algorithm for sorting in increasing order:
1. Build a max heap from the input data.
2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1. Finally, heapify the root of tree.
3. Repeat above steps while size of heap is greater than 1.

How to build the heap?
 Heapify procedure can be applied to a node only if its children nodes are heapified. So the heapification must be performed in the bottom up order.

Lets understand with the help of an example: 
Input data: 4, 10, 3, 5, 1
                 4(0)
                /   \
            10(1)   3(2)
            /   \
         5(3)    1(4)

The numbers in bracket represent the indices in the array representation of data.

Applying heapify procedure to index 1:
                 4(0)
                /   \
            10(1)    3(2)
           /   \
        5(3)    1(4)

Applying heapify procedure to index 0:
                10(0)
                /  \
            5(1)  3(2)
              / \
         4(3)    1(4)
The heapify procedure calls itself recursively to build heap in top down manner.

Notes:
 Heap sort is an in-place algorithm.
 Its typical implementation is not stable, but can be made stable (See this)

Time Complexity: O(nLogn)
Time Complexity: Time complexity of heapify is O(Logn). Time complexity of createAndBuildHeap() is O(n) and overall time complexity of Heap Sort is O(nLogn).

Applications of HeapSort
1. Sort a nearly sorted (or K sorted) array
2. k largest(or smallest) elements in an array

Heap sort algorithm has limited uses because Quicksort and Mergesort are better in practice. Nevertheless, the Heap data structure itself is enormously used.

Applications of Heap Data Structure:
Priority Queues: Priority queues can be efficiently implemented using Binary Heap because it supports insert(), delete() and extractmax(), decreaseKey() operations in O(logn) time.
Binomoial Heap and Fibonacci Heap are variations of Binary Heap. These variations perform union also in O(logn) time which is a O(n) operation in Binary Heap.
Heap Implemented priority queues are used in Graph algorithms like Prim's Algorithm and Dijkstra's algorithm.
'''
# To heapify subtree rooted at index i. n is size of heap
def heapify(arr, n, i):
    largest = i                                         # Initialize largest as root
    l = 2 * i + 1                                       # left = 2*i + 1
    r = 2 * i + 2                                       # right = 2*i + 2
    
    if l < n and arr[i] < arr[l]:                       # See if left child of root exists and is greater than root
        largest = l
    if r < n and arr[largest] < arr[r]:                 # See if right child of root exists and is greater than root
        largest = r
        
    if largest != i:                                    # Change root, if needed
        arr[i],arr[largest] = arr[largest],arr[i]       
        heapify(arr, n, largest)                        # Heapify the root.
        
def heapSort(arr):
    n = len(arr)
    
    for i in range(n, -1, -1):                          # Build a maxheap.
        heapify(arr, n, i)
        
    for i in range(n-1, 0, -1):                         # One by one extract elements
        arr[i], arr[0] = arr[0], arr[i]                 
        heapify(arr, i, 0)
        
arr = [ 12, 11, 13, 5, 6, 7]
print "Before sorting: ", arr
heapSort(arr)
print "After Heap sort: ", arr
'''
QuickSort

Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.
There are many different versions of quickSort that pick pivot in different ways.
1. Always pick first element as pivot.
2. Always pick last element as pivot (implemented below)
3. Pick a random element as pivot.
4. Pick median as pivot.

The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller
elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

Pseudo Code for recursive QuickSort function : 
/* low  --> Starting index,  high  --> Ending index */
quickSort(arr[], low, high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[pi] is now at right place */
        pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  // Before pi
        quickSort(arr, pi + 1, high); // After pi
    }
}

quicksort

Partition Algorithm
 There can be many ways to do partition, following pseudo code adopts the method given in CLRS book.
 The logic is simple, we start from the leftmost element and keep track of index of smaller (or equal to) elements as i.
 While traversing, if we find a smaller element, we swap current element with arr[i]. Otherwise we ignore current element.
/* low  --> Starting index,  high  --> Ending index */
quickSort(arr[], low, high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[p] is now at right place */
        pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  // Before pi
        quickSort(arr, pi + 1, high); // After pi
    }
}

Pseudo code for partition()
/* This function takes last element as pivot, places the pivot element at its correct position in sorted array, and places all smaller (smaller than pivot) to left of pivot and
all greater elements to right of pivot */
partition (arr[], low, high)
{
    // pivot (Element to be placed at right position)
    pivot = arr[high]; 
    i = (low - 1)  // Index of smaller element
    for (j = low; j <= high- 1; j++)
    {
        // If current element is smaller than or equal to pivot
        if (arr[j] <= pivot)
        {
            i++;    // increment index of smaller element
            swap arr[i] and arr[j]
        }
    }
    swap arr[i + 1] and arr[high])
    return (i + 1)
}

Illustration of partition() :
arr[] = {10, 80, 30, 90, 40, 50, 70}
Indexes:  0   1   2   3   4   5   6 

low = 0, high =  6, pivot = arr[h] = 70
Initialize index of smaller element, i = -1

Traverse elements from j = low to high-1
j = 0 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
i = 0 
arr[] = {10, 80, 30, 90, 40, 50, 70} // No change as i and j are same

j = 1 : Since arr[j] > pivot, do nothing
// No change in i and arr[]

j = 2 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
i = 1
arr[] = {10, 30, 80, 90, 40, 50, 70} // We swap 80 and 30 

j = 3 : Since arr[j] > pivot, do nothing
// No change in i and arr[]

j = 4 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
i = 2
arr[] = {10, 30, 40, 90, 80, 50, 70} // 80 and 40 Swapped
j = 5 : Since arr[j] <= pivot, do i++ and swap arr[i] with arr[j] 
i = 3 
arr[] = {10, 30, 40, 50, 80, 90, 70} // 90 and 50 Swapped 

We come out of loop because j is now equal to high-1. Finally we place pivot at correct position by swapping arr[i+1] and arr[high] (or pivot)
arr[] = {10, 30, 40, 50, 70, 90, 80} // 80 and 70 Swapped 

Now 70 is at its correct place. All elements smaller than 70 are before it and all elements greater than 70 are after it.
Analysis of QuickSort
 Time taken by QuickSort in general can be written as following. 
 T(n) = T(k) + T(n-k-1) + theta(n)

The first two terms are for two recursive calls, the last term is for the partition process. k is the number of elements which are smaller than pivot.
 The time taken by QuickSort depends upon the input array and partition strategy. Following are three cases.

Worst Case: The worst case occurs when the partition process always picks greatest or smallest element as pivot.
If we consider above partition strategy where last element is always picked as pivot, the worst case would occur when the array is already sorted in increasing or decreasing order.
Following is recurrence for worst case. 
 T(n) = T(0) + T(n-1) + theta(n)
which is equivalent to  
 T(n) = T(n-1) + theta(n)
 
The solution of above recurrence is theta(n2).

Best Case: The best case occurs when the partition process always picks the middle element as pivot. Following is recurrence for best case. 
 T(n) = 2T(n/2) + theta(n)

The solution of above recurrence is theta(nLogn). It can be solved using case 2 of Master Theorem.

Average Case:
 To do average case analysis, we need to consider all possible permutation of array and calculate time taken by every permutation which doesn't look easy.
 We can get an idea of average case by considering the case when partition puts O(n/9) elements in one set and O(9n/10) elements in other set. Following is recurrence for this case. 
 T(n) = T(n/9) + T(9n/10) + theta(n)
 
Solution of above recurrence is also O(nLogn)

Although the worst case time complexity of QuickSort is O(n2) which is more than many other sorting algorithms like Merge Sort and Heap Sort, QuickSort is faster in practice,
because its inner loop can be efficiently implemented on most architectures, and in most real-world data. QuickSort can be implemented in different ways by changing the choice of pivot,
so that the worst case rarely occurs for a given type of data. However, merge sort is generally considered better when data is huge and stored in external storage. 

What is 3-Way QuickSort?
 In simple QuickSort algorithm, we select an element as pivot, partition the array around pivot and recur for subarrays on left and right of pivot.
 Consider an array which has many redundant elements. For example, {1, 4, 2, 4, 2, 4, 1, 2, 4, 1, 2, 2, 2, 2, 4, 1, 4, 4, 4}. If 4 is picked as pivot in Simple QuickSort, we fix only one 4 and recursively process remaining occurrences. In 3 Way QuickSort, an array arr[l..r] is divided in 3 parts:
 a) arr[l..i] elements less than pivot.
 b) arr[i+1..j-1] elements equal to pivot.
 c) arr[j..r] elements greater than pivot.
 See this for implementation.

How to implement QuickSort for Linked Lists?
QuickSort on Singly Linked List
QuickSort on Doubly Linked List

Can we implement QuickSort Iteratively?
 Yes, please refer Iterative Quick Sort.

Why Quick Sort is preferred over MergeSort for sorting Arrays
 Quick Sort in its general form is an in-place sort (i.e. it doesn't require any extra storage) whereas merge sort requires O(N) extra storage, N denoting the array size which may be quite
 expensive. Allocating and de-allocating the extra space used for merge sort increases the running time of the algorithm.
 Comparing average complexity we find that both type of sorts have O(NlogN) average complexity but the constants differ. For arrays, merge sort loses due to the use of extra O(N) storage space.

Most practical implementations of Quick Sort use randomized version. The randomized version has expected time complexity of O(nLogn).
The worst case is possible in randomized version also, but worst case doesn't occur for a particular pattern (like sorted array) and randomized Quick Sort works well in practice.

Quick Sort is also a cache friendly sorting algorithm as it has good locality of reference when used for arrays.
Quick Sort is also tail recursive, therefore tail call optimizations is done.

Why MergeSort is preferred over QuickSort for Linked Lists?
 In case of linked lists the case is different mainly due to difference in memory allocation of arrays and linked lists. Unlike arrays, linked list nodes may not be adjacent in memory.
 Unlike array, in linked list, we can insert items in the middle in O(1) extra space and O(1) time. Therefore merge operation of merge sort can be implemented without extra space for linked lists.
                                                     
In arrays, we can do random access as elements are continuous in memory. Let us say we have an integer (4-byte) array A and let the address of A[0] be x then to access A[i],
we can directly access the memory at (x + i*4). Unlike arrays, we can not do random access in linked list. Quick Sort requires a lot of this kind of access.
In linked list to access ith index, we have to travel each and every node from the head to ith node as we don't have continuous block of memory.
Therefore, the overhead increases for quick sort. Merge sort accesses data sequentially and the need of random access is low. 

How to optimize QuickSort so that it takes O(Log n) extra space in worst case?
 Please see QuickSort Tail Call Optimization (Reducing worst case space to Log n )
'''
# This function takes last element as pivot, places the pivot element at its correct position in sorted array, and places all smaller (smaller than pivot) to left of pivot and
# all greater elements to right of pivot
def partition(arr,low,high):
    i =  low-1                                                                      # index of smaller element
    pivot = arr[high]                                                   
 
    for j in range(low , high):                                                     # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1                                                                  # increment index of smaller element
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return ( i+1 )

# Function to do Quick sort
def quickSort(arr,low,high):                                                        # The main function that implements QuickSort. 
    if low < high:                                                                  # arr[] --> Array to be sorted, low  --> Starting index, high  --> Ending index
        pi = partition(arr,low,high)                                                # pi is partitioning index, arr[p] is now at right place
        quickSort(arr, low, pi-1)                                                   # Separately sort elements before partition and after partition
        quickSort(arr, pi+1, high)

arr = [10, 7, 8, 9, 1, 5]
print ("Array is: "), arr
n = len(arr)
quickSort(arr,0,n-1)
print ("Array after Quick sort is: "), arr

'''
Counting Sort
Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (kind of hashing).
Then doing some arithmetic to calculate the position of each object in the output sequence.

Let us understand it with the help of an example. 
For simplicity, consider the data in the range 0 to 9. 
Input data: 1, 4, 1, 2, 7, 5, 2
  1) Take a count array to store the count of each unique object.
  Index:     0  1  2  3  4  5  6  7  8  9
  Count:     0  2  2  0   1  1  0  1  0  0

  2) Modify the count array such that each element at each index stores the sum of previous counts.
  Index:     0  1  2  3  4  5  6  7  8  9
  Count:     0  2  4  4  5  6  6  7  7  7

The modified count array indicates the position of each object in the output sequence.
 
  3) Output each object from the input sequence followed by decreasing its count by 1.
  Process the input data: 1, 4, 1, 2, 7, 5, 2. Position of 1 is 2.
  Put data 1 at index 2 in output. Decrease count by 1 to place next data 1 at an index 1 smaller than this index.
Time Complexity: O(n+k) where n is the number of elements in input array and k is the range of input.
Auxiliary Space: O(n+k)

Points to be noted:
1. Counting sort is efficient if the range of input data is not significantly greater than the number of objects to be sorted.
   Consider the situation where the input sequence is between range 1 to 10K and the data is 10, 5, 10K, 5K.
2. It is not a comparison based sorting. It running time complexity is O(n) with space proportional to the range of data.
3. It is often used as a sub-routine to another sorting algorithm like radix sort.
4. Counting sort uses a partial hashing to count the occurrence of the data object in O(1).
5. Counting sort can be extended to work for negative inputs also.

Exercise:
1. Modify above code to sort the input data in the range from M to N.
2. Modify above code to sort negative input data.
3. Is counting sort stable and online?
4. Thoughts on parallelizing the counting sort algorithm.

'''
def countSort(arr):
    output = [0 for i in range(256)]                                # The output character array that will have sorted arr
    count = [0 for i in range(256)]                                 # Create a count array to store count of inidividual characters and initialize count array as 0
    ans = ["" for _ in arr]                                         # For storing the resulting answer since the string is immutable
    
    for i in arr:                                                   # Store count of each character
        count[ord(i)] += 1
        
    for i in range(256):                                            # Change count[i] so that count[i] now contains actual position of this character in output array
        count[i] += count[i-1]
        
    for i in range(len(arr)):                                       # Build the output character array
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1
        
    for i in range(len(arr)):                                       # Copy the output array to arr, so that arr now contains sorted characters
        ans[i] = output[i]
    return ans

arr = "geeksforgeeks"
print "Characters: ", arr
ans = countSort(arr)
print "character array after Counting sort is %s"  %("".join(ans))

# A function to do counting sort of arr[] according to the digit represented by exp.
def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n)                                  # The output array elements that will have sorted arr
    count = [0] * (10)                                  # initialize count array as 0
    
    for i in range(0, n):                               # Store count of occurrences in count[]
        index = (arr[i]/exp1)
        count[ (index)%10 ] += 1
        
    for i in range(1,10):                               # Change count[i] so that count[i] now contains actual position of this digit in output array
        count[i] += count[i-1]
        
    i = n-1                                             # Build the output array
    while i>=0:
        index = (arr[i]/exp1)
        output[ count[ (index)%10 ] - 1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1
        
    i = 0                                               # Copying the output array to arr[], so that arr now contains sorted numbers
    for i in range(0,len(arr)):
        arr[i] = output[i]
 
# Method to do Radix Sort
def radixSort(arr):
    max1 = max(arr)                                     # Do counting sort for every digit. Note that instead of passing digit number, exp is passed. exp is 10^i where i is current digit number
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10
        
arr = [ 170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr) 
print arr
'''
Radix Sort
The lower bound for Comparison based sorting algorithm (Merge Sort, Heap Sort, Quick-Sort .. etc) is Theta(nLogn), i.e., they cannot do better than nLogn. 
Counting sort is a linear time sorting algorithm that sort in O(n+k) time when elements are in range from 1 to k.

What if the elements are in range from 1 to n2? 
 We can't use counting sort because counting sort will take O(n2) which is worse than comparison based sorting algorithms. Can we sort such an array in linear time?
Radix Sort is the answer. The idea of Radix Sort is to do digit by digit sort starting from least significant digit to most significant digit.
Radix sort uses counting sort as a subroutine to sort.

The Radix Sort Algorithm
1) Do following for each digit i where i varies from least significant digit to the most significant digit
a) Sort input array using counting sort (or any stable sort) according to the ith digit.

Example:
 Original, unsorted list:
170, 45, 75, 90, 802, 24, 2, 66
Sorting by least significant digit (1s place) gives: [*Notice that we keep 802 before 2, because 802 occurred before 2 in the original list, and similarly for pairs 170 & 90 and 45 & 75.]
170, 90, 802, 2, 24, 45, 75, 66
Sorting by next digit (10s place) gives: [*Notice that 802 again comes before 2 as 802 comes before 2 in the previous list.]
802, 2, 24, 45, 66, 170, 75, 90
Sorting by most significant digit (100s place) gives:
2, 24, 45, 66, 75, 90, 170, 802
What is the running time of Radix Sort?
 Let there be d digits in input integers. Radix Sort takes O(d*(n+b)) time where b is the base for representing numbers, for example, for decimal system, b is 10. What is the value of d?
 If k is the maximum possible value, then d would be O(logb(k)). So overall time complexity is O((n+b) * logb(k)). Which looks more than the time complexity of comparison based sorting algorithms
 for a large k. Let us first limit k. Let k <= nc where c is a constant. In that case, the complexity becomes O(nLogb(n)). But it still doesn't beat comparison based sorting algorithms.
 What if we make value of b larger?. What should be the value of b to make the time complexity linear? If we set b as n, we get the time complexity as O(n).
 In other words, we can sort an array of integers with range from 1 to nc if the numbers are represented in base n (or every digit takes log2(n) bits).
 
Is Radix Sort preferable to Comparison based sorting algorithms like Quick-Sort?
 If we have log2n bits for every digit, the running time of Radix appears to be better than Quick Sort for a wide range of input numbers. The constant factors hidden in asymptotic notation are higher for Radix Sort and Quick-Sort uses hardware caches more effectively. Also, Radix sort uses counting sort as a subroutine and counting sort takes extra space to sort numbers.

Implementation of Radix Sort
 Following is a simple C++ implementation of Radix Sort. For simplicity, the value of d is assumed to be 10. We recommend you to see Counting Sort for details of countSort()
 function in below code.


ShellSort
ShellSort is mainly a variation of Insertion Sort. In insertion sort, we move elements only one position ahead. When an element has to be moved far ahead, many movements are involved.
The idea of shellSort is to allow exchange of far items. In shellSort, we make the array h-sorted for a large value of h. We keep reducing the value of h until it becomes 1.
An array is said to be h-sorted if all sublists of every hth element is sorted.

def shellSort(arr):
 
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n/2
 
    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped 
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:
 
        for i in range(gap,n):
 
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]
 
            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
 
            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap /= 2
 
Time Complexity: O(n2).
In the above implementation gap is reduce by half in every iteration. There are many other ways to reduce gap which lead to better time complexity.


Comb Sort
Comb Sort is mainly an improvement over Bubble Sort. Bubble sort always compares adjacent values. So all inversions are removed one by one.
Comb Sort improves on Bubble Sort by using gap of size more than 1. The gap starts with a large value and shrinks by a factor of 1.3 in every iteration until it reaches the value 1.
Thus Comb Sort removes more than one inversion counts with one swap and performs better than Bubble Sort.

The shrink factor has been empirically found to be 1.3 (by testing Combsort on over 200,000 random lists) [Source: Wiki]
Although, it works better than Bubble Sort on average, worst case remains O(n2).

# To find next gap from current
def getNextGap(gap):
    # Shrink gap by Shrink factor
    gap = (gap * 10)/13
    if gap < 1:
        return 1
    return gap
 
# Function to sort arr[] using Comb Sort
def combSort(arr):
    n = len(arr)
    
    # Initialize gap
    gap = n
 
    # Initialize swapped as true to make sure that
    # loop runs
    swapped = True
 
    # Keep running while gap is more than 1 and last iteration caused a swap
    while gap !=1 or swapped == 1:
        # Find next gap
        gap = getNextGap(gap)
 
        # Initialize swapped as false so that we can
        # check if swap happened or not
        swapped = False
 
        # Compare all elements with current gap
        for i in range(0, n-gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap]=arr[i + gap], arr[i]
                swapped = True

Illustration:

Let the array elements be
8, 4, 1, 56, 3, -44, 23, -6, 28, 0

Initially gap value = 10
 After shrinking gap value => 10/1.3 = 7;
 8 4 1 56 3 -44 23 -6 28 0
-6 4 1 56 3 -44 23  8 28 0
-6 4 0 56 3 -44 23  8 28 1


New gap value => 7/1.3 = 5;
-44 4 0 56 3 -6 23 8 28 1
-44 4 0 28 3 -6 23 8 56 1
-44 4 0 28 1 -6 23 8 56 3


New gap value => 5/1.3 = 3;
-44 1  0 28 4 -6 23 8 56 3
-44 1 -6 28 4  0 23 8 56 3
-44 1 -6 23 4  0 28 8 56 3
-44 1 -6 23 4  0  3 8 56 28


New gap value => 3/1.3 = 2;
-44 1 -6 0 4 23 3 8 56 28
-44 1 -6 0 3 23 4 8 56 28
-44 1 -6 0 3 8 4 23 56 28


New gap value => 2/1.3 = 1;
-44 -6 1 0 3 8 4 23 56 28
-44 -6 0 1 3 8 4 23 56 28
-44 -6 0 1 3 4 8 23 56 28
-44 -6 0 1 3 4 8 23 28 56 

no more swaps required (Array sorted)
Time Complexity : Worst case complexity of this algorithm is O(n2) and the Best Case complexity is O(n). 
Auxiliary Space :  O(1)


Pigeonhole Sort
Pigeonhole sorting is a sorting algorithm that is suitable for sorting lists of elements where the number of elements and the number of possible key values are approximately the same.
 It requires O(n + Range) time where n is number of elements in input array and 'Range' is number of possible values in array.
 
Working of Algorithm : 
1.Find minimum and maximum values in array. Let the minimum and maximum values be 'min' and 'max' respectively. Also find range as 'max-min-1'. 
2.Set up an array of initially empty 'pigeonholes' the same size as of the range.
3.Visit each element of the array and then put each element in its pigeonhole. An element arr[i] is put in hole at index arr[i] - min.
4.Start the loop all over the pigeonhole array in order and put the elements from non- empty holes back into the original array.

Comparison with Counting Sort : 
 It is similar to counting sort, but differs in that it 'moves items twice: once to the bucket array and again to the final destination'.
 
#   Algorithm_Implementation/Sorting/Pigeonhole_sort"
def pigeonhole_sort(a):
    # size of range of values in the list 
    # (ie, number of pigeonholes we need)
    my_min = min(a)
    my_max = max(a)
    size = my_max - my_min + 1
 
    # our list of pigeonholes
    holes = [0] * size
 
    # Populate the pigeonholes.
    for x in a:
        assert type(x) is int, "integers only please"
        holes[x - my_min] += 1
 
    # Put the elements back into the array in order.
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + my_min
            i += 1
Pigeonhole sort has limited use as requirements are rarely met. For arrays where range is much larger than n, bucket sort is a generalization that is more efficient in space and time.

Bucket Sort
Bucket sort is mainly useful when input is uniformly distributed over a range. For example, consider the following problem. 
Sort a large set of floating point numbers which are in range from 0.0 to 1.0 and are uniformly distributed across the range. How do we sort the numbers efficiently?

A simple way is to apply a comparison based sorting algorithm. The lower bound for Comparison based sorting algorithm (Merge Sort, Heap Sort, Quick-Sort .. etc) is Theta(nLogn), i.e.,
they cannot do better than nLogn.
 Can we sort the array in linear time? Counting sort can not be applied here as we use keys as index in counting sort. Here keys are floating point numbers. 
 The idea is to use bucket sort. Following is bucket algorithm.

bucketSort(arr[], n)
1) Create n empty buckets (Or lists).
2) Do following for every array element arr[i]
    a) Insert arr[i] into bucket[n*array[i]]
3) Sort individual buckets using insertion sort.
4) Concatenate all sorted buckets.

BucketSort
Time Complexity: If we assume that insertion in a bucket takes O(1) time then steps 1 and 2 of the above algorithm clearly take O(n) time.
The O(1) is easily possible if we use a linked list to represent a bucket (In the following code, C++ vector is used for simplicity).
Step 4 also takes O(n) time as there will be n items in all buckets.
The main step to analyze is step 3. This step also takes O(n) time on average if all numbers are uniformly distributed (please refer CLRS book for more details)

// C++ program to sort an array using bucket sort
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
 
// Function to sort arr[] of size n using bucket sort
void bucketSort(float arr[], int n)
{
    // 1) Create n empty buckets
    vector<float> b[n];
    
    // 2) Put array elements in different buckets
    for (int i=0; i<n; i++)
    {
       int bi = n*arr[i]; // Index in bucket
       b[bi].push_back(arr[i]);
    }
 
    // 3) Sort individual buckets
    for (int i=0; i<n; i++)
       sort(b[i].begin(), b[i].end());
 
    // 4) Concatenate all buckets into arr[]
    int index = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < b[i].size(); j++)
          arr[index++] = b[i][j];
}
 
/* Driver program to test above funtion */
int main()
{
    float arr[] = {0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434};
    int n = sizeof(arr)/sizeof(arr[0]);
    bucketSort(arr, n);
 
    cout << "Sorted array is \n";
    for (int i=0; i<n; i++)
       cout << arr[i] << " ";
    return 0;
}

Output: 
Sorted array is
0.1234 0.3434 0.565 0.656 0.665 0.897

Bucket Sort To Sort an Array with Negative Numbers
How to modify Bucket Sort to sort both positive and negative numbers?

Example:
Input : arr[] = { -0.897, 0.565, 0.656, -0.1234, 0, 0.3434 } 
Output : -0.897 -0.1234  0 0.3434 0.565 0.656 

Here we considering number is in range -1.0 to 1.0 (floating point number)
 Algorithm :
sortMixed(arr[], n)
1) Split array into two parts 
   create two Empty vector Neg[], Pos[] 
   (for negative and positive element respectively)
   Store all negative element in Neg[] by converting
   into positive (Neg[i] = -1 * Arr[i] )
   Store all +ve in pos[]  (pos[i] =  Arr[i])
2) Call function bucketSortPositive(Pos, pos.size())
   Call function bucketSortPositive(Neg, Neg.size())

bucketSortPositive(arr[], n)
3) Create n empty buckets (Or lists).
4) Do following for every array element arr[i]. 
       a) Insert arr[i] into bucket[n*array[i]]
5) Sort individual buckets using insertion sort.
6) Concatenate all sorted buckets. 

Below is c++ implementation of above idea (for floating point number )

// C++ program to sort an array of positive
// and negative numbers using bucket sort
#include <bits/stdc++.h>
using namespace std;
 
// Function to sort arr[] of size n using
// bucket sort
void bucketSort(vector<float> &arr, int n)
{
    // 1) Create n empty buckets
    vector<float> b[n];
 
    // 2) Put array elements in different
    //    buckets
    for (int i=0; i<n; i++)
    {
        int bi = n*arr[i]; // Index in bucket
        b[bi].push_back(arr[i]);
    }
 
    // 3) Sort individual buckets
    for (int i=0; i<n; i++)
        sort(b[i].begin(), b[i].end());
 
    // 4) Concatenate all buckets into arr[]
    int index = 0;
    arr.clear();
    for (int i = 0; i < n; i++)
        for (int j = 0; j < b[i].size(); j++)
            arr.push_back(b[i][j]);
}
 
// This function mainly slpits array into two
// and then calls bucketSort() for two arrays.
void sortMixed(float arr[], int n)
{
    vector<float>Neg ;
    vector<float>Pos;
 
    // traverse array elements
    for (int i=0; i<n; i++)
    {
        if (arr[i] < 0)
 
            // store -Ve elements by
            // converting into +ve element
            Neg.push_back (-1 * arr[i]) ;
        else
            // store +ve elements
            Pos.push_back (arr[i]) ;
    }
 
    bucketSort(Neg, (int)Neg.size());
    bucketSort(Pos, (int)Pos.size());
 
    // First store elements of Neg[] array
    // by converting into -ve
    for (int i=0; i < Neg.size(); i++)
        arr[i] = -1 * Neg[ Neg.size() -1 - i];
 
    // store +ve element
    for(int j=Neg.size(); j < n; j++)
        arr[j] = Pos[j - Neg.size()];
}
 
/* Driver program to test above function */
int main()
{
    float arr[] = {-0.897, 0.565, 0.656,
                   -0.1234, 0, 0.3434};
    int n = sizeof(arr)/sizeof(arr[0]);
    sortMixed(arr, n);
 
    cout << "Sorted array is \n";
    for (int i=0; i<n; i++)
        cout << arr[i] << " ";
    return 0;
}

Output:
Sorted array is 
-0.897  -0.1234 0 0.3434 0.565 0.656
'''
