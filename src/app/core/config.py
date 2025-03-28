from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_VERSION: str = "1.0.0"
    DATABASE_URL: str = "sqlite:///./test.db"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()