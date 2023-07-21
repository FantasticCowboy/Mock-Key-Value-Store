import json
import copy
import logging
import pdb
from abc import ABC


# Singletone class for reading in config information
class Config(object):
    @staticmethod
    def __new__(cls, *args, **kwargs):    
        if not Config.instance:
             Config.instance = super().__new__(cls) 
        assert Config.instance != None
        return Config.instance        

    instance = None

    def __init__(self, path : str):
        config = self._read_config(path)
        self.__dict__ = config
        
    @staticmethod
    def _read_config(path : str) -> dict:
        with open(path) as config:
            return json.load(config)
    