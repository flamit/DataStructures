#!/usr/bin/python

import math
# A utility function that returns true if x is perfect square
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
 
# Returns true if n is a Fibinacci Number, else false
def isFibonacci(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both is a perferct square

# Function to print first n Fibonacci Numbers
# Time complexity: O(n)
def printFibonacciNumbers(n):   
    f1 = 0
    f2 = 1
    if (n < 1):
        return
    for x in range(0, n):
        print f2,
        nextNo = f1 + f2
        f1 = f2
        f2 = nextNo
'''
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
        
Time Complexity: T(n) = T(n-1) + T(n-2) which is exponential.
 We can observe that this implementation does a lot of repeated work (see the following recursion tree). So this is a bad implementation for nth Fibonacci number.
                         fib(5)   
                     /                  
               fib(4)                fib(3)   
             /                      /     
         fib(3)      fib(2)         fib(2)    fib(1)
        /             /           /      
  fib(2)   fib(1)  fib(1) fib(0) fib(1) fib(0)
  /    
fib(1) fib(0)


Extra Space: O(n) if we consider the function call stack size, otherwise O(1).
'''

def fact(n):
    if (n <= 1):
        return 1
    return n*fact(n-1)
 
def nPr(n, r):
    return fact(n)/fact(n-r)

# Python program to find Excel column name from a 
# given column number
 
MAX = 50
# Function to print Excel column name for a given column number
def printString(n):
    string = ["\0"]*MAX                         # To store result (Excel column name)
    i = 0                                       # To store current index in str which is result
    
    while n > 0:
        rem = n%26                              # Find remainder
        if rem == 0:                            # if remainder is 0, then a 'Z' must be there in output
            string[i] = 'Z'
            i += 1
            n = (n/26)-1
        else:
            string[i] = chr((rem-1) + ord('A'))
            i += 1
            n = n/26
    string[i] = '\0'
    string = string[::-1]                       # Reverse the string and print result
    print "".join(string)

# program to find the smallest number which is greater than a given no. has same set of digits as given number
# Given number as int array, this function finds the greatest number and returns the number as integer
'''
Input:  n = "218765"
Output: "251678"

Input:  n = "1234"
Output: "1243"

Input: n = "4321"
Output: "Not Possible"

Input: n = "534976"
Output: "536479"
'''
def findNext(number,n):
     for i in range(n-1,0,-1):                                      # Start from the right most digit and find the first digit that is smaller than the digit next to it
        if number[i] > number[i-1]:
            break
        
     if i == 0:                                                     # If no such digit found,then all numbers are in descending order, no greater number is possible
        print "Next number not possible"
        return
    
     x = number[i-1]                                                # Find the smallest digit on the right side of (i-1)'th digit that is greater than number[i-1]
     smallest = i
     for j in range(i+1,n):
        if number[j] > x and number[j] < number[smallest]:
            smallest = j
            
     number[smallest],number[i-1] = number[i-1], number[smallest]   # Swapping the above found smallest digit with (i-1)'th
     
     x = 0                                                          # X is the final number, in integer datatype
     for j in range(i):                                             # Converting list upto i-1 into number
        x = x * 10 + number[j]
        
     number = sorted(number[i:])                                    # Sort the digits after i-1 in ascending order
     for j in range(n-i):                                           # converting the remaining sorted digits into number
        x = x * 10 + number[j]
      
     print "Next number with set of digits is",x

def foo(): # given method that returns 1 to 5 with equal probability
    # some code here
    pass
'''
Generate integer from 1 to 7 with equal probability
Given a function foo() that returns integers from 1 to 5 with equal probability, write a function that returns integers from 1 to 7 with equal probability using foo() only. Minimize the number of calls to foo() method. Also

'''
def my_rand():  #returns 1 to 7 with equal probability
    i = 5*foo() + foo() - 5;
    if (i < 22):
        return i%7 + 1
    return my_rand()

def findArea(a,b,c):
    if (a < 0 or b < 0 or c < 0 or (a+b <= c) or (a+c <=b) or (b+c <=a) ):  # must be smaller than third side
        print('Not a valid trianglen')
        return
    
    s = (a + b + c) / 2                                                      # calculate the semi-perimeter
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print('Area of a traingle is %f' %area)

# Program to find sum of series 1 + 1/2 + 1/3 + 1/4 + .. + 1/n
def seriesSum(n):
    i = 1
    s = 0.0
    for i in range(1, n+1):
        s = s + 1/i;
    return s

'''
Efficient program to print all prime factors of a given number
Given a number n, write an efficient function to print all prime factors of n. For example, if the input number is 12, then output should be 2 2 3.
And if the input number is 315, then output should be 3 3 5 7
'''
def primeFactors(n):
     
    # Print the number of two's that divide n
    while n % 2 == 0:
        print 2,
        n = n / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n , print i ad divide n
        while n % i== 0:
            print i,
            n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print n

'''
Efficient program to calculate e^x or Taylor Series

The value of Exponential Function e^x can be expressed using following Taylor Series. 
e^x = 1 + x/1! + x^2/2! + x^3/3! + ...... 
or
e^x = 1 + (x/1) (1 + (x/2) (1 + (x/3) (........) ) )
'''
def exponential(n, x):
    sum = 1.0
    for i in range(n, 0, -1):
        sum = 1 + x * sum / i
    print "e^x =", sum

# Python program to check for lucky number Returns 1 if n is a lucky number otherwise returns 0
'''
Lucky Numbers
Lucky numbers are subset of integers. Rather than going into much theory, let us see the process of arriving at lucky numbers,

 Take the set of integers
 1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,...

First, delete every second number, we get following reduced set.
 1,3,5,7,9,11,13,15,17,19,...

Now, delete every third number, we get
 1, 3, 7, 9, 13, 15, 19,...

Continue this process indefinitely...
Any number that does NOT get deleted due to above process is called "lucky".

Therefore, set of lucky numbers is 1, 3, 7, 13,...
Now, given an integer 'n', write a function to say whether this number is lucky or not.
'''
def isLucky(n):
    next_position = n
     
    if isLucky.counter > n:
        return 1
    if n % isLucky.counter == 0:
        return 0
    
    next_position = next_position - next_position / isLucky.counter 
    isLucky.counter = isLucky.counter + 1
     
    return isLucky(next_position)

# Babylonian method for square root
def squareRoot(n):
    x = n
    y = 1
    while(x > y):
        x = (x + y)/2
        y = n/x
    return x

def multiply(x, y):
    if(y == 0):
        return 0

    if(y > 0 ):
       return (x + multiply(x, y-1))
  
    if(y < 0 ):
       return -multiply(x, -y)

# A utility function to calculate area of triangle formed by (x1, y1),(x2, y2) and (x3, y3) 
def area(x1, y1, x2, y2, x3, y3):
 
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

# A function to check whether point P(x, y) lies inside the triangle formed by A(x1, y1), B(x2, y2) and C(x3, y3) 
def isInside(x1, y1, x2, y2, x3, y3, x, y):
    A = area (x1, y1, x2, y2, x3, y3)   # Calculate area of triangle ABC
    A1 = area (x, y, x2, y2, x3, y3)    # Calculate area of triangle PBC 
    A2 = area (x1, y1, x, y, x3, y3)    # Calculate area of triangle PAC 
    A3 = area (x1, y1, x2, y2, x, y)    # Calculate area of triangle PAB
    
    if(A == A1 + A2 + A3):              # Check if sum of A1, A2 and A3 is same as A
        return True
    else:
        return False

'''
Count numbers that don't contain 3
Given a number n, write a function that returns count of numbers from 1 to n that don't contain digit 3 in their decimal representation. 

Examples:
Input: n = 10
Output: 9 

Input: n = 45
Output: 31 
// Numbers 3, 13, 23, 30, 31, 32, 33, 34,35, 36, 37, 38, 39, 43 contain digit 3. 

Input: n = 578
Ouput: 385
Solution:
 We can solve it recursively. Let count(n) be the function that counts such numbers. 
'msd' --> the most significant digit in n 
'd'   --> number of digits in n.

count(n) = n if n < 3
count(n) = n - 1 if 3 <= n < 10
count(n) = count(msd) * count(10^(d-1) - 1) + 
           count(msd) + 
           count(n % (10^(d-1)))
           if n > 10 and msd is not 3

count(n) = count( msd * (10^(d-1)) - 1) 
           if n > 10 and msd is 3

Let us understand the solution with n = 578. 
count(578) = 4*count(99) + 4 + count(78)
The middle term 4 is added to include numbers 
100, 200, 400 and 500.

Let us take n = 35 as another example.  
count(35) = count (3*10 - 1) = count(29)
'''
def count(n):
     
    # Base Cases ( n is not negative)
    if n < 3:
        return n
    elif n >= 3 and n < 10:
        return n-1
         
    # Calculate 10^(d-1) ( 10 raise to the power d-1 ) where d
    # is number of digits in n. po will be 100 for n = 578
     
    po = 1
    while n/po > 9:
        po = po * 10
     
    # Find the MSD ( msd is 5 for 578 )
    msd = n/po
     
    if msd != 3:
        # For 578, total will be 4*count(10^2 - 1) + 4 + ccount(78)
        return count(msd) * count(po-1) + count(msd) + count(n%po)
    else:
        # For 35 total will be equal to count(29)
        return count(msd * po - 1)
         
# Python program to generate odd sized magic squares
# A function to generate odd sized magic squares
 
def generateSquare(n):
 
    # 2-D array with all slots set to 0
    magicSquare = [[0 for x in range(n)]for y in range(n)]
 
    # initialize position of 1
    i = n/2
    j = n-1
     
    # Fill the magic square by placing values
    num = 1
    while num <= (n*n):
        if i == -1 and j == n: # third condition
            j = n-2
            i = 0
        else:
            # next number goes out of right side of square 
            if j == n:
                j = 0
            # next number goes out of upper side
            if i < 0:
                i = n-1
                 
        if magicSquare[i][j]: # 2nd condition
            j = j-2
            i = i+1
            continue
        else:
            magicSquare[i][j] = num
            num = num+1
                 
        j = j+1
        i = i-1 #1st condition
 
 
   # Printing magic square
     
    print "Magic Squre for n = ",n
    print "Sum of each row or column",n*(n*n+1)/2
     
    for i in range(0,n):
        for j in range(0,n):
     
            print '%2d ' %(magicSquare[i][j]),
        print

'''
Sieve of Eratosthenes
Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number.
 For example, if n is 10, the output should be 2, 3, 5, 7. If n is 20, the output should be 2, 3, 5, 7, 11, 13, 17, 19
Following is the algorithm to find all the prime numbers less than or equal to a given integer n by Eratosthenes method:
1.Create a list of consecutive integers from 2 to n: (2, 3, 4,..., n).
2.Initially, let p equal 2, the first prime number.
3.Starting from p, count up in increments of p and mark each of these numbers greater than p itself in the list. These numbers will be 2p, 3p, 4p, etc.; note that some of them may have already been marked.
4.Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this number (which is the next prime), and repeat from step 3.
'''
# Python program to print all primes smaller than or equal to
# n using Sieve of Eratosthenes
 
def SieveOfEratosthenes(n):
     
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
     
    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            print p,

# Find day of the week for a given date
def dayofweek(d, m, y):
    t = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ]
    y -= m < 3;
    return ( y + y/4 - y/100 + y/400 + t[m-1] + d) % 7

