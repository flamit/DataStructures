#!/usr/bin/python

# print permutations of string
# The same logic works for printing all Anagrams
# Time Complexity: O(n*n!) Note that there are n! permutations and it requires O(n) time to print a a permutation.
def permute(a, l, r):
    if l==r:
        print ''.join(a)
    else:
        for i in xrange(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack
 
# Python program to print all permutations with repetition of characters
def allLexicographic(string):
    length = len(string)
    data = [""] * (length+1)
    string = sorted(string)
    
    allLexicographicRecur(string, data, length-1, 0)
    
def allLexicographicRecur (string, data, last, index):
    length = len(string)

    for i in xrange(length):
        data[index] = string[i]

        if index==last:
            print ''.join(data)
        else:
            allLexicographicRecur(string, data, last, index+1)

# print all permutation with repeatation of characters in sorted order
def allLexicographicSorted(string):
    pass
    # Solutions:
        # 1. sort the characters in "string" and pass it to "allLexicographic"
        # 2. Push all permutations returned by "allLexicographic" to a list and sort it
        # 3. Also check https://www.geeksforgeeks.org/lexicographic-permutations-of-string/ once
        
'''
Print all possible combinations of r elements in a given array of size n
Given an array of size n, generate and print all possible combinations of r elements in array. For example, if input array is {1, 2, 3, 4} and r is 2,
then output should be {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4} and {3, 4}.

create a temporary array data[]. The idea here is similar to Subset Sum Problem. We one by one consider every element of input array, and recur for two cases:
1) The element is included in current combination (We put the element in data[] and increment next available index in data[])
 2) The element is excluded in current combination (We do not put the element and do not change index)
When number of elements in data[] become equal to r (size of a combination), we print it.
This method is mainly based on Pascal's Identity, i.e. ncr = n-1cr + n-1cr-1

'''
def combinationUtil(arr, n, r, index, data, i):
    if (index == r):
         print data
    else:
        if (i >= n):
            return

        data[index] = arr[i];
        combinationUtil(arr, n, r, index+1, data, i+1)
        combinationUtil(arr, n, r, index, data, i+1)
'''
How to handle duplicates in the above method?
 Like method 1, we can following two things to handle duplicates.
 1) Add code to sort the array before calling combinationUtil() in printCombination()
 2) Add following lines between two recursive calls of combinationUtil() in combinationUtil()
        // Since the elements are sorted, all occurrences of an element
        // must be together
        while (arr[i] == arr[i+1])
             i++; 
'''
def getRankOfString(string):
    pass
    # Solutions:
    # 1. sort the characters of the string and increment counter by 1 till we find a match with the input string. That's the rank of the string
    # 2. https://www.geeksforgeeks.org/lexicographic-rank-of-a-string/

def isPalindrome(string):
    l = 0
    h = len(string) - 1
    
    while (h > l):
        if (string[l] != string[h]):
            print string + " is Not Palindrome"
            return
        l += 1
        h -= 1
    print string + " is palindrome"

def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''

    if size1 != size2:
        return 0
    
    temp = string1 + string1
    if (temp.count(string2)> 0):
        return 1
    else:
        return 0

'''Arrange given numbers to form the biggest number | Set 1
Given an array of numbers, arrange them in a way that yields the largest value. For example, if the given numbers are {54, 546, 548, 60}, the arrangement 6054854654 gives the largest value.
And if the given numbers are {1, 34, 3, 98, 9, 76, 45, 4}, then the arrangement 998764543431 gives the largest value.

A simple solution that comes to our mind is to sort all numbers in descending order, but simply sorting doesnt work. For example, 548 is greater than 60, but in output 60 comes before 548.
As a second example, 98 is greater than 9, but 9 comes before 98 in output.

So how do we go about it? The idea is to use any comparison based sorting algorithm. In the used sorting algorithm, instead of using the default comparison, write a comparison function myCompare() and use it to sort numbers. Given two numbers X and Y, how should myCompare() decide which number to put first - we compare two numbers XY (Y appended at the end of X) and YX (X appended at the end of Y). If XY is larger, then X should come before Y in output, else Y should come before. For example, let X and Y be 542 and 60. To compare X and Y, we compare 54260 and 60542. Since 60542 is greater than 54260, we put Y first.
'''
# Python Program to get the maximum possible integer from given array of integers...
# custom comparator to sort according to the ab, ba as mentioned in description
def comparator(a, b):
    ab = str(a)+str(b)
    ba = str(b)+str(a)
    return cmp(int(ba), int(ab))        # if ba is greater it returns 1 else -1. e.g. cmp(9,8) is 1 while cmp(8,9) is -1

a = [54, 546, 548, 60,]
sorted_array = sorted(a, cmp=comparator)
print sorted_array
number = "".join([str(i) for i in sorted_array])
print(number)

from collections import OrderedDict
def getFirstNonrepeatingChar(string):
    D = OrderedDict()
    for c in list(string):
        if c in D:
            D[c] += 1
        else:
            D[c] = 1

    for key, val in D.items():
        if D[key] == 1:
            return key
    return -1

# The following solution is without using collections and without using count array
'''
NO_OF_CHARS=256
def getFirstNonrepeating(string):
    count = [0]*NO_OF_CHARS
    n = len(string)

    for i in xrange(0, n):
        count[ord(string[i])] += 1

    for j in list(string):
        if count[ord(j)] == 1:
            return j
    return -1

if __name__=='__main__':
    s = 'google'
    #s = 'geeksforgeeks'
    print getFirstNonrepeating(s)
'''
def getLastNonRepeatingChar(String):
    pass

def getMaxOccuringChar(string):
    pass

# Find kth largest element
# Time complexity: O(nlogn). Logn for sorting and n for the for loop
def kLargest(arr, k):
    arr.sort(reverse=True)                              # Sort the given array arr in reverse order
    for i in range(k):
        print arr[i],

def findTwoRepeatingElements(arr):
    # count the chars from end to start using dictionary
    # print the no if it has got occurence twice
    pass
def findTwoNosWithOddOccurences(arr):
    # count the chars from start to end using dictionary
    # print the no if it has got odd occurence by iterating over dictionary separately again
    pass
# Program to find second most frequent character
def getSecondMostFrequentChar(string):
    pass
    # Count using dictionary;
    # Compare or sort
def checkArrayElementsAreConsecutive(arr):
    #1) Sort all the elements.
    #Do a linear scan of the sorted array. If the difference between current element and next element is anything other than 1, then return false. If all differences are 1, then return true.
    # Time Complexity: O(nLogn) Extra Space: O(n)
    #Check Method 3 (Mark visited array elements as negative) at https://www.geeksforgeeks.org/check-if-array-elements-are-consecutive/. Time Complexity: O(n) Extra Space: O(1)
    pass

'''
Write a function to check whether two given strings are anagram of each other or not.
An anagram of a string is another string that contains same characters, only the order of characters can be different.
For example:
 abcd and dabc
 LISTEN and SILENT
 Other solution is: sort both the strings and check if they are equal or not.
'''
def areAnagram(string1, string2):
    if len(string1) != len(string2):
        return 0

    D1 = dict()
    D2 = dict()
    for c1 in string1:
        if c1 not in D1:
            D1[c1] = 1
        else:
            D1[c1] += 1

    for c2 in string2:
        if c2 not in D2:
            D2[c2] = 1
        else:
            D2[c2] += 1

    for k in D1.keys():
        if D1[k] != D2[k]:
            return 0
    return 1

'''
Find the maximum repeating number in O(n) time and O(1) extra space
The naive approach is to run two loops, the outer loop picks an element one by one, the inner loop counts number of occurrences of the picked element. Finally return the element with maximum count. Time complexity of this approach is O(n^2).

A better approach is to create a count array of size k and initialize all elements of count[] as 0. Iterate through all elements of input array, and for every element arr[i], increment count[arr[i]]. Finally, iterate through count[] and return the index with maximum value. This approach takes O(n) time, but requires O(k) space.

Following is the O(n) time and O(1) extra space approach. Let us understand the approach with a simple example where arr[] = {2, 3, 3, 5, 3, 4, 1, 7}, k = 8, n = 8 (number of elements in arr[]).

1) Iterate though input array arr[], for every element arr[i], increment arr[arr[i]%k] by k (arr[] becomes {2, 11, 11, 29, 11, 12, 1, 15 })
2) Find the maximum value in the modified array (maximum value is 29). Index of the maximum value is the maximum repeating element (index of 29 is 3).
3) If we want to get the original array back, we can iterate through the array one more time and do arr[i] = arr[i] % k where i varies from 0 to n-1.

How does the above algorithm work?
Since we use arr[i]%k as index and add value k at the index arr[i]%k, the index which is equal to maximum repeating element will have the maximum value in the end.
Note that k is added maximum number of times at the index equal to maximum repeating element and all array elements are smaller than k.
'''
def maxRepeating(arr, n,  k):
    for i in range(0,  n):
        arr[arr[i]%k] += k

    max = arr[0]
    result = 0
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
            result = i
    return result
'''
The above solution prints only one repeating element and doesn't work if we want to print all maximum repeating elements.
For example, if the input array is {2, 3, 2, 3}, the above solution will print only 3. What if we need to print both of 2 and 3 as both of them occur maximum number of times.
Write a O(n) time and O(1) extra space function that prints all maximum repeating elements. (Hint: We can use maximum quotient arr[i]/n instead of maximum value in step 2).
Note that the above solutions may cause overflow if adding k repeatedly makes the value more than INT_MAX. 

'''
# A simple atoi() function
# The atoi() function takes a string (which represents an integer) as an argument and returns its value.
# Time Complexity: O(n) where n is the number of characters in input string
def myAtoi(string):
    res = 0
    sign = 1
    i = 0
    
    if string[0] == '-':                                    # if number is negative then update sign
        sign = -1
        i+=1
        
    for j in xrange(i,len(string)):
        res = res*10 + (ord(string[j]) - ord('0'))
        
    return sign*res

# Python program to count words in a given string
OUT = 0
IN = 1
def countWordsWithoutUsingSplit(string):
    state = OUT
    wc = 0
    
    for i in xrange(len(string)):
        if (string[i] == ' ' or string[i] == '\n' or
            string[i] == '\t'):
            state = OUT
        elif state == OUT:
            state = IN
            wc+=1           
    return wc

# getMissingNo takes list as argument
# Time Complexity: O(n)
def getMissingNo(A):
    n = len(A)
    total = (n+1)*(n+2)/2
    sum_of_A = sum(A)
    return total - sum_of_A

'''
Majority Element: A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element).
       I/P : 3 3 4 2 4 4 2 4 4
       O/P : 4 

       I/P : 3 3 4 2 4 4 2 4
       O/P : NONE
'''
# Check https://www.geeksforgeeks.org/check-for-majority-element-in-a-sorted-array/ for O(Logn) implementation
def majorElement(arr):
    # Count each element count using dictionary
    # While counting check if it's greater than n/2   n=>length of array
    pass

'''
Count occurrences of an element in a sorted array in O(Logn) time
Note that, here if you use dictionary, it'll have O(n) complexity. As the array is sorted, use the binary search approach
Method 2 (Use Binary Search)
 1) Use Binary search to get index of the first occurrence of x in arr[]. Let the index of the first occurrence be i.
 2) Use Binary search to get index of the last occurrence of x in arr[]. Let the index of the last occurrence be j.
 3) Return (j - i + 1)
'''
def countElements(arr, x, n): 
    i = first(arr, 0, n-1, x, n)                                                # get the index of first occurrence of x 
    if i == -1:                                                                 # If x doesn't exist in arr[] then return -1
        return i
    
    j = last(arr, i, n-1, x, n)                                                 # Else get the index of last occurrence of x. Note that we are only looking in the subarray after first occurrence  
    return j-i+1

def first(arr, low, high, x, n):
    if high >= low:
        mid = (low + high)//2 
    if (mid == 0 or x > arr[mid-1]) and arr[mid] == x:
        return mid
    elif x > arr[mid]:
        return first(arr, (mid + 1), high, x, n)
    else:
        return first(arr, low, (mid -1), x, n)
    return -1

def last(arr, low, high, x, n):
    if high >= low:
        mid = (low + high)//2; 
  
    if(mid == n-1 or x < arr[mid+1]) and arr[mid] == x :
        return mid
    elif x < arr[mid]:
        return last(arr, low, (mid -1), x, n)
    else:
        return last(arr, (mid + 1), high, x, n)     
    return -1

# Search an element in sorted and rotated array using single pass of Binary Search
def search (arr, l, h, key):
    if l > h:
        return -1
     
    mid = (l + h) // 2
    if arr[mid] == key:
        return mid
    
    if arr[l] <= arr[mid]:                                                          # As this subarray is sorted, we can quickly check if key lies in half or other half 
        if key >= arr[l] and key <= arr[mid]:
            return search(arr, l, mid-1, key)
        return search(arr, mid+1, h, key)

    if key >= arr[mid] and key <= arr[h]:
        return search(a, mid+1, h, key)
    return search(arr, l, mid-1, key)

'''
Exponential Search
The name of this searching algorithm may be misleading as it works in O(Log n) time. The name comes from the way it searches an element.
Given a sorted array an element x to be searched, find position of x in the array.

Input:  arr[] = {10, 20, 40, 45, 55}
        x = 45
Output: Element found at index 3

Input:  arr[] = {10, 15, 25, 45, 55}
        x = 15
Output: Element found at index 1

We have discussed, linear search, binary search for this problem.

Exponential search involves two steps:
1.Find range where element is present
2.Do Binary Search in above found range.

How to find the range where element may be present?
 The idea is to start with subarray size 1 compare its last element with x, then try size 2, then 4 and so on until last element of a subarray is not greater.
 Once we find an index i (after repeated doubling of i), we know that the element must be present between i/2 and i (Why i/2? because we could not find a greater value in previous iteration)

Time Complexity : O(Log n)
Auxiliary Space : The above implementation of Binary Search is recursive and requires O()Log n) space. With iterative Binary Search, we need only O(1) space.
Applications of Exponential Search:
1.Exponential Binary Search is particularly useful for unbounded searches, where size of array is infinite. Please refer Unbounded Binary Search for an example.
2.It works better than Binary Search for bounded arrays also when the element to be searched is closer to the first element.

Also refer https://www.geeksforgeeks.org/pattern-searching-set-8-suffix-tree-introduction/
'''
# Python program to find an element x in a sorted array using Exponential Search
# A recurssive binary search function. Returns location of x in given array arr[l..r] is present, otherwise -1
def binarySearch( arr, left, right, x):
    if left <= right:
        mid = (left + right) // 2                                           # left + ( right - left ) // 2

        if arr[mid] == x:                                                   # If the element is present at the middle itself
            return mid
        elif arr[mid] > x:                                                  # If the element is smaller than mid, then it can only be present in the left subarray
            return binarySearch(arr, left, mid-1, x)
        else:
            return binarySearch(arr, mid+1, right, x)                       # Else he element can only be present in the right
    return -1                                                               # We reach here if the element is not present

'''
# Iterative implementation of binary search
def binarySearch( arr, left, right, x ):
    while left <= right:
        mid = left + (right - left)//2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# Time Complexity: O(Logn)
# Auxiliary Space:
# O(1)      in case of iterative implementation
# O(Logn)   in case of recursive implementation(because of recursion call stack space)
'''
# Returns the position of first occurence of x in array
def exponentialSearch(arr, n, x):
    # IF x is present at first location itself
    if arr[0] == x:
        return 0

    # Find range for binary seaarchj by repeated doubling
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2

    # Call binary search for the found range
    return binarySearch( arr, i/2, min(i,n), x)

# count inversions in an array
# using selection sort; so Time Complexity: O(n^2)
# Also check merge sort implementation. https://www.geeksforgeeks.org/counting-inversions/. Time Complexity: O(nlogn)
def getInvCount(a):
    inv_count = 0
    for i in range(0, len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                # a[i], a[j] = a[j], a[i]
                inv_count += 1
                
    return inv_count

# find Two elements whose sum is closest to zero
# using selection sort; so Time Complexity: O(n^2)
# Check https://www.geeksforgeeks.org/two-elements-whose-sum-is-closest-to-zero/ for quick sort implementation. Time Complexity: O(nlogn)
def minAbsSumPair(a):
    inv_count = 0

    if len(a) < 2:
        print("Invalid Input")
        return
    
    min_i = 0
    min_j = 1
    min_sum = a[0] + a[1]
    for i in range (0, len(a) - 1):
        for j in range (i+1, len(a)):
            Sum = a[i] + a[j]                
            if abs(min_sum) > abs(Sum):         
                min_sum = Sum
                min_i = i
                min_j = j
 
    print "The two elements whose sum is minimum are", a[min_i], "and ", a[min_j]

'''
Count all distinct pairs with difference equal to k
Given an integer array and a positive integer k, count all distinct pairs with difference equal to k. 

Examples: 
Input: arr[] = {1, 5, 3, 4, 2}, k = 3
Output: 2
There are 2 pairs with difference 3, the pairs are {1, 4} and {5, 2} 

Input: arr[] = {8, 12, 16, 4, 0, 20}, k = 4
Output: 5
There are 5 pairs with difference 4, the pairs are {0, 4}, {4, 8}, 
{8, 12}, {12, 16} and {16, 20} 
Time Complexity: O(n^2)             <= Selection sort
Check https://www.geeksforgeeks.org/count-pairs-difference-equal-k/ for O(nlogn) time complexity
'''
# https://www.geeksforgeeks.org/write-a-c-program-that-given-a-set-a-of-n-numbers-and-another-number-x-determines-whether-or-not-there-exist-two-elements-in-s-whose-sum-is-exactly-x/
# Python program to find if there are two elements wtih given sum
# this also solves count pairs with given sum(if we put a counter); See the quicksort based solution in the following link
# Also refer the quicksort based solution at https://www.geeksforgeeks.org/write-a-c-program-that-given-a-set-a-of-n-numbers-and-another-number-x-determines-whether-or-not-there-exist-two-elements-in-s-whose-sum-is-exactly-x/
# Time complexity: O(n)
CONST_MAX = 100000
def PairsWithSumK(arr, Sum):
    binmap = [0]*CONST_MAX
    
    for i in range(0,len(arr)):
        temp = Sum-arr[i]
        if (temp>=0 and binmap[temp]==1):
            print "Pair with the given sum is", arr[i], "and", temp
        binmap[arr[i]]=1
        
# Find a pair with the given difference
def PairsWithDiffK(arr,Diff):
    binmap = [0]*CONST_MAX

    for i in xrange(0, len(arr)):
      temp = arr[i] + Diff
      if binmap[arr[i]] == 1:
        print "Pair with the given diff is", abs(arr[i]-Diff), "and", arr[i]
      binmap[temp] = 1

# find the maximum j - i such that arr[j] > arr[i]
# Time complexity: O(n^2)
# Check https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/ for better complexity
def maxIndexDiff(arr, n):
    maxDiff = -1
    for i in range(0, n):
        j = n - 1
        while(j > i):
            if arr[j] > arr[i] and maxDiff < (j - i):
                maxDiff = j - i;
            j -= 1
     
    return maxDiff

# Maximum difference between two elements such that larger element appears after the smaller number
# Examples: If array is [2, 3, 10, 6, 4, 8, 1] then returned value should be 8 (Diff between 10 and 2). If array is [ 7, 9, 5, 6, 3, 2 ] then returned value should be 2 (Diff between 7 and 9)
# Time Complexity: O(n^2)           <= uses selection sort. See the solution in commented section below to this for Time Complexity: O(n)
# Auxiliary Space: O(1)
def maxDiff(a):
    max_diff = a[1] - a[0]
     
    for i in range( 0, len(a)-1 ):
        for j in range( i+1, len(a) ):
            if(arr[j] - arr[i] > max_diff):
                max_diff = arr[j] - arr[i]
     
    return max_diff
'''
def maxDiff(arr):
    max_diff = arr[1] - arr[0]
    min_element = arr[0]
     
    for i in range( 1, len(arr) ):
        if (arr[i] - min_element > max_diff):
            max_diff = arr[i] - min_element
     
        if (arr[i] < min_element):
            min_element = arr[i]
    return max_diff
'''
# Sort an array of 0s, 1s and 2s
# Time Complexity: O(n)
def sort012( a, arr_size):
    lo = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi:
        if a[mid] == 0:
            a[lo],a[mid] = a[mid],a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid],a[hi] = a[hi],a[mid] 
            hi = hi - 1
    return a

# Python program to sort a binary array in one pass
# Function to put all 0s on left and all 1s on right
# Time Complexity: O(n)
def segregate0and1(arr):
    left, right = 0, len(arr)-1
     
    while left < right:
        while arr[left] == 0 and left < right:                                                                          # Increment left index while we see 0 at left
            left += 1
            
        while arr[right] == 1 and left < right:                                                                         # Decrement right index while we see 1 at right
            right -= 1
            
        if left < right:                                                                                                # If left is smaller than right then there is a 1 at left and a 0 at right. Exchange arr[left] and arr[right
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
 
    return arr

# program to segregate even and odd elements of array; Same as above
def segregateEvenOdd(arr):
    left,right = 0,len(arr)-1
 
    while left < right:
        while (arr[left]%2==0 and left < right):
            left += 1
            
        while (arr[right]%2 == 1 and left < right):
            right -= 1
 
        if (left < right):
              # Swap arr[left] and arr[right]*/
              arr[left],arr[right] = arr[right],arr[left]
              left += 1
              right -= 1

# Python program to push zeros to the end
# Time Complexity: O(n) where n is number of elements in input array.
# Auxiliary Space: O(1)
def pushZerosToEnd(arr):
    left, right = 0, len(arr)-1
     
    while left < right:
        while arr[left] != 0 and left < right:                                                                          # Increment left index while we see 0 at left
            left += 1
            
        while arr[right] == 0 and left < right:                                                                         # Decrement right index while we see 1 at right
            right -= 1
            
        if left < right:                                                                                                # If left is smaller than right then there is a 1 at left and a 0 at right. Exchange arr[left] and arr[right
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
 
    return arr

# Function to get index of ceiling of x in a sorted array
# Given a sorted array and a value x, the ceiling of x is the smallest element in array greater than or equal to x,
# and the floor is the greatest element smaller than or equal to x.
# Assume that the array is sorted in non-decreasing order. Write efficient functions to find floor and ceiling of x.
# As the array is sorted use binary search Time complexity: O(Logn)
def ceilSearch(arr, low, high, x):
    if x <= arr[low]:
        return low 
 
    if x > arr[high]:
        return -1
    
    mid = (low + high)/2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:                                                      # If x is greater than arr[mid], then either arr[mid + 1] is ceiling of x or ceiling lies in arr[mid+1...high]
        if mid + 1 <= high and x <= arr[mid+1]:
            return mid + 1
        else:
            return ceilSearch(arr, mid+1, high, x)
    else:                                                                   # If x is smaller than arr[mid], then either arr[mid] is ceiling of x or ceiling lies in arr[mid-1...high]
        if mid - 1 >= low and x > arr[mid-1]:
            return mid
        else:
            return ceilSearch(arr, low, mid - 1, x)
'''
Print next greater element(NGE)
This can be done using two for loops which is simple enough. But the complexity in this case is O(n^2) 
Method 2 (Using Stack)
 1) Push the first element to stack.
 2) Pick rest of the elements one by one and follow following steps in loop.
        a) Mark the current element as next.
        b) If stack is not empty, then pop an element from stack and compare it with next.
        c) If next is greater than the popped element, then next is the next greater element for the popped element.
        d) Keep popping from the stack while the popped element is smaller than next. next becomes the next greater element for all such popped elements
        g) If next is smaller than the popped element, then push the popped element back.
 3) After the loop in step 2 is over, pop all the elements from stack and print -1 as next element for them.
# prints element and NGE pair for all elements of arr[]
'''
# Stack Functions to be used by printNGE()
def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, x):
    stack.append(x)

