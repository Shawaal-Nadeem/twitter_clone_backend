from fastapi import FastAPI, Depends
from typing import Annotated
from .database import get_Session, Tweet, CreateTweet
from sqlmodel import select, Session
from fastapi.middleware.cors import CORSMiddleware

app:FastAPI=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message":"To see Tweets write /tweets at end of url"}

@app.get("/tweets")
def get_tweets(session:Annotated[Session,Depends(get_Session)]):
    query = select(Tweet)
    tweets = session.exec(query).all()
    return tweets

@app.get("/tweets/{tweet_id}")
def get_specific_tweet(tweet_id:int, session:Annotated[Session, Depends(get_Session)]):
    tweet = session.get(Tweet, tweet_id)
    return tweet

@app.post("/tweets")
def post_tweet(tweet:CreateTweet, session:Annotated[Session, Depends(get_Session)]):
    tweet = Tweet.model_validate(tweet)
    session.add(tweet)
    session.commit()
    session.refresh(tweet)
    return tweet

@app.put("/tweets/{tweet_id}")
def update_tweet(tweet_id:int, tweet:CreateTweet, session:Annotated[Session, Depends(get_Session)]):
    tweet_to_update = session.get(Tweet, tweet_id)
    tweet_to_update.content = tweet.content
    tweet_to_update.username = tweet.username
    session.add(tweet_to_update)
    session.commit()
    session.refresh(tweet_to_update)
    return tweet_to_update

@app.delete("/tweets/{tweet_id}")
def delete_tweet(tweet_id:int, session:Annotated[Session, Depends(get_Session)]):
    tweet_to_delete = session.get(Tweet, tweet_id)
    session.delete(tweet_to_delete)
    session.commit()
    return {"message":"Tweet deleted successfully"}

