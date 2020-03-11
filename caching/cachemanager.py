from core.config import Config
from caching.cache import Cache

class CacheManager:
    
    __cache = None
    __instance = None
    
    def __init__(self):
        if CacheManager.__instance == None:
            CacheManager.__cache = Cache()
            CacheManager.__instance = self      
    
    @staticmethod
    def getInstance():
        if CacheManager.__instance == None:
            CacheManager()
        return  CacheManager.__instance
    
    @staticmethod
    def getCache():
        return CacheManager.getInstance().__cache
    
    
    @staticmethod
    def inprocess(dataRequest,dataResponse):
        verb = dataRequest.getVerb()
        config = dataRequest.getConfig()
        context = dataRequest.getContext()
        
        caching = Config(config.get('caching'))
        cacheObject = CacheManager.getCache().get(config.get('name'),caching)
        print('processor: in cache')
        
        
    @staticmethod
    def outprocess(dataRequest,dataResponse):
        print('processor: out cache')