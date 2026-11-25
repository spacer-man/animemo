from datetime import datetime

from sqlalchemy import FLOAT, VARCHAR, BigInteger, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(VARCHAR(32), unique=True)


class AnimeTitle(Base):
    __tablename__ = "anime_titles"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(VARCHAR(32))
    description: Mapped[str] = mapped_column(VARCHAR(4098))


class TitleScore(Base):
    __tablename__ = "title_scores"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    value: Mapped[float] = mapped_column(FLOAT)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    anime_title_id: Mapped[int] = mapped_column(ForeignKey("anime_titles.id"))
    date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
