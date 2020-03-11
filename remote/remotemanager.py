from remote.remotebase import RemoteBase
from remote.remoteclasses import RemoteClasses
from core.datarequest import DataRequest
from core.dataresponse import DataResponse
from core.processor import Processor

class RemoteManager(Processor):
    
    
    __instance = None
    
    
    def __init__(self):
        if RemoteManager.__instance == None:
            RemoteManager.__instance = self
        
    @staticmethod
    def getInstance():
        if RemoteManager.__instance == None:
            RemoteManager()
        return  RemoteManager.__instance
    
    @staticmethod
    def get(name):
        return globals()[name]
    
    @staticmethod
    def getRemote(name,config):
        return RemoteClasses.CLAZZS[name](config)
    
    @staticmethod
    def process(dataRequest,dataResponse):
        verb = dataRequest.getVerb()
        context = dataRequest.getContext()
        config = dataRequest.getConfig()
        
        file = RemoteManager.getRemote(config.get('type'), config).open()
        print('processor: remote')
        
        dataResponse.setFileObject(file)
        
        
        