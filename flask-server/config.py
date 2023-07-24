import os

class Config(object):
    """Base config, uses staging database server."""
    TESTING = False
    DB_SERVER = 'localhost'
    PW = os.getenv('MONGO_PW')

    @property
    def DATABASE_URI(self):  # Note: all caps
        if self.DB_SERVER == 'mongod-0.mongodb-service.default.svc.cluster.local:27017':
            return f"mongodb://flask-role:{self.PW}@{self.DB_SERVER}/sitecontent?authSource=sitecontent&replicaSet=MainRepSet"
        return f"mongodb://flask-role:{self.PW}@{self.DB_SERVER}:27017/sitecontent?authSource=admin"

class localConfig(Config):
    DB_SERVER = 'localhost'

class dockerConfig(Config):
    DB_SERVER = 'mongodb'

class kubernetesConfig(Config):
    DB_SERVER = 'fv-mongo-service'

class headlessConfig(Config):
    DB_SERVER = 'mongodb-service'

class headlessConfigMultiConnectConfig(Config):
    DB_SERVER = 'mongod-0.mongodb-service.default.svc.cluster.local:27017'