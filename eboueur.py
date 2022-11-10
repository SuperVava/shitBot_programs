# -*- coding: utf-8 -*-
"""
Spyder Editor

This is my Twitter bot project.

My first step is to create a boat whitch must be able to retweet all the post
with the hashtag shitPost or PoubelleMentale.
"""

import tweepy
import log

#connection to the account
auth = tweepy.OAuthHandler(log.getApi("key"), log.getApi("secret"))
#connection to the app in Twitter developpement
auth.set_access_token(log.getToken("key"), log.getToken("secret"))

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("The bot is connected")

except:
    print("Connection error...")

maxTweet = 5

tweets = api.search_tweets('#dechet')

for tweet in tweets:

    print(tweet.text)

    choice = input("\n retweet? \n y / n : ")

    if choice == 'y':
        try:
            api.retweet(tweet.id_str)
            print("retweet... ")

        except:
            print("already retweeted.")

    elif choice == 'n':
        pass

    else:
        print("Error: invalid input")
