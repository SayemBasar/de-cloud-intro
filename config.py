import os

class Config:
        DATABASE_URL=os.getenv("DATABASE_URL")
        DEBUG=os.getenv("DEBUG")

class DevConfig(Config):
        ENV="development"
        
class ProdConfig(Config):
        ENV="prodeuction"