import pymongo
import certifi
import logging
import dotenv
import os
config = dotenv.load_dotenv()

def create_client(cluster_name: str = "user"): 
    db_link = os.environ['DB_URL']
    cacert = certifi.where()
    client = pymongo.MongoClient(db_link, tlsCAFile=cacert, tlsAllowInvalidCertificates=False)
    databases = client[os.environ["DB_NAME"]]
    return databases[cluster_name]