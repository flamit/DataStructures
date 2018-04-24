#!/usr/bin/python

# binary representation of a given no
def bin(n):
    if n > 1:
        bin(n/2)
    print n % 2,

# Detect if two integers have opposite signs.
def oppositeSigns(x, y):
    return ((x ^ y) < 0)

# Turn off the rightmost set bit
# Note that the result is always 0 for 2^x nos
def fun(n):
    return n & (n-1)

# Smallest power of 2 greater than or equal to n
# Time Complexity: O(lgn)
def nextPowerOf2(n):
    count = 0;
 
    # First n in the below condition is for the case where n is 0
    if (n and not(n & (n-1)) ):
        return n
     
    while( n != 0):
        n >>= 1
        count += 1
    
    return 1 << count

# Function to check if x is power of 2
# Returns True if it's power of 2 otherwise returns False
def isPowerOfTwo (n):
    return (n and (not(n & (n - 1))) )

# Function to check if x is power of 4
def isPowerOfFour(n):
    count = 0
    if (n and (not(n & (n - 1)))):                                      # Check if there is only one bit set in n 
        while(n > 1):                                                   # count 0 bits before set bit
            n >>= 1
            count += 1         
        
        if(count % 2 == 0):                                             # If count is even then return true else false
            return True
        else:
            return False

'''
Find position of the only set bit
Given a number having only one '0's in its binary representation, find position of the only set bit. Source: Microsoft Interview | 18
The idea is to one by one right shift the set bit of given number 'n' zero. The final count is position of the set bit.
'''
def findPosOfOnlySetBit(n):
    if not isPowerOfTwo(n):
        return -1

    count = 0
    while n:
        n = n >> 1
        count += 1
    return count
'''
rightmost unset bit is 2
Input : n = 9
9 = 1001
rightmost set bit is 1
'''
import math as m
# function to find the position of rightmost set bit
def getPosOfRightmostSetBit(n):
    return int((m.log(((n & - n) + 1),2)))                                          # Remove decimal values

# function to get the position ot rightmost unset bit
def getPosOfRightmostUnsetBit(n):
    if (n == 0):
        return 1

    if ((n & (n + 1)) == 0):                                                        # if all bits of 'n' are set
        return -1

    return int(getPosOfRightmostSetBit(~n))                                         # position of rightmost unset bit in 'n' passing ~n as argument
'''
Compute modulus division by a power-of-2-number
Compute n modulo d without division(/) and modulo(%) operators, where d is a power of 2 number.

Let ith bit from right is set in d. For getting n modulus d, we just need to return 0 to i-1 (from right) bits of n as they are and other bits as 0.
For example if n = 6 (00..110) and d = 4(00..100). Last set bit in d is at position 3 (from right side). So we need to return last two bits of n as they are and other bits as 0, i.e., 00..010.
'''
def getModulo(n, d):
  return (n & (d-1))

# Function to check if n is a multiple of 3. Returns 1 if it's a multiple of 3 otherwise returns 0
# Time Complexity:  O(logn)
def isMultipleOf3(n):
    odd_count = 0
    even_count = 0
 
    # Make no positive if +n is multiple of 3 then is -n. We are doing this to avoid stack overflow in recursion
    if(n < 0): 
        n = -n
    if(n == 0):
        return 1
    if(n == 1): 
        return 0
 
    while(n):
        # If odd bit is set then increment odd counter 
        if(n & 1): 
            odd_count += 1
        n = n >> 1
 
        # If even bit is set then increment even counter 
        if(n & 1):
            even_count += 1
        n = n >> 1
    return isMultipleOf3(abs(odd_count - even_count))
