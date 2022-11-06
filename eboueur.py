# -*- coding: utf-8 -*-
"""
Spyder Editor

This is my Twitter bot project.

My first step is to create a boat whitch must be able to retweet all the post
with the hashtag shitPost or PoubelleMentale.
"""

import tweepy


#connection to the account
auth = tweepy.OAuthHandler("XMIEkLdfAiJcRAtCDUy7Y268u", "TNKhMNjgfVqHnLJ4PsoJXC5Lrsz9pjcUjABSNj5nHsliXaFZBW")
#connection to the app in Twitter developpement
auth.set_access_token("1588133381665071106-EdRy2HtcUn55wn41G54Vk4XOkmSyCD", "Tn6WoIV6heirjNISdUOKlMu6dgYCSOVKwGJu9YbqR7osa")

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
