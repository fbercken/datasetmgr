from remote.remotebase import RemoteBase

class RemoteDTAP(RemoteBase):
    
    def __init__(self,config):
        super(RemoteDTAP,self).__init__(config)
        
    def buildPath(self):
        return ''
    
    def open(path, mode="r", encoding=None):
        return open( self.buildPath(path), mode=mode, encoding=encoding)
   