'''
Check if a number is multiple of 9 using bitwise operators

Given a number n, write a function that returns true if n is divisible by 9, else false. The most simple way to check for n's divisibility by 9 is to do n%9. 
 Another method is to sum the digits of n. If sum of digits is multiple of 9, then n is multiple of 9.
 The above methods are not bitwise operators based methods and require use of % and /.
 The bitwise operators are generally faster than modulo and division operators. Following is a bitwise operator based method to check divisibility by 9.
'''
# Bitwise operator based function to check divisibility by 9
def isDivBy9(n):
    if (n == 0 or n == 9):
        return True
    if (n < 9):
        return False
    return isDivBy9((n>>3) - (n&7))                                 # If n is greater than 9, then recur for [floor(n/9) - n%8]
'''
Function to get parity of number n. It returns 1 if n has odd parity, and returns 0 if n has even parity
complexity is O(Log n)
Parity: Parity of a number refers to whether it contains an odd or even number of 1-bits.
The number has 'odd parity', if it contains odd number of 1-bits and is 'even parity' if it contains even number of 1-bits.

Algorithm:
1. Initialize parity = 0
2. Loop while n != 0      
      a. Invert parity 
             parity = !parity
      b. Unset rightmost set bit
             n = n & (n-1)
3. return parity

Example:
 Initialize: n = 13 (1101)   parity = 0

n = 13 & 12  = 12 (1100)   parity = 1
n = 12 & 11 = 8  (1000)   parity = 0
n = 8 & 7 = 0  (0000)    parity = 1

Uses: Parity is used in error detection and cryptography.
'''
def getParity( n ):
    parity = 0
    while n:
        parity = ~parity
        n = n & (n - 1)
    return parity

# Function to mutiply any number with 7
# Time Complexity: O(1)
# Space Complexity: O(1)
def multiplyBy7(n):
    return ((n << 3) - n)                                       # Note the inner bracket here. This is needed because precedence of '-' operator is higher than '<<'

'''
Multiply a given Integer with 3.5
You are not allowed to use %, /, *.
Input: 5
Output: 17 (Ignore the digits after decimal point)

Solution:
3.5x = 2x + 1x + 0.5x
We can get x*3.5 by adding 2*x, x and x/2. To calculate 2*x, left shift x by 1 and to calculate x/2, right shift x by 2.
'''
def multiplyWith3Point5(n):
    return (n<<1) + n + (n>>1)

# Program to find the element occurring odd number of times
# XOR of all elements gives us odd occurring element. Please note that XOR of two elements is 0 if both elements are same and XOR of a number x with 0 is x.
# Time Complexity: O(n)
def getOddOccurrence(arr):
    res = 0
    for element in arr:
        res = res ^ element                                     # XOR with the result
    return res

# code to find the element that appears once
#Time Complexity: O(n)
#Auxiliary Space: O(1)
def getSingle(arr, n):
    ones = 0
    twos = 0
     
    for i in range(n):
        twos = twos | (ones & arr[i])    # one & arr[i] gives the bits that are there in both 'ones' and new element from arr[]. We add these bits to 'twos' using bitwise OR
        ones = ones ^ arr[i]             # Same as above
        common_bit_mask = ~(ones & twos) # The common bits are those bits which appear third time. So these bits should not be there in both 'ones' and 'twos'. common_bit_mask contains all these bits as 0, so that the bits can be removed from 'ones' and 'twos'
        ones &= common_bit_mask          # Remove common bits (the bits that appear third time) from 'ones'
        twos &= common_bit_mask          # Remove common bits (the bits that appear third time) from 'twos'
    return ones

