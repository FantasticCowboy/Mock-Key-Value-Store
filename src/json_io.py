import json

# Files are assumed to be stored as json object key:value pairs
def read_json_file(path) -> json:
    with open(path) as f:
        return json.loads(path)

def write_json_file(path : str, file : json):
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(file)