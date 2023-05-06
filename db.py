import pymongo
import dotenv
import os
config = dotenv.load_dotenv()

def create_client(cluster_name: str = "user"): 
    db_link = os.environ['DB_URL']
    client = pymongo.MongoClient(db_link, tlsAllowInvalidCertificates=False)
    databases = client[os.environ["DB_NAME"]]
    return databases[cluster_name]