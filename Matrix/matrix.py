#!/usr/bin/python
'''
https://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/
https://www.geeksforgeeks.org/a-boolean-matrix-question/
https://www.geeksforgeeks.org/print-unique-rows/
https://www.geeksforgeeks.org/inplace-m-x-n-size-matrix-transpose/
https://www.geeksforgeeks.org/dynamic-programming-set-27-max-sum-rectangle-in-a-2d-matrix/
https://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/
https://www.geeksforgeeks.org/c-program-find-transpose-matrix/
https://www.geeksforgeeks.org/zigzag-or-diagonal-traversal-of-matrix/
'''
def printMatrix(mat):
    for i in xrange(0, len(mat)):
        for j in xrange(0, len(mat[0])):
            print mat[i][j],
        print ""

# Min Cost Path
# Time complexity: O(mn)
def minCost(cost, m, n):
    R = 3
    C = 3
    tc = [[0 for x in range(C)] for x in range(R)]                          # Instead of following line, we can use int tc[m+1][n+1] or dynamically allocate memory to save space. The following line is used to keep te program simple and make it working on all compilers.
    tc[0][0] = cost[0][0]
    
    for i in range(1, m+1):                                                 # Initialize first column of total cost(tc) array
        tc[i][0] = tc[i-1][0] + cost[i][0]
        
    for j in range(1, n+1):                                                 # Initialize first row of tc array
        tc[0][j] = tc[0][j-1] + cost[0][j]
        
    for i in range(1, m+1):                                                 # Construct rest of the tc array
        for j in range(1, n+1):
            tc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j]
 
    return tc[m][n]
'''
Given a boolean matrix mat[M][N] of size M X N, modify it such that if a matrix cell mat[i][j] is 1 (or true) then make all the cells of ith row and jth column as 1. 
Example 3
The matrix
1 0 0 1
0 0 1 0
0 0 0 0
should be changed to following
1 1 1 1
1 1 1 1
1 0 1 1
'''
def modifyMatrix(mat):
  row_flag = False
  col_flag = False

  for i in range(0, len(mat)):
    for j in range(0, len(mat[0])):
      if i == 0 and mat[i][j] == 1:
        row_flag = True
      if j == 0 and mat[i][j] == 1:
        col_flag = True
      if mat[i][j] == 1:
        mat[0][j] = 1
        mat[i][0] = 1

  for i in range(1, len(mat)):
    for j in range(1, len(mat[0])):
      if (mat[0][j] == 1 or mat[i][0] == 1):
        mat[i][j] = 1
        
  if (row_flag == True):
    for i in range(0, len(mat[0])):
      mat[0][i] = 1

  if (col_flag == True):
    for i in range(0, len(mat)):
      mat[i][0] = 1
      
# Time complexity: O(n2)
def areSame(A, B, m, n):
  for i in xrange(m):
    for j in xrange(n):
      if A[i][j] != B[i][j]:
        return 0
  return 1

def transpose(A, B, m, n):
  for i in xrange(m):
    for j in xrange(n):
      B[i][j] = A[j][i]

def subtract(A, B, C, m, n):
  for i in xrange(m):
    for j in xrange(n):
      C[i][j] = A[i][j] - B[i][j]

'''
Searches the element x in mat[][]. If the element is found, then prints its position and returns true, otherwise prints "not found" and returns false
Time Complexity: O(n)
Check it https://www.geeksforgeeks.org/search-element-sorted-matrix/
'''
def search(mat, n, x):
  i = 0
  j = n-1
  while (i < n and j >= 0):
    if mat[i][j] == x:
      print "\n Element found at mat[%d][%d]" %(i,j)
      return
    if mat[i][j] > x:
      j -= 1
    else:
      i += 1
  print "\nElement not found"
  return

# Python program to count all possible paths to reach cell at row number m and column number n from top left to bottom right
# Know this but refer the solution to this below to avoid overlapping subproblems issue
def numberOfPaths(m, n):
   if(m == 1 or n == 1):
        return 1
      
   return numberOfPaths(m-1, n) + numberOfPaths(m, n-1)                  # If diagonal movements are allowed then the last addition is required.