def pop(stack):
    if isEmpty(stack):
        print("Error : stack underflow")
    else:
        return stack.pop()

def printNGE(arr):
    s = createStack()
    element = 0
    next = 0
    
    push(s, arr[0])
    
    for i in range(1, len(arr)):
        next = arr[i]
        if isEmpty(s) == False:
            element = pop(s)
            
            while element < next :
                print(str(element)+ " -- " + str(next))
                if isEmpty(s) == True :
                    break
                element = pop(s)
                
            if  element > next:
                push(s, element)
                
        push(s, next)
        
    while isEmpty(s) == False:                                  # After iterating over the loop, the remaining elements in stack do not have the next greater element, so print -1 for them
            element = pop(s)
            next = -1
            print(str(element) + " -- " + str(next))
            
# program to find the smallest elements missing in a sorted array
# Note:  This method doesn't work if there are duplicate elements in the array.
# Time Complexity: O(Logn)
def findFirstMissing(array, start, end): 
    if (start > end):
        return end + 1
 
    if (start != array[start]):
        return start;
 
    mid = int((start + end) / 2)
    
    if (array[mid] == mid):                                             # Left half has all elements from 0 to mid
        return findFirstMissing(array, mid+1, end)
 
    return findFirstMissing(array, start, mid)

# find the maximum for each and every contiguous subarray of size k
# time complexity is O((n-k+1)*k
# Check dequeue method at https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/ for O(n) time complexity and O(k) Auxiliary space
def printMax(arr, k):
    n = len(arr)
    max = 0
   
    for i in range(n - k + 1):
        max = arr[i]
        for j in range(1, k):
            if arr[i+j] > max:
                max = arr[i + j]
        print str(max),

# Find the minimum distance between two numbers
# MY SOLUTION
# Time complexity: O(n)
def minDist(arr, n, x, y):
    first = 3
    second = 6
    first_i = 0
    second_i = 0
    min_dist = n

    for i in range(n):
        if arr[i] == first:
          first_i = i
        elif arr[i] == second:
          second_i = i
        diff = abs(first_i - second_i)

        if diff != 0 and diff < min_dist:
          min_dist = diff
    return min_dist

# Implement two stacks in a list
'''
Implement two stacks in an array
Create a data structure twoStacks that represents two stacks. Implementation of twoStacks should use only one array, i.e., both stacks should use the same array for storing elements.
Following functions must be supported by twoStacks.

push1(int x) -> pushes x to first stack
push2(int x) -> pushes x to second stack

pop1() -> pops an element from first stack and return the popped element
pop2() -> pops an element from second stack and return the popped element

Implementation of twoStack should be space efficient.
Method 1 (Divide the space in two halves)
 A simple way to implement two stacks is to divide the array in two halves and assign the half half space to two stacks, i.e., use arr[0] to arr[n/2] for stack1,
 and arr[n/2+1] to arr[n-1] for stack2 where arr[] is the array to be used to implement two stacks and size of array be n.
 
The problem with this method is inefficient use of array space. A stack push operation may result in stack overflow even if there is space available in arr[].
For example, say the array size is 6 and we push 3 elements to stack1 and do not push anything to second stack2. When we push 4th element to stack1,
there will be overflow even if we have space for 3 more elements in array.

Method 2 (A space efficient implementation)
 This method efficiently utilizes the available space. It doesn't cause an overflow if there is space available in arr[].
 The idea is to start two stacks from two extreme corners of arr[]. stack1 starts from the leftmost element, the first element in stack1 is pushed at index 0.
 The stack2 starts from the rightmost corner, the first element in stack2 is pushed at index (n-1). Both stacks grow (or shrink) in opposite direction.
 To check for overflow, all we need to check is for space between top elements of both stacks. This check is highlighted in the below code.
 Time complexity of all 4 operations of twoStack  is O(1).
'''
class twoStacks:     
    def __init__(self, n):                                                                  #constructor
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size
                                                                                            # Method to push an element x to stack1
    def push1(self, x):                                                                     # There is at least one empty space for new element
        if self.top1 < self.top2 - 1 :
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x
        else:
            print("Stack Overflow ")
            exit(1)
                                                                                            # Method to push an element x to stack2
    def push2(self, x):
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = x
        else :
           print("Stack Overflow ")
           exit(1)
                                                                                            # Method to pop an element from first stack
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 = self.top1 -1
            return x
        else:
            print("Stack Underflow ")
            exit(1)
                                                                                            # Method to pop an element from second stack
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return x
        else:
            print("Stack Underflow ")
            exit()

# print subarray with sum as given sum
# Time complexity: O(n)
def subArraySum(arr, n, Sum):
    curr_sum = arr[0]
    start = 0
    
    i = 1
    while i <= n:                                                                       # Add elements one by one to curr_sum and if the curr_sum exceeds the sum, then remove starting element
        while curr_sum > Sum and start < i-1:                                           # If curr_sum exceeds the sum, then remove the starting elements
            curr_sum = curr_sum - arr[start]
            start += 1
            
        if curr_sum == Sum:                                                             # If curr_sum becomes equal to sum, then return true
            print ("Sum found between indexes")
            print ("%d and %d"%(start, i-1))
            return 1
        
        if i < n:                                                                       # Add this element to curr_sum
            curr_sum = curr_sum + arr[i]
        i += 1
        
    print ("No subarray found")                                                         # If we reach here, then no subarray
    return 0

# find a triplet
# returns true if there is triplet with sum equal to 'sum' present in A[]. Also, prints the triplet
# A naive approach is to use 3 loops; but then the complexity becomes O(n^3). To reduce it, sort the array first. The complexity in this case becomes O(n^2)
def find3Numbers(A, arr_size, Sum): 
    A.sort() 
    for i in range(0, arr_size-2):                                  # Now fix the first element one by one and find the other two elements      
        
        l = i + 1                                                   # index of the first element in the remaining elements
        r = arr_size-1                                              # index of the last element

        while (l < r):                                              # To find the other two elements, start two index variables from two corners of the array and move them toward each other
            if( A[i] + A[l] + A[r] == Sum):
                print("Triplet is", A[i], ',', A[l], ',', A[r])
                return True
            elif (A[i] + A[l] + A[r] < Sum):
                l += 1
            else:
                r -= 1
                
    return False

