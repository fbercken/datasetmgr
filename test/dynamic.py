from loader.loader import Loader
from loader.fileloader import FileLoader
from loader.maprloader import MapRLoader

className = 'MapRLoader'
loader = globals()[className]()
print(loader.get("2"))


className = 'FileLoader'
loader = globals()[className]()
print(loader.get("Customers"))