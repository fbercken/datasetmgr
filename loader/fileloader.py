import json
import glob
from core.config import Config
from loader.loader import Loader
from remote.remotemanager import RemoteManager

class FileLoader(Loader):

    datasets = {}
    
    __instance = None
    
    def __init__(self): 
        FileLoader.__instance = self
        FileLoader.load("./datasets/")
        
    @staticmethod
    def getInstance():
        if FileLoader.__instance == None:
            FileLoader()
        return  FileLoader.__instance

    @staticmethod
    def load(path):     
        singleton = FileLoader.getInstance()
        paths = [f for f in glob.glob( path + "*.json", recursive=False)]
        
        for path in paths:
            with open(path) as file:
                config = Config(json.load(file))
                singleton.datasets[config.get('name')] = config
               # singleton.datasets[name] = RemoteManager.getRemote(type,config)
                
    @staticmethod
    def get(name):
        return FileLoader.getInstance().datasets[name]

    @staticmethod
    def put(doc):
        pass