# Python program for maximum contiguous circular sum problem 
# Standard Kadane's algorithm to find maximum subarray sum
'''
Given n numbers (both +ve and -ve), arranged in a circle, fnd the maximum sum of consecutive number. 
Input: a[] = {8, -8, 9, -9, 10, -11, 12}
Output: 22 (12 + 8 - 8 + 9 - 9 + 10)

Input: a[] = {10, -3, -4, 7, 6, 5, -4, -1} 
Output:  23 (7 + 6 + 5 - 4 -1 + 10) 

Input: a[] = {-1, 40, -14, 7, 6, 5, -4, -1}
Output: 52 (7 + 6 + 5 - 4 - 1 - 1 + 40)
'''
def kadane(a):
    n = len(a)
    max_so_far = 0
    max_ending_here = 0
    for i in range(0, n):
        max_ending_here = max_ending_here + a[i]
        if (max_ending_here < 0):
            max_ending_here = 0
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
    return max_so_far
 
# The function returns maximum circular contiguous sum in
# a[]
def maxCircularSum(a):
 
    n = len(a)
 
    # Case 1: get the maximum sum using standard kadane's
    # algorithm
    max_kadane = kadane(a)
 
    # Case 2: Now find the maximum sum that includes corner
    # elements.
    max_wrap = 0
    for i in range(0,n):
        max_wrap += a[i]
        a[i] = -a[i]
 
    # Max sum with corner elements will be:
    # array-sum - (-max subarray sum of inverted array)
    max_wrap = max_wrap + kadane(a)
 
    # The maximum circular sum will be maximum of two sums
    if max_wrap > max_kadane:
        return max_wrap
    else:
        return max_kadane

# Python Program to shuffle a given array
# Time Complexity: O(n), assuming that the function rand() takes O(1) time.
import random
def randomize (arr, n):
    for i in range(n-1,0,-1):
        j = random.randint(0,i)                                                     # Pick a random index from 0 to i
        arr[i],arr[j] = arr[j],arr[i]                                               # Swap arr[i] with the element at random index
    return arr

'''
Count all possible groups of size 2 or 3 that have sum as multiple of 3
Given an unsorted integer (positive values only) array of size n, we can form a group of two or three, the group should be such that the sum of all elements in that group is a multiple of 3.
Count all possible number of groups that can be generated in this way.
Input: arr[] = {3, 6, 7, 2, 9}
Output: 8
Groups are {3,6}, {3,9}, {9,6}, {7,2}, {3,6,9},{3,7,2}, {7,2,6}, {7,2,9}

Input: arr[] = {2, 1, 3, 4}
Output: 4
Groups are {2,1}, {2,4}, {2,1,3}, {2,4,3}

Time Complexity: O(n)
Auxiliary Space: O(1)
'''
def findgroups(arr, n):
 
    # Create an array C[3] to store
    # counts of elements with 
    # remainder 0, 1 and 2. c[i] 
    # would store count of elements 
    # with remainder i
    c = [0, 0, 0]
 
    # To store the result
    res = 0
 
    # Count elements with remainder 
    # 0, 1 and 2
    for i in range(0, n):
        c[arr[i] % 3] += 1
 
    # Case 3.a: Count groups of size
    # 2 from 0 remainder elements
    res += ((c[0] * (c[0] - 1)) >> 1)
 
    # Case 3.b: Count groups of size
    # 2 with one element with 1
    # remainder and other with 2 remainder
    res += c[1] * c[2]
 
    # Case 4.a: Count groups of size
    # 3 with all 0 remainder elements
    res += (c[0] * (c[0] - 1) * (c[0] - 2)) / 6
 
    # Case 4.b: Count groups of size 3
    # with all 1 remainder elements
    res += (c[1] * (c[1] - 1) * (c[1] - 2)) / 6
 
    # Case 4.c: Count groups of size 3 
    # with all 2 remainder elements
    res += ((c[2] * (c[2] - 1) * (c[2] - 2)) / 6)
 
    # Case 4.c: Count groups of size 3
    # with different remainders
    res += c[0] * c[1] * c[2]
 
    # Return total count stored in res
    return res

'''
Rearrange an array so that arr[i] becomes arr[arr[i]] with O(1) extra space
Examples: 
Input: arr[]  = {3, 2, 0, 1}
Output: arr[] = {1, 0, 3, 2}

Input: arr[] = {4, 0, 2, 1, 3}
Output: arr[] = {3, 4, 2, 0, 1}

Input: arr[] = {0, 1, 2, 3}
Output: arr[] = {0, 1, 2, 3}

Time Complexity: O(n)
Auxiliary Space: O(1)
'''
def rearrange(arr, n): 
    # First step: Increase all values
    # by (arr[arr[i]] % n) * n
    for i in range(0, n):
        arr[i] += (arr[arr[i]] % n) * n
 
    # Second Step: Divide all values
    # by n
    for i in range(0, n):
        arr[i] = int(arr[i] / n)

# A python 3 program to find a peak 
# element element using divide and conquer
 
# A binary search based function 
# that returns index of a peak element
def findPeakUtil(arr, low, high, n):
    # Find index of middle element (low + high)/2
    mid = low + (high - low)/2
    mid = int(mid)

    # Compare middle element with its 
    # neighbours (if neighbours exist)
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid
 
 
    # If middle element is not peak and 
    # its left neighbour is greater 
    # than it, then left half must 
    # have a peak element
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findPeakUtil(arr, low, (mid - 1), n)
 
    # If middle element is not peak and
    # its right neighbour is greater
    # than it, then right half must 
    # have a peak element
    else:
        return findPeakUtil(arr, (mid + 1), high, n)
 
 
# A wrapper over recursive 
# function findPeakUtil()
# Time Complexity: O(Logn) where n is number of elements in input array.
def findPeak(arr, n):
    return findPeakUtil(arr, 0, n - 1, n)

'''
find a sorted subsequence of size 3

Given an array of n integers, find the 3 elements such that a[i] < a[j] < a[k] and i < j < k in 0(n) time. If there are multiple such triplets, then print any one of them.
Examples:
Input:  arr[] = {12, 11, 10, 5, 6, 2, 30}
Output: 5, 6, 30

Input:  arr[] = {1, 2, 3, 4}
Output: 1, 2, 3 OR 1, 2, 4 OR 2, 3, 4

Input:  arr[] = {4, 3, 2, 1}
Output: No such triplet

Time Complexity: O(n)
Auxliary Space: O(n)
'''
def find3numbers(arr):
    n = len(arr)
    max = n-1
    min = 0

    smaller = [0]*10000                         # Create an array that will store index of a smaller element on left side. If there is no smaller element on left side, then smaller[i] will be -1.
    smaller[0] = -1
    for i in range(1,n):
        if (arr[i] <= arr[min]):
            min = i
            smaller[i] = -1
        else:
            smaller[i] = min
            
    greater = [0]*10000                         # Create another array that will store index of a greater element on right side. If there is no greater element on right side, then greater[i] will be -1.
    greater[n-1] = -1
 
    for i in range(n-2,-1,-1):
        if (arr[i] >= arr[max]):
            max = i
            greater[i] = -1
        else:
            greater[i] = max
 
    # Now find a number which has both a greater number on
    # right side and smaller number on left side
    for i in range(0,n):
        if smaller[i] != -1 and greater[i] != -1:
            print arr[smaller[i]], arr[i], arr[greater[i]]
            return
        
    print "No triplet found"
    return

'''
A simple program to find the largest subarray with equal number of 0s and 1s
Time Complexity: O(n^2)
Auxiliary Space: O(1)
for better complexity checkout https://www.geeksforgeeks.org/largest-subarray-with-equal-number-of-0s-and-1s/
'''
def findSubArray(arr, n):
    sum = 0
    maxsize = -1
 
    # Pick a starting point as i
    for i in range(0, n-1):
     
        sum = -1 if(arr[i] == 0) else 1
        # Consider all subarrays starting from i
        for j in range(i + 1, n):
            sum = sum + (-1) if (arr[j] == 0) else sum + 1
            # If this is a 0 sum subarray, then 
            # compare it with maximum size subarray
            # calculated so far
 
            if (sum == 0 and maxsize < j-i + 1):
                maxsize = j - i + 1
                startindex = i

    if (maxsize == -1):
        print("No such subarray");
    else:
        print(startindex, "to", startindex + maxsize-1);
    return maxsize

# replace every element with the greatest element on right side
'''
Given an array of integers, replace every element with the next greatest element (greatest element on the right side) in the array.
Since there is no element next to the last element, replace it with -1.
For example, if the array is {16, 17, 4, 3, 5, 2}, then it should be modified to {17, 5, 5, 5, 2, -1}.
'''
def nextGreatest(arr): 
    size = len(arr)
    # Initialize the next greatest element
    max_from_right = arr[size-1]
 
    # The next greatest element for the rightmost element
    # is always -1
    arr[size-1] = -1
 
    # Replace all other elements with the next greatest
    for i in range(size-2,-1,-1):
        # Store the current element (needed later for updating
        # the next greatest element)
        temp = arr[i]
 
        # Replace current element with the next greatest
        arr[i]=max_from_right
 
        # Update the greatest element, if needed
        if max_from_right< temp:
            max_from_right=temp

'''
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.
A pair (c, d) can follow another pair (a, b) if b < c. Chain of pairs can be formed in this fashion.
Find the longest chain which can be formed from a given set of pairs. Source: Amazon Interview | Set 2

For example, if the given pairs are {{5, 24}, {39, 60}, {15, 28}, {27, 40}, {50, 90} }, then the longest chain that
can be formed is of length 3, and the chain is {{5, 24}, {27, 40}, {50, 90}}
Time Complexity: O(n^2)
'''
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
# This function assumes that arr[] is sorted in increasing
# order according the first (or smaller) values in pairs.
def maxChainLength(arr, n):
     
    max = 0
 
    # Initialize MCL(max chain length) values for all indices
    mcl = [1 for i in range(n)]
 
    # Compute optimized chain length values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if (arr[i].a > arr[j].b and mcl[i] < mcl[j] + 1):
                mcl[i] = mcl[j] + 1
 
    # mcl[i] now stores the maximum
    # chain length ending with pair i
 
    # Pick maximum of all MCL values
    for i in range(n):
        if (max < mcl[i]):
            max = mcl[i]
 
    return max

# Rearrange positive and negative numbers in O(n) time and O(1) extra space
#  Python program to put positive numbers at even indexes (0,  // 2, 4,..) and
#  negative numbers at odd indexes (1, 3, 5, ..)
def rearrange(arr, n):
    # The following few lines are similar to partition process
    # of QuickSort.  The idea is to consider 0 as pivot and
    # divide the array around it.
    i = -1
    for j in range(n):
        if (arr[j] < 0):
            i += 1
            # swapping of arr
            arr[i], arr[j] = arr[j], arr[i]
  
    # Now all positive numbers are at end and negative numbers
    # at the beginning of array. Initialize indexes for starting
    # point of positive and negative numbers to be swapped
    pos, neg = i+1, 0
  
    # Increment the negative index by 2 and positive index by 1,
    # i.e., swap every alternate negative number with next 
    # positive number
    while (pos < n and neg < pos and arr[neg] < 0):
 
        # swapping of arr
        arr[neg], arr[pos] = arr[pos], arr[neg]
        pos += 1
        neg += 2

# Python3 program to
# sort array using
# pancake sort
 
# Reverses arr[0..i] */
def flip(arr, i):
    start = 0
    while start < i:
        temp = arr[start]
        arr[start] = arr[i]
        arr[i] = temp
        start += 1
        i -= 1
 
# Returns index of the maximum
# element in arr[0..n-1] */
def findMax(arr, n):
    mi = 0
    for i in range(0,n):
        if arr[i] > arr[mi]:
            mi = i
    return mi
 
# The main function that sorts given array using flip operations
'''
Pancake sorting
Given an an unsorted array, sort the given array. You are allowed to do only following operation on array. 
flip(arr, i): Reverse array from 0 to i 

Unlike a traditional sorting algorithm, which attempts to sort with the fewest comparisons possible, the goal is to sort the sequence in as few reversals as possible. 

The idea is to do something similar to Selection Sort. We one by one place maximum element at the end and reduce the size of current array by one. 

Following are the detailed steps. Let given array be arr[] and size of array be n.
 1) Start from current size equal to n and reduce current size by one while it's greater than 1. Let the current size be curr_size. Do following for every curr_size
 a) Find index of the maximum element in arr[0..curr_szie-1]. Let the index be mi
 b) Call flip(arr, mi)
 c) Call flip(arr, curr_size-1)
 Total O(n) flip operations are performed in above code. The overall time complexity is O(n^2).
'''
def pancakeSort(arr, n):
     
    # Start from the complete
    # array and one by one
    # reduce current size
    # by one
    curr_size = n
    while curr_size > 1:
        # Find index of the maximum
        # element in 
        # arr[0..curr_size-1]
        mi = findMax(arr, curr_size)
 
        # Move the maximum element
        # to end of current array
        # if it's not already at 
        # the end
        if mi != curr_size-1:
            # To move at the end, 
            # first move maximum 
            # number to beginning 
            flip(arr, mi)
 
            # Now move the maximum 
            # number to end by
            # reversing current array
            flip(arr, curr_size-1)
        curr_size -= 1
