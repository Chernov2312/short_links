__all__ = ('AppConfig', 'Settings')
import redis
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):

    REDIS_PASSWORD: str
    REDIS_USER: str
    REDIS_USER_PASSWORD: str

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
        case_sensitive=True,
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
