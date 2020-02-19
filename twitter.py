#Code written by Brian Park
#Account tested with https://twitter.com/qkrckddms under the organization name berk_dev
#To read more about the project, please go to my website to read more: https://www.briancpark.com/
#Here is the latest documentation for the Tweepy library: http://docs.tweepy.org/en/latest/

import tweepy
import credentials
import time
import random

"""
If you wish to test and use the Python Code with your own Twitter account, please apply for developer account
to access the API. After that please copy and paste your API keys into a separate Python file named
"credentials.py". It is important that you never share your keys!!!

ACCESS_TOKEN =        "YOUR KEY HERE"
ACCESS_TOKEN_SECRET = "YOUR KEY HERE"
CONSUMER_KEY =        "YOUR KEY HERE"
CONSUMER_SECRET =     "YOUR KEY HERE"
"""

auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

def my_timeline():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)

def user_followers(username):
    user = api.get_user(username)

    print(user.screen_name)
    print(user.followers_count)
    for friend in user.friends():
        print(friend.screen_name)

def follow_back_followers():
    count = 0

    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
        count += 1

    api.update_status("Function: follow_back_followers()\n line:72 \n Followed back "
                       + str(count) + " followers. \nStatus: Dangerous")

def tweet_text(tweet_text):
    api.update_status(tweet_text)

#Ticker that spams random numbers
def sched_tweet():
    starttime=time.time()
    while True:
        api.update_status("random number: " + str(random.randint(-1000000, 100000)))
        time.sleep(60- ((time.time() - starttime) % 60))

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

def print_followers():
    for follower in limit_handled(tweepy.Cursor(api.followers).items()):
        if follower.friends_count < 300:
            print(follower.screen_name)





#MAIN

user = 'qkrckddms'
