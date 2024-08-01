from sqlmodel import SQLModel, Field, create_engine, Session
from typing import Optional, List
from sqlalchemy import Column, JSON
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("conn_str").replace("postgres://", "postgresql+psycopg2://")

def get_Session():
    engine = create_engine(DATABASE_URL)
    with Session(engine) as session:
        yield session

class Tweet(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    profile: Optional[str] = None
    content: Optional[str] = Field(default=None)
    slug: str
    contentImage: Optional[str] = Field(default=None, alias="contentImage")
    likesNumber: int = Field(default=0, alias="likesNumber")
    password: str
    email: str
    commentsNumber: int = Field(default=0, alias="commentsNumber")
    comments: List[dict] = Field(default_factory=list, sa_column=Column(JSON), alias="comments")
    likeUserIds: List[dict] = Field(default_factory=list, sa_column=Column(JSON), alias="likeUserIds")

class CreateTweet(SQLModel):
    username: str
    profile: Optional[str] = None
    content: Optional[str] = Field(default=None)
    slug: str
    contentImage: Optional[str] = Field(default=None, alias="contentImage")
    likesNumber: int = Field(default=0, alias="likesNumber")
    password: str
    email: str
    commentsNumber: int = Field(default=0, alias="commentsNumber")
    comments: List[dict] = Field(default_factory=list, sa_column=Column(JSON), alias="comments")
    likeUserIds: List[dict] = Field(default_factory=list, sa_column=Column(JSON), alias="likeUserIds")

if __name__ == "__main__":
    engine = create_engine(DATABASE_URL)
    SQLModel.metadata.create_all(engine)
