
from core.config import Config
from core.processor import Processor
from authentication.authenticationbase import AuthenticationBase
from authentication.authenticationbasic import AuthenticationBasic
from authentication.authenticationkerberos import AuthenticationKerberos

class AuthenticationManager(Processor):
    
    __instance = None
    
    def __init__(self):
        if AuthenticationManager.__instance == None:
            AuthenticationManager.__instance = self      
    
    @staticmethod
    def getInstance():
        if AuthenticationManager.__instance == None:
            AuthenticationManager()
        return  AuthenticationManager.__instance
    
    @staticmethod
    def get(name):
        return globals()[name]
    
    @staticmethod
    def process(dataRequest,dataResponse):
        verb = dataRequest.getVerb()
        config = dataRequest.getConfig()
        context = dataRequest.getContext()
        
        authentication = Config(config.get('authentication'))
        authenticator = AuthenticationManager.get(authentication.get('type'))(authentication)
        authenticator.authenticate(context)
        