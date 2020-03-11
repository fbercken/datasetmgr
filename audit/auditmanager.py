from core.config import Config
from core.processor import Processor

class AuditManager(Processor):
    
    __instance = None
    
    def __init__(self):
        if AuditManager.__instance == None:
            AuditManager.__instance = self      
    
    @staticmethod
    def getInstance():
        if AuditManager.__instance == None:
            AuditManager()
        return  AuditManager.__instance
    
    @staticmethod
    def process(dataRequest,dataResponse):
        verb = dataRequest.getVerb()
        config = dataRequest.getConfig()
        context = dataRequest.getContext()
        
        print('processor: audit')