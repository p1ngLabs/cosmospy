from datetime import datetime, timezone
import hashlib

class Block:
  def __init__(self, previous_hash, data, index: int):
    """Initialize the block"""
    self.index = index
    self.previous_block = None
    self.previous_hash = previous_hash
    self.data = data
    self.timestamp = datetime.now(timezone.utc)
    self.hash = self.calc_hash()

  def calc_hash(self):
    """Calculate cryptographic hash from previous hash, timestamp and data of the block"""
    sha = hashlib.sha256()
    block_data =  str(self.previous_hash) + str(self.timestamp) + str(self.data)
    sha.update(block_data.encode('utf-8'))
    return sha.hexdigest()
  
  def __repr__(self) -> str:
    repr_str = f'\tprevious hash: {self.previous_hash}'
    repr_str += f'\n\thash: {self.hash}'
    repr_str += f'\n\tdata: {self.data}'
    repr_str += f'\n\ttimestamp: {self.timestamp}\n'
    return repr_str

class BlockChain:
  def __init__(self):
    """Initialize the block chain"""
    self.index = 0
    # Create a genesis block when initilize the block chain
    genesis_block = Block('0', 'First block of the chain', self.index)
    self.head = genesis_block
  
  def add_block(self, data):
    """Add new block to the block chain"""
    self.index += 1
    new_block = Block(self.head.hash, data, self.index)
    new_block.previous_block = self.head
    self.head = new_block

  def __repr__(self) -> str:
    block = self.head
    repr_str = 'Your block chain:'
    while block is not None:
      repr_str += f'\nblock index: {block.index}'
      repr_str += f'\nblock content:'
      repr_str += f'\n{block}'
      block = block.previous_block
    return repr_str

# Test Case 1: Block Chain with only the genesis block
print('\n--- Test Case 1 ---')
chain = BlockChain()
print(chain)
# print the block chain with the genesis block only

# Test Case 2: Add new block to the block chain
print('\n--- Test Case 2 ---')
chain.add_block('Second block of the chain')
print(chain)
# print the block chain with two blocks

# Test Case 3: Add new block with the same data as the second block
print('\n--- Test Case 3 ---')
chain.add_block('Second block of the chain')
chain.add_block('Second block of the chain')
print(chain)
# print the block chain in which each block has different hash
