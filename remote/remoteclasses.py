
from remote.remotes3 import RemoteS3
from remote.remotenfs import RemoteNFS
from remote.remotehttp import RemoteHTTP
from remote.remotedtap import RemoteDTAP
from remote.remotelocal import RemoteLocal

class RemoteClasses:
    
    CLAZZS = {
        's3': RemoteS3,
        'nfs': RemoteNFS,
        'http': RemoteHTTP,
        'dtap': RemoteDTAP,
        'local':  RemoteLocal
    }