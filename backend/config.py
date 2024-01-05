from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    secret_key: str 
    algorithm: str
    access_token_expire_minutes: int = 40
    database_name: str
    database_hostname: str
    database_port: str
    database_password: str
    database_username: str

    class Config:
        env_file = ".env"
    # model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

