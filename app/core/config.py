from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    API_KEY: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

