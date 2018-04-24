# Largest Sum Contiguous Subarray =>  Kadanea's Algorithm:
# Time Complexity:  O(n)
def maxSubArraySum(a,size):
    max_so_far =a[0]
    curr_max = a[0]
     
    for i in range(1,size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
         
    return max_so_far

'''
Dynamic Programming | Set 33 (Find if a string is interleaved of two other strings)
The main function that returns true if C is an interleaving of A and B, otherwise false.

Given three strings A, B and C. Write a function that checks whether C is an interleaving of A and B.
C is said to be interleaving A and B,
        i. if it contains all characters of A and B and
        ii. order of all characters in individual strings is preserved
e.g.
XXZXXXY is NOT interleaved of XXY and XXZ
WZXY is interleaved of XY and WZ
XXY is interleaved of XY and X
XXY is NOT interleaved of YX and X
XXXXZY is interleaved of XXY and XXZ

Print all interleavings of given two strings
Given two strings str1 and str2, write a function that prints all interleavings of the given two strings. You may assume that all characters in both strings are different 

Example:
Input: str1 = "AB",  str2 = "CD"
Output:
    ABCD
    ACBD
    ACDB
    CABD
    CADB
    CDAB

a) If first character of C matches with first character of A, we move one character ahead in A and C and recursively check.
b) If first character of C matches with first character of B, we move one character ahead in B and C and recursively check.
If any of the above two cases is true, we return true, else false. Following is simple recursive implementation of this approach
Time Complexity: O(MN)
Auxiliary Space: O(MN)
'''
def isInterleaved(A, B, C):
    M = len(A)
    N = len(B)
    
    IL = [[False]*(N+1) for i in xrange(M+1)]                       # Let us create a 2D table to store solutions of subproblems.  C[i][j] will be true if C[0..i+j-1] is an interleaving of A[0..i-1] and B[0..j-1]
    
    if ((M+N) != len(C)):                                           # C can be an interleaving of A and B only of sum of lengths of A & B is equal to length of C.
       return False
    
    for i in xrange(0, M+1):                                        # Process all characters of A and B
        for j in xrange(0, N+1):
            if (i==0 and j==0):                                     # Both are empty
                IL[i][j] = True
            elif (i==0 and B[j-1]==C[j-1]):                         # A is empty
                IL[i][j] = IL[i][j-1]
            elif (j==0 and A[i-1]==C[i-1]):                         # B is empty 
                IL[i][j] = IL[i-1][j]
            elif(A[i-1]==C[i+j-1] and B[j-1]!=C[i+j-1]):            # Current character of C matches with current character of A,but doesn't match with current character of B
                IL[i][j] = IL[i-1][j]
            elif (A[i-1]!=C[i+j-1] and B[j-1]==C[i+j-1]):           # Current character of C matches with current character of B,but doesn't match with current character of A
                IL[i][j] = IL[i][j-1]
            elif (A[i-1]==C[i+j-1] and B[j-1]==C[i+j-1]):           # Current character of C matches with that of both A and B
                IL[i][j]=(IL[i-1][j] or IL[i][j-1])
    return IL[M][N]

# print all interleavings of given two strings. This solution is not dp based. I've just put here as an extension to the above problem statement.
# Also check https://www.geeksforgeeks.org/check-whether-a-given-string-is-an-interleaving-of-two-other-given-strings-set-2/
def printIls(str1, str2):
    m = len(str1)
    n = len(str2)
    iStr = [''] * (m+n)
    
    printIlsRecur(str1, str2, iStr, m, n, 0)
    
def printIlsRecur(str1, str2, iStr, m, n, i):
    if m==0 and n==0:
        print ''.join(iStr)
        
    if m != 0:                                              # If some characters of str1 are left to be included, then include the first character from the remaining characters and recur for rest
        iStr[i] = str1[0]
        printIlsRecur(str1[1:], str2, iStr, m-1, n, i+1)
        
    if n != 0:                                              # If some characters of str2 are left to be included, then include the first character from the remaining characters and recur for rest
        iStr[i] = str2[0]
        printIlsRecur(str1, str2[1:], iStr, m, n-1, i+1)

A = "AB"
B = "CD"
printIls(A, B)
'''
Maximum Product Subarray
Given an array that contains both positive and negative integers, find the product of the maximum product subarray. Expected Time complexity is O(n) and only O(1) extra space can be used.

Examples:
Input: arr[] = {6, -3, -10, 0, 2}
Output:   180  // The subarray is {6, -3, -10}

Input: arr[] = {-1, -3, -10, 0, 60}
Output:   60  // The subarray is {60}

Input: arr[] = {-2, -3, 0, -2, -40}
Output:   80  // The subarray is {-2, -40}
Time Complexity: O(n)
Auxiliary Space: O(1)
'''
# find maximum product subarray
def maxsubarrayproduct(arr):
    n = len(arr)
    max_ending_here = 1
    min_ending_here = 1
    max_so_far = 1

    for i in range(0,n):
        if arr[i] > 0:  # If this element is positive, update max_ending_here. Update min_ending_here only if min_ending_here is  negative
            max_ending_here = max_ending_here*arr[i]
            min_ending_here = min (min_ending_here * arr[i], 1)
        elif arr[i] == 0: # If this element is 0, then the maximum product cannot end here, make both max_ending_here and min_ending_here 0 Assumption: Output is alway greater than or equal to 1.
            max_ending_here = 1
            min_ending_here = 1
        else:                           # If element is negative. This is tricky  max_ending_here can either be 1 or positive. i
            temp = max_ending_here      # max_ending_here * arr[i] next max_ending_here will be 1 if prev min_ending_here is 1, otherwise next max_ending_here will be prev min_ending_here * arr[i]
            max_ending_here = max (min_ending_here * arr[i], 1) #min_ending_here can either be 1 or negative. next min_ending_here will always be prev.
            min_ending_here = temp * arr[i]
        if (max_so_far <  max_ending_here):
            max_so_far  =  max_ending_here
    return max_so_far

# Longest increasing subsequence(LIS)
def lis(arr):
    n = len(arr)
    
    lis = [1]*n
    
    for i in range (1 , n):                   # Compute optimized LIS values in bottom up manner
        for j in range(0 , i):
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 :
                lis[i] = lis[j]+1

    maximum = 0
    for i in range(n):
        maximum = max(maximum , lis[i])

    return maximum

# Longest bitonic subsequence(LBS)  => a sequence which is first increasing and then decreasing
#Time Complexity: O(n^2)
#Auxiliary Space: O(n)
def lbs(arr):
    n = len(arr)

    lis = [1]*n

    for i in range(1, n):                                                                 # Compute LIS values from left to right
        for j in range(0 , i):
            if ((arr[i] > arr[j]) and (lis[i] < lis[j] +1)):
                lis[i] = lis[j] + 1

    lds = [1]*n                                                                           # allocate memory for LDS and initialize LDS values for all indexes

    for i in reversed(range(1, n)):                                                       # Compute LDS values from right to left
        for j in reversed(range(0 ,i)):
            if(arr[i] > arr[j] and lds[i] < lds[j] + 1):
                lds[i] = lds[j] + 1


    # Return the maximum value of (lis[i] + lds[i] - 1)
    maximum = lis[0] + lds[0] - 1
    for i in range(1 , n):
        maximum = max((lis[i] + lds[i]-1), maximum)

    return maximum

# Maximum Sum Increasing Subsequence (MSIS) problem
# Time Complexity: O(n^2)
def maxSumIS(arr, n):
    max = 0
    msis = [0 for x in range(n)]
    
    for i in range(n):
        msis[i] = arr[i]
        
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and msis[i] < msis[j] + arr[i]:
                msis[i] = msis[j] + arr[i]
                
    for i in range(n):
        if max < msis[i]:
            max = msis[i]
 
    return max

# program to find the length of the longest substring without repeating characters
# Time Complexity: O(n + d) where n is length of the input string and d is number of characters in input string alphabet.
# For example, if string consists of lowercase English characters then value of d is 26.
# Auxiliary Space: O(d) 
NO_OF_CHARS = 256
def longestUniqueSubsttr(string):
    n = len(string)
    cur_len = 1                                                           # To store the lenght of current substring
    max_len = 1                                                           # To store the result
    prev_index = 0                                                        # To store the previous index
    i = 0
    
    visited = [-1] * NO_OF_CHARS                                          # Initialize the visited array as -1, -1 is used to indicate  that character has not been visited yet.
    visited[ord(string[0])] = 0                                           # Mark first character as visited by storing the index of first character in visited array.
    
    for i in xrange(1,n):                                                 # Start from the second character. First character is already processed (cur_len and max_len are initialized as 1, and visited[str[0]] is set
        prev_index = visited[ord(string[i])]
        
        if prev_index == -1 or (i - cur_len > prev_index):                # If the currentt character is not present in the already processed substring or it is not part of the current NRCS, then do cur_len++
            cur_len+=1                                                    # If the current character is present in currently considered NRCS, then update NRCS to start from the next character of previous instance.
        else:
            if cur_len > max_len:
                max_len = cur_len
                print 'longest unique substring is = %s' %(string[prev_index:i])
 
            cur_len = i - prev_index
                                                                           # update the index of current character
        visited[ord(string[i])] = i
        
    if cur_len > max_len:
        max_len = cur_len
 
    return max_len

# LCS based function to find minimum number of insertions to form a palindrome
# Time complexity: O(n^2) and this method also requires O(n^2) extra space.
def findMinInsertionsLCS(strng):
    n=len(strng)
    return (n - lcs(strng, strng[::-1]))

# Longest Common Subsequence                     <= Use this function for Longest Palindromic Subsequence(lps)
# Time complexity: O(mn)
def lcs(X , Y):
    m = len(X)
    n = len(Y)
    
    L = [[None]*(n+1) for i in xrange(m+1)]                                     # declaring the array for storing the dp values
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
                
    return L[m][n]                                                              # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]

# Longest Common Substring
# Time Complexity: O(m*n)
# Auxiliary Space: O(m*n)
def lcSubstr(X , Y):
    m = len(X)
    n = len(Y)
    result = 0
    
    L = [[None]*(n+1) for i in xrange(m+1)]                                     
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
                result = max(result, L[i][j])
            else:
                L[i][j] = 0
                
    return result

def PrintLcSubstr(X , Y):
    m = len(X)
    n = len(Y)
    result = 0
    lcSubstr = ""
    
    L = [[None]*(n+1) for i in xrange(m+1)]                                     
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
                if L[i][j] > result:
                  result = L[i][j]
                  lcSubstr = X[i-result:i]
            else:
                L[i][j] = 0
                
    print "Longest common substring is ", lcSubstr

def printLcs(X, Y):
    m = len(X)
    n = len(Y)

    L = [[None]*(n+1) for i in xrange(m+1)]
    result = 0

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])

    index = L[m][n]                                                                   # Following code is used to print LCS
    lcs = [""] * (index+1)                                                            # Create a character array to store the lcs string
    lcs[index] = "\0"
    i = m                                                                             # Start from the right-most-bottom-most corner and one by one store characters in lcs[]
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:                                                          # If current character in X[] and Y are same, then current character is part of LCS
            lcs[index-1] = X[i-1]
            i-=1
            j-=1
            index-=1
        elif L[i-1][j] > L[i][j-1]:                                                   # If not same, then find the larger of two and go in the direction of larger value
            i-=1
        else:
            j-=1
    print "LCS of " + X + " and " + Y + " is " + "".join(lcs)