'''
A Binary Search based function to get index of ceiling of x in arr[low..high]
A Pancake Sorting Problem
We have discussed Pancake Sorting in the previous post. Following is a problem based on Pancake Sorting.
 Given an an unsorted array, sort the given array. You are allowed to do only following operation on array. 
flip(arr, i): Reverse array from 0 to i 

Imagine a hypothetical machine where flip(i) always takes O(1) time. Write an efficient program for sorting a given array in O(nLogn) time on the given machine. If we apply the same algorithm here, the time taken will be O(n^2) because the algorithm calls findMax() in a loop and find findMax() takes O(n) time even on this hypothetical machine.

We can use insertion sort that uses binary search. The idea is to run a loop from second element to last element (from i = 1 to n-1), and one by one insert arr[i] in arr[0..i-1] (like standard insertion sort algorithm). When we insert an element arr[i], we can use binary search to find position of arr[i] in O(Logi) time. Once we have the position, we can use some flip operations to put arr[i] at its new place. Following are abstract steps. 
// Standard Insertion Sort Loop that starts from second element
for (i=1; i < n; i++) ----> O(n)
{
  int key = arr[i];

  // Find index of ceiling of arr[i] in arr[0..i-1] using binary search
  j = celiSearch(arr, key, 0, i-1); ----> O(logn) (See this)
    
  // Apply some flip operations to put arr[i] at correct place
} 

Since flip operation takes O(1) on given hypothetical machine, total running time of above algorithm is O(nlogn). Thanks to Kumar for suggesting above problem and algorithm.
Let us see how does the above algorithm work. ceilSearch() actually returns the index of the smallest element which is greater than arr[i] in arr[0..i-1].
If there is no such element, it returns -1. Let the returned value be j. If j is -1, then we don't need to do anything as arr[i] is already the greatest element among arr[0..i]. Otherwise we need to put arr[i] just before arr[j].
 So how to apply flip operations to put arr[i] just before arr[j] using values of i and j. Let us take an example to understand this. Let i be 6 and current array be {12, 15, 18, 30, 35, 40, 20, 6, 90, 80}. To put 20 at its new place, the array should be changed to {12, 15, 18, 20, 30, 35, 40, 6, 90, 80}. We apply following steps to put 20 at its new place.
 
1) Find j using ceilSearch (In the above example j is 3).
 2) flip(arr, j-1) (array becomes {18, 15, 12, 30, 35, 40, 20, 6, 90, 80})
 3) flip(arr, i-1); (array becomes {40, 35, 30, 12, 15, 18, 20, 6, 90, 80})
 4) flip(arr, i); (array becomes {20, 18, 15, 12, 30, 35, 40, 6, 90, 80})
 5) flip(arr, j); (array becomes {12, 15, 18, 20, 30, 35, 40, 6, 90, 80})
'''
def ceilSearch(arr,low,high,x):
     
    #If x is smaller than or equal to the first element,
    #then return the first element
    if x <= arr[low]:
        return low
     
    #If x is greater than the last element, then return -1
    if x > arr[high]:
        return -1
         
    #get the index of middle element of arr[low..high]
    mid = (low + high)/2  #low + (high-low)/2
     
    #If x is same as middle element, then return mid
    if(arr[mid] == x):
        return mid
     
    #If x is greater than arr[mid], then either arr[mid + 1]
    #is ceiling of x, or ceiling lies in arr[mid+1...high]
    if(arr[mid] < x):
        if(mid + 1 <= high and x <= arr[mid+1]):
            return mid + 1
        else:
            return ceilSearch(arr, mid+1, high, x)
     
    #If x is smaller than arr[mid], then either arr[mid]
    #is ceiling of x or ceiling lies in arr[mid-1...high]
    if (mid - 1 >= low and x > arr[mid-1]):
        return mid
    else:
        return ceilSearch(arr, low, mid - 1, x)
         
#Reverses arr[0..i] */
def flip(arr,i):
     
    start = 0;
    while (start < i):
        temp = arr[start]
        arr[start] = arr[i]
        arr[i] = temp
        start+=1
        i-=1
 
#Function to sort an array using insertion sort, binary search and flip
def insertionSort(arr):
     
    #Start from the second element and one by one insert arr[i]
    #in already sorted arr[0..i-1]
    for i in range(1,len(arr)):
        #Find the smallest element in arr[0..i-1] which is also greater than
        #or equal to arr[i]
        j = ceilSearch(arr, 0, i-1, arr[i])
         
        #Check if there was no element greater than arr[i]
        if (j != -1):
            #Put arr[i] before arr[j] using following four flip operations
            flip(arr, j-1)
            flip(arr, i-1)
            flip(arr, i)
            flip(arr, j)

# Python program to find circular tour for a track  
# A petrol pump has petrol and distance to next petrol pump
'''
Find the first circular tour that visits all petrol pumps
Suppose there is a circle. There are n petrol pumps on that circle. You are given two sets of data.

1. The amount of petrol that every petrol pump has.
2. Distance from that petrol pump to the next petrol pump.

Calculate the first point from where a truck will be able to complete the circle (The truck will stop at each petrol pump and it has infinite capacity). Expected time complexity is O(n).
Assume for 1 litre petrol, the truck can go 1 unit of distance.

For example, let there be 4 petrol pumps with amount of petrol and distance to next petrol pump value pairs as {4, 6}, {6, 5}, {7, 3} and {4, 5}.
The first point from where truck can make a circular tour is 2nd petrol pump. Output should be "start = 1" (index of 2nd petrol pump).

A Simple Solution is to consider every petrol pumps as starting point and see if there is a possible tour. If we find a starting point with feasible solution, we return that starting point.
The worst case time complexity of this solution is O(n^2).

We can use a Queue to store the current tour. We first enqueue first petrol pump to the queue, we keep enqueueing petrol pumps till we either complete the tour, or
current amount of petrol becomes negative. If the amount becomes negative, then we keep dequeueing petrol pumps till the current amount becomes positive or queue becomes empty.

Instead of creating a separate queue, we use the given array itself as queue. We maintain two index variables start and end that represent rear and front of queue.
'''
class PetrolPump:
     
    # Constructor to create a new node
    def __init__(self,petrol, distance):
        self.petrol = petrol
        self.distance = distance 
 
# The funtion return starting point if there is a possible solution otherwise returns -1
def printTour(arr):
    n = len(arr)
    # Consider first petrol pump as starting point
    start = 0
    end = 1
     
    curr_petrol = arr[start].petrol - arr[start].distance 
     
    # Run a loop whie all petrol pumps are not visited
    # And we have reached first petrol pump again with 0 
    # or more petrol
    while(end != start or curr_petrol < 0 ):
         
        # If current amount of petrol pumps are not visited
        # And we have reached first petrol pump again with
        # 0 or more petrol 
        while(curr_petrol < 0 and start != end):
             
            # Remove starting petrol pump. Change start
            curr_petrol -= arr[start].petrol - arr[start].distance
            start = (start +1)%n
             
            # If 0 is being considered as start again, then
            # there is no possible solution
            if start == 0:
                return -1
 
        # Add a petrol pump to current tour
        curr_petrol += arr[end].petrol - arr[end].distance  
        end = (end +1) % n
    return start
'''
Count the number of possible triangles
Given an unsorted array of positive integers. Find the number of triangles that can be formed with three different array elements as three sides of triangles.
For a triangle to be possible from 3 values, the sum of any two values (or sides) must be greater than the third value (or third side).
 For example, if the input array is {4, 6, 3, 7}, the output should be 3. There are three triangles possible {3, 4, 6}, {4, 6, 7} and {3, 6, 7}. Note that {3, 4, 7} is not a possible triangle.
 As another example, consider the array {10, 21, 22, 100, 101, 200, 300}. There can be 6 possible triangles: {10, 21, 22}, {21, 100, 101}, {22, 100, 101}, {10, 100, 101}, {100, 101, 200} and
 {101, 200, 300}

 If we run 3 loops then Time Complexity: O(N^3) where N is the size of input array. We can reduce the complexity by sorting the array. Here is the example
Time Complexity: O(n^2). The time complexity looks more because of 3 nested loops. If we take a closer look at the algorithm, we observe that k is initialized only once in the outermost loop.
The innermost loop executes at most O(n) time for every iteration of outer most loop, because k starts from i+2 and goes upto n for all values of j. Therefore, the time complexity is O(n^2).
'''
def findnumberofTriangles(arr):
    # Sort array and initialize count as 0
    n = len(arr)
    arr.sort()
    count = 0
 
    # Fix the first element.  We need to run till n-3 as
    # the other two elements are selected from arr[i+1...n-1]
    for i in range(0,n-2):
 
        # Initialize index of the rightmost third element
        k = i + 2
 
        # Fix the second element
        for j in range(i+1,n):
 
            # Find the rightmost element which is smaller
            # than the sum of two fixed elements
            # The important thing to note here is, we use
            # the previous value of k. If value of arr[i] +
            # arr[j-1] was greater than arr[k], then arr[i] +
            # arr[j] must be greater than k, because the array
            # is sorted.
            while (k < n and arr[i] + arr[j] > arr[k]):
                k += 1
 
             # Total number of possible triangles that can be
             # formed with the two fixed elements is k - j - 1.
             # The two fixed elements are arr[i] and arr[j]. All
             # elements between arr[j+1] to arr[k-1] can form a
             # triangle with arr[i] and arr[j]. One is subtracted
             # from k because k is incremented one extra in above
             # while loop. k will always be greater than j. If j
             # becomes equal to k, then above loop will increment k,
             #  because arr[k] + arr[i] is always greater than arr[k]
            count += k - j - 1
 
    return count

'''
Time Complexity: O(n^4)

The time complexity can be improved to O(n^3) with the use of sorting as a preprocessing step, and then using method 1 of this  post to reduce a loop.

Following are the detailed steps.
 1) Sort the input array.
 2) Fix the first element as A[i] where i is from 0 to n-3. After fixing the first element of quadruple, fix the second element as A[j] where j varies from i+1 to n-2.
 Find remaining two elements in O(n) time, using the method 1 of this  post 
'''
def findFourElements(A, n, X):
    for i in range(0,n-3):
        for j in range(i+1,n-2):
            for k in range(j+1,n-1):
                for l in range(k+1,n):                
                    if A[i] + A[j] + A[k] + A[l] == X:
                        print ("%d, %d, %d, %d"
                        %( A[i], A[j], A[k], A[l]))

# https://www.geeksforgeeks.org/product-array-puzzle-set-2-o1-space/
'''
Given an array arr[] of n integers, construct a Product Array prod[] (of same size) such that prod[i] is equal to the product of all the elements of arr[] except arr[i].
Solve it without division operator and in O(n).
Example:
 arr[] = {10, 3, 5, 6, 2}
 prod[] = {180, 600, 360, 300, 900}
Algorithm:
 1) Construct a temporary array left[] such that left[i] contains product of all elements on left of arr[i] excluding arr[i].
 2) Construct another temporary array right[] such that right[i] contains product of all elements on on right of arr[i] excluding arr[i].
 3) To get prod[], multiply left[] and right[].
'''
def productArray(arr):
    n = len(arr)
    temp = 1
    prod = [0]*n
    
    for i in xrange(0, n):
        prod[i] = temp
        temp *= arr[i]

    temp = 1
    for i in reversed(range(0, n)):
        prod[i] *= temp
        temp *= arr[i]

    for i in xrange(0, n):
        print prod[i],
    return

class Interval:
    buy=0
    sell=0

#Stock Buy Sell to Maximize Profit
#This function finds the buy sell schedule for maximum profit
#Time Complexity: The outer loop runs till i becomes n-1. The inner two loops increment value of i in every iteration. So overall time complexity is O(n)
'''
The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days.  For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum profit can earned by buying on day 0, selling on day 3. Again buy on day 4 and sell on day 6. If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.
If we are allowed to buy and sell only once, then we can use following algorithm. Maximum difference between two elements. Here we are allowed to buy and sell multiple times. Following is algorithm for this problem.
1. Find the local minima and store it as starting index. If not exists, return.
2. Find the local maxima. and store it as ending index. If we reach the end, set the end as ending index.
3. Update the solution (Increment count of buy sell pairs)
4. Repeat the above steps if end is not reached.
'''
def stockBuySell(price):
    n = len(price)
    if (n == 1):                                                        # Prices must be given for at least two days
        return

    count = 0
    sol = []                                                            # solution array
    i = 0
    while (i < n - 1):
        while ((i < n - 1) and (price[i + 1] <= price[i])):             # Find Local Minima. Note that the limit is (n-2) as we are comparing present element to the next element.
            i+=1

        if (i == n - 1):                                                # If we reached the end, break as no further solution possible
            break

        e = Interval()
        e.buy = i                                                       # Store the index of minima
        i += 1
        while ((i < n) and (price[i] >= price[i - 1])):                 # Find Local Maxima.  Note that the limit is (n-1) as we are comparing to previous element
            i += 1

        e.sell = i-1                                                    # Store the index of maxima
        sol.append(e)

        count+=1                                                        # Increment number of buy/sell
    # print solution
    if (count == 0):
        print("There is no day when buying the stock will make profit")
    else:
        for j in xrange(0, count):
            print "Buy on day: " + str(sol[j].buy) +"        " + "Sell on day : " + str(sol[j].sell)

    return

# Python program to match wild card characters
# The main function that checks if two given strings match.
# The first string may contain wildcard characters
def match(first, second):
 
    # If we reach at the end of both strings, we are done
    if len(first) == 0 and len(second) == 0:
        return True
 
    # Make sure that the characters after '*' are present
    # in second string. This function assumes that the first
    # string will not contain two consecutive '*'
    if len(first) > 1 and first[0] == '*' and  len(second) == 0:
        return False
 
    # If the first string contains '?', or current characters
    # of both strings match
    if (len(first) > 1 and first[0] == '?') or (len(first) != 0
        and len(second) !=0 and first[0] == second[0]):
        return match(first[1:],second[1:]);
 
    # If there is *, then there are two possibilities
    # a) We consider current character of second string
    # b) We ignore current character of second string.
    if len(first) !=0 and first[0] == '*':
        return match(first[1:],second) or match(first,second[1:])
 
    return False
 
# A function to run test cases
def test(first, second):
    if match(first, second):
        print "Yes"
    else:
        print "No"

# Utility function to convert string to list
def toList(string):
    l = []
    for x in string:
        l.append(x)
    return l

'''
Remove b and ac from a given string
Given a string, eliminate all b and ac in the string, you have to replace them in-place, and you are only allowed to iterate over the string once. (Source Google Interview Question)

Examples: 
acbac   ==>  ""
aaac    ==>  aa
ababac  ==>   aa
bbbbd   ==>   d
'''
# Utility function to convert list to string
def toString(l):
    return ''.join(l)
 
def stringFilter(string):
 
    # length of string
    n = len(string)
 
    i = -1
    j = 0
 
    while j < n:
 
        # Check if current and next character forms ac
        if j < n-1 and string[j] == 'a' and string[j+1] == 'c':
            j += 2
 
        # If current character is b
        elif string[j] == 'b':
            j += 1
 
        # if current char is 'c && last char in output
        # is 'a' so delete both
        elif i >= 0 and string[j] == 'c' and string[i] == 'a':
            i -= 1
            j += 1
 
        # Else copy curr char to output string
        else:
            i += 1
            string[i] = string[j]
            j += 1
 
    i += 1
    return toString(string[:i])

# Python program to recursively remove all adjacent duplicates from a string 
# Recursively removes adjacent duplicates from str and returns
# new string. las_removed is a pointer to last_removed character
#Time Complexity: The time complexity of the solution can be written as T(n) = T(n-k) + O(k) where n is length of the input string and k is the number of first characters which are same.
#Solution of the recurrence is O(n)
def removeUtil(string, last_removed):
 
    # If length of string is 1 or 0
    if len(string) == 0 or len(string) == 1:
        return string
 
    # Remove leftmost same characters and recur for remaining 
    # string
    if string[0] == string[1]:
        last_removed = ord(string[0])
        while len(string) > 1 and string[0] == string[1]:
            string = string[1:]
        string = string[1:]
 
        return removeUtil(string, last_removed)
 
    # At this point, the first character is definiotely different
    # from its adjacent. Ignore first character and recursively 
    # remove characters from remaining string
    rem_str = removeUtil(string[1:], last_removed)
 
    # Check if the first character of the rem_string matches 
    # with the first character of the original string
    if len(rem_str) != 0 and rem_str[0] == string[0]:
        last_removed = ord(string[0])
        return (rem_str[1:])
 
    # If remaining string becomes empty and last removed character
    # is same as first character of original string. This is needed
    # for a string like "acbbcddc"
    if len(rem_str) == 0 and last_removed == ord(string[0]):
        return rem_str
 
    # If the two first characters of str and rem_str don't match, 
    # append first character of str before the first character of 
    # rem_str.
    return ([string[0]] + rem_str)
 
