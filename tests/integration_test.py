import requests
import random

URL = "http://localhost:5001/"
GET_URL = URL + "get"
SET_URL = URL + "set"
def get_random_key():
    keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s']
    return keys[random.randint(0,len(keys)-1)] + str(random.randint(0,10))

def validate_kv_store(local_key_value : dict):
    for key in local_key_value.keys():
        assert get(key) == local_key_value[key]
        
def get_random_value():
    return str(random.randint(0,10))

def get_rand_key_value():
    return get_random_key(), get_random_value()

def get(key):
    ret = requests.get(GET_URL, params={
        "key" : key
    }).text
    return ret
def set(key, value):
    requests.post(SET_URL, data={
        "key" : key,
        "value" : value
    } )

def test_complex():
    local_key_value = {}
    for i in range(0,100):
        key, value = get_rand_key_value()
        local_key_value[key] = value
        set(key,value)
    validate_kv_store( local_key_value)
        
test_complex()