'''
The time complexity of above recursive solution is exponential. There are many overlapping subproblems.
We can draw a recursion tree for numberOfPaths(3, 3) and see many overlapping subproblems.
The recursion tree would be similar to  Recursion tree for Longest Common Subsequence problem. So this problem has both properties (see https://www.geeksforgeeks.org/longest-common-subsequence
and https://www.geeksforgeeks.org/dynamic-programming-set-1) of a dynamic programming problem. Like other typical Dynamic Programming(DP) problems,
recomputations of same subproblems can be avoided by constructing a temporary array count[][] in bottom up manner using the above recursive formula.
Refer:
https://www.geeksforgeeks.org/longest-common-subsequence/
https://www.geeksforgeeks.org/dynamic-programming-set-1/
https://www.geeksforgeeks.org/dynamic-programming-set-2-optimal-substructure-property/
Time complexity: O(mn)
'''
def numberOfPaths2(m, n):
    count = [[0 for x in range(m)] for y in range(n)]                         # Create a 2D table to store results of subproblems
    
    for i in range(m):                                                        # Count of paths to reach any cell in first column is 1
        count[i][0] = 1
        
    for j in range(n):                                                        # Count of paths to reach any cell in first column is 1
        count[0][j] = 1
        
    for i in range(1, m):                                                     # Calculate count of paths for other cells in bottom-up manner using the recursive solution
        for j in range(n):             
            count[i][j] = count[i-1][j] + count[i][j-1]
    return count[m-1][n-1]

'''
Input : 
        1    2   3   4   5
        6    7   8   9   10
        11   12  13  14  15
        16  17  18  19   20
Output :
1 2 3 4 5 10 9 8 7 6 11 12 13 14 15 20 19 18 17 16 


Input :
        10--->24--->32
                    |
                    v
        50<---6<---17   
        |
        v
        99--->10--->11  
         
Output :
10 24 32 17 6 50 99 10 11

Time complexity: O(row*column)
'''
def printZigZag(a, row, col):
  evenRow = 0
  oddRow = 1

  while (evenRow<row and oddRow<row):
    for i in xrange(0, col):
      print a[evenRow][i],
    evenRow = evenRow + 2

    for j in reversed(xrange(0, col)):
      print a[oddRow][j],
    oddRow = oddRow + 2

'''
Given matrix is
    1     2     3     4
    5     6     7     8
    9    10    11    12
   13    14    15    16
   17    18    19    20

Diagonal printing of matrix is
    1
    5     2
    9     6     3
   13    10     7     4
   17    14    11     8
   18    15    12
   19    16
   20
   
Observe the sequence
          1 /  2 /  3 /  4
           / 5  /  6 /  7 /  8
               /  9 / 10 / 11 / 12
                   / 13 / 14 / 15 / 16
                       / 17 / 18 / 19 / 20

'''
def diagonalOrder(arr, R, C):
  for k in xrange(0, R):
    print arr[k][0],
    i = k - 1
    j = 1

    while isValid(i, j, R, C):
      print arr[i][j],
      i -= 1
      j += 1
    print "\n"
    
  for k in xrange(1, C):
    print arr[R-1][k],
    i = R - 2
    j = k + 1

    while isValid(i, j, R, C):
      print arr[i][j],
      i -= 1
      j += 1
    print "\n"

def isValid(i, j, R, C):
  if (i < 0 or i >= R or j >= C or j < 0):
    return False
  return True

# Function print matrix in spiral form
'''
Input:
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16],
          [17, 18, 19, 20]

Output: 1 2 3 4 8 12 16 20 19 18 17 13 9 5 6 7 11 15 14 10

Observation:
           1--->2--->3--->4
                          |
                          V
        5-->6-->7-->      8
        ^           |     |
        |           V     V
        9    10     11    12
        ^    ^      |     |
        |    |      V     V
        13   14<---15    16
        ^                 |
        |                 |
        |                 V
       17<---18<---19<---20
Time Complexity: O(mn)
'''
def printSpiral(a, m, n):
  k = 0
  l = 0
  while (k < m and l < n):
    for i in xrange(l, n):
      print a[k][i],
    k += 1

    for i in xrange(k, m):
      print a[i][n-1],
    n -= 1

    if k < m:
      for i in reversed(xrange(l, n)):
        print a[m-1][i],
      m -= 1

    if l < n:
      for i in reversed(xrange(k, m)):
        print a[i][l],
      l += 1
