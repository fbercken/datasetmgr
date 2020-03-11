import time
from enum import Enum

class Level(Enum):
    
    CRITICAL = 0
    ERROR = 10
    EXCEPTION = 20
    WARNING = 30
    INFO = 40
    DEBUG = 50

    

class LogRecord(dict):
    
    OWNER = 'owner'
    LEVEL = 'level'
    MESSAGE = 'message'
    TIMESTAMP = 'timestamp'
    
    def __init__(self,level=Level.INFO,message=""):
        self.put(LogRecord.LEVEL,level)
        self.put(LogRecord.MESSAGE,message)
        self.put(LogRecord.TIMESTAMP,time.time() * 1000)
    
    def put(self,name,value):
        self[name] = value
        return self
    
    def get(self,name):
        try:
            return self[name]
        except:
            return None


        
class Formatter:
    
    def format(self,logRecord):
        pass

    
    
class StringFormatter(Formatter):
    
    def __init__(self,fields=[LogRecord.TIMESTAMP,LogRecord.OWNER,LogRecord.LEVEL,LogRecord.MESSAGE]):
        self.fields = fields
    
    def format(self,logRecord):
        return "\t".join(map( lambda field : str(logRecord.get(field)), self.fields)) + "\n"
    


    
class Handler:
    
    def __init__(self):
        self.level = Level.INFO
        self.formatter = StringFormatter()
    
    def setFormatter(self,formatter):
        self.formatter = formatter
        return self
    
    def setLevel(self,level):
        self.level = level
        return self
    
    def getLevel(self):
        return self.level
    
    def write(self,logRecord):
        pass

    
    
class ConsoleHandler(Handler):
    
    def __init__(self,*args):
        super(ConsoleHandler,self).__init__()
     
    def write(self,logRecord):
        print(self.formatter.format(logRecord))


    
class Logger:
    
    def __init__(self,config={}):
        self.config = config
        self.handlers = {}
        
    def addHandler(self,name,handler):
        self.handlers[name] = handler
        return self
    
    def removeHandler(self,name):
        del self.handlers[name] 
        return self
        
    def log(self,message="",level=Level.INFO):
        record = LogRecord(level,message)
        for item in self.handlers.items():
            handler = item[1]
            if level.value <= handler.getLevel().value:
                handler.write(record)
