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


handle="CarlosBolsonaro"

result = {}
if __name__ == "__main__":
	tweepy.initialize(2)
	hashtags = tweepy.collect_hashtags(handle)
	result["hashtags"] = hashtags
	with open("data/tweets/hashtags/" + handle + "_Hashtags.json", "a", encoding="utf8") as f:
		json.dump(result, f,ensure_ascii=False)