'''
Find the smallest window in a string containing all characters of another string
Given two strings string1 and string2, find the smallest substring in string1 containing all characters of string2 efficiently.
 For Example:
Input :  string = "this is a test string"
         pattern = "tist"
Output :  Minimum window is "t stri"
Explanation: "t stri" contains all the characters of pattern

Input :  string = "geeksforgeeks"
         pattern = "ork" 
Output :  Minimum window is "ksfor"

1- First check if length of string is less than the length of given pattern, if yes then "no such window can exist ".
2- Store the occurrence of characters of given pattern in a hash_pat[].
3- Start matching the characters of pattern with the characters of string i.e. increment count if a character matches
4- Check if (count == length of pattern ) this means a window is found
5- If such window found, try to minimize it by removing extra characters from beginning of current window.
6- Update min_length.
7- Print the minimum length window.
'''
no_of_chars = 256
import sys
def findSubString(strng, pat):
    len1 = len(strng)
    len2 = len(pat)
    
    if len1 < len2:
        print "No such window can exist!"
        return
    hash_str = [0]*no_of_chars
    hash_pat = [0]*no_of_chars
    
    for i in xrange(0, len2):
        hash_pat[ord(pat[i])] += 1

    start = 0
    start_index = -1
    min_len = sys.maxint
    count = 0
    
    for j in xrange(0, len1):
        hash_str[ord(strng[j])] += 1

        if (hash_pat[ord(strng[j])] != 0 and hash_str[ord(strng[j])] <= hash_pat[ord(strng[j])] ):
            count += 1

        if (count == len2):
            while ( hash_str[ord(strng[start])] > hash_pat[ord(strng[start])] or hash_pat[ord(strng[start])] == 0):
                if (hash_str[ord(strng[start])] > hash_pat[ord(strng[start])]):
                    hash_str[ord(strng[start])] -= 1
                start += 1

            len_window = j - start + 1
            if (min_len > len_window):
                min_len = len_window
                start_index = start

    if (start_index == -1):
        print "No such window exists"
        return

    return strng[start_index:start_index + min_len]

#Time Complexity:  O(n)
#Auxiliary Space:  O(n)
def getNthUglyNo(n):
 
    ugly = [0] * n                # To store ugly numbers
    ugly[0] = 1                   # 1 is the first ugly number
    i2 = i3 =i5 = 0               # i2, i3, i5 will indicate indices for 2,3,5 respectively

    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    
    for l in range(1, n):
        ugly[l] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)                   # choose the min value of all available multiples
        
        if ugly[l] == next_multiple_of_2:                                                           # increment the value of index accordingly
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2
 
        if ugly[l] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3
 
        if ugly[l] == next_multiple_of_5: 
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5
 
    return ugly[-1]                           # return ugly[n] value

# Maximum Length Chain of Pairs
# For example, if the given pairs are {{5, 24}, {39, 60}, {15, 28}, {27, 40}, {50, 90} }, then the longest chain that can be formed is of length 3, and the chain is {{5, 24}, {27, 40}, {50, 90}}
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
# This function assumes that arr[] is sorted in increasing order according the first (or smaller) values in pairs.
# Time Complexity: O(n^2)
def maxChainLength(arr, n):     
    max = 0
    mcl = [1 for i in range(n)]
    
    for i in range(1, n):                                                                           # Compute optimized chain length values in bottom up manner
        for j in range(0, i):
            if (arr[i].a > arr[j].b and mcl[i] < mcl[j] + 1):
                mcl[i] = mcl[j] + 1
                
    for i in range(n):
        if (max < mcl[i]):
            max = mcl[i]
 
    return max

# Maximum Product Cutting

def maxProd(n):
  if (n == 2 or n == 3):                          # n equals to 2 or 3 must be handled explicitly
    return (n-1)

  res = 1
  while (n > 4):
    n -= 3
    res *= 3
  return (n * res)

# A Dynamic Programming solution for subset sum problem. Time complexity of the above solution is O(sum*n).
'''
Dynamic Programming | Set 25 (Subset Sum Problem)
Perfect sum problem
This can also help to solve "Find four elements that sum to a given value | Set 2 ( O(n^2Logn) Solution)" by putting a length check condition to the same (https://www.geeksforgeeks.org/find-four-elements-that-sum-to-a-given-value-set-2/)
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.

See the recursive solution below to this solution. It may try all subsets of given set in worst case. Therefore time complexity of the above solution is exponential.
The problem is in-fact NP-Complete (There is no known polynomial time solution for this problem).
We can solve the problem in Pseudo-polynomial time using Dynamic programming as below.
We create a boolean 2D table subset[][] and fill it in bottom up manner. The value of subset[i][j] will be true if there is a subset of set[0..j-1] with sum equal to i.,
otherwise false. Finally, we return subset[sum][n]
See better solution than this here https://www.geeksforgeeks.org/subset-sum-problem-osum-space/

This problem is mainly an extension of Subset Sum Problem. Here we not only need to find if there is a subset with given sum, but also need to print all subsets with given sum.

Like previous post, we build a 2D array dp[][] such that dp[i][j] stores true if sum j is possible with array elements from 0 to i.
 After filling dp[][], we recursively traverse it from dp[n-1][sum]. For cell being traversed, we store path before reaching it and consider two possibilities for the element.
 1) Element is included in current path.
 2) Element is not included in current path.

Whenever sum becomes 0, we stop the recursive calls and print current path.

****************************************************************************************************************
The same logic/algo can be used to solve the one below
Dynamic Programming | Set 18 (Partition problem) (https://www.geeksforgeeks.org/dynamic-programming-set-18-partition-problem/)
Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is same. 

Examples
arr[] = {1, 5, 11, 5}
Output: true 
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false 
The array cannot be partitioned into equal sum sets.

 Following are the two main steps to solve this problem:
 1) Calculate sum of the array. If sum is odd, there can not be two subsets with equal sum, so return false.
 2) If sum of array elements is even, calculate sum/2 and find a subset of array with sum equal to sum/2.
****************************************************************************************************************
'''
def printAllSubsets(arr, n, sum):
    if (n == 0 or sum < 0):
       return

    dp=[[False]*(sum+1) for i in xrange(n)]

    for i in xrange(0, n):
        dp[i][0] = True

    if (arr[0] <= sum):
        dp[0][arr[0]] = True

    for i in xrange(1, n):
        for j in xrange(0, sum+1):
            if (arr[i] <= j):
                dp[i][j] = (dp[i-1][j] or dp[i-1][j-arr[i]])
            else:
                dp[i][j] = dp[i - 1][j];

    if (dp[n-1][sum] == False):
        print "There are no subsets with"
        return
    else:
        print "Sum exists. Let's print it..."

    p = []
    printSubsetsRec(dp, arr, n-1, sum, p)

def printSubsetsRec(dp, arr, i, sum, p):
    if (i == 0 and sum != 0 and dp[0][sum]):
        p.append(arr[i]);
        print p
        p=[]
        return;

    if (i == 0 and sum == 0):
        print p
        p = []
        return;

    if (dp[i-1][sum]):
        b = []
        b.extend(p);
        printSubsetsRec(dp, arr, i-1, sum, b);

    if (sum >= arr[i] and dp[i-1][sum-arr[i]]):
        p.append(arr[i]);
        printSubsetsRec(dp, arr, i-1, sum-arr[i], p);

# A Dynamic Programming based Python program for edit distance problem
# display all the words in a dictionary that are near proximity to a given wordincorrectly spelled word
'''
Given two strings str1 and str2 and below operations that can be performed on str1. Find minimum number of edits (operations) required to convert str1 into str2.
Insert
Remove
Replace

All of the above operations are of equal cost.

Examples: 
Input:   str1 = "geek", str2 = "gesek"
Output:  1
We can convert str1 into str2 by inserting a 's'.

Input:   str1 = "cat", str2 = "cut"
Output:  1
We can convert str1 into str2 by replacing 'a' with 'u'.

Input:   str1 = "sunday", str2 = "saturday"
Output:  3
Last three and first characters are same.  We basically need to convert "un" to "atur".  This can be done using below three operations.
Replace 'n' with 'r', insert t, insert a
'''
def editDistDP(X, Y):
    m = len(X)
    n = len(Y)
    
    L = [[0]*(n+1) for x in xrange(m+1)]
                                                                                 
    for i in range(m+1):                                                                    # Fill d[][] in bottom up manner
        for j in range(n+1):
            if i == 0:                                                                      # If first string is empty, only option is to isnert all characters of second string
                L[i][j] = j                                                                # Min. operations = j
            elif j == 0:                                                                    # If second string is empty, only option is to remove all characters of second string
                L[i][j] = i                                                                # Min. operations = i
            elif X[i-1] == Y[j-1]:                                                    # If last characters are same, ignore last char and recur for remaining string
                L[i][j] = L[i-1][j-1]
            else:                                                                           # If last character are different, consider all possibilities and find minimum
                L[i][j] = 1 + min(L[i][j-1],          # Insert
                                  L[i-1][j],          # Remove
                                  L[i-1][j-1])        # Replace
    return L[m][n]