'''
Space and time efficient Binomial Coefficient
Write a function that takes two parameters n and k and returns the value of Binomial Coefficient C(n, k). For example, your function should return 6 for n = 4 and k = 2, and it should return 10 for n = 5 and k = 2.
C(n, k) = n! / (n-k)! * k!
        = [n * (n-1) *....* 1]  / [ ( (n-k) * (n-k-1) * .... * 1) * 
                                    ( k * (k-1) * .... * 1 ) ]
After simplifying, we get
C(n, k) = [n * (n-1) * .... * (n-k+1)] / [k * (k-1) * .... * 1]

Also, C(n, k) = C(n, n-k)  // we can change r to n-r if r > n-r
Time Complexity: O(k)
Auxiliary Space: O(1)
'''
# Returns value of Binomial Coefficient C(n, k)
def binomialCoefficient(n, k):
    # since C(n, k) = C(n, n - k)
    if(k > n - k):
        k = n - k
    # initialize result
    res = 1
    # Calculate value of 
    # [n * (n-1) *---* (n-k + 1)] / [k * (k-1) *----* 1]
    for i in range(k):
        res = res * (n - i)
        res = res / (i + 1)
    return res

'''
Shuffle a given array
Time Complexity: O(n), assuming that the function rand() takes O(1) time.
'''
import random
def randomize (arr, n):
    # Start from the last element and swap one by one. We don't
    # need to run for the first element that's why i > 0
    for i in range(n-1,0,-1):
        # Pick a random index from 0 to i
        j = random.randint(0,i)
 
        # Swap arr[i] with the element at random index
        arr[i],arr[j] = arr[j],arr[i]
    return arr

