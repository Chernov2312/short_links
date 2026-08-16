__all__ = ('AppConfig')
import redis
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int = 5432

    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str

    REDIS_PASSWORD: str
    REDIS_USER: str
    REDIS_USER_PASSWORD: str

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
        case_sensitive=True,
    )

    def get_db_url(self):
        return (
            f'postgresql+asyncpg://{self.POSTGRES_USER}'
            f':{self.POSTGRES_PASSWORD}'
            f'@{self.POSTGRES_HOST}'
            f':{self.POSTGRES_PORT}'
            f'/{self.POSTGRES_DB}'
        )

    @property
    def get_redis(self):
        return redis.Redis(
            host='193.3.298.206',
            port=6380,
            db=0,
            username=self.REDIS_USER,
            password=self.REDIS_PASSWORD,
        )


Settings = AppConfig()