'''
Let x and y be the non-repeating elements we are looking for and arr[] be the input array. First calculate the XOR of all the array elements.
     xor = arr[0]^arr[1]^arr[2].....arr[n-1]

All the bits that are set in xor will be set in one non-repeating element (x or y) and not in other. So if we take any set bit of xor and divide the elements of the array in two sets
one set of elements with same bit set and other set with same bit not set. By doing so, we will get x in one set and y in another set.
Now if we do XOR of all the elements in first set, we will get first non-repeating element, and by doing same in other set we will get the second non-repeating element.
Let us see an example.
   arr[] = {2, 4, 7, 9, 2, 4}
1) Get the XOR of all the elements.
     xor = 2^4^7^9^2^4 = 14 (1110)
2) Get a number which has only one set bit of the xor.   
   Since we can easily get the rightmost set bit, let us use it.
     set_bit_no = xor & ~(xor-1) = (1110) & ~(1101) = 0010
   Now set_bit_no will have only set as rightmost set bit of xor.
3) Now divide the elements in two sets and do xor of elements in each set, and we get the non-repeating elements 7 and 9. Please see implementation for this step.
   Time Complexity: O(n)
   Auxiliary Space: O(1)
'''
def get2NonRepeatingNos(arr, n, no1, no2):
  xor = arr[0]
  for i in xrange(1, n):
    xor ^= arr[i]

  set_bit_no = xor & ~(xor-1);

  for i in xrange(0, n):
    if(arr[i] & set_bit_no):
      no1 = no1 ^ arr[i]
    else:
      no2 = no2 ^ arr[i]
  return (no1, no2)
'''
Function to get no of set bits in binary representation of passed binary no.
Brian Kernighan's Algorithm:
============================
Subtraction of 1 from a number toggles all the bits (from right to left) till the rightmost set bit(including the righmost set bit).
So if we subtract a number by 1 and do bitwise & with itself (n & (n-1)), we unset the rightmost set bit.
If we do n & (n-1) in a loop and count the no of times loop executes we get the set bit count.
Beauty of this solution is number of times it loops is equal to the number of set bits in a given integer.
Time Complexity: O(logn)
'''
def countSetBits(n): 
    count = 0
    while n:
        n = n&(n-1) 
        count+=1
     
    return count

# Count total set bits in all numbers from 1 to n
'''
The easiest and simplest way is to iterate in range 1 to n and keep on adding the counts in a for loop. The complexity in this case is O(nlogn) in this case.
How to do it in O(logn) time?
Solution is as below:

If the input number is of the form 2^b -1 e.g., 1, 3, 7, 15.. etc, the number of set bits is b * 2^(b-1). This is because for all the numbers 0 to (2^b)-1, if you complement and flip the list you end up with the same list (half the bits are on, half off).
If the number does not have all set bits, then some position m is the position of leftmost set bit. The number of set bits in that position is n (1 << m) + 1. The remaining set bits are in two parts: 1) The bits in the (m-1) positions down to the point where the leftmost bit becomes 0, and 2) The 2^(m-1) numbers below that point, which is the closed form above. An easy way to look at it is to consider the number 6:
0|0 0
0|0 1
0|1 0
0|1 1
-|?
1|0 0
1|0 1
1|1 0

The leftmost set bit is in position 2 (positions are considered starting from 0). If we mask that off what remains is 2 (the "1 0" in the right part of the last row.) So the number of bits in the
2nd position (the lower left box) is 3 (that is, 2 + 1). The set bits from 0 to 3 (the upper right box above) is 2*2^(2-1) = 4. The box in the lower right is the remaining bits we havent yet counted, and is the number of set bits for all the numbers up to 2 (the value of the last entry in the lower right box) which can be figured recursively.

A O(Logn) complexity program to count set bits in all numbers from 1 to n
'''
def countSetBitsFrom1toN(n):
    m = getLeftmostBit(n)               # Get the position of leftmost set bit in n. This will be used as an upper bound for next set bit function
    return _countSetBits(n, m)          #Use the position

def _countSetBits(n, m):
    if (n == 0):                        # Base Case: if n is 0, then set bit count is 0
        return 0

    m = getNextLeftmostBit(n, m)        # get position of next leftmost set bit
    if (n == (1 << (m + 1)) - 1):
        return (m + 1) * (1 << m)

    # If n is of the form 2^x-1, i.e., if n is like 1, 3, 7, 15, 31, .. etc,then we are done.Since positions are considered starting from 0, 1 is added to m update n for next recursive call
    n = n - (1 << m);
    return (n + 1) + countSetBits(n) + m * (1 << (m - 1))