'''
Print matrix in antispiral form https://www.geeksforgeeks.org/print-matrix-antispiral-form/
The idea is simple, we traverse matrix in spiral form and put all traversed elements in a stack. Finally one by one elements from stack and print them.
e.g.
Input:
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16],
          [17, 18, 19, 20]

Output: 10 14 15 11 7 6 5 9 13 17 18 19 20 16 12 8 4 3 2 1

Observation:
           1<---2<---3<---4
                          ^
                          |
        5<--6<--7<--      8
        |           ^     ^
        V           |     |
        9    10     11    12
        |    |      ^     ^
        V    V      |     |
        13   14--->15    16
        |                 ^
        |                 |
        V                 |
       17--->18--->19--->20
'''

# Code for Maximum size square sub-matrix with all 1s
'''
Algorithm:
 Let the given binary matrix be M[R][C]. The idea of the algorithm is to construct an auxiliary size matrix S[][] in which each entry S[i][j] represents size of the square sub-matrix
 with all 1s including M[i][j] where M[i][j] is the rightmost and bottommost entry in sub-matrix.
1) Construct a sum matrix S[R][C] for the given M[R][C].
     a)    Copy first row and first columns as it is from M[][] to S[][]
     b)    For other entries, use following expressions to construct S[][]
         If M[i][j] is 1 then
            S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
         Else /*If M[i][j] is 0*/
            S[i][j] = 0
2) Find the maximum entry in S[R][C]
3) Using the value and coordinates of maximum entry in S[i], print 
   sub-matrix of M[][]

For the given M[R][C] in above example, constructed S[R][C] would be: 
   0  1  1  0  1
   1  1  0  1  0
   0  1  1  1  0
   1  1  2  2  0
   1  2  2  3  1
   0  0  0  0  0
The value of maximum entry in above matrix is 3 and coordinates of the entry are (4, 3). Using the maximum value and its coordinates, we can find out the required sub-matrix.
Time Complexity: O(m*n) where m is number of rows and n is number of columns in the given matrix.
Auxiliary Space: O(m*n)
where m is number of rows and n is number of columns in the given matrix.
Algorithmic Paradigm: Dynamic Programming
'''
def printMaxSubSquare(M):
    R = len(M)
    C = len(M[0])
 
    S = [[0 for k in range(C)] for l in range(R)]                                               # here we have set the first row and column of S[][]
 
                                                                                                # Construct other entries
    for i in range(1, R):
        for j in range(1, C):
            if (M[i][j] == 1):
                S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
            else:
                S[i][j] = 0

    # Find the maximum entry and indices of maximum entry in S[][]
    max_of_s = S[0][0]
    max_i = 0
    max_j = 0
    for i in range(R):
        for j in range(C):
            if (max_of_s < S[i][j]):
                max_of_s = S[i][j]
                max_i = i
                max_j = j
 
    print "\nMaximum size sub-matrix is: "
    print max_i
    print max_j
    for i in range(max_i, max_i - max_of_s, -1):
        for j in range(max_j, max_j - max_of_s, -1):
            print M[i][j],
        print "\n"

# Finds the maximum area under the histogram represented by histogram.  See below article for details.
# https://www.geeksforgeeks.org/largest-rectangle-under-histogram/
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
        
def maxHist(R, C, row):
  result = Stack()
  i = top_val = max_area = area = 0
  while i < C:
    if (result.isEmpty() or row[result.peek()] <= row[i]):
      result.push(i)
      i += 1
    else:
      top_val = row[result.peek()]
      result.pop()
      area = top_val * i

      if (not result.isEmpty()):
        area = top_val * (i - result.peek() - 1 )
      max_area = max(area, max_area);

  while (not result.isEmpty()):
    top_val = row[result.peek()]
    result.pop()
    area = top_val * i
    if (not result.isEmpty()):
      area = top_val * (i - result.peek() - 1 )
    max_area = max(area, max_area);

  return max_area

