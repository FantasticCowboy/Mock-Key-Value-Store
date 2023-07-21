from src.disk_manager import DiskManager
import random
import logging
import pathlib
def get_random_key():
    keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s']
    return keys[random.randint(0,len(keys)-1)] + str(random.randint(0,10))

def get_random_value():
    return random.randint(0,10)

def get_rand_key_value():
    return get_random_key(), get_random_value()

def validate_kv_store(manager : DiskManager, local_key_value : dict):
    for key in local_key_value.keys():
        print(f"key={key} value={manager.read(key)} local_value={local_key_value[key]}")
        assert manager.read(key) == local_key_value[key]



def test_simple(tmp_path):
    manager = DiskManager(tmp_path)    

    local_key_value = {}


    for i in range(0,1000):
        key, value = get_rand_key_value()
        local_key_value[key] = value
        manager.write(key, value)
        validate_kv_store(manager, local_key_value)
    
def test_complex(tmp_path):
    manager = DiskManager(tmp_path)    
    logging.basicConfig(level=logging.DEBUG)
    local_key_value = {}
    for i in range(0,100):
        if i % 10 == 0:
            print("Expanding...")
            manager.expand()
        key, value = get_rand_key_value()
        print(f"storing key={key} value={value} locally")
        local_key_value[key] = value
        manager.write(key, value)
        validate_kv_store(manager, local_key_value)

def test_read_from_disk(tmp_path :  pathlib.Path):
    path = tmp_path
    manager = DiskManager(path)
    print(path)
    
    logging.basicConfig(level=logging.DEBUG)
    local_key_value = {}
    for i in range(0,100):
        if i % 10 == 0:
            manager.expand()
        key, value = get_rand_key_value()
        local_key_value[key] = value
        manager.write(key, value)
        validate_kv_store(manager, local_key_value)

    print("reading and validating...")
    print(path)
    manager = DiskManager(path, read_from_disk=True)
    validate_kv_store(manager, local_key_value)

    for i in range(0,100):
        if i % 10 == 0:
            manager.expand()
        key, value = get_rand_key_value()
        local_key_value[key] = value
        manager.write(key, value)
        validate_kv_store(manager, local_key_value)

def test_long(tmp_path):
    manager = DiskManager(tmp_path)    
    logging.basicConfig(level=logging.DEBUG)
    local_key_value = {}
    for i in range(0,10000):
        if i % 1000 == 0:
            print("Expanding...")
            manager.expand()
        key, value = get_rand_key_value()
        print(f"storing key={key} value={value} locally")
        local_key_value[key] = value
        manager.write(key, value)
        validate_kv_store(manager, local_key_value)