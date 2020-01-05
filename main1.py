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


handle="FlavioBolsonaro"
max_tweets = 3000

result = {}
if __name__ == "__main__":
	tweepy.initialize(3)
	# tweets = tweepy.collect_tweets(handle, max_tweets)
	# result["tweets"]=tweets
	# with open("data/tweets/" + handle + ".json", "a", encoding="utf8") as f:
	# 	json.dump(result, f,ensure_ascii=False)
	# 
	replies = tweepy.collect_replies(handle)
	with open("data/tweets/" + handle + ".json","r",encoding="utf8") as f:
		result=json.load(f)

	result["replies"] = replies
	with open("data/tweets/" + handle + ".json", "w", encoding="utf8") as f:
		json.dump(result, f,ensure_ascii=False)
	
	# hashtags = tweepy.collect_hashtags(handle)
	# result["hashtags"] = hashtags
	# with open("data/tweets/hashtags/" + handle + "_Hashtags.json", "a", encoding="utf8") as f:
	# 	json.dump(result, f,ensure_ascii=False)



	

    