'''
Time Complexity: O(m x n)
Auxiliary Space: O(m x n)
Applications: There are many practical applications of edit distance algorithm, refer Lucene API(https://en.wikipedia.org/wiki/Apache_Lucene) for sample.
Another example, display all the words in a dictionary that are near proximity to a given wordincorrectly spelled word.
Below is the recursive approach but it has got a lot of overlapping subproblems and more complexity. So avoid this one...
def editDistance(str1, str2, m , n):
    if m==0:
         return n
    if n==0:
        return m
    if str1[m-1]==str2[n-1]:
        return editDistance(str1,str2,m-1,n-1)
    return 1 + min(editDistance(str1, str2, m, n-1),    # Insert
                   editDistance(str1, str2, m-1, n),    # Remove
                   editDistance(str1, str2, m-1, n-1)    # Replace
                   )
'''
# Dynamic Programming Python implementation of Coin Change problem
'''
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change?
The order of coins doesn't matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4.
For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.
Optimal Substructure
 To count total number solutions, we can divide all set solutions in two sets.
 1) Solutions that do not contain mth coin (or Sm).
 2) Solutions that contain at least one Sm.
 Let count(S[], m, n) be the function to count the number of solutions, then it can be written as sum of count(S[], m-1, n) and count(S[], m, n-Sm).
'''
def count(S, n):
    m = len(S)
    table = [0 for k in range(n+1)]                                     # table[i] will be storing the number of solutions in bottom up manner using the base case (n = 0)
    table[0] = 1
    
    for i in range(0,m):                                                # Pick all coins one by one and update the table[] values after the index greater than or equal to the value of the picked coin
        for j in range(S[i],n+1):
            table[j] += table[j-S[i]]
 
    return table[n]
'''
Time Complexity: O(mn) 
Auxiliary space: O(n)
Recursive solution with overlapping subproblems
def count(S, m, n ):
    if (n == 0):
        return 1
    if (n < 0):
        return 0;
    if (m <=0 and n >= 1):
        return 0
    return count( S, m - 1, n ) + count( S, m, n-S[m-1] );
'''
# Dynamic Programming Python implementation of Matrix Chain Multiplication. See the Cormen book for details of the following algorithm
# Printing brackets in matrix chain multiplication problem
'''
Given a sequence of matrices, find the most efficient way to multiply these matrices together. The problem is not actually to perform the multiplications,
but merely to decide in which order to perform the multiplications.

We have many options to multiply a chain of matrices because matrix multiplication is associative. In other words, no matter how we parenthesize the product, the result will be the same.
For example, if we had four matrices A, B, C, and D, we would have:
    (ABC)D = (AB)(CD) = A(BCD) = ...

However, the order in which we parenthesize the product affects the number of simple arithmetic operations needed to compute the product, or the efficiency.
For example, suppose A is a 10 x 30 matrix, B is a 30 x 5 matrix, and C is a 5 x 60 matrix. Then,
    (AB)C = (10x30x5) + (10x5x60) = 1500 + 3000 = 4500 operations
    A(BC) = (30x5x60) + (10x30x60) = 9000 + 18000 = 27000 operations.
Clearly the first parenthesization requires less number of operations.

Given an array p[] which represents the chain of matrices such that the ith matrix Ai is of dimension p[i-1] x p[i]. We need to write a function MatrixChainOrder() that should return the
minimum number of multiplications needed to multiply the chain.
  Input: p[] = {40, 20, 30, 10, 30}   
  Output: 26000  
  There are 4 matrices of dimensions 40x20, 20x30, 30x10 and 10x30.
  Let the input 4 matrices be A, B, C and D.  The minimum number of 
  multiplications are obtained by putting parenthesis in following way
  (A(BC))D --> 20*30*10 + 40*20*10 + 40*10*30

  Input: p[] = {10, 20, 30, 40, 30} 
  Output: 30000 
  There are 4 matrices of dimensions 10x20, 20x30, 30x40 and 40x30. 
  Let the input 4 matrices be A, B, C and D.  The minimum number of 
  multiplications are obtained by putting parenthesis in following way
  ((AB)C)D --> 10*20*30 + 10*30*40 + 10*40*30

  Input: p[] = {10, 20, 30}  
  Output: 6000  
  There are only two matrices of dimensions 10x20 and 20x30. So there is only one way to multiply the matrices, cost of which is 10*20*30
Optimal Substructure:
 A simple solution is to place parenthesis at all possible places, calculate the cost for each placement and return the minimum value. In a chain of matrices of size n,
 we can place the first set of parenthesis in n-1 ways. For example, if the given chain is of 4 matrices. let the chain be ABCD, then there are 3 ways to place first set of parenthesis outer side:
 (A)(BCD), (AB)(CD) and (ABC)(D). So when we place a set of parenthesis, we divide the problem into subproblems of smaller size. Therefore, the problem has optimal substructure property
 and can be easily solved using recursion.
Minimum number of multiplication needed to multiply a chain of size n = Minimum of all n-1 placements (these placements create subproblems of smaller size)
Time Complexity: O(n^3)
 Auxiliary Space: O(n^2)
'''
import sys
# Matrix Ai has dimension p[i-1] x p[i] for i = 1..n
def MatrixChainOrder(p, n):
    # For simplicity of the program, one extra row and one
    # extra column are allocated in m[][].  0th row and 0th
    # column of m[][] are not used
    m = [[0 for x in range(n)] for x in range(n)]
 
    # m[i,j] = Minimum number of scalar multiplications needed
    # to compute the matrix A[i]A[i+1]...A[j] = A[i..j] where
    # dimension of A[i] is p[i-1] x p[i]
 
    # cost is zero when multiplying one matrix.
    for i in range(1, n):
        m[i][i] = 0
 
    # L is chain length.
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1
            m[i][j] = sys.maxint
            for k in range(i, j):
 
                # q = cost/scalar multiplications
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
 
    return m[1][n-1]
 
# Dynamic Programming | Set 9 (Binomial Coefficient)
'''
1) A binomial coefficient C(n, k) can be defined as the coefficient of X^k in the expansion of (1 + X)^n.
2) A binomial coefficient C(n, k) also gives the number of ways, disregarding order, that k objects can be chosen from among n objects; more formally, the number of k-element subsets
(or k-combinations) of an n-element set.

The Problem
Write a function that takes two parameters n and k and returns the value of Binomial Coefficient C(n, k).
For example, your function should return 6 for n = 4 and k = 2, and it should return 10 for n = 5 and k = 2.
4c2=fact(4)/fact(2)fact(4-2)
5c2=fact(5)/fact(2)fact(5-2)

Optimal Substructure
 The value of C(n, k) can be recursively calculated using following standard formula for Binomial Coefficients.
   C(n, k) = C(n-1, k-1) + C(n-1, k)
   C(n, 0) = C(n, n) = 1
'''
# Python program for Optimized Dynamic Programming solution to Binomail Coefficient. This one uses the concept of pascal Triangle and less memory
# Time Complexity: O(n*k)   Auxiliary Space: O(k)
def binomialCoeff(n , k):
    C = [0 for i in xrange(k+1)]
    C[0] = 1                                # since nC0 is 1
 
    for i in range(1,n+1):                  # Compute next row of pascal triangle using the previous row
        j = min(i ,k)
        while (j>0):
            C[j] = C[j] + C[j-1]
            j -= 1
    return C[k]
'''
Other solution having O(n*k) auxiliary space
def binomialCoef(n, k):
    C = [[0 for x in range(k+1)] for x in range(n+1)]
    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                C[i][j] = 1
             else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C[n][k]

Recursive approach with overlapping subproblems:
def binomialCoeff(n , k):
    if k==0 or k ==n :
        return 1
    return binomialCoeff(n-1 , k-1) + binomialCoeff(n-1 , k)
'''
# Dynamic Programming | Set 10 ( 0-1 Knapsack Problem)
'''
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively.
Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is
smaller than or equal to W. You cannot break an item, either pick the complete item, or don't pick it (0-1 property).
A simple solution is to consider all subsets of items and calculate the total weight and value of all subsets. Consider the only subsets whose total weight is smaller than W.
From all such subsets, pick the maximum value subset.

1) Optimal Substructure:
 To consider all subsets of items, there can be two cases for every item: (1) the item is included in the optimal subset, (2) not included in the optimal set.
 Therefore, the maximum value that can be obtained from n items is max of following two values.
 1) Maximum value obtained by n-1 items and W weight (excluding nth item).
 2) Value of nth item plus maximum value obtained by n-1 items and W minus weight of the nth item (including nth item).
If weight of nth item is greater than W, then the nth item cannot be included and case 1 is the only possibility.
Time Complexity: O(nW) where n is the number of items and W is the capacity of knapsack.
'''
# A Dynamic Programming based Python Program for 0-1 Knapsack problem Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]

# Egg dropping puzzle
'''
The following is a description of the instance of this famous puzzle involving n=2 eggs and a building with k=36 floors.
Suppose that we wish to know which stories in a 36-story building are safe to drop eggs from, and which will cause the eggs to break on landing. We make a few assumptions:

- An egg that survives a fall can be used again.
- A broken egg must be discarded.
- The effect of a fall is the same for all eggs.
- If an egg breaks when dropped, then it would break if dropped from a higher floor.
- If an egg survives a fall then it would survive a shorter fall.
- It is not ruled out that the first-floor windows break eggs, nor is it ruled out that the 36th-floor do not cause an egg to break.

If only one egg is available and we wish to be sure of obtaining the right result, the experiment can be carried out in only one way. Drop the egg from the first-floor window; if it survives,
drop it from the second floor window. Continue upward until it breaks. In the worst case, this method may require 36 droppings. Suppose 2 eggs are available. What is the least number of
egg-droppings that is guaranteed to work in all cases? The problem is not actually to find the critical floor, but merely to decide floors from which eggs should be dropped so that total number
of trials are minimized.

In this post, we will discuss solution to a general problem with n eggs and k floors. The solution is to try dropping an egg from every floor (from 1 to k) and recursively calculate the minimum
number of droppings needed in worst case. The floor which gives the minimum value in worst case is going to be part of the solution.

In the following solutions, we return the minimum number of trials in worst case; these solutions can be easily modified to print floor numbers of every trials also.

1) Optimal Substructure:
 When we drop an egg from a floor x, there can be two cases (1) The egg breaks (2) The egg doesn't break.

1) If the egg breaks after dropping from xth floor, then we only need to check for floors lower than x with remaining eggs; so the problem reduces to x-1 floors and n-1 eggs
2) If the egg doesn't break after dropping from the xth floor, then we only need to check for floors higher than x; so the problem reduces to k-x floors and n eggs.

Since we need to minimize the number of trials in worst case, we take the maximum of two cases. We consider the max of above two cases for every floor and choose the floor which yields minimum
number of trials.
  k ==> Number of floors
  n ==> Number of Eggs
  eggDrop(n, k) ==> Minimum number of trials needed to find the critical floor in worst case.
  eggDrop(n, k) = 1 + min{max(eggDrop(n - 1, x - 1), eggDrop(n, k - x)): x in {1, 2, ..., k}}
Time Complexity: O(nk^2)
Auxiliary Space: O(nk)
'''
INT_MAX = 32767
# Function to get minimum number of trials needed in worst case with n eggs and k floors
def eggDrop(n, k):
    eggFloor = [[0 for x in range(k+1)] for x in range(n+1)]
    
    for i in range(1, n+1):                                                                         # We need one trial for one floor and 0 trials for 0 floors 
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0 
    for j in range(1, k+1):                                                                         # We always need j trials for one egg and j floors.
        eggFloor[1][j] = j
        
    for i in range(2, n+1):                                                                         # Fill rest of the entries in table using optimal substructure property 
        for j in range(2, k+1):
            eggFloor[i][j] = INT_MAX
            for x in range(1, j+1):
                res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x])
                if res < eggFloor[i][j]:
                    eggFloor[i][j] = res
                    
    return eggFloor[n][k]                                                                           # eggFloor[n][k] holds the result 

