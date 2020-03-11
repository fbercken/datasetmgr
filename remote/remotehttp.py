import urllib.request
from core.config import Config
from remote.remotebase import RemoteBase

class RemoteHTTP(RemoteBase):
    
    defaults = Config( {
        'encoding': 'utf-8'
    })
    
    def __init__(self,config):
        super(RemoteHTTP,self).__init__( RemoteHTTP.defaults.update(config) )
        
    def buildPath(self):
        host = self.config.get('access.host')
        port = self.config.get('access.port')
        path = self.config.get('access.path')
        scheme = self.config.get('access.scheme')
        return scheme + "://" + host + ":" + port + path
    
    def open(self, mode="r", encoding=None):
        return urllib.request.urlopen( self.buildPath())