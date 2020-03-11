import json
from core.config import Config

with open('./datasets/customers.json') as f:
    data = json.load(f)
    print(data)
    print(data['name'])
    
    config = Config(data)
    print(config)