# Dynamic Programming | Set 13 (Cutting a Rod)
'''
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces.
For example, if length of the rod is 8 and the values of different pieces are given as following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6) 

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20


And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1)
length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 3   5   8   9  10  17  17  20
Time Complexity of the above implementation is O(n^2) which is much better than the worst case time complexity of Naive Recursive implementation.
'''
INT_MIN = -32767
# Returns the best obtainable price for a rod of length n and price[] as prices of different pieces
def cutRod(price, n):
    val = [0 for x in range(n+1)]
    val[0] = 0
    
    for i in range(1, n+1):                                                                         # Build the table val[] in bottom up manner and return the last entry from the table
        max_val = INT_MIN
        for j in range(i):
             max_val = max(max_val, price[j] + val[i-j-1])
        val[i] = max_val
 
    return val[n]
'''
Recursive solution with overlapping subproblems
def cutRod(price, n):
    if(n <= 0):
        return 0
    max_val = -sys.maxsize-1
    for i in range(0, n):
        max_val = max(max_val, price[i] + cutRod(price, n - i - 1))
    return max_val
'''
# Dynamic Programming | Set 34 (Assembly Line Scheduling)
'''
A car factory has two assembly lines, each with n stations. A station is denoted by Si,j where i is either 1 or 2 and indicates the assembly line the station is on,
and j indicates the number of the station. The time taken per station is denoted by ai,j. Each station is dedicated to some sort of work like engine fitting, body fitting, painting and so on. So,
a car chassis must pass through each of the n stations in order before exiting the factory.
The parallel stations of the two assembly lines perform the same task. After it passes through station Si,j, it will continue to station Si,j+1 unless it decides to transfer to the other line.
Continuing on the same line incurs no extra cost, but transferring from line i at station j - 1 to station j on the other line takes time ti,j.
Each assembly line takes an entry time ei and exit time xi which may be different for the two lines. Give an algorithm for computing the minimum time it will take to build a car chassis.

The below figure presents the problem in a clear picture:

                e1                                                                      x1
Assembly line1-------->Engine fitting----->Body fitting----------->Painting-------------->
                        S1,1     t1,2\    ^ S1,2                    S1,3
                                      \  /
                                       \/
                                       /\
                                      /  \
                                     /    \      
                                    /      \
                 e2     S2,1   t2,2/        V S2,2                  S2,3                x2
Assembly line2------>Engine fitting---->Body fitting----------->Painting---------------->

The following information can be extracted from the problem statement to make it simpler:
 - Two assembly lines, 1 and 2, each with stations from 1 to n.
 - A car chassis must pass through all stations from 1 to n in order(in any of the two assembly lines). i.e. it cannot jump from station i to station j if they are not at one move distance.
 - The car chassis can move one station forward in the same line, or one station diagonally in the other line. It incurs an extra cost ti, j to move to station j from line i. No cost is incurred for movement in same line.
 - The time taken in station j on line i is ai, j.
 - Si, j represents a station j on line i.

Breaking the problem into smaller sub-problems:
 We can easily find the ith factorial if (i-1)th factorial is known. Can we apply the similar funda here?
 If the minimum time taken by the chassis to leave station Si, j-1 is known, the minimum time taken to leave station Si, j can be calculated quickly by combining ai, j and ti, j.

T1(j) indicates the minimum time taken by the car chassis to leave station j on assembly line 1.

T2(j) indicates the minimum time taken by the car chassis to leave station j on assembly line 2.

Base cases: 
 The entry time ei comes into picture only when the car chassis enters the car factory.

Time taken to leave first station in line 1 is given by:
 T1(1) = Entry time in Line 1 + Time spent in station S1,1
 T1(1) = e1 + a1,1
 Similarly, time taken to leave first station in line 2 is given by:
 T2(1) = e2 + a2,1

Recursive Relations:
 If we look at the problem statement, it quickly boils down to the below observations:
 The car chassis at station S1,j can come either from station S1, j-1 or station S2, j-1.

Case #1: Its previous station is S1, j-1
 The minimum time to leave station S1,j is given by:
 T1(j) = Minimum time taken to leave station S1, j-1 + Time spent in station S1, j
 T1(j) = T1(j-1) + a1, j

Case #2: Its previous station is S2, j-1
 The minimum time to leave station S1, j is given by:
 T1(j) = Minimum time taken to leave station S2, j-1 + Extra cost incurred to change the assembly line + Time spent in station S1, j
 T1(j) = T2(j-1) + t2, j + a1, j

The minimum time T1(j) is given by the minimum of the two obtained in cases #1 and #2.
 T1(j) = min((T1(j-1) + a1, j), (T2(j-1) + t2, j + a1, j))
 Similarly the minimum time to reach station S2, j is given by:
 T2(j) = min((T2(j-1) + a2, j), (T1(j-1) + t1, j + a2, j))

The total minimum time taken by the car chassis to come out of the factory is given by:
 Tmin = min(Time taken to leave station Si,n + Time taken to exit the car factory)
 Tmin = min(T1(n) + x1, T2(n) + x2)

Why dynamic programming?
 The above recursion exhibits overlapping sub-problems. There are two ways to reach station S1, j:
1.From station S1, j-1
2.From station S2, j-1

So, to find the minimum time to leave station S1, j the minimum time to leave the previous two stations must be calculated(as explained in above recursion).
 Similarly, there are two ways to reach station S2, j:
1.From station S2, j-1
2.From station S1, j-1

Please note that the minimum times to leave stations S1, j-1 and S2, j-1 have already been calculated.

So, we need two tables to store the partial results calculated for each station in an assembly line. The table will be filled in bottom-up fashion.

Note:
 In this post, the word "leave" has been used in place of "reach" to avoid the confusion. Since the car chassis must spend a fixed time in each station, the word leave suits better.
 See the pictorial representaion here https://www.geeksforgeeks.org/dynamic-programming-set-34-assembly-line-scheduling/
'''
# Python program to find minimum possible time by the car chassis to complete
def carAssembly (a, t, e, x):
     
    NUM_STATION = len(a[0])
    T1 = [0 for i in range(NUM_STATION)]
    T2 = [0 for i in range(NUM_STATION)]
     
    T1[0] = e[0] + a[0][0] # time taken to leave
                           # first station in line 1
    T2[0] = e[1] + a[1][0] # time taken to leave
                           # first station in line 2
 
    # Fill tables T1[] and T2[] using
    # above given recursive relations
    for i in range(1, NUM_STATION):
        T1[i] = min(T1[i-1] + a[0][i],
                    T2[i-1] + t[1][i] + a[0][i])
        T2[i] = min(T2[i-1] + a[1][i],
                    T1[i-1] + t[0][i] + a[1][i] )
 
    # consider exit times and return minimum
    return min(T1[NUM_STATION - 1] + x[0],
               T2[NUM_STATION - 1] + x[1])
'''
Dynamic Programming | Set 31 (Optimal Strategy for a Game)
Problem statement: Consider a row of n coins of values v1 . . . vn, where n is even. We play a game against an opponent by alternating turns. In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and receives the value of the coin. Determine the maximum possible amount of money we can definitely win if we move first.
Note: The opponent is as clever as the user.

Let us understand the problem with few examples:
    1. 5, 3, 7, 10 : The user collects maximum value as 15(10 + 5)
    2. 8, 15, 3, 7 : The user collects maximum value as 22(7 + 15)

Does choosing the best at each move give an optimal solution?

No. In the second example, this is how the game can finish:

1.
User chooses 8.
Opponent chooses 15.
User chooses 7.
Opponent chooses 3.
 Total value collected by user is 15(8 + 7)

2.
User chooses 7.
Opponent chooses 8.
User chooses 15.
Opponent chooses 3.
 Total value collected by user is 22(7 + 15)

So if the user follows the second game state, maximum value can be collected although the first move is not the best.

There are two choices:
1. The user chooses the ith coin with value Vi: The opponent either chooses (i+1)th coin or jth coin. The opponent intends to choose the coin which leaves the user with minimum value.
 i.e. The user can collect the value Vi + min(F(i+2, j), F(i+1, j-1) )
coinGame1

2. The user chooses the jth coin with value Vj: The opponent either chooses ith coin or (j-1)th coin. The opponent intends to choose the coin which leaves the user with minimum value.
 i.e. The user can collect the value Vj + min(F(i+1, j-1), F(i, j-2) )
coinGame2

Following is recursive solution that is based on above two choices. We take the maximum of two choices.
F(i, j)  represents the maximum value the user can collect from
         i'th coin to j'th coin.

    F(i, j)  = Max(Vi + min(F(i+2, j), F(i+1, j-1) ),
                   Vj + min(F(i+1, j-1), F(i, j-2) ))
Base Cases
    F(i, j)  = Vi           If j == i
    F(i, j)  = max(Vi, Vj)  If j == i+1
Why Dynamic Programming?
 The above relation exhibits overlapping sub-problems. In the above relation, F(i+1, j-1) is calculated twice.
'''
# Returns optimal value possible that a player can collect from an array of coins of size n. Note than n must be even
def optimalStrategyOfGame(arr, n):
    table = [[None]*n for i in xrange(n)]                       # Create a table to store solutions of subproblems

    for gap in xrange(0, n):    # Fill table using above recursive formula.Note that the tableis filled in diagonalfashion (similar to http://goo.gl/PQqoS)from diagonal elements to table[0][n-1]which is the result.
        i=0
        for j in xrange(gap, n):
            if ((i + 2) <= j):
                x=table[i + 2][j]
            else:
                x=0
                
            if ((i + 1) <= (j - 1)):
                y=table[i +1 ][j -  1]
            else:
                y=0
                
            if (i <= (j - 2)):
                z=table[i][j - 2]
            else:
                z=0
                
            table[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))
            i+=1
    return table[0][n - 1]
