from pydantic import BaseSettings

# put some global configs here
class Settings(BaseSettings):

    APP_NAME: str = 'My FAST API'

    APP_CREATOR: str = 'Zubair Patel'


settings = Settings()