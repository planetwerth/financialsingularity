import hashlib
import json
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(block):
    block_string = json.dumps(block.__dict__, sort_keys=True)
    return hashlib.sha256(block_string.encode('utf-8')).hexdigest()

def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block", calculate_hash(Block(0, "0", time.time(), "Genesis Block", "")))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = time.time()
    hash = calculate_hash(Block(index, previous_block.hash, timestamp, data, ""))
    return Block(index, previous_block.hash, timestamp, data, hash)
