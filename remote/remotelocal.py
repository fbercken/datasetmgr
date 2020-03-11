from core.config import Config
from remote.remotebase import RemoteBase

class RemoteLocal(RemoteBase):
    
    defaults = Config( {
        'mode': 'r',
        'encoding': 'utf-8'
    })
    
    def __init__(self,config):
        super(RemoteLocal,self).__init__(RemoteLocal.defaults.update(config))
        
    def buildPath(self):
        path = self.config.get('access.path')
        return  path;
    
    def open(self, mode="r", encoding=None):
        return open( self.buildPath(), mode=mode, encoding=encoding or self.config.get('encoding'))
    
    