'''
Given a number, check if it is divisible by 7. You are not allowed to use modulo operator, floating point arithmetic is also not allowed. 
A simple method is repeated subtraction. Following is another interesting method.
Divisibility by 7 can be checked by a recursive method. A number of the form 10a + b is divisible by 7 if and only if a - 2b is divisible by 7.
In other words, subtract twice the last digit from the number formed by the remaining digits. Continue to do this until a small number. 

Example: the number 371:37 - (2x1) = 37 - 2 = 35; 3 - (2 x 5) = 3 - 10 = -7; thus, since -7 is divisible by 7, 371 is divisible by 7.
'''
def isDivisibleBy7(num) :
     
    # If number is negative, make it positive
    if num < 0 :
        return isDivisibleBy7( -num )
 
    # Base cases
    if( num == 0 or num == 7 ) :
        return True
     
    if( num < 10 ) :
        return False
         
    # Recur for ( num / 10 - 2 * num % 10 ) 
    return isDivisibleBy7( num / 10 - 2 * ( num - num / 10 * 10 ) )

# A utility function to count smaller characters on right of arr[low]
def findSmallerInRight(st, low, high) :
     
    countRight = 0
    i = low + 1
    while i <= high :
        if st[i] < st[low] :
            countRight = countRight + 1
        i = i + 1
  
    return countRight
     
