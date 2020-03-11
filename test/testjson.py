import json
from core.config import Config
from remote.remotehttp import RemoteHTTP


with open('./datasets/customers.json') as f:
    data = json.load(f)
    print(data)
    print(data['name'])
    
    conf = Config(data)
    print(conf.data )
    
  #  http = RemoteHTTP(conf)
  #  print(http.config.data )
  #  http._buildURLPath()
    