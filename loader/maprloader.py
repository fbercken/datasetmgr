from core.config import Config
from loader.loader import Loader
from core.settings import Settings
from remote.remotemanager import RemoteManager
from mapr.ojai.storage.ConnectionFactory import ConnectionFactory


class MapRLoader(Loader):
    
    store = ''
    connectionStr = ''
    
    __instance = None
    
    def __init__(self): 
        MapRLoader.__instance = self
        self.store = Settings.store
        self.connectionStr = Settings.connectionStr
        
    @staticmethod
    def getInstance():
        if MapRLoader.__instance == None:
            MapRLoader()
        return  MapRLoader.__instance

    @staticmethod
    def get(name):
        singleton = MapRLoader.getInstance()
        
        connection = ConnectionFactory.get_connection(connection_str=singleton.connectionStr)
        store = connection.get_store(singleton.store)
        config = Config(store.find_by_id(name))
        connection.close()
        return config
      #  return RemoteManager.getRemote(config.get('type'),config)

    @staticmethod
    def put(doc):
        singleton = MapRLoader.getInstance()
        
        connection = ConnectionFactory.get_connection(connection_str=singleton.connectionStr)
        store = connection.get_store(singleton.store)
        doc = store.insertOrReplace(doc)
        connection.close()
        return doc

    
