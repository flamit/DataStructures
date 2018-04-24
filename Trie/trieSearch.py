# Time:  O(n), per operation 
# Space: O(1) 
# 
# Implement a trie with insert, search, and startsWith methods. 
# 
# Note: 
# You may assume that all inputs are consist of lowercase letters a-z. 
# 


class TrieNode: 
    # Initialize your data structure here. 
    def __init__(self): 
        self.isEndOfWord = False 
        self.leaves = {}

class Trie: 
    def __init__(self):
        self.root = TrieNode()
        self.count = 0
        self.level = 0
        self.movement = ""
        self.prefix = ""

    # @param {string} word 
    # @return {void} 
    # Inserts a word into the trie. 
    def insert(self, word): 
        print "\nInserting..."
        cur = self.root 
        for c in word:
            if not c in cur.leaves: 
                print c,
                cur.leaves[c] = TrieNode() 
            cur = cur.leaves[c] 
        cur.isEndOfWord = True 

    # @param {string} word 
    # @return {boolean} 
    # Returns if the word is in the trie. 
    def search(self, word): 
        node = self.childSearch(word) 
        if node: 
            return node.isEndOfWord 
        return False         

    # @param {string} prefix 
    # @return {boolean} 
    # Returns if there is any word in the trie 
    # that starts with the given prefix. 
    def startsWith(self, prefix): 
        return self.childSearch(prefix) is not None 

    def childSearch(self, word): 
        cur = self.root 
        for c in word: 
            if c in cur.leaves: 
                cur = cur.leaves[c] 
            else: 
                return None 
        return cur

    #function to display Trie words
    def displayTrieWords(self):
        str = [None] * 30
        lvl = 0
        self.displayWords(self.root, str, lvl)
		
    def displayWords(self, root, str, lvl):
    #If node is leaf node, it indicates end of string, so a null character is added and string is displayed
      cur = root
      if (cur.isEndOfWord):
        str[lvl] = '\0'
        print str[0:lvl]

      for obj in cur.leaves:
        # if NON NULL child is found add parent key to str and call the display function recursively for child node
        if (cur.leaves[obj]):
          str[lvl] = obj
          self.displayWords(cur.leaves[obj], str, lvl + 1)
	  
    #function to display the contents of Trie
    def displayContents(self):
        self.display(self.root)
    
    def display(self, cur):
        for obj in cur.leaves:
            if (cur.leaves[obj]):
                print obj,
                self.display(cur.leaves[obj])
	  
    #Counts and returns the number of children of the current node
    def countChildren(self, rootNode):
        cur = rootNode
        
        #print cur.leaves
        count = 0
        for obj in cur.leaves:
          count += 1
        return count

	# print all words with prefix
	def words_with_prefix(self, prefix):
		cur = self.root
		for c in prefix:
			if c in cur.leaves:
				cur = cur.leaves[c]
			else:
				return []

		result = []
		self.traverse(cur, list(prefix), result)
		return [''.join(r) for r in result]

	def traverse(self, root, prefix, result):
		if root.isEndOfWord:
			result.append(prefix[:])
		for c, n in root.leaves.items():
			prefix.append(c)
			self.traverse(n, prefix, result)
			prefix.pop(-1)
			
			
    # Peform a walk on the trie and return the longest common prefix string
    def walkTrie(self, root=None):
        cur = root or self.root
        indexs = 0
        for obj in cur.leaves:
            #if (self.countChildren(cur.leaves[obj] == 1 and cur.leaves[obj].isEndOfWord == False):
            #    prefix += obj
            #else:
			#    self.walkTrie(cur.leaves[obj])
            #pCrawl = pCrawl.leaves[obj]
            #print "Object is %s "%(obj)
            #print "Count is %d "%(self.countChildren(cur.leaves[obj]))
            
            if (cur.leaves[obj].isEndOfWord == False):
              if self.countChildren(cur.leaves[obj]) == 1:
            #    print "Hello"
                #print "Object is %s "%(obj)
                #print "within if Object is %s "%(obj)
                self.prefix += obj
                self.walkTrie(cur.leaves[obj])
              elif self.countChildren(cur.leaves[obj]) == 2:
                self.prefix += obj
                #print "prefix is " + self.prefix
                
            #if (self.countChildren(pCrawl) == 1 and pCrawl.isEndOfWord == False):
                
            #    prefix += pCrawl
            #    indexs += 1
                #prefix += (char)('a' + indexs)
            #    print pCrawl
        return self.prefix
        print "prefix is " + self.prefix