def remove(string):
    last_removed = 0
    return toString(removeUtil(toList(string), last_removed))
 
# Utility functions
def toList(string):
    x = []
    for i in string:
        x.append(i)
    return x
 
def toString(x):
    return ''.join(x)

#Python program to rearrange a string so that all same 
#characters become at least d distance away
'''
Time Complexity: Time complexity of above implementation is O(n + mLog(MAX)). Here n is the length of str, m is count of distinct characters in str[] and
MAX is maximum possible different characters. MAX is typically 256 (a constant) and m is smaller than MAX. So the time complexity can be considered as O(n). 
'''
MAX = 256
 
# A structure to store a character 'c' and its frequency 'f'
# in input string
class charFreq(object):
    def __init__(self,c,f):
        self.c = c
        self.f = f
 
# A utility function to swap two charFreq items.
def swap(x, y):
    return y, x
 
# A utility function
def toList(string):
    t = []
    for x in string:
        t.append(x)
 
    return t
 
# A utility function
def toString(l):
    return ''.join(l)
 
# A utility function to maxheapify the node freq[i] of a heap
# stored in freq[]
def maxHeapify(freq, i, heap_size):
    l = i*2 + 1
    r = i*2 + 2
    largest = i
    if l < heap_size and freq[l].f > freq[i].f:
        largest = l
    if r < heap_size and freq[r].f > freq[largest].f:
        largest = r
    if largest != i:
        freq[i], freq[largest] = swap(freq[i], freq[largest])
        maxHeapify(freq, largest, heap_size)
 
# A utility function to convert the array freq[] to a max heap
def buildHeap(freq, n):
    i = (n - 1)/2
    while i >= 0:
        maxHeapify(freq, i, n)
        i-=1
 
# A utility function to remove the max item or root from max heap
def extractMax(freq, heap_size):
    root = freq[0]
    if heap_size > 1:
        freq[0] = freq[heap_size-1]
        maxHeapify(freq, 0, heap_size-1)
 
    return root
 
# The main function that rearranges input string 'str' such that
# two same characters become d distance away
def rearrangeDdistance(string, d):
    # Find length of input string
    n = len(string)
 
    # Create an array to store all characters and their
    # frequencies in str[]
    freq = []
    for x in xrange(MAX):
        freq.append(charFreq(0,0))
 
    m = 0
 
    # Traverse the input string and store frequencies of all
    # characters in freq[] array.
    for i in xrange(n):
        x = ord(string[i])
 
        # If this character has occurred first time, increment m
        if freq[x].c == 0:
            freq[x].c = chr(x)
            m+=1
 
        freq[x].f+=1
        string[i] = '\0'
 
    # Build a max heap of all characters
    buildHeap(freq, MAX)
 
    # Now one by one extract all distinct characters from max heap
    # and put them back in str[] with the d distance constraint
    for i in xrange(m):
        x = extractMax(freq, MAX-i)
 
        # Find the first available position in str[]
        p = i
        while string[p] != '\0':
            p+=1
 
        # Fill x.c at p, p+d, p+2d, .. p+(f-1)d
        for k in xrange(x.f):
 
            # If the index goes beyond size, then string cannot
            # be rearranged.
            if p + d*k >= n:
                print "Cannot be rearranged"
                return
 
            string[p + d*k] = x.c
 
    return toString(string)
 
'''
Maximum and minimum of an array using minimum number of comparisons
Time Complexity: O(n)
In this method, total number of comparisons is 1 + 2(n-2) in worst case and 1 + n - 2 in best case.
In the above implementation, worst case occurs when elements are sorted in descending order and best case occurs when elements are sorted in ascending order.

METHOD 2 (Tournament Method)
 Divide the array into two parts and compare the maximums and minimums of the the two parts to get the maximum and the minimum of the the whole array.

 METHOD 3 (Compare in Pairs)
 If n is odd then initialize min and max as first element.
 If n is even then initialize min and max as minimum and maximum of the first two elements respectively.
 For rest of the elements, pick them in pairs and compare their
 maximum and minimum with max and min respectively.

In general, method 3 seems to be the best.
'''
def getMinMax(arr):
    n = len(arr)
    if n == 1:
        Min = Max = arr[0]
        return (Min, Max)
    
    if arr[0] > arr[1]:
        Min = arr[1]
        Max = arr[0]
    else:
        Min = arr[0]
        Max = arr[1]

    for i in xrange(2, n):
        if arr[i] < Min:
            Min = arr[i]
        elif arr[i] > Max:
            Max = arr[i]
    return (Min, Max)

# Python program to find minimum element in a sorted and rotated array
'''
Examples 
Input: {5, 6, 1, 2, 3, 4}
Output: 1

Input: {1, 2, 3, 4}
Output: 1

Input: {2, 1}
Output: 1
A simple solution is to traverse the complete array and find minimum. This solution requires O(n) time.
 We can do it in O(Logn) using Binary Search. If we take a closer look at above examples, we can easily figure out following pattern:
 - The minimum element is the only element whose previous is greater than it. If there is no previous element element, then there is no rotation (first element is minimum).
 We check this condition for middle element by comparing it with (mid-1)'th and (mid+1)'th elements.
 - If minimum element is not at middle (neither mid nor mid + 1), then minimum element lies in either left half or right half.
 1.If middle element is smaller than last element, then the minimum element lies in left half
 2.Else minimum element lies in right half.
'''
def findMin(arr, low, high):
    if high < low:
        return arr[0]
    if high == low:
        return arr[low]

    mid = int((low + high)/2)
 
    if mid < high and arr[mid+1] < arr[mid]:
        return arr[mid+1]
    if mid > low and arr[mid] < arr[mid - 1]:
        return arr[mid]
    if arr[high] > arr[mid]:
        return findMin(arr, low, mid-1)
    return findMin(arr, mid+1, high)

'''
Solution: If we use Counting Sort, it would take O(n^2) time as the given range is of size n^2. Using any comparison based sorting like Merge Sort, Heap Sort, .. etc would take O(nLogn) time.
 Now question arises how to do this in 0(n)? Firstly, is it possible? Can we use data given in question? n numbers in range from 0 to n2 - 1?
 The idea is to use  Radix Sort. Following is standard Radix Sort algorithm.
1) Do following for each digit i where i varies from least 
   significant digit to the most significant digit...
   a) Sort input array using counting sort (or any stable sort) according to the i'th digit
   
Let there be d digits in input integers. Radix Sort takes O(d*(n+b)) time where b is the base for representing numbers, for example, for decimal system, b is 10. Since n2-1 is the maximum
possible value, the value of d would be O(logb(n)). So overall time complexity is O((n+b)*O(logb(n)). Which looks more than the time complexity of comparison based sorting algorithms for a
large k. The idea is to change base b. If we set b as n, the value of O(logb(n)) becomes O(1) and overall time complexity becomes O(n). 
arr[] = {0, 10, 13, 12, 7}

Let us consider the elements in base 5. For example 13 in
base 5 is 23, and 7 in base 5 is 12.
arr[] = {00(0), 20(10), 23(13), 22(12), 12(7)}

After first iteration (Sorting according to the last digit in 
base 5),  we get.
arr[] = {00(0), 20(10), 12(7), 22(12), 23(13)}

After second iteration, we get
arr[] = {00(0), 12(7), 20(10), 22(12), 23(13)}
Following is C++ implementation to sort an array of size n where elements are in range from 0 to n2 - 1.

'''
def countSort(arr, n, exp):
    output = [None]*n
    count = [None]*n
    for i in xrange(0, n):
        count[i] = 0
    for i in xrange(0, n):
        count[ (arr[i]/exp)%n ] += 1

    for i in xrange(1, n):
        count[i] += count[i-1]
    for i in reversed(xrange(0, n)):
        output[count[ (arr[i]/exp)%n] - 1] = arr[i]
        count[(arr[i]/exp)%n] -= 1

    for i in xrange(0, n):
        arr[i] = output[i]

def sortIt(arr, n):
    countSort(arr, n, 1)
    countSort(arr, n, n)
'''
How to sort if range is from 1 to n2?
 If range is from 1 to n n2, the above process can not be directly applied, it must be changed. Consider n = 100 and range from 1 to 10000.
 Since the base is 100, a digit must be from 0 to 99 and there should be 2 digits in the numbers. But the number 10000 has more than 2 digits.
 So to sort numbers in a range from 1 to n2, we can use following process.
 1) Subtract all numbers by 1.
 2) Since the range is now 0 to n2, do counting sort twice as done in the above implementation.
 3) After the elements are sorted, add 1 to all numbers to obtain the original numbers.

How to sort if range is from 0 to n^3 -1?
 Since there can be 3 digits in base n, we need to call counting sort 3 times. 
'''

'''
Run Length Encoding
Given an input string, write a function that returns the Run Length Encoded string for the input string.
For example, if the input string is "wwwwaaadexxxxxx", then the function should return "w4a3d1e1x6"

The solution provided below in python takes slightly more time than O(n). Check the following Algorithm at https://www.geeksforgeeks.org/run-length-encoding/ for O(n) solution 
Algorithm:
 a) Pick the first character from source string.
 b) Append the picked character to the destination string.
 c) Count the number of subsequent occurrences of the picked character and append the count to destination string.
 d) Pick the next character and repeat steps b) c) and d) if end of string is NOT reached.
'''
from collections import OrderedDict
def runLengthEncoding(strng):
    D=OrderedDict.fromkeys(strng, 0)         # Generate ordered dictionary of all lower case alphabets, its output will be D = {'w':0, 'a':0, 'd':0, 'e':0, 'x':0}
    
    for ch in strng:                         # Now iterate through input string to calculate frequency of each character, its output will be D = {'w':4,'a':3,'d':1,'e':1,'x':6}
        D[ch] += 1
        
    output = ''            
    for key,value in D.iteritems():          # now iterate through dictionary to make output string from (key,value) pairs
         output = output + key + str(value)
    return output
# program to find length of longest increasing subsequence in O(n Log n) time
'''
Given an array of random numbers. Find longest increasing subsequence (LIS) in the array. I know many of you might have read recursive and dynamic programming (DP) solutions.
There are few requests for O(N log N) algo in the forum posts.
It will be clear with an example, let us take example from wiki {0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15}.
A[0] = 0. Case 1. There are no active lists, create one.
0.
-----------------------------------------------------------------------------
A[1] = 8. Case 2. Clone and extend.
0.
0, 8.
-----------------------------------------------------------------------------
A[2] = 4. Case 3. Clone, extend and discard.
0.
0, 4.
0, 8. Discarded
-----------------------------------------------------------------------------
A[3] = 12. Case 2. Clone and extend.
0.
0, 4.
0, 4, 12.
-----------------------------------------------------------------------------
A[4] = 2. Case 3. Clone, extend and discard.
0.
0, 2.
0, 4. Discarded.
0, 4, 12.
-----------------------------------------------------------------------------
A[5] = 10. Case 3. Clone, extend and discard.
0.
0, 2.
0, 2, 10.
0, 4, 12. Discarded.
-----------------------------------------------------------------------------
A[6] = 6. Case 3. Clone, extend and discard.
0.
0, 2.
0, 2, 6.
0, 2, 10. Discarded.
-----------------------------------------------------------------------------
A[7] = 14. Case 2. Clone and extend.
0.
0, 2.
0, 2, 6.
0, 2, 6, 14.
-----------------------------------------------------------------------------
A[8] = 1. Case 3. Clone, extend and discard.
0.
0, 1.
0, 2. Discarded.
0, 2, 6.
0, 2, 6, 14.
-----------------------------------------------------------------------------
A[9] = 9. Case 3. Clone, extend and discard.
0.
0, 1.
0, 2, 6.
0, 2, 6, 9.
0, 2, 6, 14. Discarded.
-----------------------------------------------------------------------------
A[10] = 5. Case 3. Clone, extend and discard.
0.
0, 1.
0, 1, 5.
0, 2, 6. Discarded.
0, 2, 6, 9.
-----------------------------------------------------------------------------
A[11] = 13. Case 2. Clone and extend.
0.
0, 1.
0, 1, 5.
0, 2, 6, 9.
0, 2, 6, 9, 13.
-----------------------------------------------------------------------------
A[12] = 3. Case 3. Clone, extend and discard.
0.
0, 1.
0, 1, 3.
0, 1, 5. Discarded.
0, 2, 6, 9.
0, 2, 6, 9, 13.
-----------------------------------------------------------------------------
A[13] = 11. Case 3. Clone, extend and discard.
0.
0, 1.
0, 1, 3.
0, 2, 6, 9.
0, 2, 6, 9, 11.
0, 2, 6, 9, 13. Discarded.
-----------------------------------------------------------------------------
A[14] = 7. Case 3. Clone, extend and discard.
0.
0, 1.
0, 1, 3.
0, 1, 3, 7.
0, 2, 6, 9. Discarded.
0, 2, 6, 9, 11.
----------------------------------------------------------------------------
A[15] = 15. Case 2. Clone and extend.
0.
0, 1.
0, 1, 3.
0, 1, 3, 7.
0, 2, 6, 9, 11.
0, 2, 6, 9, 11, 15. <-- LIS List

The loop runs for N elements. In the worst case (what is worst case input?), we may end up querying ceil value using binary search (log i) for many A[i].
Therefore, T(n) < O( log N! )  = O(N log N). Analyse to ensure that the upper and lower bounds are also O( N log N ). The complexity is THETA (N log N).
'''
def GetCeilIndex(arr, T, l, r, key):
    while (r - l > 1):
        m = l + (r - l)/2
        if (arr[T[m]] >= key):
            r = m
        else:
            l = m
    return r

def LongestIncreasingSubsequence(arr, n):
    tailIndices = [0]*n
    prevIndices = [-1]*n

    len = 1
    for i in xrange(1, n):
        if (arr[i] < arr[tailIndices[0]]):
            tailIndices[0] = i
        elif (arr[i] > arr[tailIndices[len-1]]):
            prevIndices[i] = tailIndices[len-1]
            tailIndices[len] = i
            len += 1
        else:
            pos = GetCeilIndex(arr, tailIndices, -1, len-1, arr[i])
            prevIndices[i] = tailIndices[pos-1]
            tailIndices[pos] = i

    #print "LIS of given input: "
    #for (int i = tailIndices[len-1]; i >= 0; i = prevIndices[i])
    #    cout << arr[i] << " ";
    #cout << endl;
 
    return len

