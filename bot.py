import tweepy
import json

with open("./auth.json", "r+", encoding="utf-8") as auth:
    keys = json.load(auth)
    auth.close()

print (keys)
