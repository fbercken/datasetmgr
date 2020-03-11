import json
from core.utility import Utility
from core.datasetmanager import DatasetManager

mgr = DatasetManager.getInstance()
print(mgr)

    
    
print('--------------------')    
#print( DatasetManager.open('Customers') )

print( DatasetManager.open('sample:1').read() )
print( DatasetManager.open('data:1').read() )
#print( DatasetManager.open('sample:lastest').read() )


experiment1 = {
     "inputA": "sample", 
     "output1": "preprocessed",
     "log": "zz"
}


#print( Utility.getValue( globals()['experiment1'], 'inputA' ) )

#print( DatasetManager.getDataset('${experiment1.inputA}' )) 
    
#with DatasetManager.open('${experiment1.inputA}') as f:
#    print(f.read())