# Returns position of leftmost set bit. The rightmost position is considered as 0
def getLeftmostBit(n):
    m = 0;
    while (n > 1):
        n = n >> 1
        m += 1
    return m

# Given the position of previous leftmost set bit in n (or an upper bound on leftmost position) returns the new position of leftmost set bit in n
def getNextLeftmostBit(n, m):
    temp = 1 << m
    while (n < temp):
        temp = temp >> 1
        m -= 1
    return m



# Function that return count of flipped number
# Count number of bits to be flipped to convert A to B
def FlippedCount(a , b):                                                                                                         # Return count of set bits in a XOR b
    return countSetBits(a^b)

'''
 Add two numbers without using arithmetic operators
 Solution:
 carry now contains common set bits of x and y
 carry = x & y
 Sum of bits of x and y where at least one of the bits is not set
 x = x ^ y
 Carry is shifted by one so that adding it to x gives the required sum
 y = carry << 1
'''
def Add (x, y):
    if (y == 0):
        return x
    else:
        return Add( x ^ y, (x & y) << 1)

'''

Compute the minimum or maximum of two integers without branching
On some rare machines where branching is expensive, the below obvious approach to find minimum can be slow as it uses branching.
/* The obvious approach to find minimum (involves branching) */
int min(int x, int y)
{
  return (x < y) ? x : y
}
Minimum of x and y will be 
y ^ ((x ^ y) & -(x < y))

It works because if x < y, then -(x < y) will be all ones, so r = y ^ (x ^ y) & ~0 = y ^ x ^ y = x. Otherwise, if x >= y, then -(x < y) will be all zeros, so r = y ^ ((x ^ y) & 0) = y. On some machines, evaluating (x < y) as 0 or 1 requires a branch instruction, so there may be no advantage. To find the maximum, use 
x ^ ((x ^ y) & -(x < y));
'''
def findMin(x, y):
    return y ^ ((x ^ y) & -(x < y))
 
def findMax(x, y):
    return x ^ ((x ^ y) & -(x < y))

'''
Compute the integer absolute value (abs) without branching
We need not to do anything if a number is positive. We want to change only negative numbers. Since negative numbers are stored in 2's complement form, to get the absolute value of a
negative number we have to toggle bits of the number and add 1 to the result.

For example -2 in a 8 bit system is stored as follows 1 1 1 1 1 1 1 0 where leftmost bit is the sign bit. To get the absolute value of a negative number,
we have to toggle all bits and add 1 to the toggled number i.e, 0 0 0 0 0 0 0 1 + 1 will give the absolute value of 1 1 1 1 1 1 1 0.
Also remember, we need to do these operations only if the number is negative (sign bit is set).
'''
def getAbs(n):
    CHAR_BIT = 8
    SIZE_OF_INT = 4             # (sizeof(int) in C
    
    mask = n >> (SIZE_OF_INT * CHAR_BIT - 1)
    return ((n + mask) ^ mask)

# this function returns next higher number with same number of set bits as x. Read more at https://www.geeksforgeeks.org/next-higher-number-with-same-number-of-set-bits/
def snoob(x):
  nextHigher = 0
  if x:
    rightOne = x & -(x)                                 # right most set bit
    nextHigherOneBit = x + rightOne                     # reset the pattern and set next higher bit left part of x will be here
    rightOnesPattern = x ^ nextHigherOneBit             # nextHigherOneBit is now part [D] of the above explanation. isolate the pattern
    rightOnesPattern = (rightOnesPattern)/rightOne      # right adjust pattern
    rightOnesPattern >>= 2                              # correction factor
    nextHigher = nextHigherOneBit | rightOnesPattern    # rightOnesPattern is now part [A] of the above explanation. integrate new pattern (Add [D] and [A])
  return nextHigher

# program to find Smallest of three integers without comparison operators
# Note: This method doesn't work for negative numbers
def smallest(x, y, z):
    c = 0 
    while ( x and y and z ):
        x=x-1
        y=y-1
        z=z-1
        c=c+1
        
    return c

