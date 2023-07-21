import hashlib
from src.circular_array import SortedCircularArray

class ConsistenHash():
    def __init__(self):
        self.array = SortedCircularArray()

    def __call__(self, value : str) -> int:
        return self.hash(value)
    
    def get_node(self, value : str) -> int:
        val = self.hash(value)
        return self.array.get_upper_bound(val)

    def hash(self, value) -> int:
        return int.from_bytes(hashlib.sha256(value).digest())

    def add_node(self, node : int) -> int:
        new_node_pos = self.hash(node)
        self.array.insert(new_node_pos)
        predecessor = self.array.previous(new_node_pos)
        return predecessor
