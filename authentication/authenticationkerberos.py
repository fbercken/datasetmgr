from authentication.authenticationbase import AuthenticationBase

class AuthenticationKerberos(AuthenticationBase):
    
    def __init__(self,config):
        self.config = config
        
        
    def authenticate(self,context):
          print('processor: Kerberos Authentication')