'''
Dynamic Programming | Set 35 (Longest Arithmetic Progression)
Given a sett of numbers, find the Length of the Longest Arithmetic Progression (LLAP) in it.

Examples:
sett[] = {1, 7, 10, 15, 27, 29}
output = 3
The longest arithmetic progression is {1, 15, 29}

sett[] = {5, 10, 15, 20, 25, 30}
output = 6
The whole sett is in AP

For simplicity, we have assumed that the given sett is sorted. We can always add a pre-processing step to first sort the sett and then apply the below algorithms.

A simple solution is to one by one consider every pair as first two elements of AP and check for the remaining elements in sorted sett. To consider all pairs as first two elements, we need to run a O(n^2) nested loop. Inside the nested loops, we need a third loop which linearly looks for the more elements in Arithmetic Progression (AP). This process takes O(n3) time.

We can solve this problem in O(n2) time using Dynamic Programming. To get idea of the DP solution, let us first discuss solution of following simpler problem.

Given a sorted sett, find if there exist three elements in Arithmetic Progression or not
 Please note that, the answer is true if there are 3 or more elements in AP, otherwise false.
 To find the three elements, we first fix an element as middle element and search for other two (one smaller and one greater). We start from the second element and fix every element as middle element. For an element sett[j] to be middle of AP, there must exist elements 'sett[i]' and 'sett[k]' such that sett[i] + sett[k] = 2*sett[j] where 0 <= i < j and j < k <=n-1. How to efficiently find i and k for a given j? We can find i and k in linear time using following simple algorithm.
1) Initialize i as j-1 and k as j+1
2) Do following while i >= 0 and j <= n-1 ..........a) If sett[i] + sett[k] is equal to 2*sett[j], then we are done.
        b) If sett[i] + sett[k] > 2*sett[j], then decrement i (do i--).
        c) Else if sett[i] + sett[k] < 2*sett[j], then increment k (do k++). Following is C++ implementation of the above algorithm for the simpler problem.


# The function returns true if there exist three elements in AP
# Assumption: sett[0..n-1] is sorted.
# The code strictly implements the algorithm provided in the reference.
bool arithmeticThree(int sett[], int n)
{
    # One by fix every element as middle element
    for (int j=1; j<n-1; j++)
    {
        # Initialize i and k for the current j
        int i = j-1, k = j+1;

        # Find if there exist i and k that form AP
        # with j as middle element
        while (i >= 0 && k <= n-1)
        {
            if (sett[i] + sett[k] == 2*sett[j])
                return true;
            (sett[i] + sett[k] < 2*sett[j])? k++ : i--;
        }
    }

    return false;
}
How to extend the above solution for the original problem?
 The above function returns a boolean value. The required output of original problem is Length of the Longest Arithmetic Progression (LLAP) which is an integer value. If the given sett has two or more elements, then the value of LLAP is at least 2 (Why?).

The idea is to create a 2D table L[n][n]. An entry L[i][j] in this table stores LLAP with sett[i] and sett[j] as first two elements of AP and j > i. The last column of the table is always 2 (Why - see the meaning of L[i][j]). Rest of the table is filled from bottom right to top left. To fill rest of the table, j (second element in AP) is first fixed. i and k are searched for a fixed j. If i and k are found such that i, j, k form an AP, then the value of L[i][j] is sett as L[j][k] + 1. Note that the value of L[j][k] must have been filled before as the loop traverses from right to left columns.

Time Complexity: O(n2)
Auxiliary Space: O(n2)
'''
def lenghtOfLongestAP(sett, n):
        if (n <= 2):
             return n;

        # Create a table and initialize all
        # values as 2. The value ofL[i][j] stores
        # LLAP with sett[i] and sett[j] as first two
        # elements of AP. Only valid entries are
        # the entries where j>i
        L = [[0]*n for i in xrange(n)]

         # Initialize the result
        llap = 2;

        # Fill entries in last column as 2.
        # There will always be two elements in
        # AP with last number of sett as second
        # element in AP
        for i in xrange(0, n):
            L[i][n - 1] = 2

        # Consider every element as second element of AP
        for j in reversed(range(1, n-1)):
            i = j -1
            k = j + 1
            while (i>=0 and k <= n-1):
                if (sett[i] + sett[k] < 2*sett[j]):
                    k+=1
                elif (sett[i] + sett[k] > 2 * sett[j]):
                    L[i][j] = 2
                    i -= 1
                else:
                    L[i][j] = L[j][k] + 1
                    llap = max(llap, L[i][j]);
                    i -=1
                    k +=1
            while (i >= 0):
                L[i][j] = 2
                i-=1
        return llap

'''
Dynamic Programming | Set 27 (Maximum sum rectangle in a 2D matrix)
Given a 2D array, find the maximum sum subarray in it. For example, in the following 2D array, the maximum sum subarray is highlighted with blue rectangle and sum of this subarray is 29.
This problem is mainly an extension of Largest Sum Contiguous Subarray for 1D array.

1       2       -1      4       -20

-8      -3      4       2       1

3       8       10      -8      3

-4      -1      1       7       -6

Ans is:
        -3      4       2

        8       10      -8

        -1      1       7
The naive solution for this problem is to check every possible rectangle in given 2D array. This solution requires 4 nested loops and time complexity of this solution would be O(n^4).

Kadane's algorithm for 1D array can be used to reduce the time complexity to O(n^3). The idea is to fix the left and right columns one by one and find the maximum sum contiguous rows for every left and right column pair. We basically find top and bottom row numbers (which have maximum sum) for every fixed left and right column pair. To find the top and bottom row numbers, calculate sum of elements in every row from left to right and store these sums in an array say temp[]. So temp[i] indicates sum of elements from left to right in row i. If we apply Kadane's 1D algorithm on temp[], and get the maximum sum subarray of temp, this maximum sum would be the maximum possible sum with left and right as boundary columns. To get the overall maximum sum, we compare this sum with the maximum sum so far.
Time Complexity: O(n^3)
'''
import sys
def kadane(a):
        #result[0] == maxSum, result[1] == start, result[2] == end;
        result = [-sys.maxsize-1, 0, -1]
        currentSum = 0;
        localStart = 0;

        for i in xrange(0, len(a)):
            currentSum += a[i];
            if (currentSum < 0):
                  currentSum = 0;
                  localStart = i + 1;
            elif (currentSum > result[0]):
                result[0] = currentSum;
                result[1] = localStart;
                result[2] = i;

        #all numbers in a are negative
        if (result[2] == -1):
            result[0] = 0;
            for i in xrange(0, len(a)):
                if (a[i] > result[0]):
                    result[0] = a[i];
                    result[1] = i;
                    result[2] = i;

        return result;
# To find and print maxSum, (left, top),(right, bottom)
def findMaxSubMatrix(a):
        cols = len(a[0])
        rows = len(a)
        maxSum = -sys.maxsize-1
        left = 0;
        top = 0;
        right = 0;
        bottom = 0;
        for leftCol in xrange(0, cols):
              tmp = [0]*rows

              for rightCol in xrange(leftCol, cols):
                for i in xrange(0, rows):
                      tmp[i] += a[i][rightCol];
                currentResult = kadane(tmp);
                if (currentResult[0] > maxSum):
                    maxSum = currentResult[0];
                    left = leftCol;
                    top = currentResult[1];
                    right = rightCol;
                    bottom = currentResult[2];
        print("MaxSum: " + str(maxSum) + ", int(range): [(" + str(left) + ", " + str(top) +  ")(" + str(right) + ", " + str(bottom) + ")]")

# A Dynamic Programming based function that calculates minimum cost of a Binary Search Tree.
'''
Dynamic Programming | Set 24 (Optimal Binary Search Tree)
Given a sorted array keys[0.. n-1] of search keys and an array freq[0.. n-1] of frequency counts, where freq[i] is the number of searches to keys[i]. Construct a binary search tree of all keys such that the total cost of all the searches is as small as possible.

Let us first define the cost of a BST. The cost of a BST node is level of that node multiplied by its frequency. Level of root is 1.
Example 1
Input:  keys[] = {10, 12}, freq[] = {34, 50}
There can be following two possible BSTs
        10                       12
          \                     /
           12                 10
          I                     II
Frequency of searches of 10 and 12 are 34 and 50 respectively.
The cost of tree I is 34*1 + 50*2 = 134
The cost of tree II is 50*1 + 34*2 = 118

Example 2
Input:  keys[] = {10, 12, 20}, freq[] = {34, 8, 50}
There can be following possible BSTs
    10                12                 20         10              20
      \             /    \              /             \            /
      12          10     20           12               20         10
        \                            /                 /           \
         20                        10                12             12
     I               II             III             IV             V
Among all possible BSTs, cost of the fifth BST is minimum.
Cost of the fifth BST is 1*50 + 2*34 + 3*8 = 142
The idea of above formula is simple, we one by one try all nodes as root (r varies from i to j in second term). When we make rth node as root, we recursively calculate optimal cost
from i to r-1 and r+1 to j. We add sum of frequencies from i to j (see first term in the above formula), this is added because every search will go through root and one comparison
will be done for every search.
See https://www.geeksforgeeks.org/dynamic-programming-set-24-optimal-binary-search-tree/ to see the formula.
1) The time complexity of the above solution is O(n^4). The time complexity can be easily reduced to O(n^3) by pre-calculating sum of frequencies instead of calling sum() again and again.
2) In the above solutions, we have computed optimal cost only. The solutions can be easily modified to store the structure of BSTs also. We can create another auxiliary array of size n to
   store the structure of tree. All we need to do is, store the chosen 'r' in the innermost loop.
'''
def optimalSearchTree(keys, freq, n):
    cost = [[0]*(n+1) for i in xrange(n+1)]                                             # Create an auxiliary 2D matrix to store results of subproblems

    for i in xrange(0, n):                                                              # For a single key, cost is equal to frequency of the key
        cost[i][i] = freq[i]

    for L in xrange(2, n+1):                                                    # Now we need to consider chains of length 2, 3, .... L is chain length.
        for i in xrange(0, n-L+2):
            j = i + L - 1                                                               # Get column number j from row number i and chain length L
            cost[i][j] = sys.maxint
            for r in xrange(i, j+1):                                            # Try making all keys in interval keys[i..j] as root
                c = sum(freq, i, j)                                                     # c = cost when keys[r] becomes root of this subtree
                if r > i:
                    c += cost[i][r - 1]
                if r < j:
                    c += cost[r + 1][j]

                if (c < cost[i][j]):
                    cost[i][j] = c
    return cost[0][n - 1]

# A utility function to get sum of array elements freq[i] to freq[j]
def sum(freq, i, j):
    s = 0
    for k in xrange(i, j+1):
        if (k >= len(freq)):
            continue
        s += freq[k]
    return s

'''
Dynamic Programming | Set 32 (Word Break Problem)
Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words.
 This is a famous Google interview question, also being asked by many other companies now a days.
e.g.
Consider the following dictionary 
{ i, like, sam, sung, samsung, mobile, ice, cream, icecream, man, go, mango}

Input:  ilike
Output: Yes 
The string can be segmented as "i like".

Input:  ilikesamsung
Output: Yes

Solving word break problem using backtracking
'''
def wordBreak(strng):
    wordBreakUtil(strng, len(strng), "");

