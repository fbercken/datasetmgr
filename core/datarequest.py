class DataRequest:
    
    def __init__(self,verb,config,context):
        self.verb = verb
        self.config = config
        self.context = context
            
    def getVerb(self):
        return self.verb
    
    def getConfig(self):
        return self.config
    
    def getContext(self):
        return self.context