# Returns area of the largest rectangle with all 1s in A[][]
'''
Maximum size rectangle binary sub-matrix with all 1s
Given a binary matrix, find the maximum size rectangle binary-sub-matrix with all 1's.
Input :   0 1 1 0
          1 1 1 1
          1 1 1 1
          1 1 0 0

Output :  1 1 1 1
          1 1 1 1
We have discussed a dynamic programming based solution for finding largest square with 1s. 
In this post an interesting method is discussed that uses largest rectangle under histogram as a subroutine. Below are steps.
The idea is to update each column of a given row with corresponding column of previous row and find largest histogram area for for that row.

Step 1: Find maximum area for row[0]
Step 2:
    for each row in 1 to N - 1
        for each column in that row
            if A[row][column] == 1
              update A[row][column] with
                A[row][column] += A[row - 1][column]
    find area for that row
    and update maximum area so far 

Illustration : 
step 1:    0 1 1 0  maximum area  = 2
step 2:
    row 1  1 2 2 1  area = 4, maximum area becomes 4
    row 2  2 3 3 2  area = 8, maximum area becomes 8
    row 3  3 4 0 0  area = 6, maximum area remains 8

Time Complexity : O(R x X)
'''
def maxRectangle(R, C, A):
  result = maxHist(R,C,A[0])                                                                # Calculate area for first row and initialize it as result

  for i in xrange(1, R):                                                                    # iterate over row to find maximum rectangular area considering each row as histogram
    for j in xrange(0, C):
      if (A[i][j] == 1):
        A[i][j] += A[i - 1][j]
    result = max(result, maxHist(R,C,A[i]))
  return result

'''
Print unique rows in a given boolean matrix.py                  => https://www.geeksforgeeks.org/print-unique-rows/
Given a binary matrix, print all unique rows of the given matrix.
Input:
        {0, 1, 0, 0, 1}
        {1, 0, 1, 1, 0}
        {0, 1, 0, 0, 1}
        {1, 1, 1, 0, 0}
Output:
        0 1 0 0 1
        1 0 1 1 0
        1 1 1 0 0

Method 1 (Simple)
 A simple approach is to check each row with all processed rows. Print the first row. Now, starting from the second row, for each row, compare the row with already processed rows. If the row matches with any of the processed rows, don't print it. If the current row doesn't match with any row, print it.

Time complexity: O( ROW^2 x COL )
Auxiliary Space: O( 1 )

Method 2 (Use Binary Search Tree)
Find the decimal equivalent of each row and insert it into BST. Each node of the BST will contain two fields, one field for the decimal value, other for row number. Do not insert a node if it is duplicated. Finally, traverse the BST and print the corresponding rows.

Time complexity: O( ROW x COL + ROW x log( ROW ) )
Auxiliary Space: O( ROW )

This method will lead to Integer Overflow if number of columns is large.

Method 3 (Use Trie data structure)
Since the matrix is boolean, a variant of Trie data structure can be used where each node will be having two children one for 0 and other for 1. Insert each row in the Trie. If the row is already there, don't print the row. If row is not there in Trie, insert it in Trie and print it.
Time complexity: O( ROW x COL )
Auxiliary Space: O( ROW x COL )

This method(See below) has better time complexity. Also, relative order of rows is maintained while printing.
'''
class TrieNode:
  def __init__(self):
    self.isEndOfWord = False
    self.leaves = {}

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    cur = self.root
    
    for c in word:
      if c not in cur.leaves:
        cur.leaves[c] = TrieNode()
      cur = cur.leaves[c]
      
      if cur.isEndOfWord:                                                     # Duplicate found if isEndOfWord is True. Return False.
        return False
      
    cur.isEndOfWord = True
    return True

