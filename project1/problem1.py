from typing import Dict

DEFAULT_CAPACITY = 5

class DoublyLinkedListNode:
  def __init__(self, value):
    """Create a new Doubly Linked List Node"""
    self.value = value  # actual value that is stored in cache
    self.prev = None    # key of previous cache value
    self.next = None    # key of next cache value


class LRU_Cache(object):
  """Implementation of LRU (Least Recently Used) Cache"""

  def __init__(self, capacity=DEFAULT_CAPACITY):
    # Initialize class variables
    if type(capacity) is not int:
        raise TypeError('Invalid capacity type')
    elif capacity < 0:
        capacity = DEFAULT_CAPACITY
    self.capacity = capacity
    self._cache: Dict[int, DoublyLinkedListNode] = {}
    self.head = None # key of least recently used cache
    self.tail = None # key of most recently used cache

  @property
  def size(self):
    # Get cache's current size
    return len(self._cache.keys())

  def get(self, key):
    # Retrieve item from provided key. Return -1 if nonexistent. 
    if key not in self._cache: return -1 # cache miss
    # cache hit
    self.update_most_recently_used(key)
    return self._cache[key].value

  def set(self, key, value):
    # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
    if key in self._cache:
        # assign new node value then update cache
        self._cache[key].value = value
        self.update_most_recently_used(key)
    else:
        self.insert_new_cache(key, value)
    
  def update_most_recently_used(self, key):
    if key == self.tail: return # do nothing
    elif key == self.head:
      # update least recently used cache by detaching head
      self.head = self._cache[self.head].next
      self._cache[self.head].prev = None
      # update most recently used cache by attaching tail
      self._cache[key].prev = self.tail
      self._cache[key].next = None
      self._cache[self.tail].next = key
      self.tail = key
    else:
      if self.size == 1: return
      # update adjacent caches in current position
      self._cache[self._cache[key].prev].next = self._cache[key].next
      self._cache[self._cache[key].next].prev = self._cache[key].prev
      # move accessed cache to tail
      self._cache[key].prev = self.tail
      self._cache[key].next = None
      self._cache[self.tail].next = key
      self.tail = key

  def insert_new_cache(self, key, value):
    self._cache[key] = DoublyLinkedListNode(value)
    if self.size == 1:
      self.head = key
    else:
      self._cache[key].prev = self.tail
      self._cache[self.tail].next = key
    self.tail = key
    if self.size > self.capacity:
      # update least recently used cache by detaching head then deleting from the cache
      deleted_key = self.head
      self.head = self._cache[self.head].next
      self._cache[self.head].prev = None
      del self._cache[deleted_key]


# Test Case 1: Get value that is not in cache
print('--- Test Case 1 ---')
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      
# returns -1 because 9 is not present in the cache

# Test Case 2: Get older cache after exceeding capacity with new cache
print('--- Test Case 2 ---')
our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.get(3))      
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Test Case 3: Get from empty cache
print('--- Test Case 3 ---')
zero_cache = LRU_Cache(-2)
print(zero_cache.get(3))    
# return -1 because the cache is empty

# Test Case 4: Cache capacity is None
print('--- Test Case 4 ---')
invalid_cache = LRU_Cache(None)
invalid_cache.set(2,3)
# raise TypeError as expected because cache size can not be None
