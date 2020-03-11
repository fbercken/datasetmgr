import re

class Utility:
    
    PATTERN = r"([^\[|\.]+)\[?([0-9]+)?\]?"

    @staticmethod
    def getValue(obj,path):
        elt = obj
        fields = re.findall(Utility.PATTERN,path)
        for field in fields:
            elt = Utility._getElement(elt,field)    
        return elt
    
    @staticmethod
    def _getElement(obj,attr):
        name = attr[0]
        index = attr[1]
        if index == '':
            return obj[name]
        else:
            return obj[name][int(index)]