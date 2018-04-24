'''
Searching for Patterns | Set 5 (Finite Automata)
Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.

Examples: 
Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12
pattern-searching

We have discussed the following algorithms in the previous posts:

Naive Algorithm 
KMP Algorithm
Rabin Karp Algorithm

In this post, we will discuss Finite Automata (FA) based pattern searching algorithm. In FA based algorithm, we preprocess the pattern and build a 2D array that represents a Finite Automata.
Construction of the FA is the main tricky part of this algorithm. Once the FA is built, the searching is simple. In search, we simply need to start from the first state of the automata and
the first character of the text. At every step, we consider next character of text, look for the next state in the built FA and move to a new state. If we reach the final state,
then the pattern is found in the text. The time complexity of the search process is O(n).

In the following code, computeTF() constructs the FA. The time complexity of the computeTF() is O(m^3*NO_OF_CHARS), where m is length of the pattern and NO_OF_CHARS is size of alphabet
(total number of possible characters in pattern and text). The implementation tries all possible prefixes starting from the longest possible that can be a suffix of "pat[0..k-1]x".
There are better implementations to construct FA in O(m*NO_OF_CHARS) (Hint: we can use something like lps array construction in KMP algorithm).
We have covered the better implementation in our next post on pattern searching.
Time Complexity for FA construction is O(M*NO_OF_CHARS). The code for search is same as the previous post and time complexity for it is O(n).
'''
# Python program for Finite Automata 
# Pattern searching Algorithm
 
NO_OF_CHARS = 256 
def getNextState(pat, M, state, x):
    if state < M and x == ord(pat[state]):                      # If the character c is same as next character in pattern, then simply increment state
        return state+1
 
    i=0
    for ns in range(state,0,-1):                                # ns stores the result which is next state. ns finally contains the longest prefix which is also suffix in "pat[0..state-1]c"
        if ord(pat[ns-1]) == x:                                 # Start from the largest possible value and stop when you find a prefix which is also suffix
            while(i<ns-1):
                if pat[i] != pat[state-ns+1+i]:
                    break
                i+=1
            if i == ns-1:
                return ns 
    return 0

# This function builds the TF table which represents Finite Automata for a given pattern 
def computeTF(pat, M):
    global NO_OF_CHARS
 
    TF = [[0 for i in range(NO_OF_CHARS)]\
          for _ in range(M+1)]
 
    for state in range(M+1):
        for x in range(NO_OF_CHARS):
            z = getNextState(pat, M, state, x)
            TF[state][x] = z
 
    return TF

# Prints all occurrences of pat in txt
def search_using_finite_automata(pat, txt):
    global NO_OF_CHARS
    M = len(pat)
    N = len(txt)
    TF = computeTF(pat, M)    
 
    # Process txt over FA.
    state=0
    for i in range(N):
        state = TF[state][ord(txt[i])]
        if state == M:
            print("Pattern found at index: {}".\
                   format(i-M+1))


def badCharHeuristic(string, size):
    '''
    The preprocessing function for
    Boyer Moore's bad character heuristic
    '''
 
    # Initialize all occurence as -1
    badChar = [-1]*NO_OF_CHARS
 
    # Fill the actual value of last occurence
    for i in range(size):
        badChar[ord(string[i])] = i;
 
    # retun initialized list
    return badChar
 
def search_using_boyer_moore_algorithm(txt, pat):
    '''
    A pattern searching function that uses Bad Character
    Heuristic of Boyer Moore Algorithm
    '''
    m = len(pat)
    n = len(txt)
 
    # create the bad character list by calling 
    # the preprocessing function badCharHeuristic()
    # for given pattern
    badChar = badCharHeuristic(pat, m) 
 
    # s is shift of the pattern with respect to text
    s = 0
    while(s <= n-m):
        j = m-1
 
        # Keep reducing index j of pattern while 
        # characters of pattern and text are matching
        # at this shift s
        while j>=0 and pat[j] == txt[s+j]:
            j -= 1
 
        # If the pattern is present at current shift, 
        # then index j will become -1 after the above loop
        if j<0:
            print("Pattern occur at shift = {}".format(s))
 
            '''    
                Shift the pattern so that the next character in text
                      aligns with the last occurrence of it in pattern.
                The condition s+m < n is necessary for the case when
                   pattern occurs at the end of text
               '''
            s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
        else:
            '''
               Shift the pattern so that the bad character in text
               aligns with the last occurrence of it in pattern. The
               max function is used to make sure that we get a positive
               shift. We may get a negative shift if the last occurrence
               of bad character in pattern is on the right side of the
               current character.
            '''
            s += max(1, j-badChar[ord(txt[s+j])])
 
# Driver program to test above function            
def main():
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    print "Searching using finite automata"
    search_using_finite_automata(pat, txt)
    print "Searching using Boyer Moore algorithm"
    search_using_boyer_moore_algorithm(txt, pat)
 
if __name__ == '__main__':
    main()
'''    
 
  Pattern found at index 0
  Pattern found at index 9
  Pattern found at index 13
'''
