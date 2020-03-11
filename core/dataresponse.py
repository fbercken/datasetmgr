class DataResponse:
    
    status = True
    fileObject = None
    
    def __init__(self):
        pass
    
    def getStatus(self):
        return seld.status
    
    def setFileObject(self,obj):
        self.fileObject = obj
        
    def getFileObject(self):
        return self.fileObject