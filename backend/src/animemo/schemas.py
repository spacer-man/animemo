from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int
    username: str


@dataclass
class AnimeTitle:
    id: int
    title: str
    description: str


@dataclass
class TitleScore:
    id: int
    value: float
    user_id: int
    anime_title_id: int
    date: datetime