def wordBreakUtil(strng, n, result):
    for i in xrange(1, n+1):
        prefix = strng[0:i]
        if (dictionaryContains(prefix)):
            if (i == n):
                result += prefix;
                print result
                return
            wordBreakUtil(strng[i:n], n-i, result + prefix + " ")

def dictionaryContains(word):
    dictionary = ["mobile","samsung","sam","sung",
                            "man","mango", "icecream","and",
                            "go","i","love","ice","cream"]
    n = len(dictionary)
    for w in dictionary:
        if w==word:
            return True
    return False

# Dynamic Programming based solution to check word break. Return True if word breaking is possible else False
# Also solve it and above using trie
# Also see the same solution in trie
def wordBreakCheck(strng):
    n = len(strng)
    if (n == 0):
        return True
    
    wb = [False]*(n+1)                      # Create the DP table to store results of subroblems. The value wb[i] will be true if str[0..i-1] can be segmented into dictionary words, otherwise false.
    
    for i in xrange(1, n+1):
        if (wb[i] is False and dictionaryContains( strng[0:i])):
            wb[i] = True
        if (wb[i] is True):                 # If we reached the last prefix
            if i == n:
                return True

            for j in xrange(i+1, n+1):
                if (wb[j] is False and dictionaryContains( strng[i:j] )):
                    wb[j] = True
                if (wb[j] is True):
                    if j == n:
                        return True
    return False
'''
program to find number of ways to get sum 'x' with 'n' dice where every dice has 'm' faces
Time Complexity: O(m * n * x) where m is number of faces, n is number of dice and x is given sum.
'''
def findWays(m, n, x):
    # Create a table to store results of subproblems.  One extra
    # row and column are used for simpilicity (Number of dice
    # is directly used as row index and sum is directly used
    # as column index).  The entries in 0th row and 0th column
    # are never used.
    table = [[0]*(x+1) for i in xrange(n+1)]

    # Table entries for only one dice
    for j in xrange(1, m+1):
        if j <= x:
            table[1][j] = 1

    for i in xrange(2, n+1):
        for j in xrange(1, x+1):
            for k in xrange(1, m+1):
                if k<j:
                    table[i][j] += table[i-1][j-k];

    #Uncomment these lines to see content of table
    '''
    for i in xrange(0, n+1):
      print ""
      for j in xrange(0, x+1):
        print table[i][j],
      print ""
    '''
    return table[n][x]
'''
We can add following two conditions at the beginning of findWays() to improve performance of program for extreme cases (x is too high or x is too low)
# When x is so high that sum can not go beyond x even when we get maximum value in every dice throw.
if (m*n <= x)
    return (m*n == x);

# When x is too low
if (n >= x)
    return (n == x);

With above conditions added, time complexity becomes O(1) when x >= m*n or when x <= n.
Exercise:
Extend the above algorithm to find the probability to get Sum > X.
'''
'''
Note: This solution gives incorrect result as compared to what it's in geeksforgeeks(https://www.geeksforgeeks.org/dynamic-programming-set-21-box-stacking-problem/).
Verify it again.
Dynamic Programming | Set 22 (Box Stacking Problem)
You are given a set of n types of rectangular 3-D boxes, where the i^th box has height h(i), width w(i) and depth d(i) (all real numbers). You want to create a stack of boxes which is as tall as
possible, but you can only stack a box on top of another box if the dimensions of the 2-D base of the lower box are each strictly larger than those of the 2-D base of the higher box.
Of course, you can rotate a box so that any side functions as its base. It is also allowable to use multiple instances of the same type of box.
Source: http:#people.csail.mit.edu/bdean/6.046/dp/. The link also has video for explanation of solution.

The Box Stacking problem is a variation of LIS problem. We need to build a maximum height stack.

Following are the key points to note in the problem statement:
 1) A box can be placed on top of another box only if both width and depth of the upper placed box are smaller than width and depth of the lower box respectively.
 2) We can rotate boxes. For example, if there is a box with dimensions {1x2x3} where 1 is height, 2x3 is base, then there can be three possibilities, {1x2x3}, {2x1x3} and {3x1x2}.
 3) We can use multiple instances of boxes. What it means is, we can have two different rotations of a box as part of our maximum height stack.

Following is the solution based on DP solution of LIS problem.
1) Generate all 3 rotations of all boxes. The size of rotation array becomes 3 times the size of original array. For simplicity, we consider depth as always smaller than or equal to width.
2) Sort the above generated 3n boxes in decreasing order of base area.
3) After sorting the boxes, the problem is same as LIS with following optimal substructure property.
 MSH(i) = Maximum possible Stack Height with box i at top of stack
 MSH(i) = { Max ( MSH(j) ) + height(i) } where j < i and width(j) > width(i) and depth(j) > depth(i).
 If there is no such j then MSH(i) = height(i)

4) To get overall maximum height, we return max(MSH(i)) where 0 < i < n

Time Complexity: O(n^2)
Auxiliary Space: O(n)
'''
# Representation of a box
# h --> height, w --> width,d --> depth
# for simplicity of solution, always keep w <= d
class Box:
    def __init__(self, h, w, d):
        self.h = h
        self.w = w
        self.d = d

def compare(a, b):
    return ( b.d * b.w ) - (a.d * a.w )

# Returns the height of the tallest stack that can be formed with give type of boxes
def maxStackHeight(arr, n):
        b = Box(None, None, None)
        rot = [b]*(n*3)

        # New Array of boxes is created - considering all 3 possible rotations, with width always greater than equal to width
        for i in xrange(0, n):
            box = arr[i]
            # Orignal Box
            rot[3*i] = Box(box.h, max(box.w,box.d), min(box.w,box.d))
            # First rotation of box
            rot[3*i + 1] = Box(box.w, max(box.h,box.d), min(box.h,box.d))
            # Second rotation of box
            rot[3*i + 2] = Box(box.d, max(box.w,box.h), min(box.w,box.h))

        # Calculating base area of each of the boxes
        for i in xrange(0, len(rot)):
            rot[i].area = rot[i].w * rot[i].d

        # Sorting the Boxes on the bases of Area in non Increasing order.
        rot.sort()
        #rot=sorted(rot, key=compare)

        count = 3 * n
        # Initialize msh values for all indexes msh[i] --> Maximum possible Stack Height with box i on top
        msh = [0]*count
        for i in xrange(0, count):
            msh[i] = rot[i].h

        # Computing optimized msh[] values in bottom up manner
        for i in xrange(0, count):
            msh[i] = 0
            box = rot[i]
            val = 0

            for j in xrange(0, i):
                prevBox = rot[j]
                if(box.w < prevBox.w and box.d < prevBox.d):
                    val = max(val, msh[j])
            msh[i] = val + box.h

        maxm = -1

        # Pick maximum of all msh values
        for i in xrange(0, count):
            maxm = max(maxm, msh[i])

        return maxm

# Python program for Bellman-Ford's single source shortest path algorithm.
'''
Dynamic Programming | Set 23 (Bellman-Ford Algorithm)
Given a graph and a source vertex src in graph, find shortest paths from src to all vertices in the given graph. The graph may contain negative weight edges.
We have discussed Dijkstra's algorithm for this problem. Dijksra's algorithm is a Greedy algorithm and time complexity is O(VLogV) (with the use of Fibonacci heap).
Dijkstra doesn't work for Graphs with negative weight edges, Bellman-Ford works for such graphs. Bellman-Ford is also simpler than Dijkstra and suites well for distributed systems.
But time complexity of Bellman-Ford is O(VE), which is more than Dijkstra.
Algorithm
 Following are the detailed steps.

Input: Graph and a source vertex src
Output: Shortest distance to all vertices from src. If there is a negative weight cycle, then shortest distances are not calculated, negative weight cycle is reported.

1) This step initializes distances from source to all vertices as infinite and distance to source itself as 0. Create an array dist[] of size |V| with all values as infinite except dist[src] where src is source vertex.

2) This step calculates shortest distances. Do following |V|-1 times where |V| is the number of vertices in given graph.
    a) Do following for each edge u-v
    If dist[v] > dist[u] + weight of edge uv, then update dist[v]
    dist[v] = dist[u] + weight of edge uv

3) This step reports if there is a negative weight cycle in graph. Do following for each edge u-v
    If dist[v] > dist[u] + weight of edge uv, then "Graph contains negative weight cycle"
The idea of step 3 is, step 2 guarantees shortest distances if graph doesn't contain negative weight cycle.
If we iterate through all edges one more time and get a shorter path for any vertex, then there is a negative weight cycle
See the pictorial representation here https://www.geeksforgeeks.org/dynamic-programming-set-23-bellman-ford-algorithm/
'''
from collections import defaultdict
class Graph:
 
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = [] # default dictionary to store graph
  
    # function to add an edge to graph
    def addEdge(self,u,v,w):
        self.graph.append([u, v, w])
         
    # utility function used to print the solution
    def printArr(self, dist):
        print("Vertex   Distance from Source")
        for i in range(self.V):
            print("%d \t\t %d" % (i, dist[i]))
     
    # The main function that finds shortest distances from src to
    # all other vertices using Bellman-Ford algorithm.  The function
    # also detects negative weight cycle
    def BellmanFord(self, src):
 
        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0
 
 
        # Step 2: Relax all edges |V| - 1 times. A simple shortest 
        # path from src to any other vertex can have at-most |V| - 1 
        # edges
        for i in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
 
        # Step 3: check for negative-weight cycles.  The above step 
        # guarantees shortest distances if graph doesn't contain 
        # negative weight cycle.  If we get a shorter path, then there
        # is a cycle.
 
        for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        print "Graph contains negative weight cycle"
                        return
                         
        # print all distance
        self.printArr(dist)
'''
Notes
1)  Negative weights are found in various applications of graphs. For example, instead of paying cost for a path, we may get some advantage if we follow the path.
2) Bellman-Ford works better (better than Dijksra's) for distributed systems. Unlike Dijksra's where we need to find minimum value of all vertices, in Bellman-Ford,
edges are considered one by one.
'''
g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)
 
#Print the solution
g.BellmanFord(0)
 
a = [[4, 5, 3, 2],
     [2, 10, 1, 4]]
t = [[0, 7, 4, 5],
     [0, 9, 2, 8]]
e = [10, 12]
x = [18, 7]
 
print(carAssembly(a, t, e, x))

sett1 = [1, 7, 10, 13, 14, 19]
n1 = len(sett1)
print ( lenghtOfLongestAP(sett1, n1));