# Program to count islands in boolean 2D matrix
# Time complexity: O(ROW x COL)
'''
https://www.geeksforgeeks.org/find-number-of-islands/
What is an island?
 A group of connected 1s forms an island. For example, the below matrix contains 5 islands
	                {1, 1, 0, 0, 0},
                        {0, 1, 0, 0, 1},
                        {1, 0, 0, 1, 1},
                        {0, 0, 0, 0, 0},
                        {1, 0, 1, 0, 1}
'''
class Graph: 
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g
 
    # A function to check if a given cell (row, col) can be included in DFS
    def isSafe(self, i, j, visited):
        # row number is in range, column number is in range and value is 1 and not yet visited
        return (i >= 0 and i < self.ROW and
                j >= 0 and j < self.COL and
                not visited[i][j] and self.graph[i][j])
      
    # A utility function to do DFS for a 2D boolean matrix. It only considers the 8 neighbours as adjacent vertices
    def DFS(self, i, j, visited):
 
        # These arrays are used to get row and column numbers of 8 neighbours of a given cell
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]      
                                                                                                                                                # Mark this cell as visited
        visited[i][j] = True                                                                                                                    # Recur for all connected neighbours
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited)
                
    def countIslands(self):
        count = 0                                                                                                                               # Make a bool array to mark visited cells. Initially all cells are unvisited
        visited = [[False for j in range(self.COL)]for i in range(self.ROW)]
        
        for i in range(self.ROW):
            for j in range(self.COL):                                                                                                           # If a cell with value 1 is not visited yet, then new island found
                if visited[i][j] == False and self.graph[i][j] ==1:
                    self.DFS(i, j, visited)
                    count += 1
        return count

# find the row with maximum number of 1s
# Time Complexity: O(mLogn) where m is number of rows and n is number of columns in matrix.
'''
A simple method is to do a row wise traversal of the matrix, count the number of 1s in each row and compare the count with max.
Finally, return the index of row with maximum 1s. The time complexity of this method is O(m*n) where m is number of rows and n is number of columns in matrix.

We can do better. Since each row is sorted, we can use Binary Search to count of 1s in each row. We find the index of first instance of 1 in each row.
The count of 1s will be equal to total number of columns minus the index of first 1.
'''
def rowWithMax1s( mat):
    R = len(mat)
    C = len(mat[0])
    max_row_index = 0
    max = -1
    
    for i in range(0, R):
        index = first (mat[i], 0, C - 1)
        if index != -1 and C - index > max:
            max = C - index
            max_row_index = i
 
    return max_row_index

# find the index of first index of 1 in a boolean array arr[] 
def first( arr, low, high):
    if high >= low:
        mid = low + (high - low)//2
        
        if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1:
            return mid
        elif arr[mid] == 0:
            return first(arr, (mid + 1), high)
        else:
            return first(arr, low, (mid - 1))
    return -1

'''
The Celebrity Problem
In a party of N people, only one person is known to everyone. Such a person may be present in the party, if yes, (s)he doesn't know anyone in the party.
We can only ask questions like "does A know B?". Find the stranger (celebrity) in minimum number of questions.

We can describe the problem input as an array of numbers/characters representing persons in the party. We also have a hypothetical function HaveAcquaintance(A, B) which returns true if A knows B,
false otherwise. How can we solve the problem.

The idea is to use two pointers, one from start and one from the end. Assume the start person is A, and the end person is B. If A knows B, then A must not be the celebrity.
Else, B must not be the celebrity. We will find a celebrity candidate at the end of the loop. Go through each person again and check whether this is the celebrity.
'''
def knows(MATRIX, a, b):                                            # Returns true if a knows b, false otherwise
    if MATRIX[a][b] == 1:
        return True
    else:
        return False
    
def findCelebrity(M, n):                                            # Returns -1 if celebrity is not present. If present, returns id (value from 0 to n-1)
    a = 0                                                           # Initialize two pointers as two corners
    b = n - 1
    
    while (a < b):                                                  # Keep moving while the two pointers don't become same
        if knows(M, a, b):
            a+=1
        else:
            b-=1
            
    for i in xrange(0, n):                                          # Check if a is actually a celebrity or not
        if (i != a and (knows(M, a, i) or not knows(M, i, a))):     # If any person doesn't know 'a' or 'a' doesn't know any person, return -1
            return -1
    return a

