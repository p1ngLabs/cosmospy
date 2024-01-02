import sys
import heapq
from collections import defaultdict

class HuffmanNode:
  def __init__(self, char, frequency):
    # leaf node properties
    self.char = char
    self.frequency = frequency
    # huffman internal node properties
    self.left = None
    self.right = None

  def __lt__(self, other):
    return self.frequency < other.frequency
  
  def __repr__(self) -> str:
    repr_str = '\n----- Huffman Node:'
    repr_str += f'\ncharacter: {self.char}'
    repr_str += f'\nfrequency: {self.frequency}'
    return repr_str

def build_frequency_dict(data):
  # Create a mapping between data character and its frequency
  result = defaultdict(int)
  for char in data:
    result[char] += 1
  return result

def build_huffman_tree(frequency_dict):
  # Initialize a priority queue from the created frequency dictionary then
  # transform it into a heap using `heapify` method
  priority_queue = [HuffmanNode(char, freq) for char, freq in frequency_dict.items()]
  heapq.heapify(priority_queue)

  if len(priority_queue) == 1:
    # If data has single symbol/character
    node = HuffmanNode(priority_queue[0].char, priority_queue[0].frequency)
    priority_queue[0].left = node
    priority_queue[0].right = None

  while len(priority_queue) > 1:
    # Get two least frequency nodes as left and right leaf for the merged nodes
    left = heapq.heappop(priority_queue)
    right = heapq.heappop(priority_queue)
    # Create a new node in the Huffman tree with a frequency equal to the sum of the two above nodes
    merged = HuffmanNode(None, left.frequency + right.frequency)
    merged.left = left
    merged.right = right
    heapq.heappush(priority_queue, merged)

  # Return the root of the Huffman tree
  return priority_queue[0]

def generate_huffman_codes(root: HuffmanNode, current_code: str, huffman_codes):
  if root is not None:
    if root.char is not None:
      huffman_codes[root.char] = current_code
    generate_huffman_codes(root.left, current_code + '0', huffman_codes)
    generate_huffman_codes(root.right, current_code + '1', huffman_codes)

def huffman_encoding(data):
  """Encode data string."""
  if data == '': 
    # If data is an empty string
    return '', None

  frequency_dict = build_frequency_dict(data)
  root = build_huffman_tree(frequency_dict)

  huffman_code_mapping = {}
  # Populate huffman_code_mapping by recursively traversing Huffman tree from the root
  generate_huffman_codes(root, '', huffman_code_mapping)
  # Encode the given data with codes from the mapping
  encoded_data = ''.join(huffman_code_mapping[char] for char in data)
  return encoded_data, root

def huffman_decoding(encoded_data, root):
  """For every bit in the encoded data, traverse the Huffman tree from the root down to decode."""
  decoded_data = ''
  current_node: HuffmanNode = root

  for bit in encoded_data:
    if bit == '0':
      current_node = current_node.left
    else:
      current_node = current_node.right

    if current_node.char is not None:
      decoded_data += current_node.char
      current_node = root

  return decoded_data

if __name__ == "__main__":
  def test(description, data):
    print(f'\n{description}')
    print("The size of the data is: {}".format(sys.getsizeof(data)))
    print("The content of the data is: \'{}\'".format(data))

    encoded_data, root = huffman_encoding(data)
    if encoded_data:
      print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    else:
      print("The size of the encoded data is: 0")
    print("The content of the encoded data is: \'{}\'".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, root)
    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: \'{}\'".format(decoded_data))

    print(f"=> Is decoded data the same as the original data: {data == decoded_data}\n")

  # Test Case 1: Great data
  description = '--- Test Case 1 ---'
  sentence = 'The quick brown fox jumps over the lazy dog, carrying a bag full of miscellaneous items, including a quirky umbrella and a dozen zippers'
  test(description, sentence)
  
  # Test Case 2: Empty string data
  description = '--- Test Case 2 ---'
  empty = ''
  test(description, empty)

  # Test Case 3: Data has only one type of character
  description = '--- Test Case 3 ---'
  sentence = 'AAAAAAAA'
  test(description, sentence)
