from core.utility import Utility


data = { 
    "firstname": "fred",
    "lastname": "berque",
    "phones": [
        { "type": "home", "number": "12221" },
        { "type": "mobile", "number": "346666" }
    ]
}

print( Utility.getValue( data, "lastname") )
print( Utility.getValue( data, "phones[1]") )
print( Utility.getValue( data, "phones[1].number") )