'''
Stable Marriage Problem
The Stable Marriage Problem states that given N men and N women, where each person has ranked all members of the opposite sex in order of preference, marry the men and women together such that
there are no two people of opposite sex who would both rather have each other than their current partners. If there are no such people, all the marriages are "stable" (Source Wiki).

Consider the following example.
Let there be two men m1 and m2 and two women w1 and w2.
 Let m1's list of preferences be {w1, w2}
 Let m2's list of preferences be {w1, w2}
 Let w1's list of preferences be {m1, m2}
 Let w2's list of preferences be {m1, m2}

The matching { {m1, w2}, {w1, m2} } is not stable because m1 and w1 would prefer each other over their assigned partners. The matching {m1, w1} and {m2, w2} is stable because there are no
two people of opposite sex that would prefer each other over their assigned partners.

It is always possible to form stable marriages from lists of preferences (See references for proof). Following is Gale-Shapley algorithm to find a stable matching:
The idea is to iterate through all free men while there is any free man available. Every free man goes to all women in his preference list according to the order.
For every woman he goes to, he checks if the woman is free, if yes, they both become engaged. If the woman is not free, then the woman chooses either says no to him or dumps her
current engagement according to her preference list. So an engagement done once can be broken if a woman gets better option.

Following is complete algorithm from Wiki
Initialize all men and women to free
while there exist a free man m who still has a woman w to propose to 
{
    w = m's highest ranked such woman to whom he has not yet proposed
    if w is free
       (m, w) become engaged
    else some pair (m', w) already exists
       if w prefers m to m'
          (m, w) become engaged
           m' becomes free
       else
          (m', w) remain engaged    
}

Input & Output: Input is a 2D matrix of size (2*N)*N where N is number of women or men. Rows from 0 to N-1 represent preference lists of men and rows from N to 2*N - 1 represent preference lists
of women. So men are numbered from 0 to N-1 and women are numbered from N to 2*N - 1. The output is list of married pairs.
'''
N=4                                                                     # Number of Men or Women
# Prints stable matching for N boys and N girls. Boys are numbered as 0 to N-1. Girls are numbereed as N to 2N-1.
def stableMarriage(prefer):
    # Stores partner of women. This is our output array that stores pairng information.  The value of wPartner[i] indicates the partner assigned to woman N+i.  Note that
    wPartner=[-1]*N                                                     # the woman numbers between N and 2*N-1. The value -1 indicates that (N+i)'th woman is free
    mFree=[False]*N                                                     # An array to store availability of men.  If mFree[i] is false, then man 'i' is free, otherwise engaged.
    freeCount = N                                                       # Initialize all men and women as free

    while (freeCount > 0):                                              # While there are free men
        for m in xrange(0, N):                                          # Pick the first free man (we could pick any)
            if (mFree[m] == False):
                break

        for i in xrange(0, N):                                          # One by one go to all women according to m's preferences. Here m is the picked free man
            if mFree[m] == False:
                w = prefer[m][i]
            if (wPartner[w-N] == -1):                                   # The woman of preference is free, w and m become  partners (Note that the partnership maybe changed later).
                wPartner[w-N] = m                                       # So we can say they are engaged not married
                mFree[m] = True
                freeCount-=1
            else:                                                       # If w is not free
                m1 = wPartner[w-N];                                     # Find current engagement of w

                if (wPrefersM1OverM(prefer, w, m, m1) == False):        # If w prefers m over her current engagement m1, then break the engagement between w and m1 and engage m with w.
                    wPartner[w-N] = m;
                    mFree[m] = True;
                    mFree[m1] = False                                   # End of the for loop that goes to all women in m's list

    print "Woman   Man"
    for i in xrange(0, N):
        print " ", i+N, "\t", wPartner[i]
        
# This function returns true if woman 'w' prefers man 'm1' over man 'm'
def wPrefersM1OverM(prefer, w, m, m1):
    for i in xrange(0, N):                                              # Check if w prefers m over her current engagment m1
        if (prefer[w][i] == m1):                                        # If m1 comes before m in lisr of w, then w prefers her cirrent engagement, don't do anything
            return True

        if (prefer[w][i] == m):                                         # If m cmes before m1 in w's list, then free her current engagement and engage her with m
           return False
        
