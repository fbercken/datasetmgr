
class RemoteBase:
    
    config = {}

    
    def __init__(self,config):
        self.config = config
        
    def getName():
        return self.config.get('name')
        
    def open(path, mode="r", encoding=None):
        pass
    
    def delete(path):
        pass
    
    def exists(path):
        pass
        
    def create(path):
        pass
    