# A function to find rank of a string in all permutations of characters
'''
Lexicographic rank of a string
Given a string, find its rank among all its permutations sorted lexicographically. For example, rank of "abc" is 1, rank of "acb" is 2, and rank of "cba" is 6.
Examples:
Input : str[] = "acb"
Output : Rank = 2

Input : str[] = "string"
Output : Rank = 598

Input : str[] = "cba"
Output : Rank = 6

'''
def findRank (st) :
    ln = len(st)
    mul = fact(ln)
    rank = 1
    i = 0
  
    while i < ln :
         
        mul = mul / (ln - i)
         
        # count number of chars smaller 
        # than str[i] fron str[i+1] to
        # str[len-1]
        countRight = findSmallerInRight(st, i, ln-1)
  
        rank = rank + countRight * mul
        i = i + 1
    return rank

# Function to multiply two numbers using Russian Peasant method
def russianPeasant(a, b):
    res = 0
    while (b > 0):
        if ((b & 1) != 0):          # If second number becomes odd, add the first number to result
            res = res + a
        a = a << 1                  # Double the first number and halve the second number
        b = b >> 1
    return res

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Given three colinear points p, q, r, the function checks if point q lies on line segment 'pr'
def onSegment(p, q, r):
    if (q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y)):
        return True
    return False

'''
To find orientation of ordered triplet (p, q, r).
The function returns following values
 0 --> p, q and r are colinear
 1 --> Clockwise
 2 --> Counterclockwise
'''
def orientation(p, q, r):
    # See https://www.geeksforgeeks.org/orientation-3-ordered-points/ for details of below formula.
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    
    if (val == 0):
        return 0  # colinear

    if val > 0:
        return 1
    else:
        return 2    # clock or counterclock wise