'''
We know that the negative number is represented in 2's complement form on most of the architectures.
>>> -(~-14)
-13
>>> ~(14)
-15
>>> -(~14)
15
 Note that this method works only if the numbers are stored in 2's complement form.

Code to add 1 to a given number
''' 
def addOne(x):
    return (-(~x))

'''
Swap all odd and even bits

For example, if the given number is 23 (00010111), it should be converted to 43 (00101011).
If we take a closer look at the example, we can observe that we basically need to right shift (>>) all even bits (In the above example, even bits of 23 are highlighted) by 1 so that they become odd bits (highlighted in 43), and left shift (<<) all odd bits by 1 so that they become even bits. The following solution is based on this observation. The solution assumes that input number is stored using 32 bits.

Let the input number be x
 1) Get all even bits of x by doing bitwise and of x with 0xAAAAAAAA. The number 0xAAAAAAAA is a 32 bit number with all even bits set as 1 and all odd bits as 0.
 2) Get all odd bits of x by doing bitwise and of x with 0x55555555. The number 0x55555555 is a 32 bit number with all odd bits set as 1 and all even bits as 0.
 3) Right shift all even bits.
 4) Left shift all odd bits.
 5) Combine new even and odd bits and return.
'''
def swapOddAndEvenBits(x) :
    even_bits = x & 0xAAAAAAAA          # Get all even bits of x
    odd_bits = x & 0x55555555           # Get all odd bits of x
    even_bits >>= 1                     # Right shift even bits
    odd_bits <<= 1                      # Left shift odd bits

    return (even_bits | odd_bits)       # Combine even and odd bits
'''
Rotate bits of a number
Bit Rotation: A rotation (or circular shift) is an operation similar to shift except that the bits that fall off at one end are put back to the other end.

In left rotation, the bits that fall off at left end are put back at right end.
In right rotation, the bits that fall off at right end are put back at left end.

Example:
 Let n is stored using 8 bits. Left rotation of n = 11100101 by 3 makes n = 00101111 (Left shifted by 3 and first 3 bits are put back in last ).
 Right rotation of n = 11100101 by 3 makes n = 10111100 (Right shifted by 3 and last 3 bits are put back in first ) if n is stored using 8 bits.

If n is stored using 16 bits or 32 bits then left rotation of n (000...11100101) becomes 00..0011100101000.
If n is stored using 16 bits or 32 bits then right rotation of n (000...11100101) by 3 becomes 101000..0011100.
'''
INT_BITS = 32
# Function to left rotate n by d bits
def leftRotate(n, d):
    return (n << d) or (n >> (INT_BITS - d))                                                                                # To put first 3 bits of n at last, do bitwise or of n<<d with n >>(INT_BITS - d)

# Function to right rotate n by d bits
def rightRotate(n, d):
   return (n >> d) or (n << (INT_BITS - d))                                                                                 # In n>>d, first d bits are 0. To put last 3 bits of at first, do bitwise or of n>>d with n <<(INT_BITS - d)

# Reverse bits of a given 32 bits unsigned integer.
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
#
# Time : O(logn) = O(32)
# Space: O(1)
def reverseBits(n):
    result = 0
    for i in xrange(INT_BITS):
        result <<= 1
        result |= n & 1
        n >>= 1
    return result
