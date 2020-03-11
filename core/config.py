import re
from core.utility import Utility

class Config:

    def __init__(self,data = {}):
        self.data = data 
        
    def get(self,path):
        return Utility.getValue(self.data,path)
        
    def update(self,config):
        self.data.update(config.data)
        return self

    