'''
Merge Overlapping Intervals
Given a set of time intervals in any order, merge all overlapping intervals into one and output the result which should have only mutually exclusive intervals. Let the intervals be represented as
pairs of integers for simplicity.
 For example, let the given set of intervals be {{1,3}, {2,4}, {5,7}, {6,8} }. The intervals {1,3} and {2,4} overlap with each other, so they should be merged and become {1, 4}. Similarly {5, 7}
and {6, 8} should be merged and become {5, 8}

Write a function which produces the set of merged intervals for the given set of intervals.

A simple approach is to start from the first interval and compare it with all other intervals for overlapping, if it overlaps with any other interval, then remove the other interval from list and
merge the other into the first interval. Repeat the same steps for remaining intervals after first. This approach cannot be implemented in better than O(n^2) time.

An efficient approach is to first sort the intervals according to starting time. Once we have the sorted intervals, we can combine all intervals in a linear traversal. The idea is, in sorted array of intervals, if interval[i] doesn't overlap with interval[i-1], then interval[i+1] cannot overlap with interval[i-1] because starting time of interval[i+1] must be greater than or equal to
interval[i]. Following is the detailed step by step algorithm.
1. Sort the intervals based on increasing order of
    starting time.
2. Push the first interval on to a stack.
3. For each interval do the following
   a. If the current interval does not overlap with the stack
       top, push it.
   b. If the current interval overlaps with stack top and ending
       time of current interval is more than that of stack top,
       update stack top with the ending  time of current interval.
4. At the end stack contains the merged intervals.

Time complexity of the method is O(nLogn) which is for sorting. Once the array of intervals is sorted, merging takes linear time.
A O(n Log n) and O(1) Extra Space Solution
 The above solution requires O(n) extra space for stack. We can avoid use of extra space by doing merge operations in-place. Below are detailed steps.
1) Sort all intervals in decreasing order of start time.
2) Traverse sorted intervals starting from first interval,
   do following for every interval.
      a) If current interval is not first interval and it
         overlaps with previous interval, then merge it with
         previous interval. Keep doing it while the interval
         overlaps with the previous one.
      b) Else add current interval to output list of intervals.

Note that if intervals are sorted by decreasing order of start times, we can quickly check if intervals overlap or not by comparing start time of previous interval with end time of
current interval.
Note that the below solution has been copied from stack exchange and is not something original from geeksforgeeks
'''
def merge(times):
    saved = list(times[0])
    for st, en in sorted([sorted(t) for t in times]):
        if st <= saved[1]:
            saved[1] = max(saved[1], en)
        else:
            yield tuple(saved)
            saved[0] = st
            saved[1] = en
    yield tuple(saved)

data = [
    [(1, 5), (2, 4), (3, 6)],
    [(1, 3), (2, 4), (5, 8)]
    ]
print "Merged intervals are: "
for times in data:
    print list(merge(times))

'''
Unbounded Binary Search Example (Find the point where a monotonically increasing function becomes positive first time)
Given a function int 'f(unsigned int x) which takes a non-negative integer 'x' as input and returns an integer as output.  The function is monotonically increasing with respect to value of x, i.e., the value of f(x+1) is greater than f(x) for every input x. Find the value 'n' where f() becomes positive for the first time. Since f() is monotonically increasing, values of f(n+1), f(n+2), must be positive and values of f(n-2), f(n-3), .. must be negative.
 Find n in O(logn) time, you may assume that f(x) can be evaluated in O(1) time for any input x.

A simple solution is to start from i equals to 0 and one by one calculate value of f(i) for 1, 2, 3, 4 .. etc until we find a positive f(i). This works, but takes O(n) time.

Can we apply Binary Search to find n in O(Logn) time? We can't directly apply Binary Search as we don't have an upper limit or high index. The idea is to do repeated doubling until we find a positive value, i.e., check values of f() for following values until f(i) becomes positive.
  f(0)
  f(1)
  f(2)
  f(4)
  f(8)
  f(16)
  f(32)
  ....
  ....
  f(high)
Let 'high' be the value of i when f() becomes positive for first time.
Can we apply Binary Search to find n after finding 'high'? We can apply Binary Search now, we can use 'high/2' as low and 'high' as high indexes in binary search. The result n must lie between
'high/2' and 'high'.

Number of steps for finding 'high' is O(Logn). So we can find 'high' in O(Logn) time. What about time taken by Binary Search between high/2 and high? The value of 'high' must be less than 2*n. The number of elements between high/2 and high must be O(n). Therefore, time complexity of Binary Search is O(Logn) and overall time complexity is 2*O(Logn) which is O(Logn).
'''
# program for Unbound Binary search.
# Let's take an example function as
# f(x) = x^2 - 10*x - 20
# Note that f(x) can be any monotonocally
# increasing function
def f(x):
    return (x * x - 10 * x - 20)

# Returns the value x where above function
# f() becomes positive first time.
def findFirstPositive() :

    # When first value itself is positive
    if (f(0) > 0):
        return 0

    # Find 'high' for binary search
    # by repeated doubling
    i = 1
    while (f(i) <= 0) :
        i = i * 2

    # Call binary search
    return binarySearch2(i/2, i)

# Searches first positive value of
# f(i) where low <= i <= high
def binarySearch2(low, high):
    if (high >= low) :
        mid = low + (high - low)/2;

        # If f(mid) is greater than 0
        # and one of the following two
        # conditions is true:
        # a) mid is equal to low
        # b) f(mid-1) is negative
        if (f(mid) > 0 and (mid == low or f(mid-1) <= 0)) :
            return mid;

        # If f(mid) is smaller than or equal to 0
        if (f(mid) <= 0) :
            return binarySearch2((mid + 1), high)
        else : # f(mid) > 0
            return binarySearch2(low, (mid-1))
        
    # Return -1 if there is no positive
    # value in given range
    return -1
'''
Sort a nearly sorted (or K sorted) array
Given an array of n elements, where each element is at most k away from its target position, devise an algorithm that sorts in O(n log k) time. 
For example, let us consider k is 2, an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

We can use Insertion Sort to sort the elements efficiently.
The inner loop will run at most k times. To move every element to its correct place, at most k elements need to be moved. So overall complexity will be O(nk)

We can sort such arrays more efficiently with the help of Heap data structure. Following is the detailed process that uses Heap.
 1) Create a Min Heap of size k+1 with first k+1 elements. This will take O(k) time (See this GFact)
 2) One by one remove min element from heap, put it in result array, and add a new element to heap from remaining elements.

Removing an element and adding a new element to min heap will take Logk time. So overall complexity will be O(k) + O((n-k)*logK)
So the Min Heap based method takes O(nLogk) time and uses O(k) auxiliary space. 

We can also use a Balanced Binary Search Tree instead of Heap to store K+1 elements. The insert and delete operations on Balanced BST also take O(Logk) time.
So Balanced BST based method will also take O(nLogk) time, but the Heap bassed method seems to be more efficient as the minimum element will always be at root.
Also, Heap doesn't need extra space for left and right pointers. See the solution here
'''
# Function to sort an array using insertion sort
def insertionSort(A):
    n = len(A)
    for i in xrange(1, n):
        key = A[i]
        j = i-1

        while (j >= 0 and A[j] > key):  # Move elements of A[0..i-1], that are greater than key, to one position ahead of their current position. This loop will run at most k times
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key
'''
Median of two sorted arrays of same size
There are 2 sorted arrays A and B of size n each. Write an algorithm to find the median of the array obtained after merging the above 2 arrays(i.e. array of length 2n).
The complexity should be O(log(n)).

Note : Since size of the set for which we are looking for median is even (2n), we need take average of middle two numbers and return floor of the average.

Method 1 (Simply count while Merging)
 Use merge procedure of merge sort. Keep track of count while comparing elements of two arrays. If count becomes n(For 2n elements), we have reached the median.
 Take the average of the elements at indexes n-1 and n in the merged array. See the below implementation.
See Method 2(Divide and Conquer based) below to this(Method 1) for O(logn) time complexity
'''
# A Simple Merge based O(n) solution to find median of two sorted lists of same size
# Assumptions in this function: Both ar1[] and ar2[] are sorted arrays and Both have n elements
def getMedian_method1( ar1, ar2 , n):
    i = 0                                                           # Current index of i/p list ar1[] 
    j = 0                                                           # Current index of i/p list ar2[] 
    m1 = -1
    m2 = -1
    
    count = 0
    while count < n + 1:                                            # Since there are 2n elements, median will be average of elements at index n-1 and n in the array obtained after merging ar1 and ar2
        count += 1
        if i == n:                                                  # Below is to handle case where all elements of ar1[] are smaller than smallest(or first) element of ar2[]
            m1 = m2
            m2 = ar2[0]
            break
        elif j == n:                                                # Below is to handle case where all  elements of ar2[] are smaller than smallest(or first) element of ar1[]
            m1 = m2
            m2 = ar1[0]
            break
        if ar1[i] < ar2[j]:
            m1 = m2                                                 # Store the prev median
            m2 = ar1[i]
            i += 1
        else:
            m1 = m2                                                 # Store the prev median
            m2 = ar2[j]
            j += 1
    return (m1 + m2)/2

ar1 = [1, 12, 15, 26, 38]
ar2 = [2, 13, 17, 30, 45]
n1 = len(ar1)
n2 = len(ar2)
if n1 == n2:
    print("Median is ", getMedian_method1(ar1, ar2, n1))
else:
    print("Doesn't work for arrays of unequal size")

'''
 Method 2 (By comparing the medians of two arrays)
 This method works by first getting medians of the two sorted arrays and then comparing them.

Let ar1 and ar2 be the input arrays. 
Algorithm:
1) Calculate the medians m1 and m2 of the input arrays ar1[] and ar2[] respectively.
2) If m1 and m2 both are equal then we are done.  return m1 (or m2)
3) If m1 is greater than m2, then median is present in one of the below two subarrays.
    a)  From first element of ar1 to m1 (ar1[0...|_n/2_|])
    b)  From m2 to last element of ar2  (ar2[|_n/2_|...n-1])
4) If m2 is greater than m1, then median is present in one of the below two subarrays.
   a)  From m1 to last element of ar1  (ar1[|_n/2_|...n-1])
   b)  From first element of ar2 to m2 (ar2[0...|_n/2_|])
5) Repeat the above process until size of both the subarrays becomes 2.
6) If size of the two arrays is 2 then use below formula to get the median.
    Median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1]))/2

Example:
   ar1[] = {1, 12, 15, 26, 38}
   ar2[] = {2, 13, 17, 30, 45}

For above two arrays m1 = 15 and m2 = 17

For the above ar1[] and ar2[], m1 is smaller than m2. So median is present in one of the following two subarrays.
   [15, 26, 38] and [2, 13, 17]

Let us repeat the process for above two subarrays: 
    m1 = 26 m2 = 13.

m1 is greater than m2. So the subarrays become
  [15, 26] and [13, 17]
Now size is 2, so median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1]))/2
                       = (max(15, 13) + min(26, 17))/2 
                       = (15 + 17)/2
                       = 16


Time Complexity: O(logn)        <= here the size of the arrays are same
 Algorithmic Paradigm: Divide and Conquer

Median of two sorted arrays of different sizes
This is an extension of median of two sorted arrays of equal size problem. Here we handle arrays of unequal size also.

The approach discussed in this post is similar to method 2 of equal size post. The basic idea is same, we find the median of two arrays and compare the medians to discard almost half of the elements in both arrays. Since the number of elements may differ here, there are many base cases that need to be handled separately. Before we proceed to complete solution, let us first talk about all base cases.

Let the two arrays be A[N] and B[M]. In the following explanation, it is assumed that N is smaller than or equal to M. 

Base cases:
 The smaller array has only one element
 Case 0: N = 0, M = 2
 Case 1: N = 1, M = 1.
 Case 2: N = 1, M is odd
 Case 3: N = 1, M is even
 The smaller array has only two elements
 Case 4: N = 2, M = 2
 Case 5: N = 2, M is odd
 Case 6: N = 2, M is even
 
Case 0: There are no elements in first array, return median of second array. If second array is also empty, return -1.
Case 1: There is only one element in both arrays, so output the average of A[0] and B[0].
Case 2: N = 1, M is odd
 Let B[5] = {5, 10, 12, 15, 20}
 First find the middle element of B[], which is 12 for above array. There are following 4 sub-cases.
    2.1 If A[0] is smaller than 10, the median is average of 10 and 12.
    2.2  If A[0] lies between 10 and 12, the median is average of A[0] and 12.
    2.3 If A[0] lies between 12 and 15, the median is average of 12 and A[0].
    2.4  If A[0] is greater than 15, the median is average of 12 and 15.
 In all the sub-cases, we find that 12 is fixed. So, we need to find the median of B[ M / 2 - 1 ], B[ M / 2 + 1], A[ 0 ] and take its average with B[ M / 2 ].

Case 3: N = 1, M is even
 Let B[4] = {5, 10, 12, 15}
 First find the middle items in B[], which are 10 and 12 in above example. There are following 3 sub-cases.
    3.1 If A[0] is smaller than 10, the median is 10.
    3.2  If A[0] lies between 10 and 12, the median is A[0].
    3.3 If A[0] is greater than 12, the median is 12.
 So, in this case, find the median of three elements B[ M / 2 - 1 ], B[ M / 2] and A[ 0 ].

Case 4: N = 2, M = 2
 There are four elements in total. So we find the median of 4 elements.

Case 5: N = 2, M is odd
 Let B[5] = {5, 10, 12, 15, 20}
 The median is given by median of following three elements: B[M/2], max(A[0], B[M/2 - 1]), min(A[1], B[M/2 + 1]).

Case 6: N = 2, M is even
 Let B[4] = {5, 10, 12, 15}
 The median is given by median of following four elements: B[M/2], B[M/2 - 1], max(A[0], B[M/2 - 2]), min(A[1], B[M/2 + 1]) 

Remaining Cases:
 Once we have handled the above base cases, following is the remaining process.
1) Find the middle item of A[] and middle item of B[].
    1.1) If the middle item of A[] is greater than middle item of B[], ignore the last half of A[], let length of ignored part is idx. Also, cut down B[] by idx from the start.
    1.2) else, ignore the first half of A[], let length of ignored part is idx. Also, cut down B[] by idx from the last.
'''
def MO2(a, b):                                                                                  # A utility function to find median of two integers
    return float( a + b ) / 2.0

def MO3(a, b, c):                                                                               # A utility function to find median of three integers
    return a + b + c - max(a, max(b, c)) - min(a, min(b, c))

def MO4(a, b, c, d):                                                            # A utility function to find median of four integers
    Max = max( a, max( b, max( c, d ) ) )
    Min = min( a, min( b, min( c, d ) ) )
    return float( a + b + c + d - Max - Min ) / 2.0

def medianSingle(arr, n):                                                                       # Utility function to find median of single array
    if (n == 0):
        return -1
    if (n%2 == 0):
        return (arr[n/2] + arr[n/2-1])/2
    return arr[n/2]

