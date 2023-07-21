import hashlib
from src.circular_array import SortedCircularArray
import random

class ConsistenHash():
    def __init__(self):
        self.array = SortedCircularArray()
        self.HASH_SPACE = pow(2,256)

    def __call__(self, value : str) -> int:
        return self.hash(value)
    
    def get_node(self, value : str) -> int:
        val = self.hash(value)
        return self.array.get_upper_bound(val)

    def hash(self, value) -> int:
        return int.from_bytes(hashlib.sha256(bytes(value, encoding="utf-8")).digest(), byteorder="little")

    def add_node(self, new_node_pos=None) -> int:
        if not new_node_pos:
            new_node_pos = random.randint(0, self.HASH_SPACE)
        self.array.insert(new_node_pos)        
        return new_node_pos
