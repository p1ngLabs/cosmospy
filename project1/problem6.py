class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __repr__(self):
    return str(self.value)


class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def __str__(self):
    cur_head = self.head
    out_string = ""
    while cur_head:
      out_string += str(cur_head.value) + " -> "
      cur_head = cur_head.next
    return out_string

  def append(self, value):
    if self.head is None:
      self.head = Node(value)
      self.tail = self.head
      return
    node = Node(value)
    self.tail.next = node
    self.tail = node

  def size(self):
    size = 0
    node = self.head
    while node:
      size += 1
      node = node.next

    return size

def union(linked_list_1, linked_list_2):
  # Traverse two linked lists and store their items into corresponding sets
  set_1 = linked_list_to_set(linked_list_1)
  set_2 = linked_list_to_set(linked_list_2)
  # Find the union of both sets
  union_set = set_1.union(set_2)
  # Return a linked list contains the elements of the union set
  return to_linked_list(union_set)

def intersection(linked_list_1, linked_list_2):
  # Traverse two linked lists and store their items into corresponding sets
  set_1 = linked_list_to_set(linked_list_1)
  set_2 = linked_list_to_set(linked_list_2)
  # Find the intersection of both sets
  intersective_set = set_1.intersection(set_2)
  # Return a linked list contains the elements of the intersective set
  return to_linked_list(intersective_set)

def linked_list_to_set(linked_list: DoublyLinkedList):
  # Traverse the linked list then return a set from the list elements
  result_set = set()
  node = linked_list.head
  while node is not None:
    result_set.add(node.value)
    node = node.next
  return result_set

def to_linked_list(iterable):
  # Return a doubly linked list from the iterable elements
  linked_list = DoublyLinkedList()
  for element in iterable:
    linked_list.append(element)
  return linked_list

def list_to_linked_list(list):
  # Traverse Python list then return a linked list from the list elements
  linked_list = DoublyLinkedList()
  for element in list:
    linked_list.append(element)
  return linked_list


# Test Case 1: Two linked lists with union and intersection
print('\n--- Test Case 1 ---')
linked_list_1 = DoublyLinkedList()
linked_list_2 = DoublyLinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1: linked_list_1.append(i)
for i in element_2: linked_list_2.append(i)

print('Union:', union(linked_list_1, linked_list_2))
print('Intersection:', intersection(linked_list_1, linked_list_2))

# Test Case 2: Two linked lists with no intersection
print('\n--- Test Case 2 ---')
linked_list_3 = DoublyLinkedList()
linked_list_4 = DoublyLinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1: linked_list_3.append(i)
for i in element_2: linked_list_4.append(i)

print('Union:', union(linked_list_3, linked_list_4))
print('Intersection:', intersection(linked_list_3, linked_list_4))

# Test Case 3: Two empty linked lists
print('\n--- Test Case 3 ---')
linked_list_5 = DoublyLinkedList()
linked_list_6 = DoublyLinkedList()
print('Union:', union(linked_list_5, linked_list_6))
print('Intersection:', intersection(linked_list_5, linked_list_6))
# Expect nothing as we have two empty linked lists
