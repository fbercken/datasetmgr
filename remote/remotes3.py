import boto3
from remote.remotebase import RemoteBase

class RemoteS3(RemoteBase):
    
    def __init__(self,config):
        super(RemoteS3,self).__init__(config)
        
    def buildPath(self):
        return '';
    
    def open(path, mode="r", encoding=None):
        return open( self.buildPath(path), mode=mode, encoding=encoding)