sett2 = [1, 7, 10, 15, 27, 29]
n2 = len(sett2)
print(lenghtOfLongestAP(sett2, n2));

sett3 = [2, 4, 6, 8, 10]
n3 = len(sett3)
print(lenghtOfLongestAP(sett3, n3)) ;

arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is " + str(cutRod(arr, size)))

keys = [ 10, 12, 20 ]
freq = [ 34, 8, 50 ]
n = len(keys)
print "Cost of Optimal BST is ", optimalSearchTree(keys, freq, n)

n = 2
k = 36
print("Minimum number of trials in worst case with" + str(n) + "eggs and " + str(k) + " floors is " + str(eggDrop(n, k)))

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))

n = 5
k = 2
print "Value of C(%d,%d) is %d" %(n,k,binomialCoeff(n,k))

arr = [1, 2, 3 ,4]
size = len(arr)
print("Minimum number of multiplications is " + str(MatrixChainOrder(arr, size)))

arr = [1, 2, 3]
n = 4
x = count(arr, n)
print (x)

A=[[1, 2, -1, -4, -20],
   [-8, -3, 4, 2, 1],
   [3, 8, 10, 1, 3],
   [-4, -1, 1, 7, -6]]
findMaxSubMatrix(A)

str1 = "sunday"
str2 = "saturday" 
print(editDistDP(str1, str2))

arr = [1, 2, 3, 4, 5]
n = len(arr)
sum = 10
printAllSubsets(arr, n, sum)

arr1 = [8, 15, 3, 7]
n = len(arr1)
print optimalStrategyOfGame(arr1, n)
arr2 = [2, 2, 2, 2]
n = len(arr2)
print optimalStrategyOfGame(arr2, n)

arr3 = [20, 30, 2, 2, 2, 10]
n = len(arr3)
print optimalStrategyOfGame(arr3, n)

'''
def isSubsetSum(set,n, sum) :
    if (sum == 0) :
        return True
    if (n == 0 and sum != 0) :
        return False
    if (set[n - 1] > sum) :
        return isSubsetSum(set, n - 1, sum) 
    return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1])
'''

'''
Given a rope of length n meters, cut the rope in different parts of integer lengths in a way that maximizes product of lengths of all parts. You must make at least one cut. Assume that the length of rope is more than 2 meters. 

Examples: 
Input: n = 2
Output: 1 (Maximum obtainable product is 1*1)

Input: n = 3
Output: 2 (Maximum obtainable product is 1*2)

Input: n = 4
Output: 4 (Maximum obtainable product is 2*2)

Input: n = 5
Output: 6 (Maximum obtainable product is 2*3)

Input: n = 10
Output: 36 (Maximum obtainable product is 3*3*4)
'''
print ("Maximum Product is ", maxProd(10));

arr = [Pair(5, 24), Pair(15, 25), Pair(27, 40), Pair(50, 60)]
print('Length of maximum size chain is', maxChainLength(arr, len(arr)))

a = [-2, -3, 4, -1, -2, 1, 5, -3]
print"Maximum contiguous sum is" , maxSubArraySum(a,len(a))     # 4, -1, -2, 1, 5

'''
Input  : arr[] = {3, 10, 2, 1, 20}
Output : Length of LIS = 3
The longest increasing subsequence is 3, 10, 20

Input  : arr[] = {3, 2}
Output : Length of LIS = 1
The longest increasing subsequences are {3} and {2}
'''
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print "Length of lis is", lis(arr)

'''
Input arr[] = {1, 11, 2, 10, 4, 5, 2, 1};
Output: 6 (A Longest Bitonic Subsequence of length 6 is 1, 2, 10, 4, 2, 1)

Input arr[] = {12, 11, 40, 5, 3, 1}
Output: 5 (A Longest Bitonic Subsequence of length 5 is 12, 11, 5, 3, 1)
'''
arr =  [0 , 8 , 4, 12, 2, 10 , 6 , 14 , 1 , 9 , 5 , 13, 3, 11 , 7 , 15]
print "Length of LBS is",lbs(arr)

# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, shows the first 11 ugly numbers. By convention, 1 is included. 
n = 150
print "print %dth ugly no is %d" %(n, getNthUglyNo(n))

string = "ABDEFGABEF"
print "The input string is " + string
length = longestUniqueSubsttr(string)
print ("The length of the longest non-repeating character substring is " + str(length))

arr = [1, 101, 2, 3, 100, 4, 5]
n = len(arr)
print "Sum of maximum sum increasing subsequence is " + str(maxSumIS(arr, n))

X = "AGGTAB"
Y = "GXTXAYB"
print "Length of LCS is ", lcs(X, Y)
printLcs(X, Y)

X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'
printLcs(X, Y)

# Longest Palindromic subsequence
X = "GEEKS FOR GEEKS"
Y = X[::-1]
print "The length of the LPS is ", lcs(X, Y)

X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'
print 'Length of Longest Common Substring is',lcSubstr(X, Y)
PrintLcSubstr(X, Y)

X = "forgeeksskeegfor"
Y = X[::-1]
print 'Length of Longest Palindromic Substring is',lcSubstr(X, Y)
PrintLcSubstr(X, Y)

s = "geeks"
print "Minimum no of insertions to form a palindrome is: ", findMinInsertionsLCS(s)
    
S = "this is a test string"
P = "tist"
print "Smallest window is: ", findSubString(S, P)

arr = [1, -2, -3, 0, 7, -8, -2]
print "Maximum product subarray is",maxsubarrayproduct(arr)

A="XXY"
B="XXZ"
C="XXZXXXY"

if (isInterleaved(A, B, C)):
    print C + " is interleaved of " + A+  " and " + B
else:
    print C + " is NOT interleaved of " + A + " and " + B
A="XY"
B="WZ"
C="WZXY"
if (isInterleaved(A, B, C)):
    print C + " is interleaved of " + A + " and " + B
else:
    print C + " is NOT interleaved of " + A + " and " + B

A="XY"
B="X"
C="XXY"
if (isInterleaved(A, B, C)):
    print C + " is interleaved of " + A + " and " + B
else:
    print C + " is NOT interleaved of " + A + " and " + B

A="YX"
B="X"
C="XXY"
if (isInterleaved(A, B, C)):
    print C + " is interleaved of " + A + " and " + B
else:
    print C + " is NOT interleaved of " + A + " and " + B

A="XXY"
B="XXZ"
C="XXXXZY"
if (isInterleaved(A, B, C)):
    print C + " is interleaved of " + A + " and " + B
else:
    print C + " is NOT interleaved of " + A + " and " + B

print findWays(4, 2, 1)
print findWays(2, 2, 3)
print findWays(6, 3, 8)
print findWays(4, 2, 5)
print findWays(4, 3, 5)

b= Box(None, None, None)
arr = [b]*4
arr[0] = Box(4, 6, 7);
arr[1] = Box(1, 2, 3);
arr[2] = Box(4, 5, 6);
arr[3] = Box(10, 12, 32)
print "The maximum possible height of stack is ", maxStackHeight(arr,4)

print "First Test:"
wordBreak("iloveicecreamandmango");

print "\nSecond Test:\n"
wordBreak("ilovesamsungmobile")

