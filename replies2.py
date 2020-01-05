import json
import tweepy
import datetime as dt
import time
import os
import sys
import pprint
import re
import config

from twitter import tweepy
from tweepy import OAuthHandler


handle="BolsonaroSP"

result = {}
if __name__ == "__main__":
	tweepy.initialize(1)
	replies = tweepy.collect_replies(handle)
	with open("data/tweets/" + handle + ".json", "r", encoding="utf8") as f:
		result=json.load(f)

	result["replies"] = replies
	with open("data/tweets/" + handle + ".json", "w", encoding="utf8") as f:
		json.dump(result, f, ensure_ascii=False)