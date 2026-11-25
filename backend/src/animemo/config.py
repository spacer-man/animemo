import msgspec
from msgspec_ext import BaseSettings, SecretStr, SettingsConfigDict


class DBConfig(msgspec.Struct):
    url: SecretStr
    echo: bool = False


class ServerConfig(msgspec.Struct, frozen=True):
    host: str = "127.0.0.1"
    port: int = 8081


class Config(BaseSettings):
    db: DBConfig
    server: ServerConfig = ServerConfig()

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        env_nested_delimiter="__",
    )