# The main function that returns true if line segment 'p1q1' and 'p2q2' intersect.
'''
How to check if two given line segments intersect?
How is Orientation useful here?
 Two segments (p1,q1) and (p2,q2) intersect if and only if one of the following two conditions is verified

1. General Case:
    (p1, q1, p2) and (p1, q1, q2) have different orientations and
    (p2, q2, p1) and (p2, q2, q1) have different orientations.

2. Special Case 
    (p1, q1, p2), (p1, q1, q2), (p2, q2, p1), and (p2, q2, q1) are all collinear and
    the x-projections of (p1, q1) and (p2, q2) intersect
    the y-projections of (p1, q1) and (p2, q2) intersect
Also read https://www.geeksforgeeks.org/given-a-set-of-line-segments-find-if-any-two-segments-intersect/
'''
def doIntersect(p1, q1, p2, q2):
    # Find the four orientations needed for general and special cases
    o1 = orientation(p1, q1, p2);
    o2 = orientation(p1, q1, q2);
    o3 = orientation(p2, q2, p1);
    o4 = orientation(p2, q2, q1);
    
    if (o1 != o2 and o3 != o4):                 # General case
        return True
    
    if (o1 == 0 and onSegment(p1, p2, q1)):     # Special Cases p1, q1 and p2 are colinear and p2 lies on segment p1q1
        return True
    
    if (o2 == 0 and onSegment(p1, q2, q1)):     # p1, q1 and p2 are colinear and q2 lies on segment p1q1
        return True
    
    if (o3 == 0 and onSegment(p2, p1, q2)):      # p2, q2 and p1 are colinear and p1 lies on segment p2q2
        return True
    
    if (o4 == 0 and onSegment(p2, q1, q2)):      # p2, q2 and q1 are colinear and q1 lies on segment p2q2
        return True
 
    return False

# Returns true if two rectangles (l1, r1) and (l2, r2) overlap
def doOverlap(l1, r1, l2, r2):
    if (l1.x > r2.x or l2.x > r1.x):                     # If one rectangle is on left side of other
        return False

    if (l1.y < r2.y or l2.y < r1.y):                     # If one rectangle is above other
        return False

    return True

# Utility function to find GCD of two numbers GCD of a and b
def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a%b)

# Finds the no. of Integral points between two given points
def getCount(p, q):
    if (p.x==q.x):                                          # If line joining p and q is parallel to x axis, then count is difference of y values
        return abs(p.y - q.y) - 1

    if (p.y == q.y):                                        # If line joining p and q is parallel to y axis, then count is difference of x values
        return abs(p.x - q.x) - 1
 
    return gcd(abs(p.x - q.x), abs(p.y - q.y)) - 1

# Returns true if the point p lies inside the polygon[] with n vertices
# Check it again https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/
'''INF=10000
def isInsidePolygon(polygon, n, p):
    if (n < 3):                         # There must be at least 3 vertices in polygon[]
        return False
    extreme = Point(INF, p.y)           # Create a point for line segment from p to infinite
    
    count = 0
    i = 0                    # Count intersections of the above line with sides of polygon

    while (i != 0):
        nextNo = (i+1)%n
        #Check if the line segment from 'p' to 'extreme' intersects
        #with the line segment from 'polygon[i]' to 'polygon[next]'
        if (doIntersect(polygon[i], polygon[next], p, extreme)):
            #If the point 'p' is colinear with line segment 'i-next',
            #then check if it lies on segment. If it lies, return true,
            #otherwise false
            if (orientation(polygon[i], p, polygon[nextNo]) == 0):
               return onSegment(polygon[i], p, polygon[nextNo])
 
            count += 1
        i = nextNo
    
 
    # Return true if count is odd, false otherwise
    return count&1  # Same as (count%2 == 1)

p1 = Point(0, 0)
p2 = Point(10, 0)
p3 = Point(10, 10)
p4 = Point(0, 10)
polygon1 = [p1, p2, p3, p4]
n = len(polygon1)
p = Point(20, 20)
if isInsidePolygon(polygon1, n, p):
    print "Yes, inside polygon"
else:
    print "No, not inside polygon"

p = Point(5, 5)
if isInsidePolygon(polygon1, n, p):
    print "Yes, inside polygon"
else:
    print "No, not inside polygon"
'''
p1 = Point(1, 1)
q1 = Point(10, 1)
p2 = Point(1, 2)
q2 = Point(10, 2)
print doIntersect(p1, q1, p2, q2)