# Your Trie object will be instantiated and called as such: 
trie = Trie() 
keys = ["she","sells","sea","shore","the","by","sheer"]
trie = Trie()
for key in keys:
    trie.insert(key)
# print trie.search("sea")
#print trie.countChildren()
#trie.displayContents()
#print "Count = %d" %(trie.level)
#print "Movement = %s" %(trie.movement)
trie.displayTrieWords()
#trie.insert("geeksforgeeks")
#trie.insert("geeks")
#trie.insert("geek")
#trie.insert("geezer")
#print trie.walkTrie()
#trie.insert("somestring")
#trie.insert("hello")
#trie.insert("omestr") 
#trie.insert("cat") 
#trie.insert("cats")
#trie.insert("ecatsssszzz")
#trie.insert("edog")
#print trie.search("key") 
#print trie.search("mest")
#print trie.search("somestring")
#print trie.startsWith("somestr")
#trie.countChildren()
#print trie.count
#trie.walkTrie()
'''trie.insert('foobar')
trie.insert('foo')
trie.insert('bar')
trie.insert('foob')
trie.insert('foof')
'''

'''
Tried is a tree-based data structure, which is used for efficient reTRIEval of a key in a large data-set of strings. Unlike a binary search tree, where node in the trees stores the key associated with that node, in trie node s position in the tree defines the key with which it is associated and the key are only associated with the leaves. It is also known as prefix tree as all descendants of a node have commnon prefix of the string associated with that node, and the root is assocaited with the empty string.

Time complexity of a Trie data structure for insertion/deletion/search operation is just O(n) where n is the key length.

Space complexity of a Trie data structure is O(N*M*C) where N is the number of strings and M is the highest length of the string and C is the size of the alphabet.
Application of Trie Data Structure:
==================================
1. As a replacement for other data structures
	Trie has a number of advantages over bst. It can also be used to replace a hash table as lookup is generally faster in trie even in the worst case.
	Also there are no collisions of different keys in a trie and a trie can provide an alphabetical ordering of the entries by key.
2. Autocomplete / Dictionary
3. Spell checker
4. Lexicographic sorting of a set of keys
5. Longest prefix matching

Structure:
==========
We use a trie to store pieces of data that have a key (used to identify the data) and possibly a value (which holds any additional data associated with the key). 
Here, we will use data whose keys are strings. 
Suppose we want to store a bunch of name/age pairs for a set of people (we ll consider names to be a single string here).

Now, how will we store these name/value pairs in a trie? A trie allows us to share prefixes that are common among keys. Again, our keys are names, which are strings. 

Lets start off with amy. We ll build a tree with each character in her name in a separate node. There will also be one node under the last character in her name (i.e., under y). In this final node, we ll put the nul character (\0) to represent the end of the name. This last node is also a good place to store the age for amy.

      .     <- level 0 (root)
      |
      a     <- level 1
      |
      m     <- level 2
      |
      y     <- level 3
      |
    \0 56   <- level 4

Note that each level in the trie holds a certain character in the string amy. The first character of a string key in the trie is always at level 1, the second character at level 2, etc. 
Now, when we go to add ann, we do the same thing; however, we already have stored the letter a at level 1, so we dont need to store it again, we just reuse that node with a as the first character. Under a (at level 1), however, there is only a second character of m...But, since ann has a second character of n, we ll have to add a new branch for the rest of ann, giving:

amy	56
ann	15
emma	30
rob	27
roger	52

      |
      a --------- e ----- r
      |           |       |
      m --- n     m       o
      |     |     |       |
      y     n     m       b ----- g
      |     |     |       |       |
    \0 56 \0 15   a     \0 27     e
                  |               |
                \0 30             r
                                  |
                                \0 52


http://www.geeksforgeeks.org/longest-common-prefix-set-5-using-trie/

Longest Common Prefix | Set 5 (Using Trie)

3.7 
 

Given a set of strings, find the longest common prefix.
Input  : {"geeksforgeeks", "geeks", "geek", "geezer"}
Output : "gee" 

Input  : {"apple", "ape", "april"}
Output : "ap"


Previous Approaches :  Word by Word Matching ,  Character by Character Matching,  Divide and Conquer , Binary Search.

In this article, an approach using Trie date structure  is discussed.
Steps:
 Insert all the words one by one in the trie. After inserting we perform a walk on the trie.
 In this walk, go deeper until we find a node having more than 1 children(branching occurs) or 0 children (one of the string gets exhausted). 
This is because the characters (nodes in trie) which are present in the longest common prefix must be the single child of its parent, i.e- there should not be a branching in any of these nodes.

Algorithm Illustration considering strings as "geeksforgeeks", "geeks", "geek", "geezer"
'''


