from sqlmodel import SQLModel, Field, create_engine, Relationship, Session
from typing import Optional, List
from dotenv import load_dotenv
import os

load_dotenv()

def get_Session():
    engine = create_engine(DATABASE_URL)
    with Session(engine) as session:
        yield session

DATABASE_URL = os.getenv("conn_str").replace("postgres://", "postgresql+psycopg2://")

class Comment(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    tweet_id: Optional[int] = Field(default=None, foreign_key="tweet.id")
    profile: str
    username: str
    content: str
    tweet: 'Tweet' = Relationship(back_populates="comments")

class UserLike(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    tweet_id: Optional[int] = Field(default=None, foreign_key="tweet.id")
    e_mail: str
    pass_word: str
    tweet: 'Tweet' = Relationship(back_populates="likeUserIds")

class Tweet(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    profile: str
    content: str
    slug: str
    contentImage: Optional[str] = Field(default=None, alias="contentImage")
    likesNumber: int = Field(default=0, alias="likesNumber")
    password: str
    email: str
    commentsNumber: int
    comments: List[Comment] = Relationship(back_populates="tweet")
    likeUserIds: List[UserLike] = Relationship(back_populates="tweet")


class CreateTweet(SQLModel):
    username: str
    profile: str
    content: str
    slug: str
    contentImage: Optional[str] = Field(default=None, alias="contentImage")
    likesNumber: int = Field(default=0, alias="likesNumber")
    password: str
    email: str
    commentsNumber: int
    comments: List[Comment] = Relationship(back_populates="tweet")
    likeUserIds: List[UserLike] = Relationship(back_populates="tweet")

if __name__ == "__main__":
    engine = create_engine(DATABASE_URL)
    SQLModel.metadata.create_all(engine)