print "Word break test:"
print wordBreakCheck("iloveicecreamandmango")
print wordBreakCheck("ilovesamsungmobile")
print wordBreakCheck("dsfsdfdsf")
'''
Dynamic Programming | Set 1 (Overlapping Subproblems Property)
Dynamic Programming is an algorithmic paradigm that solves a given complex problem by breaking it into subproblems and stores the results of subproblems to avoid computing the same results again.
Following are the two main properties of a problem that suggest that the given problem can be solved using Dynamic programming.

In this post, we will discuss first property (Overlapping Subproblems) in detail. The second property of Dynamic programming is discussed in next post i.e. Set 2.

1) Overlapping Subproblems
2) Optimal Substructure

1) Overlapping Subproblems:
Like Divide and Conquer, Dynamic Programming combines solutions to sub-problems. Dynamic Programming is mainly used when solutions of same subproblems are needed again and again. In dynamic programming, computed solutions to subproblems are stored in a table so that these don't have to recomputed. So Dynamic Programming is not useful when there are no common (overlapping) subproblems because there is no point storing the solutions if they are not needed again. For example, Binary Search doesn't have common subproblems. If we take example of following recursive program for Fibonacci Numbers, there are many subproblems which are solved again and again.

/* simple recursive program for Fibonacci numbers */
int fib(int n)
{
   if ( n <= 1 )
      return n;
   return fib(n-1) + fib(n-2);
}
Recursion tree for execution of fib(5)
                         fib(5)
                     /             \
               fib(4)                fib(3)
             /      \                /     \
         fib(3)      fib(2)         fib(2)    fib(1)
        /     \        /    \       /    \
  fib(2)   fib(1)  fib(1) fib(0) fib(1) fib(0)
  /    \
fib(1) fib(0)

We can see that the function f(3) is being called 2 times. If we would have stored the value of f(3), then instead of computing it again, we could have reused the old stored value. There are
following two different ways to store the values so that these values can be reused:
 a) Memoization (Top Down)
 b) Tabulation (Bottom Up)

 a) Memoization (Top Down):  The memoized program for a problem is similar to the recursive version with a small modification that it looks into a lookup table before computing solutions.
 We initialize a lookup array with all initial values as NIL. Whenever we need solution to a subproblem, we first look into the lookup table. If the precomputed value is there then we return
 that value, otherwise we calculate the value and put the result in lookup table so that it can be reused later.

# Python program for Memoized version of nth Fibonacci number
def fib(n, lookup):
    if n == 0 or n == 1 :
        lookup[n] = n

    if lookup[n] is None:
        lookup[n] = fib(n-1 , lookup)  + fib(n-2 , lookup)

    return lookup[n]

def main():
    n = 34
    lookup = [None]*(101)
    print "Fibonacci Number is ", fib(n, lookup)

if __name__=="__main__":
    main()

 b) Tabulation (Bottom Up):  The tabulated program for a given problem builds a table in bottom up fashion and returns the last entry from table. For example, for the same Fibonacci number, we first calculate fib(0) then fib(1) then fib(2) then fib(3) and so on. So literally, we are building the solutions of subproblems bottom-up.

# Python program Tabulated (bottom up) version
def fib(n):
    f = [0]*(n+1)
    f[1] = 1
    for i in xrange(2 , n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

def main():
    n = 9
    print "Fibonacci number is " , fib(n)

if __name__=="__main__":
    main()

 Output:
 Fibonacci number is 34

Both Tabulated and Memoized store the solutions of subproblems. In Memoized version, table is filled on demand while in Tabulated version, starting from the first entry, all entries are filled one by one. Unlike the Tabulated version, all entries of the lookup table are not necessarily filled in Memoized version. For example,  Memoized solution  of the  LCS problem  doesn't necessarily fill all entries.

To see the optimization achieved by Memoized and Tabulated solutions over the basic Recursive solution, see the time taken by following runs for calculating 40th Fibonacci number:

Recursive solution
Memoized solution
Tabulated solution

Time taken by Recursion method is much more than the two Dynamic Programming techniques mentioned above - Memoization and Tabulation!

Also see method 2 of Ugly Number post for one more simple example where we have overlapping subproblems and we store the results of subproblems.

We will be covering Optimal Substructure Property and some more example problems in future posts on Dynamic Programming.

Try following questions as an exercise of this post.
 1) Write a Memoized solution for LCS problem. Note that the Tabular solution is given in the CLRS book.
 2) How would you choose between Memoization and Tabulation?

Tabulation Method - Bottom Up Dynamic Programming

As the name itself suggests starting from the bottom and cumulating answers to the top. Let's discuss in terms of state transition.

Let's describe a state for our DP problem to be dp[x] with dp[0] as  base state and  dp[n] as our destination state. So,  we need to find the value of destination state i.e dp[n].
 If we start our transition from our base state i.e dp[0] and follow our state transition relation to reach our destination state dp[n], we call it Bottom Up approach as it is quite clear that we started our transition from the bottom base state and reached the top most desired state.
Now, Why do we call it tabulation method?

To know this let's first write some code to calculate the factorial of a number using bottom up approach. Once, again as our general procedure to solve a DP we first define a state. In this case, we define a state as dp[x], where dp[x] tis to find  the factorial of x.

Now, it is quite obvious that dp[x+1] = dp[x] * (x+1)
// Tabulated version to find factorial x.
int dp[MAXN];

// base case
int dp[0] = 1;
for (int i = 1; i< =n; i++)
{
    dp[i] = dp[i-1] * i;
}
The above code clearly follows the bottom up approach as it starts its transition from the bottom most base case dp[0] and reaches it destination state dp[n]. Here, we may notice that the dp table is being populated sequentially and we are directly accessing the calculated states from the table itself and hence, we call it tabulation method.

Memoization Method - Top Down Dynamic Programming

Once, again let's describe it in terms of state transition. If we need to find the value for some state say dp[n] and instead of starting from the base state that i.e dp[0] we ask our answer from the states that can reach the destination state dp[n] following the state transition relation, then it is the top-down fashion of DP.

Here, we start our journey from the top most destination state and compute its answer by taking in count the values of states that can reach the destination state, till we reach the bottom most base state.

Once again, let's write the code for the factorial problem in top down fashion

// Memoized version to find factorial x.
// To speed up we store the values
// of calculated states

// initialized to -1
int dp[MAXN]

// return fact x!
int solve(int x)
{
    if (x==0)
        return 1;
    if (dp[x]!=-1)
        return dp[x];
    return (dp[x] = x * solve(x-1));
}
As we can see we are storing the most recent cache up to a limit so that if next time we got a call for the same state we simply return it from the memory. So, this is why we call it memoization as we are storing the most recent state values.

In this case the memory layout is linear that's why it may seem that the memory is being filled in a sequential manner like the tabulation method, but you may consider any other top down DP having 2D memory layout like Min Cost Path, here the memory is not filled in a sequential manner.

Tabulation:
==========
STATE transition relation is difficult to think
CODE gets complicated when lot of conditions are required
SPEED is fast as we directly access previous states from the table
If all subproblems must be solved atleast once, a bottom-up dynamic programming usually outperforms a top-down memoized algorithm by a constant factor
In tabulated version, starting from the first entry, all entries are filled one by one

Memoization:
===========
STATE transition relation is easy to think
CODE is easy and less complicated
SPEED is slow due to lot of recursive calls and return statements
If some subproblems in the subproblem space need not be solved at all, the memoized solution has the advantage of solving only those subproblems that are definitely required
Unlike the tabulated version, all entries of the loopup table are not necessarily filled. The table is filled on demand

Dynamic Programming | Set 2 (Optimal Substructure Property)
As we discussed in Set 1, following are the two main properties of a problem that suggest that the given problem can be solved using Dynamic programming:
 1) Overlapping Subproblems
 2) Optimal Substructure

We have already discussed Overlapping Subproblem property in the Set 1. Let us discuss Optimal Substructure property here.

 2) Optimal Substructure:  A given problems has Optimal Substructure Property if optimal solution of the given problem can be obtained by using optimal solutions of its subproblems.

For example, the Shortest Path problem has following optimal substructure property:
 If a node x lies in the shortest path from a source node u to destination node v then the shortest path from u to v is combination of shortest path from u to x and shortest path from x to v.
 The standard All Pair Shortest Path algorithms like Floyd-Warshall and Bellman-Ford are typical examples of Dynamic Programming.

On the other hand, the Longest Path problem doesn't have the Optimal Substructure property. Here by Longest Path we mean longest simple path (path without cycle) between two nodes.
Consider the following unweighted graph given in the CLRS book. There are two longest paths from q to t: q->r->t and q->s->t. Unlike shortest paths, these longest paths do not have the
optimal substructure property. For example, the longest path q->r->t is not a combination of longest path from q to r and longest path from r to t, because the longest path from q to r is
q->s->t->r and the longest path from r to t is r->q->s->t.

          ------------->
        q                r
      ^   <------------>^ |
      | |               | |
      | |               | |
      | |               | |
      | |               | |
      | |               | |
      | |               | V
        V ------------->
        s                t
          <------------>

How to solve a Dynamic Programming Problem ?
Dynamic Programming (DP) is a technique that solves some particular type of problems in Polynomial Time. Dynamic Programming solutions are faster than exponential brute method and can be easily proved for their correctness. Before we study how to think Dynamically for a problem, we need to learn:

1.Overlapping Subproblems
2.Optimal Substructure Property

Steps to solve a DP
1) Identify if it is a DP problem
2) Decide a state expression with least parameters
3) Formulate state relationship
4) Do tabulation (or add memoization)

Step 1 : How to classify a problem as a Dynamic Programming Problem?
Typically, all the problems that require to maximize or minimize certain quantity or counting problems that say to count the arrangements under certain condition or certain probability problems can be solved by using Dynamic Programming.
All dynamic programming problems satisfy the overlapping subproblems property and most of the classic dynamic problems also satisfy the optimal substructure property. Once, we observe these properties in a given problem, be sure that it can be solved using DP.

Step 2 : Deciding the state
 DP problems are all about state and their transition. This is the most basic step which must be done very carefully because the state transition depends on the choice of state definition you make. So, let's see what do we mean by the term "state".

State A state can be defined as the set of parameters that can uniquely identify a certain position or standing in the given problem. This set of parameters should be as small as possible to reduce state space.

For example: In our famous Knapsack problem, we define our state by two parameters index and weight i.e DP[index][weight]. Here DP[index][weight] tells us the maximum profit it can make by taking items from range 0 to index having the capacity of sack to be weight. Therefore, here the parameters index and weight together can uniquely identify a subproblem for the knapsack problem.

So, our first step will be deciding a state for the problem after identifying that the problem is a DP problem.

As we know DP is all about using calculated results to formulate the final result.
 So, our next step will be to find a relation between previous states to reach the current state.

Step 3 : Formulating a relation among the states
 This part is the hardest part of for solving a DP problem and requires a lots of intuition, observation and practice. Let's understand it by considering a sample problem

Given 3 numbers {1, 3, 5}, we need to tell
the total number of ways we can form a number 'N'
using the sum of the given three numbers.
(allowing repetitions and different arrangements).

Total number of ways to form 6 is : 8
1+1+1+1+1+1
1+1+1+3
1+1+3+1
1+3+1+1
3+1+1+1
3+3
1+5
5+1

Let's think dynamically for this problem. So, first of all, we decide a state for the given problem. We will take a parameter n to decide state as it can uniquely identify any subproblem. So, our state dp will look like state(n). Here, state(n) means the total number of arrangements to form n by using {1, 3, 5} as elements.

Now, we need to compute state(n).

How to do it?
 So here the intuition comes into action. As we can only use 1, 3 or 5 to form a given number. Let us assume that we know the result for n = 1,2,3,4,5,6 ; being termilogistic let us say we know the result for the
 state (n = 1), state (n = 2), state (n = 3) state (n = 6)

Now, we wish to know the result of the state (n = 7). See, we can only add 1, 3 and 5. Now we can get a sum total of 7 by the following 3 ways:

1) Adding 1 to all possible combinations of state (n = 6)
 Eg : [ (1+1+1+1+1+1) + 1]
 [ (1+1+1+3) + 1]
 [ (1+1+3+1) + 1]
 [ (1+3+1+1) + 1]
 [ (3+1+1+1) + 1]
 [ (3+3) + 1]
 [ (1+5) + 1]
 [ (5+1) + 1]

2) Adding 3 to all possible combinations of state (n = 4);

Eg : [(1+1+1+1) + 3]
 [(1+3) + 3]
 [(3+1) + 3]

3) Adding 5 to all possible combinations of state(n = 2)
 Eg : [ (1+1) + 5]

Now, think carefully and satisfy yourself that the above three cases are covering all possible ways to form a sum total of 7;

Therefore, we can say that result for
 state(7) = state (6) + state (4) + state (2)
 or
 state(7) = state (7-1) + state (7-3) + state (7-5)

In general,
state(n) = state(n-1) + state(n-3) + state(n-5)

So, our code will look like:

// Returns the number of arrangements to
// form 'n'
int solve(int n)
{
   // base case
   if (n < 0)
      return 0;
   if (n == 0)
      return 1;

   return solve(n-1) + solve(n-3) + solve(n-5);
}

The above code seems exponential as it is calculating the same state again and again. So, we just need to add a memoization.

Step 4 : Adding memoization or tabulation for the state
 This is the easiest part of a dynamic programming solution. We just need to store the state answer so that next time that state is required, we can directly use it from our memory

Adding memoization to the above code

// initialize to -1
int dp[MAXN];

// this function returns the number of
// arrangements to form 'n'
int solve(int n)
{
  // base case
  if (n < 0)
      return 0;
  if (n == 0)
      return 1;

  // checking if already calculated
  if (dp[n]!=-1)
      return dp[n];

  // storing the result and returning
  return dp[n] = solve(n-1) + solve(n-3) + solve(n-5);
}
Another way is to add tabulation and make solution iterative. Please refer tabulation and memoization for more details.

Dynamic Programming comes with a lots of practice. One must try solving various classic DP problems that can be found here. You may check the below problems first and try solving them using the above described steps:-
'''
