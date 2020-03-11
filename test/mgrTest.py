from core.datasetmanager import DatasetManager


datasetName = 'sample:1'
print('Print %s' % (datasetName))
with DatasetManager.open('sample:1') as f:
    print('- Data ----------')
    print(f.read())
   


datasetName = 'data:1'
print('Print %s' % (datasetName)  )
with DatasetManager.open('data:1') as f:
    print('- Data ----------')
    print(f.read())
    
#print( DatasetManager.open('sample:lastest').read() )


experiment1 = {
     "inputA": "sample", 
     "output1": "preprocessed",
     "log": "zz"
}


#print( DatasetManager.getDataset('${experiment1.inputA}' ))   
#with DatasetManager.open('${experiment1.inputA}') as f:
#    print(f.read())