p1 = Point(10, 0)
q1 = Point(0, 10)
p2 = Point(0, 0)
q2 = Point(10, 10)
print doIntersect(p1, q1, p2, q2)

l1 = Point(0, 10)
r1 = Point(10, 0)
l2 = Point(5, 5)
r2 = Point(15, 0)
if (doOverlap(l1, r1, l2, r2)):
    print ("Rectangles Overlap")
else:
    print ("Rectangles Don't Overlap")
    
print "Multiplication using ruussian Peasant method", russianPeasant(18, 1)
print "Multiplication using ruussian Peasant method", russianPeasant(20, 12)

st = "string"
print "Rank = ",(findRank(st))

num = 616
isDivisibleBy7(num)
 
arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(arr)
print(randomize(arr, n))

n = 8
k = 2
res = binomialCoefficient(n, k)

n = 10
x = 1.0
print "Taylor series sum is ", exponential(n, x)
day = dayofweek(30, 8, 2010);
print day 
# driver program
if __name__=='__main__':
    n = 30
    print "Following are the prime numbers smaller",
    print "than or equal to", n
    SieveOfEratosthenes(n)

# Works only when n is odd
n = 7
generateSquare(n)

n = 578
print count(n)

# Driver program to test above function Let us check whether the point P(10, 15) lies inside the triangle formed by A(0, 0), B(20, 0) and C(10, 30)
if (isInside(0, 0, 20, 0, 10, 30, 10, 15)):
    print('Inside')
else:
    print('Not Inside') 
    
isLucky.counter = 2 # Acts as static variable
x = 5
if isLucky(x):
    print x,"is a Lucky number"
else:
    print x,"is not a Lucky number"
printFibonacciNumbers(7)
n=9
r=3
print "\n nPr is ", nPr(n, r)

a = 3
b = 4
c = 5
findArea(a,b,c)
n = 5
print("Sum is", round(seriesSum(n), 6))
print "Checking Fibonacci for no 8; It's ", isFibonacci(8)

printString(26)
printString(51)
printString(52)
printString(80)
printString(676)
printString(702)
printString(705)

digits = "534976"      
# converting into integer array, number becomes [5,3,4,9,7,6]
number = map(int ,digits) 
findNext(number, len(digits))

p = Point(1, 9)
q = Point(8, 16)
print "The number of integral points between ( %d  , %d ) and ( %d , %d) is %d " %(p.x, p.y, q.x, q.y, getCount(p, q))
'''
Notes the following will be covered in
https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/ backtracking/strings
https://www.geeksforgeeks.org/find-the-largest-multiple-of-2-3-and-5/
https://www.geeksforgeeks.org/pascal-triangle/
https://www.geeksforgeeks.org/find-the-largest-number-multiple-of-3/
https://www.geeksforgeeks.org/write-a-program-to-add-two-numbers-in-base-14/
https://www.geeksforgeeks.org/print-all-combinations-of-points-that-can-compose-a-given-number/
https://www.geeksforgeeks.org/write-you-own-power-without-using-multiplication-and-division/
https://www.geeksforgeeks.org/dfa-based-division/
https://www.geeksforgeeks.org/given-a-number-find-next-smallest-palindrome-larger-than-this-number/
https://www.geeksforgeeks.org/print-0-and-1-with-50-probability/
https://www.geeksforgeeks.org/lexicographic-permutations-of-string/
https://www.geeksforgeeks.org/reservoir-sampling/
https://www.geeksforgeeks.org/select-a-random-number-from-stream-with-o1-space/
https://www.geeksforgeeks.org/measure-1-litre-from-two-vessels-infinite-water-supply/
https://www.geeksforgeeks.org/print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n/
https://www.geeksforgeeks.org/print-all-combinations-of-given-length/
https://www.geeksforgeeks.org/random-number-generator-in-arbitrary-probability-distribution-fashion/
https://www.geeksforgeeks.org/convex-hull-set-1-jarviss-algorithm-or-wrapping/
https://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/
https://www.geeksforgeeks.org/draw-circle-without-floating-point-arithmetic/

https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/
https://www.geeksforgeeks.org/c-program-print-palindromes-given-range/

https://www.geeksforgeeks.org/closest-pair-of-points-onlogn-implementation/


'''
