import json

def read_json(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
    return data

def write_json(path: str, data: dict):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)