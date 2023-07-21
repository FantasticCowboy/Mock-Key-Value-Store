import json
from src.json_io import write_json_file, read_json_file
from src.consistent_hash_function import ConsistenHash


class DiskManager():

    # TODO: need to make this able to read from disk
    def __init__(self, directory):
        self.directory = directory
        self.hash = ConsistenHash()
        self.key_value_store = { self.hash.add_node()  : {}}
        self.key_value_store : dict[int,dict[str,dict]]
        
    def _get_file_name(self, node : int):
        return f"{self.directory}/{str(node)}.json"

    def _sync_to_disk(self):
        """
            Writes whole key value store to disk
        """
        for node in self.key_value_store.keys():
            write_json_file(self._get_file_name(node), self.key_value_store[node])

    def expand(self):
        self.key_value_store[self.hash.add_node()] = {}
        self._rehash()

    # TODO: don't need to rehash everything this is inefficent
    def _rehash(self):
        for node in self.key_value_store.keys():
            self._rehash_node(node)

    # TODO: don't delete keys data here after rehashing, should probably do that
    def _rehash_node(self, node : int):
        for key in self.key_value_store[node].keys():
            self.write(key, self.key_value_store[node][key])

    # TODO: needs to handle  errors if value isn't json serializable
    def write(self, key : str, value : json):         
        node = self.hash.get_node(key)
        self.key_value_store[node][key] = value

    def read(self, key : str): 
        node = self.hash.get_node(key)
        return self.key_value_store[node][key]
    