prefer = [ [7, 5, 6, 4],
        [5, 4, 6, 7],
        [4, 5, 6, 7],
        [4, 5, 6, 7],
        [0, 1, 2, 3],
        [0, 1, 2, 3],
        [0, 1, 2, 3],
        [0, 1, 2, 3],]
stableMarriage(prefer)

M = [[ 0, 0, 1, 0 ],
     [ 0, 0, 1, 0 ],
     [ 0, 0, 0, 0 ],
     [ 0, 0, 1, 0 ]];
n = 4;
result = findCelebrity(M, n)
if (result == -1):
    print "No Celebrity"
else:
    print "Celebrity ID ",result

'''
Other Solutions:
We measure the complexity in terms of calls made to HaveAcquaintance().
Method 1 (Graph)
We can model the solution using graphs. Initialize indegree and outdegree of every vertex as 0. If A knows B, draw a directed edge from A to B, increase indegree of B and outdegree of A by 1.
Construct all possible edges of the graph for every possible pair [i, j]. We have NC2 pairs. If celebrity is present in the party, we will have one sink node in the graph with outdegree of zero,
and indegree of N-1. We can find the sink node in (N) time, but the overall complexity is O(N2) as we need to construct the graph first.

Method 2 (Recursion)
We can decompose the problem into combination of smaller instances. Say, if we know celebrity of N-1 persons, can we extend the solution to N? We have two possibilities, Celebrity(N-1) may know N,
or N already knew Celebrity(N-1). In the former case, N will be celebrity if N doesn't know anyone else. In the later case we need to check that Celebrity(N-1) doesn't know N.

Solve the problem of smaller instance during divide step. On the way back, we find the celebrity (if present) from the smaller instance. During combine stage,
check whether the returned celebrity is known to everyone and he doesn't know anyone. The recurrence of the recursive decomposition is,
T(N) = T(N-1) + O(N)
T(N) = O(N2). You may try writing pseudo code to check your recursion skills.

Method 3 (Using Stack)
 The graph construction takes O(N2) time, it is similar to brute force search. In case of recursion, we reduce the problem instance by not more than one, and also combine step may examine M-1
 persons (M - instance size).

We have following observation based on elimination technique (Refer Polya's How to Solve It book).
.If A knows B, then A can't be celebrity. Discard A, and B may be celebrity.
.If A doesn't know B, then B can't be celebrity. Discard B, and A may be celebrity.
.Repeat above two steps till we left with only one person.
.Ensure the remained person is celebrity. (Why do we need this step?)

We can use stack to verity celebrity.
1.Push all the celebrities into a stack.
2.Pop off top two persons from the stack, discard one person based on return status of HaveAcquaintance(A, B).
3.Push the remained person onto stack.
4.Repeat step 2 and 3 until only one person remains in the stack.
5.Check the remained person in stack doesn't have acquaintance with anyone else.

We will discard N elements utmost (Why?). If the celebrity is present in the party, we will call HaveAcquaintance() 3(N-1) times. Here is code using stack.

Complexity O(N). Total comparisons 3(N-1). Try the above code for successful MATRIX {{0, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 1}}.

Note: You may think that why do we need a new graph as we already have access to input matrix. Note that the matrix MATRIX used to help the hypothetical function HaveAcquaintance(A, B),
but never accessed via usual notation MATRIX[i, j]. We have access to the input only through the function HaveAcquiantance(A, B). Matrix is just a way to code the solution.
We can assume the cost of hypothetical function as O(1).

If still not clear, assume that the function HaveAcquiantance accessing information stored in a set of linked lists arranged in levels. List node will have next and nextLevel pointers.
Every level will have N nodes i.e. an N element list, next points to next node in the current level list and the nextLevel pointer in last node of every list will point to head of next level list.
For example the linked list representation of above matrix looks like,

L0 0->0->1->0
             |
L1           0->0->1->0
                       |
L2                     0->0->1->0
                                 |
L3                               0->0->1->0

The function HaveAcquanintance(i, j) will search in the list for j-th node in the i-th level. Out goal is to minimize calls to HaveAcquanintance function.
'''
    