'''
Swap bits in a given number
Given a number x and two positions (from right side) in binary representation of x, write a function that swaps n bits at given two positions and returns the result. It is also given that the two sets of bits do not overlap.

Let p1 and p2 be the two given positions.
Example 1
 Input:
 x = 47 (00101111)
 p1 = 1 (Start from second bit from right side)
 p2 = 5 (Start from 6th bit from right side)
 n = 3 (No of bits to be swapped)
 Output:
 227 (11100011)
 The 3 bits starting from the second bit (from right side) are
 swapped with 3 bits starting from 6th position (from right side)

Example 2
 Input:
 x = 28 (11100)
 p1 = 0 (Start from first bit from right side)
 p2 = 3 (Start from 4th bit from right side)
 n = 2 (No of bits to be swapped)
 Output:
 7 (00111)
 The 2 bits starting from 0th postion (from right side) are
 swapped with 2 bits starting from 4th position (from right side)
'''
def swapBits(x, p1, p2, n):
  set1 = (x >> p1) & ((1 << n) - 1)     # Move all bits of first set to rightmost side
  set2 = (x >> p2) & ((1 << n) - 1)     # Moce all bits of second set to rightmost side
  xor = (set1 ^ set2)
  xor = (xor << p1) | (xor << p2)       # Put the xor bits back to their original positions
  result = x ^ xor                      # XOR the 'xor' with the original number so that the  two sets are swapped
  return result

'''
Swap two nibbles in a byte
A nibble is a four-bit aggregation, or half an octet. There are two nibbles in a byte.
Given a byte, swap the two nibbles in it. For example 100 is be represented as 01100100 in a byte (or 8 bits).
The two nibbles are (0110) and (0100). If we swap the two nibbles, we get 01000110 which is 70 in decimal.

To swap the nibbles, we can use bitwise &, bitwise '<<' and '>>' operators. A byte can be represented using a unsigned char in C as size of char is 1 byte in a typical C compiler.
Following is a python program to swap the two nibbles in a byte.

Explanation:
 100 is 01100100 in binary. The operation can be split mainly in two parts
1) The expression "x & 0x0F" gives us last 4 bits of x. For x = 100, the result is 00000100. Using bitwise "<<" operator, we shift the last four bits to the left 4 times and
    make the new last four bits as 0. The result after shift is 01000000.
2) The expression "x & 0xF0" gives us first four bits of x. For x = 100, the result is 01100000. Using bitwise '>>' operator, we shift the digit to the right 4 times and
    make the first four bits as 0. The result after shift is 00000110.

At the end we use the bitwise OR '|' operation of the two expressions explained above. The OR operator places first nibble to the end and last nibble to first.
For x = 100, the value of (01000000) OR (00000110) gives the result 01000110 which is equal to 70 in decimal.
'''
def swapNibbles(x):
    return ( (x & 0x0F)<<4 | (x & 0xF0)>>4 )

x = 100;
print swapNibbles(x)
'''
A Boolean Array Puzzle

Input: A array arr[] of two elements having value 0 and 1
Output: Make both elements 0.

Specifications: Following are the specifications to follow.
 1) It is guaranteed that one element is 0 but we do not know its position.
 2) We can't say about another element it can be 0 or 1.
 3) We can only complement array elements, no other operation like and, or, multi, division,... etc.
 4) We can't use if, else and loop constructs.
 5) Obviously, we can't directly assign 0 to array elements.

There are several ways we can do it as we are sure that always one Zero is there. Thanks to devendraiiit  for suggesting following 3 methods.
'''
def changeToZero(a):
  a[ a[1] ] = a[ a[0] ]

n = 9
print "The number after turning off the right most set bit is ", fun(n)
print(nextPowerOf2(n))
print "isMultipleOf3: ", isMultipleOf3(n)
print ("Parity of no ", n," = ",
     ( "odd" if getParity(n) else "even"))
print "When multiplied by 7 = ", (multiplyBy7(n))

