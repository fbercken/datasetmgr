class Settings:
    
    loader = 'FileLoader'
    #loader = 'MapRLoader'
    store = '/user/mapr/datasets'
    connectionStr = "localhost:5678?auth=basic;user=mapr;password=mapr;" \
        "ssl=false;" \
        "sslCA=/opt/mapr/conf/ssl_truststore.pem;" \
        "sslTargetNameOverride=node1.mapr.com"