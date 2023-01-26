import json

with open('json_read.json')as f:
    data = json.load(f)
banana = list(data.keys())
print(banana)
