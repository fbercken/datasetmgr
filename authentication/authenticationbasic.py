from authentication.authenticationbase import AuthenticationBase

class AuthenticationBasic(AuthenticationBase):
    
    def __init__(self,config):
        self.config = config
        
        
    def authenticate(self,context):
        print('processor: Basic Authentication')