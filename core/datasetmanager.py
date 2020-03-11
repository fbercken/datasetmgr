import re
import json
import glob
from core.config import Config
from core.context import Context
from core.settings import Settings
from core.datarequest import DataRequest
from core.dataresponse import DataResponse
from loader.fileloader import FileLoader
from loader.maprloader import MapRLoader
from audit.auditmanager import AuditManager
from caching.cachemanager import CacheManager
from remote.remotemanager import RemoteManager
from authentication.authenticationmanager import AuthenticationManager


class DatasetManager:
    
    __loader = None
    __instance = None
    

    VAR_PATTERN = r"\$\{([^\}]*)\}"
    VER_PATTERN = r"([^\:]*):?([^\:])"
    
    def __init__(self):        
        if DatasetManager.__instance == None:
            DatasetManager.__instance = self
            DatasetManager.__loader = globals()[Settings.loader]
        
    @staticmethod
    def getInstance():
        if DatasetManager.__instance == None:
            DatasetManager()
        return  DatasetManager.__instance
    
    @staticmethod
    def getLoader():
        return  DatasetManager.getInstance().__loader
    
    @staticmethod
    def isvariable(str):
        return re.match( DatasetManager.VAR_PATTERN, str) != None
    
    @staticmethod
    def getDataset(str):
        #if DatasetManager.isvariable(str):
        match = re.search( DatasetManager.VAR_PATTERN, str)
        if match:
            print(eval('experiment1'))
            print( Utility.getValue(eval('experiment1'),'inputA')  ) 
            name = eval(match.group(1))
        else:
            name = str
        return DatasetManager.getLoader().get(name)    
    
    
    @staticmethod
    def open(name,mode = 'r'):
        context = Context()
        config = DatasetManager.getDataset(name)
        
        dataResponse = DataResponse()
        dataRequest = DataRequest('open',config,context)
        
        AuthenticationManager.process(dataRequest,dataResponse)
        CacheManager.inprocess(dataRequest,dataResponse)
        RemoteManager.process(dataRequest,dataResponse)
        CacheManager.outprocess(dataRequest,dataResponse)
        AuditManager.process(dataRequest,dataResponse)
        
        return dataResponse.getFileObject()