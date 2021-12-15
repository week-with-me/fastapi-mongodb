from functools import lru_cache
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    LEVEL: str = 'DEVELOP'
    PROJECT_TITLE: str = 'FastAPI with MongoDB'
    DB_NAME: str
    
    class Config:
        env_file = '.env'
        
        
class DevelopSettings(Settings):
    DB_URL: str = Field(env='DEVELOP_DB_URL')
    

class ProductSettings(Settings):
    DB_URL: str = Field(env='PRODUCT_DB_URL')
    
    
@lru_cache
def get_settings():
    if Settings().LEVEL == 'DEVELOP':
        return DevelopSettings()
    else:
        return ProductSettings()