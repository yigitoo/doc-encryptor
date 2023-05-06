import pymongo
import certifi
import logging
import dotenv

config = dotenv.dotenv_values(".env")

def create_client(cluster_name: str = "user"): 
    db_link = config['DB_URL']
    cacert = certifi.where()
    client = pymongo.MongoClient(db_link, tlsCAFile=cacert, tlsAllowInvalidCertificates=False)
    databases = client[config["DB_NAME"]]
    return databases[cluster_name]