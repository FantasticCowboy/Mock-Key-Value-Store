import json
from src.json_io import write_json_file, read_json_file
from src.consistent_hash_function import ConsistenHash
import logging
import os
import glob
import pathlib
class DiskManager():

    # TODO: need to make this able to read from disk
    def __init__(self, directory : pathlib.Path, read_from_disk=False, MAX_KEYS=1000):
        self.directory = directory
        self.MAX_KEYS = MAX_KEYS
        self.hash = ConsistenHash()
        self.key_value_store : dict[int,dict[str,dict]]
        self.key_value_store = {}
        self._read_from_disk()

    def _read_from_disk(self):
        for name in os.listdir(self.directory):
            print(name)
            self.key_value_store[int(name[:-5])] = read_json_file(self.directory / name)
            self.hash.add_node(int(name[:-5]))
        if len(self.key_value_store) == 0:
            self.key_value_store = { self.hash.add_node()  : {}}

    def _get_file_name(self, node : int):
        return self.directory/f"{str(node)}.json"

    def _sync_to_disk(self):
        """
            Writes whole key value store to disk
        """
        for node in self.key_value_store.keys():
            write_json_file(self._get_file_name(node), self.key_value_store[node])

    def expand(self):
        node = self.hash.add_node()
        self.key_value_store[node] = {}
        self._rehash()
        self._sync_to_disk()

    # TODO: don't need to rehash everything this is inefficent
    def _rehash(self):
        for node in self.key_value_store.keys():
            self._rehash_node(node)

    # TODO: don't delete keys data here after rehashing, should probably do that
    def _rehash_node(self, node : int):
        for key in list(self.key_value_store[node].keys()):
            if self.hash.get_node(key) != node:
                print(f"rehashing key={key}")
                self.write(key, self.key_value_store[node][key])
                del self.key_value_store[node][key]

    # TODO: needs to handle  errors if value isn't json serializable
    def write(self, key : str, value : json):         
        node = self.hash.get_node(key)        
        self.key_value_store[node][key] = value
        print(f"writing key={key},value={value} to node={node}")
        if len(self.key_value_store[node]) > self.MAX_KEYS:
            self.expand()
        else:
            self._sync_to_disk()

    def read(self, key : str): 
        node = self.hash.get_node(key)
        return self.key_value_store[node][key] if key in self.key_value_store[node] else None
    
