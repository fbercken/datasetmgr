class AuthenticationBase:
    
    def __init__(self,config):
        self.config = config
        
    def getName():
        return self.config.get('name')
        
    def authenticate(self,context):
        pass