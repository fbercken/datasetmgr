from remote.remotebase import RemoteBase

class RemoteNFS(RemoteBase):
    
    def __init__(self,config):
        super(RemoteNFS,self).__init__(config)
        
    def buildPath(self):
        return ''
    
    def open(path, mode="r", encoding=None):
        return open(self.buildPath(path), mode=mode, encoding=encoding)
   