# This function assumes that N is smaller than or equal to M. This function returns -1 if both arrays are empty
def findMedianUtil( A, N, B, M ):
    if (N == 0):                                                                                # If smaller array is empty, return median from second array
        return medianSingle(B, M)
    if (N == 1):                                                                                # If the smaller array has only one element
        if (M == 1):                                                                            # Case 1: If the larger array also has one element, simply call MO2()
            return MO2(A[0], B[0])
        if (M & 1):                                                                             # Case 2: If the larger array has odd number of elements, then consider the middle 3 elements of larger array and the only element of smaller array
            return MO2( B[M/2], MO3(A[0], B[M/2 - 1], B[M/2 + 1]) )                             # e.g. A = {9}, B[] = {5, 8, 10, 20, 30} and A[] = {1}, B[] = {5, 8, 10, 20, 30}
        return MO3( B[M/2], B[M/2 - 1], A[0] )                                                  # Case 3: If the larger array has even number of element, then median will be one of the following 3 elements
    elif (N == 2):                                                                           # If the smaller array has two elements
        if (M == 2):                                                                            # Case 4: If the larger array also has two elements, simply call MO4()
            return MO4(A[0], A[1], B[0], B[1])
        if (M & 1):                                                                             # Case 5: If the larger array has odd number of elements, then median will be one of the following 3 elements
            return MO3 ( B[M/2], max(A[0], B[M/2 - 1]), min(A[1], B[M/2 + 1]) )
        return MO4 ( B[M/2], B[M/2 - 1], max( A[0], B[M/2 - 2] ), min( A[1], B[M/2 + 1] ) )     # Case 6: If the larger array has even number of elements, then median will be one of the following 4 elements

    idxA = ( N - 1 ) / 2
    idxB = ( M - 1 ) / 2

    if (A[idxA] <= B[idxB] ):                                                                   # if A[idxA] <= B[idxB], then median must exist in A[idxA....] and B[....idxB]
      return findMedianUtil(A + idxA, N/2 + 1, B, M - idxA )
    return findMedianUtil(A, N/2 + 1, B + idxA, M - idxA )                                      # if A[idxA] > B[idxB], then median must exist in A[...idxA] and B[idxB....]

def findMedian( A, N, B, M ):
    if (N > M):
       return findMedianUtil( B, M, A, N )
    return findMedianUtil( A, N, B, M );

A = [900]
B = [5, 8, 10, 20]
N = len(A)
M = len(B)
print "Median of two sorted arrays of different sizes is: ",
print findMedian( A, N, B, M )
'''
Given an array of of size n and a number k, find all elements that appear more than n/k times
Given an array of size n, find all elements in array that appear more than n/k times. For example, if the input arrays is {3, 1, 2, 2, 1, 2, 3, 3} and k is 4, then the output
should be [2, 3]. Note that size of array is 8 (or n = 8), so we need to find all elements that appear more than 2 (or 8/4) times. There are two elements that appear more than two times, 2 and 3. 

Generally asked variations of this problem are, find all elements that appear n/3 times or n/4 times in O(n) time complexity and O(1) extra space.

By hashing we can solve it in O(n) time on average. But extra space required hashing would be higher than O(k).
Also, hashing cannot be used to solve above variations with O(1) extra space.
'''
def elements_appearing_more_than_n_by_k(arr, n_by_k):
    D = {}
    for e in arr:
        if e in D:
            D[e] += 1
        else:
            D[e] = 1

        if D[e] > n_by_k:
            print e,

# pythonic way of C/C++ strcmp "strcmp(a.suff, b.suff) < 0? 1 : 0"
def strcmp(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2):
        if ord(s1[i]) | 32 != ord(s2[i]) | 32:
            break
        i += 1
    if i == len(s1) and i == len(s2):
        return 0
    if i == len(s1) or i != len(s2) and ord(s1[i]) | 32 < ord(s2[i]) | 32:
        return -1
    return 1
'''
Suffix Array | Set 1 (Introduction)
We strongly recommend to read following post on suffix trees as a pre-requisite for this post.

Pattern Searching | Set 8 (Suffix Tree Introduction)

A suffix array is a sorted array of all suffixes of a given string. The definition is similar to Suffix Tree which is compressed trie of all suffixes of the given text.
Any suffix tree based algorithm can be replaced with an algorithm that uses a suffix array enhanced with additional information and solves the same problem in the same time complexity.

 A suffix array can be constructed from Suffix tree by doing a DFS traversal of the suffix tree. In fact Suffix array and suffix tree both can be constructed from each other in linear time.
 Advantages of suffix arrays over suffix trees include improved space requirements, simpler linear time construction algorithms (e.g., compared to Ukkonen's algorithm) and
 improved cache locality

Example:
Let the given string be "banana".

0 banana                          5 a
1 anana     Sort the Suffixes     3 ana
2 nana      ---------------->     1 anana
3 ana        alphabetically       0 banana
4 na                              4 na
5 a                               2 nana

So the suffix array for "banana" is {5, 3, 1, 0, 4, 2}
'''
# sorted(mydict.iteritems(), key=lambda (k,v): (k,v))   => sorting dictionary by key
# sorted(mydict.iteritems(), key=lambda (k,v): (v,k))   => sorting dictionary by value
# s[-1]                                                 => remove last element
# s[0:-1]                                               => chop last element
# s[1:]                                                 => chop first element
# sorted(mydict, key=mydict.get)                        => returns keys sorted by value
def suffix_array(s):
    #return [rank for suffix, rank in sorted((s[i:], i) for i in range(len(s)))]
    mydict={}
    i=0

    print "Preparing for suffix array"
    while len(s)>0:
        print str(i) + " " + s
        mydict[i] = s
        s=s[1:]
        i+=1
    print "Suffix dictionary after sorting by values:"
    print sorted(mydict.iteritems(), key=lambda (k,v): (v,k))
    return sorted(mydict, key=mydict.get)

strng='banana'
sa=suffix_array('banana')
print "Suffix array for " + strng + " is: ", sa
'''
Searching in a suffix array
// This code only contains search() and main. To make it a complete running
// above code or see https://ide.geeksforgeeks.org/oY7OkD

// A suffix array based search function to search a given pattern
// 'pat' in given text 'txt' using suffix array suffArr[]
void search(char *pat, char *txt, int *suffArr, int n)
{
    int m = strlen(pat);  // get length of pattern, needed for strncmp()

    // Do simple binary search for the pat in txt using the
    // built suffix array
    int l = 0, r = n-1;  // Initilize left and right indexes
    while (l <= r)
    {
        // See if 'pat' is prefix of middle suffix in suffix array
        int mid = l + (r - l)/2;
        int res = strncmp(pat, txt+suffArr[mid], m);

        // If match found at the middle, print it and return
        if (res == 0)
        {
            cout << "Pattern found at index " << suffArr[mid];
            return;
        }

        // Move to left half if pattern is alphabtically less than
        // the mid suffix
        if (res < 0) r = mid - 1;

        // Otherwise move to right half
        else l = mid + 1;
    }

    // We reach here if return statement in loop is not executed
    cout << "Pattern not found";
}
    char txt[] = "banana";  // text
    char pat[] = "nan";   // pattern to be searched in text

    // Build suffix array
    int n = strlen(txt);
    int *suffArr = buildSuffixArray(txt, n);

    // search pat in txt using the built suffix array
    search(pat, txt, suffArr, n);
Output:
Pattern found at index 2

The time complexity of the above search function is O(mLogn). There are more efficient algorithms to search pattern once the suffix array is built. In fact there is a O(m) suffix array based algorithm to search a pattern. We will soon be discussing efficient algorithm for search.

Applications of Suffix Array
 Suffix array is an extremely useful data structure, it can be used for a wide range of problems. Following are some famous problems where Suffix array can be used.
 1) Pattern Searching
 2) Finding the longest repeated substring
 3) Finding the longest common substring
 4) Finding the longest palindrome in a string
'''

print(strcmp('Geek', 'geel'))
print(strcmp('Geel', 'geek'))
print(strcmp('Geel', 'geeL'))

A = [3, 1, 2, 2, 1, 2, 3, 3]
k = 4
NbyK=len(A)/k
elements_appearing_more_than_n_by_k(A, NbyK)

arr = [2, 6, 3, 12, 56, 8]
print "Before sorting: ", arr
insertionSort(arr)
print "After sorting : ", arr

arr = [2, 3, 4, 10, 40]
n = len(arr)
x = 10
result = exponentialSearch(arr, n, x)
if result == -1:
    print "Element not found in thye array"
else:
    print "Element is present at index %d" %(result)
    
print ("The value n where f() becomes "+
      "positive first is ", findFirstPositive())

A = [ 2, 5, 3, 7, 11, 8, 10, 13, 6 ]
n = len(A)
print "Length of Longest Increasing Subsequence is ", LongestIncreasingSubsequence(A, n)
'''
Merge k sorted arrays | Set 1
Given k sorted arrays of size n each, merge them and print the sorted output.

Example:
Input:
k = 3, n =  4
arr[][] = { {1, 3, 5, 7},
            {2, 4, 6, 8},
            {0, 9, 10, 11}} ;

Output: 0 1 2 3 4 5 6 7 8 9 10 11 

A simple solution is to create an output array of size n*k and one by one copy all arrays to it. Finally, sort the output array using any O(nLogn) sorting algorithm.
This approach takes O(nkLognk) time. 

We can merge arrays in O(nk*Logk) time using Min Heap. Following is detailed algorithm.

1. Create an output array of size n*k.
2. Create a min heap of size k and insert 1st element in all the arrays into the heap
3. Repeat following steps n*k times.
    a) Get minimum element from heap (minimum is always at root) and store it in output array.
    b) Replace heap root with next element from the array from which the element is extracted. If the array doesn't have any more elements, then replace root with infinite.
    After replacing the root, heapify the tree.

    See https://www.geeksforgeeks.org/merge-k-sorted-arrays/ for solution
    Also see heapsort(https://www.geeksforgeeks.org/heap-sort/)
'''

'''
Median in a stream of integers (running integers)
Given that integers are read from a data stream. Find median of elements read so for in efficient way. For simplicity assume there are no duplicates.
For example, let us consider the stream 5, 15, 1, 3

After reading 1st element of stream - 5 -> median - 5
After reading 2nd element of stream - 5, 15 -> median - 10
After reading 3rd element of stream - 5, 15, 1 -> median - 5
After reading 4th element of stream - 5, 15, 1, 3 -> median - 4, so on...

Making it clear, when the input size is odd, we take the middle element of sorted data. If the input size is even, we pick average of middle two elements in sorted stream.
Note that output is effective median of integers read from the stream so far. Such an algorithm is called online algorithm. Any algorithm that can guarantee output of i-elements
after processing i-th element, is said to be online algorithm. Let us discuss three solutions for the above problem.

Method 1: Insertion Sort
If we can sort the data as it appears, we can easily locate median element. Insertion Sort is one such online algorithm that sorts the data appeared so far. At any instance of sorting,
say after sorting i-th element, the first i elements of array are sorted. The insertion sort doesn't depend on future data to sort data input till that point. In other words,
insertion sort considers data sorted so far while inserting next element. This is the key part of insertion sort that makes it an online algorithm.

However, insertion sort takes O(n2) time to sort n elements. Perhaps we can use binary search on insertion sort to find location of next element in O(log n) time.
Yet, we can't do data movement in O(log n) time. No matter how efficient the implementation is, it takes polynomial time in case of insertion sort.

Method 2: Augmented self balanced binary search tree (AVL, RB, etc)
At every node of BST, maintain number of elements in the subtree rooted at that node. We can use a node as root of simple binary tree, whose left child is self balancing BST with elements
less than root and right child is self balancing BST with elements greater than root. The root element always holds effective median.

If left and right subtrees contain same number of elements, root node holds average of left and right subtree root data. Otherwise, root contains same data as the root of subtree which is
having more elements. After processing an incoming element, the left and right subtrees (BST) are differed utmost by 1.

Self balancing BST is costly in managing balancing factor of BST. However, they provide sorted data which we don't need. We need median only. The next method make use of Heaps to trace median.

Method 3: Heaps
Similar to balancing BST in Method 2 above, we can use a max heap on left side to represent elements that are less than effective median,
and a min heap on right side to represent elements that are greater than effective median.

After processing an incoming element, the number of elements in heaps differ utmost by 1 element. When both heaps contain same number of elements,
we pick average of heaps root data as effective median. When the heaps are not balanced, we select effective median from the root of heap containing more elements.

For algorithm to build these heaps, please refer https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/
'''

'''
Find number of pairs (x, y) in an array such that x^y > y^x    https://www.geeksforgeeks.org/find-number-pairs-xy-yx/
Given two arrays X[] and Y[] of positive integers, find number of pairs such that  x^y > y^x where x is an element from X[] and y is an element from Y[].

Examples:
  Input: X[] = {2, 1, 6}, Y = {1, 5}
  Output: 3 
  // There are total 3 pairs where pow(x, y) is greater than pow(y, x)
  // Pairs are (2, 1), (2, 5) and (6, 1)
  
  Input: X[] = {10, 19, 18}, Y[] = {11, 15, 9};
  Output: 2
  // There are total 2 pairs where pow(x, y) is greater than pow(y, x)
  // Pairs are (10, 11) and (10, 15)

The brute force solution is to consider each element of X[] and Y[], and check whether the given condition satisfies or not.
Time Complexity of this solution is O(m*n) where m and n are sizes of given arrays. 

Efficient Solution: 
 The problem can be solved in O(nLogn + mLogn) time. The trick here is, if y > x then x^y > y^x with some exceptions. Following are simple steps based on this trick.

1) Sort array Y[].
2) For every x in X[], find the index idx of smallest number greater than x (also called ceil of x) in Y[] using binary search or we can use the inbuilt function upper_bound() in algorithm library.
3) All the numbers after idx satisfy the relation so just add (n-idx) to the count.

Base Cases and Exceptions:
 Following are exceptions for x from X[] and y from Y[]
 If x = 0, then the count of pairs for this x is 0.
 If x = 1, then the count of pairs for this x is equal to count of 0s in Y[].
 The following cases must be handled separately as they don't follow the general rule that x smaller than y means x^y is greater than y^x.
 a) x = 2, y = 3 or 4
 b) x = 3, y = 2
 Note that the case where x = 4 and y = 2 is not there

Following diagram shows all exceptions in tabular form. The value 1 indicates that the corresponding (x, y) form a valid pair.
exception table

Following is implementation. In the following implementation, we pre-process the Y array and count 0, 1, 2, 3 and 4 in it, so that we can handle all exceptions in constant time.
The array NoOfY[] is used to store the counts.
'''

