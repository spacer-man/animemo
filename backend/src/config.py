import msgspec
from msgspec_ext import BaseSettings, SecretStr, SettingsConfigDict


class DBConfig(msgspec.Struct):
    url: SecretStr
    echo: bool = False


class Config(BaseSettings):
    db: DBConfig

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        env_nested_delimiter="__",
    )
