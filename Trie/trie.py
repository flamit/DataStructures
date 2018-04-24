# Time:  O(n), per operation 
# Space: O(1)
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
    cur.isEndOfWord = True

  def search(self, word):
    cur = self.root
    for c in word:
      if c in cur.leaves:
        cur = cur.leaves[c]
      else:
        return False
    return cur.isEndOfWord

  # Display all the trie words; Practise it well; It can help achieve all the problems
  def displayTrieWords(self):
        Str = [None]*30
        lvl = 0
        self.displayWords(self.root, Str, lvl)

  def displayWords(self, cur, Str, lvl):
        if cur.isEndOfWord:
            Str[lvl] = '\0'
            print Str[0:lvl]
            
        for c in cur.leaves:
            Str[lvl] = c
            self.displayWords(cur.leaves[c], Str, lvl+1)

  def displayContents(self):
    self.display(self.root)
    
  def display(self, cur):
      for c in cur.leaves:
        if (cur.leaves[c]):
          print c,
          self.display(cur.leaves[c])
          
  def words_with_prefix(self, prefix):
    cur = self.root
    for c in prefix:
      if c in cur.leaves:
        cur = cur.leaves[c]
      else:
        return []
      
    Str=[prefix]*30
    lvl=0
    self.displayWords(cur, Str, lvl+1)
    
    '''result = []
    self.traverse(cur, list(prefix), result)
    return [''.join(r) for r in result]'''

  # Longest prefix matching
  def longest_prefix_matching(self, prefix):
    cur = self.root
    for c in prefix:
      if c in cur.leaves:
        cur = cur.leaves[c]
      else:
        return []

    Str = [prefix]*30
    lvl = 0
    self.longest=''
    self.displayWords2(cur, Str, lvl+1)
    print "Longest is ", self.longest
    
    '''result = []
    self.traverse_for_longest(cur, list(prefix))
    return t.longest_prefix'''

  # Same as displayWords definition except the length comparison line
  def displayWords2(self, cur, Str, lvl):
    if cur.isEndOfWord:
      Str[lvl] = '\0'
      if len(Str[0:lvl])>len(self.longest):
        self.longest=Str[0:lvl]

    for c in cur.leaves:
      Str[lvl] = c
      self.displayWords2(cur.leaves[c], Str, lvl+1)
      
  def traverse(self, root, prefix, result):
    if root.isEndOfWord:
      result.append(prefix[:])
    for c, n in root.leaves.items():
      prefix.append(c)
      self.traverse(n, prefix, result)
      prefix.pop(-1)

  def traverse_for_longest(self, root, prefix):
    if root.isEndOfWord:
      if len(prefix[:]) > t.max_len:
        t.max_len = len(prefix[:])
        t.longest_prefix = ''.join(prefix[:])
        
    for c, n in root.leaves.items():
      prefix.append(c)
      self.traverse_for_longest(n, prefix)
      prefix.pop(-1)
      
  def wordBreak(self, strng):
    n = len(strng)
    if (n == 0):
      return True
    
    for i in xrange(1, n+1):
      if (self.search(strng[0:i]) and self.wordBreak(strng[i:n])):
        #print strng[0:i],
        return True
    return False

if __name__=="__main__":
  trie = Trie()
  
  keys = ["she","sells","sea","shore","the","by","sheer", "she", "shearsholdings"]
  for key in keys:
    trie.insert(key)
  #print trie.search("she")
  #trie.displayTrieWords()
  #trie.displayContents()
  print trie.words_with_prefix("sh")
  
  t = TrieNode()
  t.longest_prefix = ""
  t.max_len = 0
  print trie.longest_prefix_matching("sh")

  t = Trie()
  dictionary = ["mobile","samsung","sam",
                           "sung","man","mango",
                           "icecream","and","go","i",
                           "like","ice","cream"]
  for key in dictionary:
    t.insert(key)
  print t.wordBreak("ilikesamsung")
  '''print t.wordBreak("iiiiiiii")
  print t.wordBreak("")
  print t.wordBreak("ilikelikeimangoiii")
  print t.wordBreak("samsungandmango")
  print t.wordBreak("samsungandmangok")'''
'''
Example:
If we have words such as :
 JavaOne
 JavaTwo
 JavaThree
 JavaFour
 JavaFive

The Trie would look like
       ()
       |
       J
       |
       a
       |
       V
       |
       a
    /  |   \ 
   F   O    T
  /\   |    /\
 i  o  n   h  w
 |  |  |   |  |
 V  u  e   r  o
 |  |      |
 e  r      e
           |
           e
'''
