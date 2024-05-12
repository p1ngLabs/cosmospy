## Represents a single node in the Trie
class TrieNode:
  def __init__(self):
    ## Initialize this node in the Trie
    self.is_word = False
    self.children = {}

  def insert(self, char):
    ## Add a child node in this Trie
    if char not in self.children:
      self.children[char] = TrieNode()

  def suffixes(self, suffix = ''):
    ## Recursive function that collects the suffix for
    ## all complete words below this point
    suffixes_list = []

    for char, child in self.children.items():
      if child.is_word:
        suffixes_list.append(suffix + char)
      suffixes_list.extend(child.suffixes(suffix + char))

    return suffixes_list

        
## The Trie itself containing the root node and insert/find functions
class Trie:
  def __init__(self):
    ## Initialize this Trie (add a root node)
    self.root = TrieNode()

  def insert(self, word):
    ## Add a word to the Trie
    node = self.root

    for char in word:
      node.insert(char)
      node = node.children[char]

    node.is_word = True

  def find(self, prefix):
    ## Find the Trie node that represents this prefix
    if type(prefix) is not str or prefix == '':
      return TrieNode()

    node = self.root

    for char in prefix:
      if char not in node.children:
        return None
      node = node.children[char]
    return node


# Arrange tests
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# Test Case 1: Sanity test
prefix = 'f'
prefixNode = MyTrie.find(prefix)
print(f"Prefix: '{prefix}'")
print(prefixNode.suffixes())
print('\n')

prefix = 'trig'
prefixNode = MyTrie.find(prefix)
print(f"Prefix: '{prefix}'")
print(prefixNode.suffixes())
print('\n')

# Test Case 2: Empty string as prefix
prefix = ''
prefixNode = MyTrie.find(prefix)
print(f"Prefix: '{prefix}'")
print(prefixNode.suffixes())
print('\n') # should print empty list

# Test Case 3: Existing word in the list
prefix = 'function'
prefixNode = MyTrie.find(prefix)
print(f"Prefix: '{prefix}'")
print(prefixNode.suffixes()) # should print empty list