arr = [ 2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
print "%d" % getOddOccurrence(arr)

arr = [3, 3, 2, 3]
n = len(arr)
print("The element with single occurrence is ", getSingle(arr, n))

arr = [2, 3, 7, 9, 11, 2, 3, 11]
no1 = 0
no2 = 0
(x, y) = get2NonRepeatingNos(arr, 8, no1, no2)
print("The non-repeating elements are ", x, y);
print "No of set bits are: ", countSetBits(n)
n = 17
print "Total set bit count from 1 to 17 is ", countSetBitsFrom1toN(n)

a = 10
b = 20
print(FlippedCount(a, b))
print "15 + 33 = ", Add(15, 33)
print(addOne(14))
print "Minimum of %d and %d is " %(a, b), findMin(a, b)
print "Maximum of %d and %d is " %(a, b), findMax(a, b)
print "Absolute of -6 is ", getAbs(-6)
x = 156
print "Next higher number with same number of set bits is ", snoob(x)
print "Left shift 10 by 3 gives ", leftRotate(10, 3)
print "Reversing the bits of 9 it gives ", reverseBits(9)
n = 6
d = 4
print ("%u moduo %u is %u", n, d, getModulo(n, d))
print "isDivBy9 ", isDivBy9(36)

n = 16
print "Position of the only set bit is ", findPosOfOnlySetBit(n) #Position 5
n = 12
print "Position of the only set bit is ", findPosOfOnlySetBit(n) # -1 => Invalid number
n = 128
print "Position of the only set bit is ", findPosOfOnlySetBit(n) #Position 8

# 00010111
x = 23
print "After swapping even and odd bits it becomes: ", swapOddAndEvenBits(x)                      # Output is 43 (00101011)

print "binary representation of 7 is ",
bin(7)

x = 100
y = 1
if (oppositeSigns(x, y) == True):
    print "\nSigns are opposite"
else:
    print "\nSigns are not opposite"
res = swapBits(28, 0, 3, 2)
print "Result = ", res

a = [1, 0]
changeToZero(a)
print " arr[0] = ", a[0]
print " arr[1] = ", a[1]

a = [0, 1]
changeToZero(a)
print " arr[0] = ", a[0]
print " arr[1] = ", a[1]
print "Position of right most set bit is ", getPosOfRightmostSetBit(8)
print "Position of right most unset bit is ", getPosOfRightmostUnsetBit(8)

'''
Do it:
https://www.geeksforgeeks.org/add-two-bit-strings/
https://www.geeksforgeeks.org/reverse-digits-integer-overflow-handled/
https://www.geeksforgeeks.org/write-your-own-strcmp-which-ignores-cases/
https://www.geeksforgeeks.org/program-to-count-number-of-set-bits-in-an-big-array/
https://www.geeksforgeeks.org/divide-and-conquer-set-2-karatsuba-algorithm-for-fast-multiplication/

http://graphics.stanford.edu/~seander/bithacks.html#SwappingBitsXOR

Can integers overflow in python?

Short answers:
* No => if the operations are done in pure python, because python integers have arbitrary precision
*Yes => if the operations are done in the pydata stack (numpy/pandas), because they use C-style fixed-precision integers

Then how to check integer overflow in C?
Check for Integer Overflow
Write a C function, int addOvf(int* result, int a, int b) If there is no overflow, the function places the resultant = sum a+b in "result" and returns 0.
Otherwise it returns -1. The solution of casting to long and adding to find detecting the overflow is not allowed.

Method 1
 There can be overflow only if signs of two numbers are same, and sign of sum is opposite to the signs of numbers.
1)  Calculate sum
2)  If both numbers are positive and sum is negative then return -1
     Else 
        If both numbers are negative and sum is positive then return -1
        Else return 0

#include<stdio.h>
#include<stdlib.h>
 
/* Takes pointer to result and two numbers as
    arguments. If there is no overflow, the function
    places the resultant = sum a+b in "result" and
    returns 0, otherwise it returns -1 */
 int addOvf(int* result, int a, int b)
 {
     *result = a + b;
     if(a > 0 && b > 0 && *result < 0)
         return -1;
     if(a < 0 && b < 0 && *result > 0)
         return -1;
     return 0;
 }
 
 int main()
 {
     int *res = (int *)malloc(sizeof(int));
     int x = 2147483640;
     int y = 10;
 
     printf("%d", addOvf(res, x, y));
 
     printf("\n %d", *res);
     getchar();
     return 0;
}

Time Complexity : O(1)
Space Complexity: O(1)
'''