'''
Find the Increasing subsequence of length three with maximum product
Given a sequence of non-negative integers, find the subsequence of length 3 having maximum product with the numbers of the subsequence being in ascending order. 

Examples:
Input: 
arr[] = {6, 7, 8, 1, 2, 3, 9, 10} 
Output: 
8 9 10

Input: 
arr[] = {1, 5, 10, 8, 9}
Output: 5 8 9

Since we want to find the maximum product, we need to find following two things for every element in the given sequence:
LSL: The largest smaller element on left of given element
LGR: The largest greater element on right of given element.

Once we find LSL and LGR for an element, we can find the product of element with its LSL and LGR (if they both exist). We calculate this product for every element and return maximum of all products.
A simple method is to use nested loops. The outer loop traverses every element in sequence. Inside the outer loop, run two inner loops (one after other) to find LSL and LGR of current element. Time complexity of this method is O(n2). 

We can do this in O(nLogn) time. For simplicity, let us first create two arrays LSL[] and LGR[] of size n each where n is number of elements in input array arr[]. The main task is to fill two arrays LSL[] and LGR[]. Once we have these two arrays filled, all we need to find maximum product LSL[i]*arr[i]*LGR[i] where 0 < i < n-1 (Note that LSL[i] doesn't exist for i = 0 and LGR[i] doesn't exist for i = n-1). We can fill LSL[] in O(nLogn) time. The idea is to use a Balanced Binary Search Tree like AVL. We start with empty AVL tree, insert the leftmost element in it. Then we traverse the input array starting from the second element to second last element. For every element currently being traversed, we find the floor of it in AVL tree. If floor exists, we store the floor in LSL[], otherwise we store NIL. After storing the floor, we insert the current element in the AVL tree. 
We can fill LGR[] in O(n) time. The idea is similar to this post. We traverse from right side and keep track of the largest element. If the largest element is greater than current element, we store it in LGR[], otherwise we store NIL. 

Finally, we run a O(n) loop and return maximum of LSL[i]*arr[i]*LGR[i]
Overall complexity of this approach is O(nLogn) + O(n) + O(n) which is O(nLogn). Auxiliary space required is O(n). Note that we can avoid space required for LSL, we can find and use LSL values in final loop. 
'''

strng='wwwwaaadexxxxxx'
print runLengthEncoding(strng)

S="geeksforgeeks"
print runLengthEncoding(S)

'''
Double the first element and move zero to end

Given an array of integers of size n. Assume '0' as invalid number and all other as valid number.
Convert the array in such a way that if next valid number is same as current number, double its value and replace the next number with 0.
After the modification, rearrange the array such that all 0's are shifted to the end. 

Examples:
Input : arr[] = {2, 2, 0, 4, 0, 8}
Output : 4 4 8 0 0 0

Input : arr[] = {0, 2, 2, 2, 0, 6, 6, 0, 0, 8}
Output :  4 2 12 8 0 0 0 0 0 0
Time Complexity: O(n)
'''
def modifyAndRearrangeArr(arr):
    n = len(arr)

    for i in xrange(0, n-1):
        if arr[i] == arr[i+1]:
            arr[i] = 2*arr[i]
            arr[i+1] = 0
            i+=1

    left = 0
    right = n-1

    while left < right:
        while arr[right] == 0 and left < right:
            right -= 1

        while arr[left] != 0 and left < right:
            left += 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
    return arr
# Driver program to test above
arr = [ 0, 2, 2, 2, 0, 6, 6, 0, 0, 8 ]
n = len(arr) 
 
print("Original array:")
print arr

brr = modifyAndRearrangeArr(arr)
print "Modified array: ", brr

arr = [40, 12, 45, 32, 33, 1, 22]
n = len(arr)
print("Given array"), arr
sortIt(arr, n)
print("Sorted array"), arr

arr1 = [5, 6, 1, 2, 3, 4]
n1 = len(arr1)
print("The minimum element is " + str(findMin(arr1, 0, n1-1)))
 
arr2 = [1, 2, 3, 4]
n2 = len(arr2)
print("The minimum element is " + str(findMin(arr2, 0, n2-1)))
 
arr3 = [1]
n3 = len(arr3)
print("The minimum element is " + str(findMin(arr3, 0, n3-1)))
 
arr4 = [1, 2]
n4 = len(arr4)
print("The minimum element is " + str(findMin(arr4, 0, n4-1)))
 
arr5 = [2, 1]
n5 = len(arr5)
print("The minimum element is " + str(findMin(arr5, 0, n5-1)))
 
arr6 = [5, 6, 7, 1, 2, 3, 4]
n6 = len(arr6)
print("The minimum element is " + str(findMin(arr6, 0, n6-1)))
 
arr7 = [1, 2, 3, 4, 5, 6, 7]
n7 = len(arr7)
print("The minimum element is " + str(findMin(arr7, 0, n7-1)))
 
arr8 = [2, 3, 4, 5, 6, 7, 8, 1]
n8 = len(arr8)
print("The minimum element is " + str(findMin(arr8, 0, n8-1)))
 
arr9 = [3, 4, 5, 1, 2]
n9 = len(arr9)
print("The minimum element is " + str(findMin(arr9, 0, n9-1)))

string = "aabbcc"
print rearrangeDdistance(toList(string), 3)
 
# Driver program
string1 = "geeksforgeeg"
print remove(string1)
 
string2 = "azxxxzy"
print remove(string2)
 
string3 = "caaabbbaac"
print remove(string3)
 
string4 = "gghhg"
print remove(string4)
 
string5 = "aaaacddddcappp"
print remove(string5)
 
string6 = "aaaaaaaaaa"
print remove(string6)
 
string7 = "qpaaaaadaaaaadprq"
print remove(string7)
 
string8 = "acaaabbbacdddd"
print remove(string8)
 
string9 = "acbbcddc"
print remove(string9)
 
# Driver program
string1 = "ad"
print "Input => " + string1 + "\nOutput => ",
print stringFilter(toList(string1)) + "\n"
 
string2 = "acbac"
print "Input => " + string2 + "\nOutput => ",
print stringFilter(toList(string2)) + "\n"
 
string3 = "aaac"
print "Input => " + string3 + "\nOutput => ",
print stringFilter(toList(string3)) + "\n"
 
string4 = "react"
print "Input => " + string4 + "\nOutput => ",
print stringFilter(toList(string4)) + "\n"
 
string5 = "aa"
print "Input => " + string5 + "\nOutput => ",
print stringFilter(toList(string5)) + "\n"
 
string6 = "ababaac"
print "Input => " + string6 + "\nOutput => ",
print stringFilter(toList(string6)) + "\n"
 
string7 = "abc"
print "Input => " + string7 + "\nOutput => ",
print stringFilter(toList(string7)) + "\n"
 
# Driver program
test("g*ks", "geeks") # Yes
test("ge?ks*", "geeksforgeeks") # Yes
test("g*k", "gee") # No because 'k' is not in second
test("*pqrs", "pqrst") # No because 't' is not in first
test("abc*bcd", "abcdhghgbcd") # Yes
test("abc*c?d", "abcd") # No because second must have 2 instances of 'c'
test("*c*d", "abcd") # Yes
test("*?c*d", "abcd") # Yes

price = [100, 180, 260, 310, 40, 535, 695]
stockBuySell(price)

arr = [10, 3, 5, 6, 2]
print "\nThe product array is : ", productArray(arr)
        
A = [10, 2, 3, 4, 5, 9, 7, 8]
n = len(A)
X = 23
findFourElements (A, n, X)

arr = [10, 21, 22, 100, 101, 200, 300]
print "Number of Triangles:",findnumberofTriangles(arr)

arr = [PetrolPump(6,4), PetrolPump(3,6), PetrolPump(7,3)]
start = printTour(arr) 
print "No solution" if start == -1 else "start =", start

arr=[18, 40, 35, 12, 30, 35, 20, 6, 90, 80]
insertionSort(arr)
print arr

arr = [2, 3, 3, 5, 3, 4, 1, 7]
n = len(arr)
k = 8
print("The maximum repeating number is",maxRepeating(arr, n, k))

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
rearrange(arr, n)
print arr

arr = [Pair(5, 24), Pair(15, 25), Pair(27, 40), Pair(50, 60)]
 
print('Length of maximum size chain is',
      maxChainLength(arr, len(arr)))

arr = [16, 17, 4, 3, 5, 2]
nextGreatest(arr)
print "Modified array is", arr

arr = [1, 0, 0, 1, 0, 1, 1]
size = len(arr)
findSubArray(arr, size)
'''
Find a peak element
Given an array of integers. Find a peak element in it. An array element is peak if it is NOT smaller than its neighbors.
For corner elements, we need to consider only one neighbor.

For example, for input array {5, 10, 20, 15}, 20 is the only peak element. For input array {10, 20, 15, 2, 23, 90, 67}, there are two peak elements: 20 and 90.
Note that we need to return any one peak element.

Following corner cases give better idea about the problem.
1) If input array is sorted in strictly increasing order, the last element is always a peak element. For example, 50 is peak element in {10, 20, 30, 40, 50}.
2) If input array is sorted in strictly decreasing order, the first element is always a peak element. 100 is the peak element in {100, 80, 60, 50, 20}.
3) If all elements of input array are same, every element is a peak element.

'''
arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
print("Index of a peak point is", findPeak(arr, n))
        
#arr = [1, 5, 3, 4, 2] 
#k = 3
#print ("Count of pairs with given diff is ",
#                countPairsWithDiffK(arr, k))

arr = [3, 2, 0, 1]
n = len(arr) 
print ("Given array is"), arr

rearrange(arr, n);
print ("Modified array is"),arr

arr = [3, 6, 7, 2, 9]
n = len(arr)
print ("Required number of groups are",
               int(findgroups(arr, n)))

arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(arr)
print(randomize(arr, n))

a = [11, 10, -20, 5, -3, -5, 8, -13, 10]
print "Maximum circular sum is", maxCircularSum(a)

A = [1, 4, 45, 6, 10, 8]
Sum = 22
arr_size = len(A)
 
find3Numbers(A, arr_size, Sum)

arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
Sum = 23
subArraySum(arr, n, Sum)

ts = twoStacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)
print("Popped element from stack1 is " + str(ts.pop1()))
ts.push2(40)
print("Popped element from stack2 is " + str(ts.pop2()))
 
arr = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
n = len(arr)
x = 3
y = 6
print("Minimum distance between ",x," and ",y,"is",minDist(arr, n, x, y))
'''
Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.
Examples:
Input :
 arr[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13}
 k = 4
 Output :
 aS K=4, between 8, 5, 10, 7 the largest one is 10
                 5, 10, 7, 9 the largest one is 10
                 10, 7, 9, 4 it's 10
                 7, 9, 4, 15 it's 15
                 9, 4, 15, 12 it's 15
                 4, 15, 12, 90 it's 90
                 15, 12, 90, 13 it's 90
                 
                 
 10 10 10 15 15 90 90
 
Input :
 arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}
 k = 3
 Output :
 3 3 4 5 5 5 6
'''
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
printMax(arr, k)
'''
Given a sorted array of n distinct integers where each integer is in the range from 0 to m-1 and m > n.  Find the smallest number that is missing from the array. 

Examples
 Input: {0, 1, 2, 6, 9}, n = 5, m = 10
 Output: 3

Input: {4, 5, 10, 11}, n = 4, m = 12
 Output: 0

Input: {0, 1, 2, 3}, n = 4, m = 5
 Output: 4

Input: {0, 1, 2, 3, 4, 5, 6, 7, 10}, n = 9, m = 11
 Output: 8
'''
arr = [0, 1, 2, 3, 4, 5, 6, 7, 10]
n = len(arr)
print("Smallest missing element is", findFirstMissing(arr, 0, n-1))

'''
Given an array, print the Next Greater Element (NGE) for every element. The Next greater Element for an element x is the first greater element on the right side of x in array.
Elements for which no greater element exist, consider next greater element as -1. 

Examples:
a) For any array, rightmost element always has next greater element as -1.
b) For an array which is sorted in decreasing order, all elements have next greater element as -1.
c) For the input array [4, 5, 2, 25}, the next greater elements for each element are as follows.
Element       NGE
   4      -->   5
   5      -->   25
   2      -->   25
   25     -->   -1


d) For the input array [13, 7, 6, 12}, the next greater elements for each element are as follows.
  Element        NGE
   13      -->    -1
   7       -->     12
   6       -->     12
   12     -->     -1

'''
arr = [11, 13, 21, 3]
printNGE(arr)

arr = [1, 2, 8, 10, 10, 12, 19]
n = len(arr)
x = 11
index = ceilSearch(arr, 0, n-1, x); 
if index == -1:
    print ("Ceiling of %d doesn't exist in array "% x)
else:
    print ("ceiling of %d is %d"%(x, arr[index]))

arr = [1, 2, 90, 10, 110]
print ("Maximum difference is", maxDiff(arr))
 
# driver program to test
arr = [0, 1, 0, 1, 1, 1]
print("Array after segregation")
print(segregate0and1(arr))

arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
print("Array after pushing all zeros to end of array:")
print pushZerosToEnd(arr)

arr = [1, 60, -10, 70, -80, 85, 81]
minAbsSumPair(arr)

arr = [1, 20, 6, 4, 5]
print("Number of inversions are", getInvCount(arr))

arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
key = 6
i = search(arr, 0, len(arr)-1, key)
if i != -1:
    print ("Index: %d"%i)
else:
    print ("Key not found")
'''
Get the sum of numbers.           total = n*(n+1)/2
Subtract all the numbers from sum and you will get the missing number.
'''
A = [1, 2, 4, 5, 6]
miss = getMissingNo(A)
print(miss)

string = "-123"
print myAtoi(string)

s1 = "LISTEN"
s2 = "SILENT"
if areAnagram(list(s1), list(s2)):
    print "Anagram"
else:
    print "Not anagram"
    
string = "ABC"
permute(list(string), 0, len(string)-1)
print "All permutations with repetition of " + string + " are:"
allLexicographic(string)

string1 = "AACD"
string2 = "ACDA"
if areRotations(string1, string2):
    print "Strings are rotations of each other"
else:
    print "Strings are not rotations of each other"
    
isPalindrome("abba");
isPalindrome("abbccbba");
isPalindrome("geeks")

#A = [6,1,4,45,6,10,-8, 5, 3, 11,10]
#n = 16
#print "No of pairs with above sum is ", countPairsWithSumK(A, n)
#print PairsWithSumK(A, n)

arr = [1, 8, 30,90, 40, 100]
n = 60
PairsWithDiffK(arr, n)

arr = [1, 2, 2, 3, 3, 3, 3]
x = 3
n = len(arr)
c = countElements(arr, x, n)
print ("%d occurs %d times "%(x, c))

arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
n = len(arr)
maxDiff = maxIndexDiff(arr, n)
print(maxDiff)

arr = [12, 11, 10, 5, 6, 2, 30]
find3numbers(arr)
'''
Backtracking:
Read it:
https://www.geeksforgeeks.org/sort-elements-frequency-set-4-efficient-approach-using-hash/
https://www.geeksforgeeks.org/sorting-array-elements-frequency-set-3-using-stl/
https://www.geeksforgeeks.org/sort-elements-by-frequency-set-2/
https://www.geeksforgeeks.org/sort-elements-by-frequency/

https://www.geeksforgeeks.org/backtracking-set-8-solving-cryptarithmetic-puzzles/
https://www.geeksforgeeks.org/tug-of-war/
'''
