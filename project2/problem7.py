class RouteTrie:
  def __init__(self, handler):
    # Initialize the trie with an root node and a handler, this is the root path or home page node
    self.root = RouteTrieNode()
    self.root.handler = handler

  def insert(self, path_parts, handler):
    # Similar to our previous example you will want to recursively add nodes
    # Make sure you assign the handler to only the leaf (deepest) node of this path
    node = self.root
    for part in path_parts:
      node.insert(part)
      node = node.children[part]
    node.handler = handler

  def find(self, path_parts):
    # Starting at the root, navigate the Trie to find a match for this path
    # Return the handler for a match, or None for no match
    node = self.root
    for part in path_parts:
      if part not in node.children: return None
      node = node.children[part]
    return node.handler


class RouteTrieNode:
  def __init__(self):
    # Initialize the node with children as before, plus a handler
    self.handler = None
    self.children = {}

  def insert(self, path_part):
    # Insert the node as before
    if path_part not in self.children:
      self.children[path_part] = RouteTrieNode()


class Router:
  def __init__(self, root_handler, not_found_handler):
    # Create a new RouteTrie for holding our routes
    # You could also add a handler for 404 page not found responses as well!
    self.route_trie = RouteTrie(root_handler)
    self.not_found_handler = not_found_handler

  def add_handler(self, path, handler):
    # Add a handler for a path
    # You will need to split the path and pass the pass parts
    # as a list to the RouteTrie
    path_parts = self.split_path(path)
    self.route_trie.insert(path_parts, handler)
        
  def lookup(self, path):
    # lookup path (by parts) and return the associated handler
    # you can return None if it's not found or
    # return the "not found" handler if you added one
    # bonus points if a path works with and without a trailing slash
    # e.g. /about and /about/ both return the /about handler
    path_parts = self.split_path(path)
    handler = self.route_trie.find(path_parts)
    if handler is None: return self.not_found_handler
    return handler
    
  def split_path(self, path):
    # you need to split the path into parts for 
    # both the add_handler and loopup functions,
    # so it should be placed in a function here
    if path == '/' or path == '': return []
    return path.strip('/').split('/')
  

# Arrange tests
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")

# Test Case 1: Sanity test
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

# Test Case 2: Look for empty path string
print(router.lookup(""))
# should print 'root handler'

# Test Case 3: Change existing handler to None
router.add_handler("/home/about", None)
print(router.lookup("home/about")) # should print not found handler now