if __name__=="__main__":
  A = [ [1, 1, 1, 1],
        [2, 2, 2, 2],
        [3, 3, 3, 3],
        [4, 4, 4, 4] ]

  B = [ [1, 1, 1, 1],
        [2, 2, 2, 2],
        [3, 3, 3, 3],
        [4, 4, 4, 4] ]

  # 4x4 matrix
  m = 4
  n = 4
  if areSame(A, B, m, n):
    print "Matrices are identical"
  else:
    print "Matrices are not identical"

  print "matrix before transpose is \n"
  for i in xrange(m):
    for j in xrange(n):
      print A[i][j],
  transpose(A, B, m, n)
  print ("Result matrix after transpose is\n");
  for i in xrange(m):
    for j in xrange(n):
      print B[i][j],

  C = [[None] * m for i in xrange(n)]
  subtract(A, B, C, m, n)
  print "Result matrix after subtraction is\n"
  for i in xrange(m):
    for j in xrange(n):
      print C[i][j],

  mat = [ [10, 20, 30, 40],
          [15, 25, 35, 45],
          [27, 29, 37, 48],
          [32, 33, 39, 50] ]
  search(mat, 4, 29)

  print "\nNo of paths of a m*n matrix is", (numberOfPaths(m, n))
  print "\n2. No of paths of a m*n matrix is", (numberOfPaths2(m, n))

  M = [ [0, 1, 0, 0, 1],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0] ]
  t = Trie()
  for row in M:
    if t.insert(row):
      print row

  r = 4
  c = 5
  mat = [ [1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20] ]
  printZigZag(mat, r , c)

  arr = [ [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16],
          [17, 18, 19, 20] ]

  r=len(arr)
  c=len(arr[0])
  print "\nPrinting matrix diagonally...\n"
  diagonalOrder(arr, r, c)

  print "\nSpiral printing..."
  printSpiral(arr, r, c)

  M = [[0, 1, 1, 0, 1],
       [1, 1, 0, 1, 0],
       [0, 1, 1, 1, 0],
       [1, 1, 1, 1, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0]]
  printMaxSubSquare(M)
  '''
  Output:
  Maximum size sub-matrix is: 
  1 1 1 
  1 1 1 
  1 1 1
  '''
  M = [ [0, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0] ]

  print "Area of maximum rectangle is ",maxRectangle(4, 4, M)

  graph = [ [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]]

  row = len(graph)
  col = len(graph[0])
  g= Graph(row, col, graph)
  print "Number of islands is :",
  print g.countIslands()

'''
Min Cost Path

Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function that returns cost of minimum cost path to reach (m, n) from (0, 0).
Each cell of the matrix represents a cost to traverse through that cell. Total cost of a path to reach (m, n) is sum of all the costs on that path (including both source and destination).
You can only traverse down, right and diagonally lower cells from a given cell, i.e.,
from a given cell (i, j), cells (i+1, j), (i, j+1) and (i+1, j+1) can be traversed. You may assume that all costs are positive integers.

For example, in the following figure, what is the minimum cost path to (2, 2)?
1 2 3
4 8 2
1 5 3

The path with minimum cost is highlighted in the following figure. The path is (0, 0) -> (0, 1) -> (1, 2) -> (2, 2). The cost of the path is 8 (1 + 2 + 2 + 3).
'''
cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print minCost(cost, 2, 2)

mat = [[1, 0, 0, 1],
       [0, 0, 1, 0],
       [0, 0, 0, 0]]
print "Matrix before modification..."
printMatrix(mat)
modifyMatrix(mat)
print "Matrix after modification..."
printMatrix(mat)

mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]
print ("Index of row with maximum 1s is", rowWithMax1s(mat))
'''
Check it
https://www.geeksforgeeks.org/find-the-largest-rectangle-of-1s-with-swapping-of-columns-allowed/
https://www.geeksforgeeks.org/search-element-sorted-matrix/

https://www.geeksforgeeks.org/inplace-m-x-n-size-matrix-transpose/
https://www.geeksforgeeks.org/balanced-expressions-such-that-given-positions-have-opening-brackets/
https://www.geeksforgeeks.org/maximum-number-of-trailing-zeros-in-the-product-of-the-subsets-of-size-k/
'''
